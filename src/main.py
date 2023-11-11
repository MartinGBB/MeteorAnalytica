from user_inputs import user_inputs


months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
monthly_data = {}


try:

  for month_index in range(12):
    month = user_inputs.get_month()
    temperature = user_inputs.get_temperature()

    monthly_data[month_index] = { 'month': months[month -1], 'temperature': temperature }

  print(monthly_data)



except KeyboardInterrupt:
  print("\nPrograma interrompido manualmente.\nAté mais.")
