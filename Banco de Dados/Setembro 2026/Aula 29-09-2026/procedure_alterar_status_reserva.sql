CREATE OR REPLACE PROCEDURE sp_alterar_status_reserva(
    p_id_reserva BIGINT,
    p_novo_status VARCHAR(20)
)

LANGUAGE plpgsql
AS $$

BEGIN
    IF p_novo_status NOT IN ('Confirmada', 'Hospedada', 'Concluída', 'Cancelada') THEN
        RAISE EXCEPTION 'Status inválido: %. Permitidos: Confirmada, Hospedada, Concluída, Cancelada.', p_novo_status;
    END IF;

    UPDATE reserva
    SET status = p_novo_status
    WHERE id_reserva = p_id_reserva;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Reserva com ID % não encontrada.', p_id_reserva;
    END IF;

    RAISE NOTICE 'Status da reserva % alterado para %.', p_id_reserva, p_novo_status;

END;
$$