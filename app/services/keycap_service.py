from typing import List

from app.services.build_data import BuildData
from app.models.keycap import KeyCap
from app.services.supabase_service import SupabaseService

client = SupabaseService.get_client()


class KeyCapService(BuildData):
    @classmethod
    def get_all(cls) -> List[KeyCap]:
        keycaps_data = client.table("keycaps").select("*").execute()

        return keycaps_data["data"]

    @classmethod
    def get_one(cls, id: str) -> KeyCap:
        keycap_data = client.table("keycaps").select("*").eq("id", id).single().execute()

        return keycap_data["data"]
