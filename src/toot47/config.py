from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Typed application settings"""
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra="ignore"
    )

    OPENAI_API_KEY: str | None = None
    NEO4J_URI: str = "bolt://neo4j:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASS: str = "password"

    # Server settings
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_RELOAD: bool = True

    @property
    def prompts_dir(self) -> "Path":
        """Returns the path to the prompts directory."""
        return Path(__file__).parent.parent.parent / "prompts"

    def load_system_prompt(self) -> str:
        """Loads the system prompt."""
        try:
            with open(self.prompts_dir / "system.md", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "You are a helpful AI assistant."

settings = Settings() 