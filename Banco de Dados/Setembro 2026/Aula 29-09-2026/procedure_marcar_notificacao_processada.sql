CREATE OR REPLACE PROCEDURE sp_marcar_notificacao_processada(
    p_id_notidicacao BIGINT
)

LANGUAGE plpgsql
AS $$

BEGIN
    UPDATE notificacao
    SET processada = TRUE 
    WHERE id_notificacao = p_id_notificacao;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Notificação com ID % não encontrada.', p_id_notificacao;
    END IF;

    RAISE NOTICE 'Notificação % marcada como processada.', p_id_notificacao;

END;
$$
