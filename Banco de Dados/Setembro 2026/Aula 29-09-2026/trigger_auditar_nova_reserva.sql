CREATE OR REPLACE FUNCTION fn_auditar_nova_reserva()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    INSERT INTO auditoria_nova_reserva (id_reserva, id_hospede, id_quarto, valor_total)
    VALUES (NEW.id_reserva, NEW.id_hospede, NEW.id_quarto, NEW.valor_total);

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_auditar_nova_reserva
AFTER INSERT ON reserva
FOR EACH ROW
EXECUTE FUNCTION fn_auditar_nova_reserva();