create table public.layouts (
  id uuid not null default gen_random_uuid (),
  name text not null,
  constraint layouts_pkey primary key (id)
) tablespace pg_default;