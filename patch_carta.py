import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

edits = []

edits.append((
"""  /* MAIN NAME BLOCK */""",
"""  /* CARTA / REVEAL */
  .carta{max-width:640px;margin:0 auto;text-align:left;}
  .carta .verse{
    font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.3rem;line-height:1.7;
    color:var(--gold-soft);text-align:center;border-bottom:1px solid var(--line);padding-bottom:22px;margin-bottom:30px;
  }
  .carta .verse-ref{display:block;margin-top:12px;font-style:normal;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--text-dim);}
  .carta p{color:var(--text-dim);font-size:1.02rem;line-height:1.9;margin-bottom:22px;}
  .reveal-block .verse, .reveal-block p{
    opacity:0;transform:translateY(16px);transition:opacity .9s ease, transform .9s ease;
  }
  .reveal-block.in-view .verse{opacity:1;transform:translateY(0);transition-delay:0s;}
  .reveal-block.in-view p:nth-of-type(1){opacity:1;transform:translateY(0);transition-delay:.35s;}
  .reveal-block.in-view p:nth-of-type(2){opacity:1;transform:translateY(0);transition-delay:.7s;}
  .reveal-block.in-view p:nth-of-type(3){opacity:1;transform:translateY(0);transition-delay:1.05s;}
  .reveal-block.in-view p:nth-of-type(4){opacity:1;transform:translateY(0);transition-delay:1.4s;}

  /* MAIN NAME BLOCK */"""
))

edits.append((
"""  </div>
</section>

<!-- COUNTDOWN -->""",
"""  </div>
</section>

<!-- CARTA -->
<section>
  <div class="wrap">
    <div class="carta reveal-block" id="cartaBlock">
      <div class="verse">
        "Porque yo sé los planes que tengo para ti —declara el Señor—, planes de bienestar y no de mal, para darte un futuro y una esperanza."
        <span class="verse-ref">Jeremías 29:11</span>
      </div>
      <p>Hay personas que llegan a este mundo para dejar una huella en cada corazón que conocen. Uma es una de ellas.</p>
      <p>Dios nos regaló una hija con un corazón noble, sensible y lleno de amor. Es de esas personas que abrazan con el alma, que se emocionan con las alegrías de los demás, que siempre está para su familia y sus amigos. Es una hija maravillosa, una nieta orgullosa de sus raíces, una amiga leal, una sobrina, ahijada y prima que entrega su cariño de la forma más sincera.</p>
      <p>Como papá y mamá, damos gracias a Dios por el privilegio de verla crecer y convertirse en la hermosa persona que es hoy.</p>
      <p>Con inmensa emoción queremos invitarlos a compartir este momento tan esperado. Su presencia será un regalo para Uma y para nosotros, porque las personas que amamos son quienes hacen eternos los recuerdos más felices.</p>
    </div>
  </div>
</section>

<!-- COUNTDOWN -->"""
))

edits.append((
"""  // Countdown""",
"""  // Carta reveal on scroll
  (function(){
    var el = document.getElementById('cartaBlock');
    if(!el) return;
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          el.classList.add('in-view');
          obs.unobserve(el);
        }
      });
    }, {threshold:0.25});
    obs.observe(el);
  })();

  // Countdown"""
))

missing = []
for i, (old, new) in enumerate(edits):
    if old not in c:
        missing.append(i)
    else:
        c = c.replace(old, new, 1)

if missing:
    print("ATENCION: no se encontraron estos bloques (indices):", missing)
else:
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("OK: carta agregada con animacion de aparicion por parrafo.")
