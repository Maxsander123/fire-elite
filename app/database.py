import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://fireelite:fireelite@db:5432/fireelite"
)

# Session-Zeitzone fest auf Europe/Berlin: Postgres liefert TIMESTAMPTZ sonst in
# der Server-Zeitzone (im Docker-Image UTC) zurück, und Templates/Formulare, die
# per strftime formatieren, zeigen die Zeit dann 1h (Winter) bzw. 2h (Sommer)
# zu früh an.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"options": "-c timezone=Europe/Berlin"},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
