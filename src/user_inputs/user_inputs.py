import user_inputs.validations as validations
from input_handling.input_handler import handle_user_input

def get_month():
  value_type = int
  validation = validations.validate_month
  messageErrorType = "O valor do mês é inválido. Deve ser um número inteiro."
  prompt = "\nDigite o numero do mês: "

  month = handle_user_input(value_type, validation, prompt, messageErrorType)
  return month
