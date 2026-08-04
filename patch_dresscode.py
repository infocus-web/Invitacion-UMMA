import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

edits = []

edits.append((
"""  .palette{display:flex;justify-content:center;gap:22px;margin-top:44px;flex-wrap:wrap;}
  .swatch{display:flex;flex-direction:column;align-items:center;gap:10px;}
  .swatch .dot{width:52px;height:52px;border-radius:50%;border:1px solid var(--line);}""",
"""  .palette{display:flex;justify-content:center;gap:22px;margin-top:28px;flex-wrap:wrap;}
  .swatch{display:flex;flex-direction:column;align-items:center;gap:10px;}
  .swatch .dot{width:52px;height:52px;border-radius:50%;border:1px solid var(--line);}
  .dresscode-group{margin-top:40px;}
  .dresscode-group:first-of-type{margin-top:44px;}
  .dresscode-label{
    display:inline-block;background:var(--gold-soft);color:#0a0a0b;font-weight:700;
    font-size:1.2rem;padding:9px 30px;border-radius:30px;font-family:'Montserrat',sans-serif;
  }
  .dot-wrap{position:relative;display:inline-block;}
  .no-badge{
    position:absolute;top:-10px;right:-16px;background:#8a4a26;color:#ffb98a;font-weight:800;
    font-size:.65rem;padding:3px 9px;border-radius:5px;transform:rotate(18deg);letter-spacing:.05em;
    box-shadow:0 2px 5px rgba(0,0,0,.4);text-transform:uppercase;
  }"""
))

edits.append((
"""    <p style="color:var(--text-dim);margin-top:10px;">Elegante noche, en tonos que acompañen la paleta de la fiesta.</p>
    <div class="palette">
      <div class="swatch"><div class="dot" style="background:#1b2a4a;"></div><span>Azul marino</span></div>
      <div class="swatch"><div class="dot" style="background:#8a8f98;"></div><span>Gris</span></div>
      <div class="swatch"><div class="dot" style="background:#c7cad1;"></div><span>Plata</span></div>
      <div class="swatch"><div class="dot" style="background:#111318;"></div><span>Negro</span></div>
      <div class="swatch"><div class="dot" style="background:#f3f2ee;"></div><span>Blanco</span></div>
    </div>
  </div>
</section>""",
"""    <p style="color:var(--text-dim);margin-top:10px;">Elegante noche, en tonos que acompañen la paleta de la fiesta.</p>

    <div class="dresscode-group">
      <div class="dresscode-label">Mujeres</div>
      <div class="palette">
        <div class="swatch"><div class="dot" style="background:#1b2a4a;"></div><span>Azul marino</span></div>
        <div class="swatch"><div class="dot" style="background:#8a8f98;"></div><span>Gris</span></div>
        <div class="swatch"><div class="dot" style="background:#c7cad1;"></div><span>Plata</span></div>
        <div class="swatch">
          <div class="dot-wrap">
            <div class="dot" style="background:#111318;"></div>
            <span class="no-badge">No</span>
          </div>
          <span>Negro</span>
        </div>
        <div class="swatch"><div class="dot" style="background:#f3f2ee;"></div><span>Blanco</span></div>
      </div>
    </div>

    <div class="dresscode-group">
      <div class="dresscode-label">Hombres</div>
      <div class="palette">
        <div class="swatch"><div class="dot" style="background:#1b2a4a;"></div><span>Azul marino</span></div>
        <div class="swatch"><div class="dot" style="background:#8a8f98;"></div><span>Gris</span></div>
        <div class="swatch"><div class="dot" style="background:#c7cad1;"></div><span>Plata</span></div>
        <div class="swatch"><div class="dot" style="background:#111318;"></div><span>Negro</span></div>
        <div class="swatch"><div class="dot" style="background:#f3f2ee;"></div><span>Blanco</span></div>
      </div>
    </div>
  </div>
</section>"""
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
    print("OK: codigo de vestimenta separado por Mujeres/Hombres.")
