"""Testes inválidos do interpretador (erros semânticos).

Resultado esperado: cada caso lança ErroSemantico com a mensagem indicada.
  - buscar variável nunca definida -> "variável 'z' não definida"   (S1)
"""

import pytest

from src.interpreter import ErroSemantico, TabelaSimbolos


def test_buscar_variavel_nao_definida():
    tabela = TabelaSimbolos()
    with pytest.raises(ErroSemantico, match="variável 'z' não definida"):
        tabela.buscar("z")


def test_erro_informa_posicao():
    tabela = TabelaSimbolos()
    with pytest.raises(ErroSemantico) as erro:
        tabela.buscar("z", linha=3, coluna=7)
    assert erro.value.linha == 3
    assert "linha 3, coluna 7" in str(erro.value)
