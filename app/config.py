import dotenv
import os

dotenv.load_dotenv()


class Config:
    supabase_url: str | None = None
    supabase_key: str | None = None
    _initialized = False

    @classmethod
    def get_env_variables(cls):
        cls.supabase_url = os.getenv("SUPABASE_URL")
        cls.supabase_key = os.getenv("SUPABASE_KEY")
        cls._initialized = True

    @classmethod
    def _check_initialized(cls):
        if not cls._initialized:
            raise RuntimeError(
                "Environment variables not initialized. Call get_env_variables() first."
            )

    @classmethod
    def get_supabase_url(cls):
        cls._check_initialized()
        return cls.supabase_url

    @classmethod
    def get_supabase_key(cls):
        cls._check_initialized()
        return cls.supabase_key
