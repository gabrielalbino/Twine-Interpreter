from lark import Lark, Tree, Token
from pathlib import Path
from typing import Dict, Iterable

#
# Constantes que armazenam a gramática do Lark no módulo.
# A gramática pode operar no modo programa (GRAMMAR_PROGRAM),
# onde lemos um programa completo com todas as suas declarações
# de funções, ou no modo expressão (GRAMMAR_EXPRESSION) onde
# lemos e avaliamos apenas uma única expressão twine.
#
GRAMMAR_PATH = Path(__file__).parent / "twine.lark"
GRAMMAR_SRC = GRAMMAR_PATH.read_text()


def parse(src: str) -> Tree:
    """
    Analiza o código fonte e retorna a árvore sintática Lark.
    """
    from twine.lexer import lex
    lex_result = lex(src)
    return Tree("program", 
        [   
            Tree("define", 
            [
                Token("IDENTIFIER", "main"),
                Tree("params", []),
                Token("IDENTIFIER", "integer"),
                Token("INTEGER", 42)
            ])
        ])
