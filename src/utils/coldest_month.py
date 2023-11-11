def get_coldest_month(listOfValues):
  min_temperature = 0
  min_monthly_temperature = ""

  for data in listOfValues.values():
    temperature = data["temperature"]
    month = data["month"]
    
    if temperature < min_temperature:
      min_temperature = temperature
      min_monthly_temperature = month
      continue    

  print(f"\nMês menos quente do ano foi no mês de {min_monthly_temperature} com {min_temperature} graus.")
