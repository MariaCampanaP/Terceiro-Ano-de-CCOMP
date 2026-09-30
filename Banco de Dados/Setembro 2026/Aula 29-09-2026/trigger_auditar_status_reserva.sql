CREATE OR REPLACE FUNCTION fn_auditar_status_reserva()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    IF OLD.status IS DISTINCT FROM NEW.status THEN
        INSERT INTO auditoria_status_reserva (id_reserva, status_anterior, status_novo)
        VALUES (NEW.id_reserva, OLD.status, NEW.status);
    END IF;

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_auditar_status_reserva
AFTER UPDATE OF status ON reserva
FOR EACH ROW
EXECUTE FUNCTION fn_auditar_status_reserva();