from database.connection import * 
from utils.login import * 
from database.repositories.trip import * 

def main():
    '''Utilizará para testes''' 
    update_date_trip(2,1,1)
    print(check_trip())


if __name__ == "__main__":
    main()