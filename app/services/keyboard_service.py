from typing import List

from app.services.build_data import BuildData
from app.models.keyboard import KeyboardFull, KeyboardPartial
from app.services.supabase_service import SupabaseService

client = SupabaseService.get_client()


class KeyboardService(BuildData):
    @classmethod
    def get_all(cls) -> List[KeyboardPartial]:
        keyboards_data = client.table("keyboards").select("*").execute()

        return keyboards_data["data"]

    @classmethod
    def get_one(cls, id: str) -> KeyboardFull:
        keyboard_data = (
            client.table("keyboards")
            .select(
                "id, name, brand_name, color_way, led, hot_swap, price, num_of_pins, led_direction, switch:switch_id(*, type(*)), keycap:keycap_id(*), layout:layout_id(*)"
            )
            .eq("id", id)
            .single()
            .execute()
        )

        return keyboard_data["data"]
