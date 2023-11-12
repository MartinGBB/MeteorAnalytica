from utils.calculations.max_avg_temperature import get_max_avg_temperature
from utils.calculations.hot_months_counter import get_hot_months_counter
from utils.calculations.hottest_month import get_hottest_month
from utils.calculations.coldest_month import get_coldest_month
from utils.calculations.coldest_month import get_coldest_month

monthly_data = {
  0: {'month': 'Janeiro', 'temperature': 34.3},
  3: {'month': 'Fevereiro', 'temperature': 31},
  1: {'month': 'Março', 'temperature': 36},
  4: {'month': 'Maio', 'temperature': 31.7},
  5: {'month': 'Abril', 'temperature': 31},
  6: {'month': 'Junho', 'temperature': 20},
  7: {'month': 'Julho', 'temperature': 17},
  8: {'month': 'Agosto', 'temperature': 42.5},
  9: {'month': 'Setembro', 'temperature': 37},
  10: {'month': 'Outubro', 'temperature': 32.1},
  11: {'month': 'Novembro', 'temperature': 33},
  12: {'month': 'Dezembro', 'temperature': 23}
}

def mock_weather_analysis():
  get_max_avg_temperature(monthly_data)
  get_hot_months_counter(monthly_data)
  get_hottest_month(monthly_data)
  get_coldest_month(monthly_data)

mock_weather_analysis()