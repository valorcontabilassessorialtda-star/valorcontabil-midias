"""Renderiza um Reel animado (HTML com window.render(t) e window.TOTAL) em MP4 1080x1920.

Uso: python3 scripts/render_reel.py caminho/reel.html pasta/de/saida prefixo [segundo_da_capa]
Gera <prefixo>-reel.mp4 (H.264, 30 fps, com faixa de áudio silenciosa para a música ser
adicionada no Instagram) e <prefixo>-reel-capa.jpg.
Para conferência, gera também quadros de prévia em <saida>/_previa/ (não versionar).
"""
import sys, os, subprocess, shutil, tempfile
from playwright.sync_api import sync_playwright

html, outdir, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
capa_t = float(sys.argv[4]) if len(sys.argv) > 4 else 3.5
FPS = 30
os.makedirs(outdir, exist_ok=True)
tmp = tempfile.mkdtemp()
prev = os.path.join(outdir, "_previa"); os.makedirs(prev, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + os.path.abspath(html))
    pg.wait_for_timeout(800)
    total = pg.evaluate("window.TOTAL")
    n = int(round(total * FPS))
    for i in range(n):
        t = i / FPS
        pg.evaluate(f"window.render({t})")
        pg.screenshot(path=os.path.join(tmp, f"f{i:05d}.jpg"), type="jpeg", quality=92)
    pg.evaluate(f"window.render({capa_t})")
    pg.screenshot(path=os.path.join(outdir, f"{prefix}-reel-capa.jpg"), type="jpeg", quality=95)
    # prévias: fim de cada cena (estado final) para conferência visual
    ends = pg.evaluate("[...document.querySelectorAll('.scene')].map(s=>s._b)")
    for k, e in enumerate(ends):
        pg.evaluate(f"window.render({e - 0.05})")
        pg.screenshot(path=os.path.join(prev, f"cena-{k+1}.jpg"), type="jpeg", quality=85)
    b.close()
out = os.path.join(outdir, f"{prefix}-reel.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%05d.jpg"),
                "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
shutil.rmtree(tmp)
print(f"{out}: {total:.1f} s, {n} quadros")
