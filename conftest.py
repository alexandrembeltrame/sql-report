import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.connection import Base
from src.core.config import Settings


@pytest.fixture(scope="function")
def db():
    """
    Fixture que cria um banco de dados em memória para testes isolados.
    Cada teste recebe uma sessão limpa e independente.
    """
    # Usar SQLite em memória para testes rápidos e isolados
    engine = create_engine("sqlite:///:memory:", echo=False)
    
    # Criar todas as tabelas
    Base.metadata.create_all(bind=engine)
    
    # Criar sessão
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()
        # Limpar todas as tabelas após o teste
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def test_settings():
    """
    Fixture que retorna as configurações de teste.
    """
    return Settings()
