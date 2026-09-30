CREATE OR REPLACE PROCEDURE sp_aplicar_desconto_reserva(
    p_id_reserva BIGINT,
    p_percentual NUMERIC
)

LANGUAGE plpgsql
AS $$

DECLARE
    v_novo_valor NUMERIC(10, 2);

BEGIN
    IF p_percentual < 0 OR p_percentual > 100 THEN
        RAISE EXCEPTION 'Percentual de desconto inválido (%). Deve estar entre 0 e 100.', p_percentual;
    END IF;

    UPDATE reserva
    SET valor_total = ROUND(valor_total * (1 - p_percentual/100), 2)
    WHERE id_reserva = p_id_reserva
    RETURNING valor_total INTO v_novo_valor;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Reserva com ID % não encontrada.', p_id_reserva;
    END IF;

    RAISE NOTICE 'Desconto aplicado com sucesso. Novo valor total da reserva %: R$ %', p_id_reserva, v_novo_valor;

END;
$$