CREATE OR REPLACE FUNCTION fn_notificar_cancelamento_aluno()

RETURNS TRIGGER

LANGUAGE plpgsql
AS $$

BEGIN
    INSERT INTO notificacao (id_reserva, mensagem)
    VALUES (NEW.id_reserva, 'Atenção: A reserva ' || NEW.id_reserva || ' mudou para Cancelada.');

    RETURN NEW;

END;
$$

CREATE TRIGGER trg_notificar_cancelamento_aluno
AFTER UPDATE OF status ON reserva
FOR EACH ROW
WHEN (OLD.status <> 'Cancelada' AND NEW.status = 'Cancelada')
EXECUTE FUNCTION fn_notificar_cancelamento_aluno();