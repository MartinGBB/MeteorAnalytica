def validate_month(month):
  if not(month >= 1 and month <= 12):
    raise ValueError("O valor do mês é inválido. Insira um número entre 1 e 12.")
  
  return month

def validate_temperature(temperature):
  if not(temperature >= -60 and temperature <= 50):
    raise ValueError("A temperatura tem que estar dentro de um intervalo de -60 graus à +50 graus.")
    
  return temperature
