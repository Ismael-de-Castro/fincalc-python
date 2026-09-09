# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros compostos."""
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_aposentadoria(
    patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_parcela_price(
    valor_emprestimo: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    i = taxa_mensal / 100
    parcela = (
        valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
    )
    return parcela


def calcular_depreciacao_linear(valor_inicial:
float, valor_residual: float, vida_util_anos: int) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    return (valor_inicial - valor_residual) / vida_util_anos


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    montante_simples = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples (R$ 1.000 a 5% por 2 anos): R$ {montante_simples:.2f}")

    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos (R$ 1.000 a 5% por 2 anos): R$ {montante_comp:.2f}")

    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")

    vf = calcular_valor_futuro(500.0, 1.0, 12)
    print(f"Valor Futuro (R$ 500/mês a 1% por 12 meses): R$ {vf:.2f}")

    imposto = calcular_irrf(3000.0)
    print(f"IRRF Estimado (Salário R$ 3.000,00): R$ {imposto:.2f}")

    parcela = calcular_parcela_price(10000.0, 1.5, 12)
    print(
        "Parcela Tabela Price (R$ 10.000 a 1,5% a.m. em 12x): "
        f"R$ {parcela:.2f}"
    )

    valor_depreciacao = calcular_depreciacao_linear(10000.0, 2000.0, 5)
    print(f"Depreciação Anual Calculada: R$ {valor_depreciacao:.2f}")
    