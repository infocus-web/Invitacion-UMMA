import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

edits = []

edits.append((
"""  :root{
    --bg: #4d4d4d;
    --bg-soft: #575757;
    --card: #636363;
    --gold: #8a5a9e;
    --gold-soft: #ffffff;
    --silver: #b8bcc4;
    --text: #f5f5f7;
    --text-dim: #c1694a;
    --line: rgba(255,255,255,0.16);
  }""",
"""  :root{
    --bg: #0a0a0a;
    --bg-soft: #121212;
    --card: #181818;
    --gold: #e9e9ec;
    --gold-soft: #ffffff;
    --silver: #b8bcc4;
    --text: #ffffff;
    --text-dim: #b3b3b8;
    --line: rgba(255,255,255,0.16);
    --bokeh-img: url('images/bokeh.svg');
  }"""
))

edits.append((
"""  .parallax .parallax-overlay{position:absolute;inset:0;background:rgba(77,77,77,.75);z-index:1;}""",
"""  .parallax .parallax-overlay{position:absolute;inset:0;background:rgba(0,0,0,.72);z-index:1;}

  /* BOKEH */
  .bokeh-top, .bokeh-bottom{
    position:absolute;left:0;right:0;height:200px;pointer-events:none;z-index:1;
    background-image:var(--bokeh-img);background-repeat:no-repeat;background-size:cover;
    mix-blend-mode:screen;opacity:.85;
  }
  .bokeh-top{top:0;background-position:top center;}
  .bokeh-bottom{bottom:0;background-position:top center;transform:scaleY(-1);}
  @media(max-width:700px){.bokeh-top,.bokeh-bottom{height:130px;}}"""
))

edits.append((
"""  .wrap{max-width:920px;margin:0 auto;text-align:center;}""",
"""  .wrap{max-width:920px;margin:0 auto;text-align:center;position:relative;z-index:2;}"""
))

edits.append((
"""  footer{
    text-align:center;padding:70px 24px 40px;border-top:1px solid var(--line);background:var(--bg-soft);
  }""",
"""  footer{
    text-align:center;padding:70px 24px 40px;border-top:1px solid var(--line);background:var(--bg-soft);
    position:relative;overflow:hidden;
  }"""
))

edits.append((
"""  .music-gate{
    position:fixed;inset:0;z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;
    text-align:center;padding:24px;background:linear-gradient(180deg,#4d4d4d 0%, #474747 100%);
    transition:opacity .6s ease;
  }""",
"""  .music-gate{
    position:fixed;inset:0;z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;
    text-align:center;padding:24px;background:linear-gradient(180deg,#050505 0%, #0f0f0f 100%);
    transition:opacity .6s ease;overflow:hidden;
  }
  .music-gate .bokeh-top, .music-gate .bokeh-bottom{height:260px;}
  .music-gate > *:not(.bokeh-top):not(.bokeh-bottom){position:relative;z-index:2;}"""
))

edits.append((
"""<section class="hero parallax" id="top">
  <div class="parallax-img" style="background-image:url('images/uma-01.jpg')"></div>
  <div class="parallax-overlay"></div>
  <div class="hero-content">""",
"""<section class="hero parallax" id="top">
  <div class="parallax-img" style="background-image:url('images/uma-01.jpg')"></div>
  <div class="parallax-overlay"></div>
  <div class="bokeh-top"></div>
  <div class="bokeh-bottom"></div>
  <div class="hero-content">"""
))

edits.append((
"""<section id="rsvp" style="background:var(--bg-soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
  <div class="wrap">""",
"""<section id="rsvp" style="background:var(--bg-soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
  <div class="bokeh-top"></div>
  <div class="wrap">"""
))

edits.append((
"""<div class="music-gate" id="musicGate">
  <div class="gate-script">Uma</div>""",
"""<div class="music-gate" id="musicGate">
  <div class="bokeh-top"></div>
  <div class="bokeh-bottom"></div>
  <div class="gate-script">Uma</div>"""
))

edits.append((
"""<!-- FOOTER -->
<footer>
  <div class="name-script">Uma</div>
  <div class="sub">Mis XV Años</div>
  <nav>
    <a href="#rsvp">Confirmar asistencia</a>
    <a href="#musica">Sugerir canción</a>
    <a href="#detalles">Agendar fiesta</a>
  </nav>
  <div class="credit">Hecho con ♥ para Uma</div>
</footer>""",
"""<!-- FOOTER -->
<footer>
  <div class="bokeh-top"></div>
  <div style="position:relative;z-index:2;">
    <div class="name-script">Uma</div>
    <div class="sub">Mis XV Años</div>
    <nav>
      <a href="#rsvp">Confirmar asistencia</a>
      <a href="#musica">Sugerir canción</a>
      <a href="#detalles">Agendar fiesta</a>
    </nav>
    <div class="credit">Hecho con ♥ para Uma</div>
  </div>
</footer>"""
))

missing = []
for i, (old, new) in enumerate(edits):
    if old not in c:
        missing.append(i)
    else:
        c = c.replace(old, new, 1)

if missing:
    print("ATENCION: no se encontraron estos bloques (indices):", missing)
    print("Avisa a Claude con este mensaje antes de continuar.")
else:
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("OK: tema negro/blanco + bokeh aplicado.")
