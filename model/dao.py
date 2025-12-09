from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = 'sqlite:///database/app.db' # URL do banco de dados SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=False) # Cria o engine do SQLAlchemy

Session = sessionmaker(bind=engine) # Cria a classe de sessão
Base = declarative_base() # Cria a classe base para os models do SQLAlchemy

def init_db():
    import model.user  # Importa os models para criar as tabelas
    Base.metadata.create_all(engine)  # Cria as tabelas no banco de dados
