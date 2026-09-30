CREATE OR REPLACE FUNCTION fn_auditar_valor_diaria()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    IF OLD.valor_diaria IS DISTINCT FROM NEW.valor_diaria THEN
        INSERT INTO auditoria_valor_diaria (id_tipo, valor_anterior, valor_novo)
        VALUES (NEW.id_tipo, OLD.valor_diaria, NEW.valor_diaria);
    END IF;

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_auditar_valor_diaria
AFTER UPDATE OF valor_diaria ON tipo_quarto
FOR EACH ROW
EXECUTE FUNCTION fn_auditar_valor_diaria();