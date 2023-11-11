import sys
import validations

def ask_retry():
    user_input = input("\nDeseja tentar novamente? (S - tentar novamente / Qualquer tecla - sair): ")
    if user_input.upper() != 'S':
      print("\nAté mais...")
      sys.exit(1)

def handle_inputs(input_type, func_validation, prompt, messageErrorType):
  while True:
    user_input = input(prompt)
    try:
      validated_input = input_type(user_input)
      return func_validation(validated_input)
    except ValueError as error:
      if "invalid literal" in str(error):
        print(messageErrorType)
      else:
        print(error)
      ask_retry()


def get_month():
  value_type = int
  validation = validations.validate_month
  messageErrorType = "O valor do mês é inválido. Deve ser um número inteiro."
  prompt = "\nDigite o numero do mês: "

  month = handle_inputs(value_type, validation, prompt, messageErrorType)
  return month
