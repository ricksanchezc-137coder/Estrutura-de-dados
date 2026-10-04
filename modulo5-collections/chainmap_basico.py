from collections import ChainMap

padrao = {"cor": "azul", "tamanho": 10}
usuario = {"cor": "verde"}

cfg = ChainMap(usuario, padrao)
print(cfg["cor"], cfg["tamanho"])
print(len(cfg), list(cfg))
print(cfg.maps)

cfg["fonte"] = "mono"
print(usuario)
print(padrao)

del cfg["cor"]
print(cfg["cor"])
print(usuario)
filho = cfg.new_child({"cor": "vermelho"})
print(filho["cor"], cfg["cor"])
padrao["tamanho"] = 99
print(cfg["tamanho"])
