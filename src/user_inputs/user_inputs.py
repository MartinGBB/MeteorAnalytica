import user_inputs.validations as validations
from input_handling.input_handler import handle_user_input

def get_month():
  value_type = int
  validation = validations.validate_month
  messageErrorType = "O valor do mês é inválido. Deve ser um número inteiro."
  prompt = "\nDigite o numero do mês: "

  month = handle_user_input(value_type, validation, prompt, messageErrorType)
  return month

def get_temperature():
  value_type = float
  validation = validations.validate_temperature
  messageErrorType = "O valor da temperatura é inválido. Deve ser um número."
  prompt = "\nDigite a temperatura: "

  temperature = handle_user_input(value_type, validation, prompt, messageErrorType)
  return temperature
