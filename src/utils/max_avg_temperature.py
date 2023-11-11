def get_max_avg_temperature(listOfValues):
  sumTemperature = 0

  for data in listOfValues.values():
    temperatures = data['temperature']
    sumTemperature += temperatures

  average = round(sumTemperature/len(listOfValues), 2)
  
  print(f"\nTemperatura média máxima anual é de {average} graus.")
