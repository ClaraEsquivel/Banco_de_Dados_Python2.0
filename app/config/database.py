from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros de conexão com o BD MySQL
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço/caminhio para conexão com BD MySQL
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()


# Gerenciando sessão
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit  # se der certo, faz commit
    except Exception as erro:
        db.rollback()  # se der errado, desfaz a operação.
        raise erro  # lança a exceção, informando o erro.
    finally:
        db.close()  # garante o fechamento da sessão.
