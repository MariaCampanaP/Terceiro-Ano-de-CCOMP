CREATE OR REPLACE FUNCTION fn_validar_datas_reserva()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    IF NEW.data_checkout <= NEW.data_checkin THEN
        RAISE EXCEPTION 'Data de checkout (%) deve ser estritamente maior que a data check-in (%).', NEW.data_checkout, NEW.data_checkin;
    END IF;

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_validar_datas_reserva
BEFORE INSERT OR UPDATE ON reserva
FOR EACH NOW
EXECUTE FUNCTION fn_validar_datas_reserva(); 