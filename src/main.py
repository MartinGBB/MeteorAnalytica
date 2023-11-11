from user_inputs import user_inputs
from utils.max_avg_temperature import get_max_avg_temperature
from utils.monts_data import months

monthly_data = {}

def weather_analysis():
  for month_index in range(3):
    month = user_inputs.get_month()
    temperature = user_inputs.get_temperature()

    monthly_data[month_index] = { 'month': months[month -1], 'temperature': temperature }

  get_max_avg_temperature(monthly_data)
    
try:
  weather_analysis()
except KeyboardInterrupt:
  print("\nPrograma interrompido manualmente.\nAté mais.")