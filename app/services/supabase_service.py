from supabase_py import create_client, Client
from typing import TypedDict, List, Any
from app.config import Config

config = Config()
config.get_env_variables()

class QueryParameter(TypedDict):
    field_name: str
    value: str | int | float

class SupabaseService:
    url = config.get_supabase_url()
    key = config.get_supabase_key()

    @classmethod
    def get_client(cls) -> Client | None:
        return create_client(cls.url, cls.key)