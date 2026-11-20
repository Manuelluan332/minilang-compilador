"""Testes do lexer com entradas INVÁLIDAS.

Resultado esperado: tokenizar() lança LexerError, com a mensagem e a
posição (linha, coluna) indicadas em cada teste.
"""

import pytest

from src.lexer import LexerError, tokenizar


def erro(codigo):
    with pytest.raises(LexerError) as info:
        tokenizar(codigo)
    return info.value


def test_caractere_invalido_arroba():
    e = erro("x = @;")
    assert "caractere inválido '@'" in e.mensagem
    assert (e.linha, e.coluna) == (1, 5)


def test_outros_caracteres_fora_do_alfabeto():
    for c in "#$%&?\"'^~|[]":
        assert "caractere inválido" in erro(f"x {c} y").mensagem


def test_numero_seguido_de_letra():
    e = erro("valor = 1x + 2;")
    assert "número seguido de letra: '1x'" in e.mensagem
    assert (e.linha, e.coluna) == (1, 9)


def test_numero_seguido_de_identificador_longo():
    assert "'12abc3'" in erro("12abc3").mensagem


def test_exclamacao_isolada():
    e = erro("x ! y")
    assert "'!' isolado" in e.mensagem
    assert (e.linha, e.coluna) == (1, 3)


def test_exclamacao_no_fim_da_entrada():
    assert "'!' isolado" in erro("!").mensagem


def test_comentario_de_bloco_nao_fechado():
    e = erro("x = 1;\n/* comentário sem fim")
    assert "comentário de bloco não fechado" in e.mensagem
    # a posição apontada é a do início do comentário
    assert (e.linha, e.coluna) == (2, 1)


def test_comentario_de_bloco_com_asterisco_final_mas_sem_barra():
    assert "não fechado" in erro("/* abc *").mensagem


def test_abertura_de_comentario_sem_fechamento_imediato():
    assert "não fechado" in erro("/*").mensagem
    assert "não fechado" in erro("/*/").mensagem


def test_erro_em_linha_posterior():
    e = erro("x = 1;\ny = 2;\nz = @;")
    assert (e.linha, e.coluna) == (3, 5)