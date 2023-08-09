create type led_direction as enum ('north', 'south');
create table public.keyboards (
  id uuid not null default gen_random_uuid (),
  name text null,
  brand_name text null,
  color_way text [] null,
  led boolean null default false,
  hot_swap boolean null default false,
  price double precision null,
  num_of_pins integer null,
  led_direction public.led_direction null,
  switch uuid null,
  keycap uuid null,
  layout uuid null,
  constraint keyboards_pkey primary key (id),
  constraint keyboards_keycap_fkey foreign key (keycap) references keycaps (id),
  constraint keyboards_layout_fkey foreign key (layout) references layouts (id),
  constraint keyboards_switch_fkey foreign key (switch) references switches (id),
  constraint keyboards_num_of_pins_check check ((num_of_pins = any (array [3, 5])))
) tablespace pg_default;