def get_hottest_month(listOfValues):
  max_temperature = float("-inf")
  max_monthly_temperature = ""

  for data in listOfValues.values():
    temperature = data["temperature"]
    month = data["month"]
    
    if temperature > max_temperature:
      max_temperature = temperature
      max_monthly_temperature = month
      continue    

  print(f"Mês mais escaldante do ano foi no mês de {max_monthly_temperature} com {max_temperature} graus.")
