# Resumo de entregas com dados sintéticos

**Estágio: experimental / em teste. Demonstração parcial sanitizada, não pronta para produção.**

Extrato de agregação de registros: agrupamento por entregador, contagem de registros pagáveis, soma de taxas e alerta de zonas não cadastradas. Categorias de 5 e 8 são exemplos fictícios.

## Estágio
Demonstração local de um módulo existente, com dados sintéticos. Não é uma cópia completa do sistema operacional nem um produto pronto para produção.

## Executar
Python 3.10 ou superior. Sem dependências externas. Dentro desta pasta:

```sh
python demo.py
python -m unittest -v
```

## Arquitetura e limites
Não inclui dashboard, integração, nomes reais, cobrança ou pagamento. Usa float e arredondamento conforme algoritmo de origem: demonstração, não motor contábil. Entradas devem conter o esquema mostrado em demo.py; não há validação completa de dados malformados.

Nenhum acesso à rede, configuração operacional, histórico Git, base de dados ou artefato binário é distribuído. Exemplos e testes foram escritos para esta demonstração. Nenhuma licença de redistribuição foi presumida; o responsável deve definir a licença antes de promover reutilização de terceiros.
