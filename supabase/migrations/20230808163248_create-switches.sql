create table public.switches (
  id uuid not null default gen_random_uuid (),
  name character varying(255) null,
  brand_name character varying(255) null,
  total_travel character varying(50) null,
  pre_travel character varying(50) null,
  num_of_pins integer null,
  type uuid null,
  constraint switches_pkey primary key (id),
  constraint switches_type_fkey foreign key (type) references switch_types (id),
  constraint switches_num_of_pins_check check ((num_of_pins = any (array [3, 5])))
) tablespace pg_default;