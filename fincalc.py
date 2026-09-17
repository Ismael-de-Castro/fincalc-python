# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0:
        raise ValueError("Capital não pode ser negativo")
    if anos < 0:
        raise ValueError("Tempo não pode ser negativo")
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante

def calcular_aposentadoria(
        patrimonio_atual: float, aporte_mensal: float,
        anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    montante_simples = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples (R$ 1.000 a 5% por 2 anos): R$ {montante_simples:.2f}")

    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos (R$ 1.000 a 5% por 2 anos): R$ {montante_comp:.2f}")

    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto < 0:
        raise ValueError("Salário não pode ser negativo")

    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44

    return 0.0
