"""import sys
from antlr4 import *
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from antlr4.tree.Trees import Trees

def main(input_code):
    input_stream = InputStream(input_code)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.program()

    #print("Tree:")
    #print(Trees.toStringTree(tree, None, parser))

input_code = "
function procedure (choice, g1, g2){
    graph g;
    if (choice <= 0)(){ break;}
    switch (choice){
        case 1: g = g1 + g2; break;
        case 2: g = g1 & g2; break;
        case 3: g = g1 - g2; break;
        case 4: g = g1 / g2; break;
        case 5: g = g1 * g2; break;
    }
    return g;
}
result_graph = procedure (1, g1, g2);
"

main(input_code)
"""

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from antlr4.tree.Trees import Trees

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax Error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors


def main(input_code):
    input_stream = InputStream(input_code)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners() 
    parser.addErrorListener(error_listener)

    try:
        tree = parser.program()
        if error_listener.has_errors():
            print("Errors detected:")
            for error in error_listener.get_errors():
                print(error)
        else:
            print("Parsed successfully!")
            print("Tree:")
            print(Trees.toStringTree(tree, None, parser))
    except Exception as e:
        print(f"An exception occurred during parsing: {e}")


input_code = """
function procedure (choice, g1, g2){
    graph g;
    if (choice <= 0){ break;}
    switch (choice){
        case 1: g = g1 + g2; break;
        case 2: g = g1 & g2; break;
        case 3: g = g1 - g2; break;
        case 4: g = g1 / g2; break;
        case 5: g = g1 * g2; break;
    }
    return g;
}
result_graph = procedure (1, g1, g2);
"""

main(input_code)
