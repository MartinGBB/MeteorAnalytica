def validate_month(value):
  if not(value >= 1 and value <= 12):
    raise ValueError("O valor do mês é inválido. Insira um número entre 1 e 12.")
  else:
    return value
