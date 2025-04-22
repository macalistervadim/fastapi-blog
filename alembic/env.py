from logging.config import fileConfig

from sqlalchemy import pool

from alembic import context
from src.core.config import settings
from src.models.post import Base

# this is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your models here
target_metadata = Base.metadata

# URL из settings
db_url = settings.DATABASE_URL


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Run migrations in online mode."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    """In this scenario we need to create an AsyncEngine by hand."""
    from sqlalchemy.ext.asyncio import create_async_engine

    # Create an AsyncEngine
    connectable = create_async_engine(db_url, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def run_migrations_online():
    """Run migrations in 'online' mode."""
    from asyncio import run

    # Run the async migrations
    run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
