from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Pydantic Settings automatically reads from a .env file and maps
    each field name to an environment variable (case-insensitive).

    Example:
        SUPABASE_URL in .env → settings.supabase_url in Python
    """

    # Supabase
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str

    # App
    environment: str = "development"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


# Single instance reused across the app
settings = Settings()
