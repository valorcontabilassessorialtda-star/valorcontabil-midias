"""Renderiza cada elemento .slide (com id s1, s2, ...) de um HTML em JPG 1080x1350.

Uso: python3 scripts/render.py caminho/do/post.html pasta/de/saida prefixo
Exemplo: python3 scripts/render.py posts/2026-10-22-tema/post.html posts/2026-10-22-tema tema
Gera tema-1.jpg, tema-2.jpg, ... na pasta de saída.
"""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image

html, outdir, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1400}, device_scale_factor=1)
    pg.goto("file://" + os.path.abspath(html))
    pg.wait_for_timeout(800)
    slides = pg.locator(".slide")
    n = slides.count()
    for i in range(n):
        png = os.path.join(outdir, f"_tmp{i}.png")
        slides.nth(i).screenshot(path=png)
        Image.open(png).convert("RGB").save(os.path.join(outdir, f"{prefix}-{i+1}.jpg"), quality=95)
        os.remove(png)
    b.close()
print(f"{n} imagem(ns) gerada(s)")
