def get_hot_months_counter(listfTemperatures):
  hot_months = 0

  for data in listfTemperatures.values():
    temperature = data['temperature']

    if temperature > 38:
      hot_months += 1
      continue

  if hot_months > 1:
    print(f"Teve {hot_months} meses escaldantes.")
  elif hot_months == 0:
    print("Não teve meses escaldantes")
  else:
    print(f"Teve apenas um mês escaldante.")
