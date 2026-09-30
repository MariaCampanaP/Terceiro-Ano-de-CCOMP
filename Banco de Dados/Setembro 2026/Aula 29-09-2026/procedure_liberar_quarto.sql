CREATE OR REPLACE PROCEDURE sp_liberar_quarto(
    p_id_quarto INTEGER
)

LANGUAGE plpgsql
AS $$

BEGIN
    UPDATE quarto
    SET status = 'Disponível'
    WHERE id_quarto = p_id_quarto;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Quarto com ID % não encontrado.', p_id_quarto;
    END IF;

    RAISE NOTICE 'Quarto % alterado para status Disponível.', p_id_quarto;

END;
$$