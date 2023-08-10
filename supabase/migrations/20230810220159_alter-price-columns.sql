ALTER TABLE public.switches
    ADD COLUMN unit_count int null,
    ADD COLUMN price_per_unit float null;

ALTER TABLE public.keycaps
    ADD COLUMN unit_count int null,
    ADD COLUMN price_per_unit float null;
