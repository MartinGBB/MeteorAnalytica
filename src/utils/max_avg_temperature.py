def get_max_avg_temperature(listOfTemperatures):

  sumTemperature = 0

  for data in listOfTemperatures.values():
    temperatures = data['temperature']
    sumTemperature += temperatures

  average = round(sumTemperature/len(listOfTemperatures), 2)
  
  return average
