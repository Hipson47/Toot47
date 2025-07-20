import fire
from fastapi import FastAPI
from . import graph_builder, qa

# --- CLI ---

class Toot47CLI:
    """Toot47 Command Line Interface"""

    def graph_build(self, data_dir: str = "data/"):
        """Builds the knowledge graph from documents."""
        graph_builder.build_graph(data_dir)

    def ask(self, question: str):
        """Asks a question to the Graph RAG agent."""
        agent = qa.GraphAgent()
        answer = agent.ask(question)
        print(answer)

# --- FastAPI App ---

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# --- Main entry point ---

def main():
    fire.Fire(Toot47CLI)

if __name__ == '__main__':
    main()