from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# URL de la base de datos
DATABASE_URL = "sqlite+aiosqlite:///./linksnap.db"

# Creamos el motor para ver los comandos de SQL en consola
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Creamos una función par obtener la sesión
async def get_session():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session