import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select

from .config import settings
from .db import engine
from .models import User, Post, SQLModel
from pamps.security import HashedPassword, get_password_hash  # Importe a função de hashing

main = typer.Typer(name='Pamps CLI')

@main.command()
def shell():
    """"Opens interative shell"""

    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "User": User,
        "Post": Post
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython
        start_ipython(argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars)
    except ImportError:
        import code
        code.InteractiveConsole(_vars).interact()

@main.command()
def user_list():
    """"List All Users"""
    table = Table(title="Pamps Users")
    fields = ['username', 'email']
    for header in fields:
        table.add_column(header, style='magenta')
    
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        for user in users:
            table.add_row(user.username, user.email)
    
    Console().print(table)

@main.command(name="create-user")
def create_user(email: str, username: str, password: str):
    """Create a new user"""
    hashed_password = get_password_hash(password)  # Gere o hash da senha
    with Session(engine) as session:
        user = User(email=email, username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        typer.echo(f"User {username} created successfully!")

@main.command(name="reset-db")
def reset_db(
    force: bool = typer.Option(False, "--force", "-f", help="Run with no confirmation")
):
    """Resets the database tables"""
    force = force or typer.confirm("Are you sure?")
    if force:
        SQLModel.metadata.drop_all(engine)