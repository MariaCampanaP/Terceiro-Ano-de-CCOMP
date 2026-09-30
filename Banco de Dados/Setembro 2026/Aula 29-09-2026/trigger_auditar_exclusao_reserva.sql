CREATE OR REPLACE FUNCTION fn_auditar_exclusao_reserva()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    INSERT INTO auditoria_exclusao_reserva (id_reserva, status_anterior, valor_anterior)
    VALUES (OLD.id_reserva, OLD.status, OLD.valor_total);

    RETURN OLD;

END;
$$

CREATE TRIGGER trg_auditar_exclusao_reserva
AFTER DELETE ON reserva
FOR EACH ROW
EXECUTE FUNCTION fn_auditar_exclusao_reserva();