ALTER TABLE public.keyboards
    RENAME COLUMN switch to switch_id;
ALTER TABLE public.keyboards
    RENAME COLUMN keycap to keycap_id;
ALTER TABLE public.keyboards
    RENAME COLUMN layout to layout_id;