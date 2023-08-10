ALTER TABLE public.switches
ADD temp_price FLOAT;

UPDATE public.switches
SET temp_price = price_per_unit * unit_count;

ALTER TABLE public.switches
RENAME COLUMN price TO old_price;

ALTER TABLE public.switches
RENAME COLUMN temp_price TO price;

ALTER TABLE public.switches
DROP COLUMN old_price;

ALTER TABLE public.keycaps
ADD temp_price FLOAT;

UPDATE public.keycaps
SET temp_price = price_per_unit * unit_count;

ALTER TABLE public.keycaps
RENAME COLUMN price TO old_price;

ALTER TABLE public.keycaps
RENAME COLUMN temp_price TO price;

ALTER TABLE public.keycaps
DROP COLUMN old_price;

