create table
  public.switch_types (
    id uuid not null default gen_random_uuid (),
    name text not null,
    constraint switch_types_pkey primary key (id)
  ) tablespace pg_default;