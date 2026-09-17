# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0:
<<<<<<< Updated upstream
        raise ValueError("Capital não pode ser negativo")
    if anos < 0:
        raise ValueError("Tempo não pode ser negativo")
=======
        raise ValueError("O capital inicial não pode ser negativo.")
    if anos < 0:
        raise ValueError("O tempo em anos não pode ser negativo.")

>>>>>>> Stashed changes
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


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto < 0:
        raise ValueError("Salário não pode ser negativo")
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
    # Validação de entradas inválidas
    if valor_emprestimo <= 0 or meses <= 0 or taxa_mensal < 0:
        raise ValueError("O valor do empréstimo e os meses devem ser maiores que zero.")
    # Caso limite: Taxa de juros nula (divisão direta)
    if taxa_mensal == 0:
        return valor_emprestimo / meses
    # Cálculo padrão da Tabela Price
    i = taxa_mensal / 100
    parcela = valor_emprestimo * (i * (1 + i) ** meses) / (((1 + i) ** meses) - 1)
    return parcela


def calcular_depreciacao_linear(
    valor_inicial: float, valor_residual: float, vida_util_anos: int
) -> float:
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
