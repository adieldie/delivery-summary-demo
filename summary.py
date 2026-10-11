from collections import defaultdict
from typing import Any

def calcular_resumo(registros: list[dict[str, Any]]) -> dict[str, Any]:
    por_motoboy: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"qtd_total": 0, "qtd_5": 0, "qtd_8": 0, "total": 0.0}
    )
    for registro in registros:
        if not registro.get("pagavel"):
            continue
        taxa = float(registro.get("taxa", 0))
        motoboy = str(registro.get("motoboy") or "Não identificado")
        linha = por_motoboy[motoboy]
        linha["qtd_total"] += 1
        linha["qtd_5"] += int(abs(taxa - 5.0) < 0.01)
        linha["qtd_8"] += int(abs(taxa - 8.0) < 0.01)
        linha["total"] = round(linha["total"] + taxa, 2)

    linhas = [{"motoboy": nome, **dados} for nome, dados in sorted(por_motoboy.items())]
    return {
        "motoboys": linhas,
        "qtd_total": sum(item["qtd_total"] for item in linhas),
        "qtd_5": sum(item["qtd_5"] for item in linhas),
        "qtd_8": sum(item["qtd_8"] for item in linhas),
        "total": round(sum(item["total"] for item in linhas), 2),
        "pedidos_no_extrato": len(registros),
        "bairros_nao_cadastrados": sorted(
            {
                str(item["bairro"])
                for item in registros
                if not item["bairro_cadastrado"] and item["taxa"] > 0
            }
        ),
    }
