import typer
import uvicorn
from .config import settings

cli_app = typer.Typer()

@cli_app.command()
def run():
    """
    Starts the FastAPI server.
    """
    uvicorn.run(
        "toot47.api.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
    )

if __name__ == "__main__":
    cli_app()