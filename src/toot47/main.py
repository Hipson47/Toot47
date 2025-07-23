import typer
import uvicorn
from src.toot47.config import settings

cli_app = typer.Typer()

@cli_app.command()
def run():
    """
    Starts the FastAPI server, prompting for OpenAI key if not set.
    """
    if not settings.OPENAI_API_KEY:
        api_key = typer.prompt("Please enter your OpenAI API key", hide_input=True)
        if not api_key:
            typer.echo("OpenAI API key is required to run the application.")
            raise typer.Exit(code=1)
        settings.OPENAI_API_KEY = api_key

    uvicorn.run(
        "toot47.api.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
    )

def main():
    cli_app()

if __name__ == "__main__":
    main()