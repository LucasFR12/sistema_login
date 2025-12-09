from view.view import run
from model.dao import init_db

init_db() # Inicializa o banco de dados

if __name__ == "__main__":
    run()
