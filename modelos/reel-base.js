// Motor de animação dos Reels — Valor Contábil
// Cada .scene tem data-dur (segundos). Elementos com data-a="atraso,duração,tipo" (relativo ao início da cena).
// Tipos: up, left, right, pop, rise, drop, fade, sweep, grow (largura de barra até data-w%).
// data-count="atraso,duração,alvo[,casas]" anima números (formato pt-BR).
// data-pulse="atraso" faz o elemento pulsar; .float flutua suavemente.
(function(){
  const scenes=[...document.querySelectorAll('.scene')];
  let acc=0; scenes.forEach(s=>{s._a=acc; acc+=parseFloat(s.dataset.dur); s._b=acc;});
  window.TOTAL=acc;
  const cl=x=>Math.max(0,Math.min(1,x));
  const ease=x=>1-Math.pow(1-x,3);
  const back=x=>{const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
  const fmt=(v,d)=>v.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
  window.render=function(t){
    const bar=document.getElementById('prog'); if(bar) bar.style.width=(cl(t/acc)*100)+'%';
    scenes.forEach((s,i)=>{
      const a=s._a, b=s._b, last=i===scenes.length-1;
      const vis=t>=a && (t<b+0.4 || (last && t<=b));
      const pin=i===0?1:cl((t-a)/0.4);
      s.style.opacity=vis?pin:0;
      s.style.transform=`translateX(${(1-ease(pin))*120}px)`;
      s.style.zIndex=vis?10+i:0;
      const lt=t-a;
      s.querySelectorAll('[data-a]').forEach(e=>{
        const [st,d,ty]=e.dataset.a.split(','); const p=cl((lt-parseFloat(st))/parseFloat(d)), q=ease(p);
        let tr='',op=q;
        if(ty==='up')tr=`translateY(${(1-q)*70}px)`;
        if(ty==='left')tr=`translateX(${(1-q)*-160}px)`;
        if(ty==='right')tr=`translateX(${(1-q)*160}px)`;
        if(ty==='pop'){tr=`scale(${0.6+0.4*back(p)})`;op=cl(p*2)}
        if(ty==='rise')tr=`translateY(${(1-q)*220}px)`;
        if(ty==='drop')tr=`translateY(${(1-back(p))*-200}px)`;
        if(ty==='sweep'){tr=`scaleX(${q})`;op=1}
        if(ty==='grow'){e.style.width=(q*parseFloat(e.dataset.w))+'%';op=1}
        e.style.opacity=op; if(tr)e.style.transform=tr;
      });
      s.querySelectorAll('[data-count]').forEach(e=>{
        const [st,d,tg,dec]=e.dataset.count.split(',').map(Number);
        e.textContent=fmt(ease(cl((lt-st)/d))*tg,dec||0);
      });
      s.querySelectorAll('[data-pulse]').forEach(e=>{
        const st=+e.dataset.pulse; if(lt>st){e.style.transform=`scale(${1+0.04*Math.sin((lt-st)*2*Math.PI*1.2)})`;}
      });
      s.querySelectorAll('.float').forEach(e=>{e.style.transform=`translateY(${Math.sin(lt*1.6)*10}px)`;});
    });
  };
  window.render(0);
})();
