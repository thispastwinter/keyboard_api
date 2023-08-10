CREATE OR REPLACE FUNCTION update_price()
RETURNS TRIGGER AS $$
BEGIN
    NEW.price = NEW.price_per_unit * NEW.unit_count;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_price_switches
BEFORE UPDATE OF price_per_unit, unit_count
ON public.switches
FOR EACH ROW
EXECUTE FUNCTION update_price();

CREATE TRIGGER trigger_update_price_keycaps
BEFORE UPDATE OF price_per_unit, unit_count
ON public.keycaps
FOR EACH ROW
EXECUTE FUNCTION update_price();