create table
  public.keycaps (
    id uuid not null default gen_random_uuid (),
    name character varying(255) null,
    brand_name character varying(255) null,
    material character varying(100) null,
    constraint keycaps_pkey primary key (id)
  ) tablespace pg_default;