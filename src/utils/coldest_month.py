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

get_coldest_month({0: {'month': 'Janeiro', 'temperature': 22.0}, 1: {'month': 'Março', 'temperature': 12.0}, 2: {'month': 'Fevereiro', 'temperature': 42.0}, 3: {'month': 'Maio', 'temperature': 44.0}, 4: {'month': 'Abril', 'temperature': 33.0}, 5: {'month': 'Junho', 'temperature': 23.0}, 6: {'month': 'Julho', 'temperature': 34.0}, 7: {'month': 'Agosto', 'temperature': 33.2}, 8: {'month': 'Setembro', 'temperature': 23.0}, 9: {'month': 'Outubro', 'temperature': -43.22}, 10: {'month': 'Novembro', 'temperature': 11.4}, 11: {'month': 'Dezembro', 'temperature': -40.0}})
