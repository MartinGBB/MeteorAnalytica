def get_coldest_month(listOfValues):
  min_temperature = float("inf")
  min_monthly_temperature = ""

  for data in listOfValues.values():
    temperature = data["temperature"]
    month = data["month"]
    
    if temperature < min_temperature:
      min_temperature = temperature
      min_monthly_temperature = month
      continue    

  print(f"Mês menos quente do ano foi no mês de {min_monthly_temperature} com {min_temperature} graus.")
