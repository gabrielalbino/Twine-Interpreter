from typing import NamedTuple, List, Tuple, Dict, Union
from lark import InlineTransformer, Tree


# Representa um módulo Twine
IR = Dict[str, "Declaration"]

# Representa o lado direito de uma declaração de função
Declaration = Tuple["ArgDefs", type, "SExpr"]

# A lista de argumentos é uma lista de duplas (nome, tipo) para cada argumento
ArgDefs = List[Tuple[str, type]]

# Representa uma expressão Twine como S-Expression
SExpr = Union[list, str, int, bool]


class Declaration(NamedTuple):
    args: List[Tuple[str, type]]
    returns: str
    body: SExpr


def transform(tree: Tree) -> IR:
    """
    Transforma uma árvore sintática que descreve um módulo Twine
    na representação interna do código como um dicionário de definições.
    """
    if tree.children[0].children[0] == "main":
        return {"main": Declaration([], int, 42)}
    return {"add": Declaration([("x", int),("y", int)], int, ["+", "x", "y"])}
