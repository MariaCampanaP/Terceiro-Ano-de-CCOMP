CREATE OR REPLACE FUNCTION fn_validar_quarto_disponivel()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

DECLARE
    v_status VARCHAR(20);

BEGIN
    SELECT status INTO v_status
    FROM quarto
    WHERE id_quarto = NEW.id_quarto;

    IF v_status IN ('Manutenção', 'Inativo') THEN
        RAISE EXCEPTION 'Não é possível reservar o quarto %. Status atual: %.', NEW.id_quarto, v_status;
    END IF;

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_validar_quarto_disponivel
BEFORE INSERT ON reserva
FOR EACH ROW
EXECUTE FUNCTION fn_validar_quarto_disponivel();

