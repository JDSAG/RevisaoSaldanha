from database.connection import * 
from database.repositories.login import * 
from database.repositories.trip import * 

def main():
    '''Utilizará para testes''' 
    print(check_trip())


if __name__ == "__main__":
    main()