import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

edits = []

edits.append((
"""<meta name="description" content="Invitación a los XV años de Uma - 11 de Octubre 2026" />""",
"""<meta name="description" content="Invitación a los XV años de Uma - 11 de Octubre 2026" />
<meta name="color-scheme" content="dark" />"""
))

edits.append((
"""  :root{
    --bg: #0a0a0a;""",
"""  :root{
    color-scheme: dark;
    --bg: #0a0a0a;"""
))

edits.append((
"""  .btn{
    display:inline-block;margin-top:40px;padding:14px 34px;border:1px solid var(--gold);
    color:var(--gold-soft);text-decoration:none;letter-spacing:.15em;text-transform:uppercase;
    font-size:.78rem;border-radius:2px;transition:all .3s ease;background:transparent;cursor:pointer;font-family:'Montserrat',sans-serif;
  }""",
"""  .btn{
    -webkit-appearance:none;appearance:none;
    display:inline-block;margin-top:40px;padding:14px 34px;border:1px solid var(--gold);
    color:var(--gold-soft);text-decoration:none;letter-spacing:.15em;text-transform:uppercase;
    font-size:.78rem;border-radius:2px;transition:all .3s ease;background:transparent;cursor:pointer;font-family:'Montserrat',sans-serif;
  }"""
))

edits.append((
"""  form.rsvp .btn{align-self:center;margin-top:12px;background:none;}""",
"""  form.rsvp .btn{align-self:center;margin-top:12px;background:none;color:var(--gold-soft);}"""
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
    print("OK: boton de RSVP corregido.")
