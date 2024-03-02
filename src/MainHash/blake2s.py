import hashlib as _hl
def path(p):
  h=_hl.blake2s()
  with open(p,"rb") as f:
    for i in f:
      h.update(i)
  return h.hexdigest()
def file(f):
  h=_hl.blake2s()
  for i in f:
    h.update(i)
  return h.hexdigest()
def text(t,encoding="utf-8"):
  return _hl.blake2s(str(t).encode(encoding)).hexdigest()
def bytes(b):
  return _hl.blake2s(bytes).hexdigest()
