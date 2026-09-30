CREATE OR REPLACE PROCEDURE sp_colocar_quarto_manutencao(
    p_id_quarto INTEGER
)

LANGUAGE plpgsql
AS $$

BEGIN
    UPDATE quarto
    SET status = 'Manutenção'
    WHERE id_quarto = p_id_quarto;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Quarto com ID % não encontrado.', p_id_quarto;
    END IF;

    RAISE NOTICE 'Quarto % alterado para status Manutenção.', p_id_quarto;

END;
$$