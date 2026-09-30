CREATE OR REPLACE FUNCTION fn_notificar_reserva_alto_valor()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    INSERT INTO notificacao (id_reserva, mensagem)
    VALUES (NEW.id_reserva, 'Reserva de alto valor registrada! ID: ' || NEW.id_reserva || ' | Valor: R$ ' || NEW.valor_total);

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_notificar_reserva_alto_valor
AFTER INSERT ON reserva
FOR EACH ROW
WHEN (NEW.valor_total > 2000)
EXECUTE FUNCTION fn_notificar_reserva_alto_valor();