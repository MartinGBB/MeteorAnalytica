from user_inputs import user_inputs

try:
  month = user_inputs.get_month()
  print(month)

  temperature = user_inputs.get_temperature()
  print(temperature)


except KeyboardInterrupt:
  print("\nPrograma interrompido manualmente.\nAté mais.")
