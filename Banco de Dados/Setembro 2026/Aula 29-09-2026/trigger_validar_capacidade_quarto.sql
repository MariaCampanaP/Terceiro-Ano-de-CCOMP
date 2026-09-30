CREATE OR REPLACE FUNCTION fn_validar_capacidade_quarto()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

DECLARE 
    v_capacidade INTEGER;

BEGIN
    SELECT tq.capacidade INTO v_capacidade
    FROM quarto q
    JOIN tipo_quarto tq ON q.id_tipo = tq.id_tipo
    WHERE q.id_quarto = NEW.id_quarto;

    IF NEW.quantidade_hospedes > v.capacidade THEN
        RAISES EXCEPTION 'A quantidade de hóspedes (%) excede a capacidade do quarto (%).',  NEW.quantidade_hospedes, v_capacidade;
    END IF;

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_validar_capacidade_quarto
BEFORE INSERT OR UPDATE ON reserva
FOR EACH ROW
EXECUTE FUNCTION fn_validar_capacidade_quarto();