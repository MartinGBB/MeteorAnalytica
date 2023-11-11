from user_inputs import user_inputs
from utils.monts_data import months
from utils.max_avg_temperature import get_max_avg_temperature
from utils.hot_months_counter import get_hot_months_counter

monthly_data = {}

def weather_analysis():
  for month_index in range(3):
    month = user_inputs.get_month()
    temperature = user_inputs.get_temperature()

    monthly_data[month_index] = { 'month': months[month -1], 'temperature': temperature }

  get_max_avg_temperature(monthly_data)
  get_hot_months_counter(monthly_data)
    
try:
  weather_analysis()
except KeyboardInterrupt:
  print("\nPrograma interrompido manualmente.\nAté mais.")