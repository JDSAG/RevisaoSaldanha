from exceptions.exceptions import * 
from database.queries import * 
from database.connection import * 
#Validação do usuario
def validation_email(email:str):    
    if "@" not in email or ".com" not in email:
        raise EmailException('Validation Error: Formato de Email inválido')

def validation_password(password:str):
    if not password.isdigit() and len(password) != 8 : 
        raise PasswordException('Validation Error: Senha deve conter 8 dígitos.')  

