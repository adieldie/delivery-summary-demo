from summary import calcular_resumo
import json
records=[dict(motoboy='Pessoa Exemplo A',taxa=5,pagavel=True,bairro='Zona fictícia',bairro_cadastrado=True),dict(motoboy='Pessoa Exemplo B',taxa=8,pagavel=True,bairro='Zona fictícia B',bairro_cadastrado=False),dict(motoboy='Pessoa Exemplo A',taxa=5,pagavel=False,bairro='Zona fictícia',bairro_cadastrado=True)]
print(json.dumps(calcular_resumo(records),ensure_ascii=False,indent=2))
