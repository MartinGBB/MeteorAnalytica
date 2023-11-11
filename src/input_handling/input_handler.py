import sys

def ask_retry():
    user_input = input("\nDeseja tentar novamente? (S - tentar novamente / Qualquer tecla - sair): ")
    if user_input.upper() != 'S':
      print("\nAté mais...")
      sys.exit(1)

def handle_user_input(input_type, func_validation, prompt, messageErrorType):
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
