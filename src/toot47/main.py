from pathlib import Path
import typer
from . import graph_builder, qa

app = typer.Typer()

@app.command()
def graph_build(
    data_dir: Path = typer.Option("data/", help="Directory with source documents.")
):
    """Builds the knowledge graph from documents."""
    print(f"Building graph from: {data_dir}")
    graph_builder.build_graph(data_dir)
    print("Graph building complete.")

@app.command()
def ask(question: str):
    """Asks a question to the Graph RAG agent."""
    agent = qa.GraphAgent()
    answer = agent.ask(question)
    print(answer)

def main():
    app()

if __name__ == "__main__":
    main()