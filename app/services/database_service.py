from typing import Generic, TypeVar, List, Literal
from pydantic import BaseModel
from httpx import AsyncClient

from app.config import Config

config = Config()
config.get_env_variables()

Data = TypeVar("Data")
Table = Literal["keyboards", "switches", "keycaps", "switch_types", "layouts"]


class RelatedFieldBase(BaseModel):
    name: str
    alias: str


class RelatedField(RelatedFieldBase):
    nested_fields: RelatedFieldBase | None = None


class DatabaseService(Generic[Data]):
    url = config.get_supabase_url()
    key = config.get_supabase_key()

    @staticmethod
    # This function handles building our parameters for the select query, should this grow more complex
    # the method for querying our db should likely change
    def _build_parameters(
        fields: List[str] | None = None,
        related_fields: List[RelatedField] | None = None,
    ):
        parameters = ["*"]

        if fields:
            # If there are fields specified, we replace the default wildcard with the user defined fields
            parameters = fields

        # Here we process any related fields
        if related_fields:
            for field in related_fields:
                # We build the reference to the foreign key along with the defined alias
                name = f"{field.alias}:{field.name}"
                if field.nested_fields is not None:
                    # If there are nested fields, we need to build the reference for those
                    nested_name = (
                        f"{field.nested_fields.alias}:{field.nested_fields.name}"
                    )
                    # We grab all fields on the related table and all fields on the nested table
                    parameters.append(f"{name}(*, {nested_name}(*))")
                else:
                    # We grab all fields on the related table
                    parameters.append(f"{name}(*)")

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
        fields: List[str] | None = None,
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
