from typing import List

from app.services.build_data import BuildData
from app.models.switch import Switch
from app.services.supabase_service import SupabaseService

client = SupabaseService.get_client()


class SwitchService(BuildData):
    @classmethod
    def get_all(cls) -> List[Switch]:
        switches_data = client.table("switches").select("*, type(*)").execute()

        return switches_data["data"]

    @classmethod
    def get_one(cls, id: str) -> Switch:
        switch_data = client.table("switches").select("*, type(*)").eq("id", id).single().execute()

        return switch_data["data"]
