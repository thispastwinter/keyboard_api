from typing import Generic, TypeVar, List, Literal, Optional
from pydantic import BaseModel
from httpx import AsyncClient

from app.config import Config

config = Config()
config.get_env_variables()

Data = TypeVar("Data")
Table = Literal["keyboards", "switches", "keycaps", "switch_types", "layouts"]
Fields = List[str]


class RelatedField(BaseModel):
    name: str
    alias: Optional[str] = None
    fields: Optional[Fields] = None
    related_fields: Optional[List["RelatedField"]] = None


class DatabaseService(Generic[Data]):
    url = config.get_supabase_url()
    key = config.get_supabase_key()

    @classmethod
    # This function handles building our parameters for the select query, should this grow more complex
    # the method for querying our db should likely change
    def _build_parameters(
        cls,
        fields: Fields | None = None,
        related_fields: List[RelatedField] | None = None,
    ):
        parameters = ["*"]

        if fields:
            # If there are fields specified, we replace the default wildcard with the user defined fields
            parameters = fields

        # Here we recursively process any related fields to the nth number of related_fields
        if related_fields:
            for field in related_fields:
                # We build the reference to the foreign key along with the defined alias
                name = f"{field.alias}:{field.name}" if field.alias else field.name
                # We build the nested params
                nested_parameters = cls._build_parameters(
                    fields=field.fields, related_fields=field.related_fields
                )
                # We append the nested params
                parameters.append(f"{name}({nested_parameters})")

        return ",".join(parameters)

    @classmethod
    def get_client(cls):
        assert cls.url and cls.key, "Url and key must be defined!"
        headers = {"apiKey": cls.key}
        return AsyncClient(headers=headers, base_url=cls.url)

    @classmethod
    async def get_all(
        cls,
        table: Table,
        fields: Fields | None = None,
        related_fields: List[RelatedField] | None = None,
    ) -> List[Data]:
        client = cls.get_client()
        parameters = cls._build_parameters(fields=fields, related_fields=related_fields)

        res = await client.get(f"/{table}?select={parameters}")

        return res.json()

    @classmethod
    async def get_one(
        cls,
        table: Table,
        id: str,
        fields: List[str] | None = None,
        related_fields: List[RelatedField] | None = None,
    ) -> Data:
        client = cls.get_client()
        parameters = cls._build_parameters(fields=fields, related_fields=related_fields)

        res = await client.get(f"/{table}?select={parameters}?limit=1?id={id}")

        return res.json()[0]
