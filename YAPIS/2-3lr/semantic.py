from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from generated.ExprListener import ExprListener


# Семантический анализатор
class SemanticAnalyzer(ExprListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = {}  # Таблица символов для проверки переменных
        self.errors = []

    def enterVarDecl(self, ctx: ExprParser.VarDeclContext):
        # Объявление переменной
        var_name = ctx.ID().getText()
        if var_name in self.symbol_table:
            self.errors.append(f"Semantic Error: Variable '{var_name}' is already declared.")
        else:
            self.symbol_table[var_name] = None  # Добавляем переменную в таблицу

    def enterAssign(self, ctx: ExprParser.AssignContext):
        # Проверка использования переменной
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            self.errors.append(f"Semantic Error: Variable '{var_name}' is not declared.")

    def enterReturnStmt(self, ctx: ExprParser.ReturnStmtContext):
        # Проверка возвращаемого значения
        expr = ctx.expr()
        if expr is None:
            self.errors.append("Semantic Error: Return statement must return a value.")

    def enterFunctionDecl(self, ctx: ExprParser.FunctionDeclContext):
        # Начало области видимости функции
        function_name = ctx.ID().getText()
        if function_name in self.symbol_table:
            self.errors.append(f"Semantic Error: Function '{function_name}' is already declared.")
        self.symbol_table[function_name] = {"type": "function", "params": []}  # Сохраняем функцию

    def exitProgram(self, ctx: ExprParser.ProgramContext):
        # Вывод ошибок после завершения разбора программы
        if self.errors:
            print("Semantic errors detected:")
            for error in self.errors:
                print(error)
        else:
            print("Semantic analysis completed successfully.")


def main(input_code):
    # Лексический и синтаксический анализ
    input_stream = InputStream(input_code)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.program()

    # Семантический анализ
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)


# Тестовые входные данные
input_code = """
function procedure (choice, g1, g2){
    graph g;
    g = g1 + g2;
    return g;
}
result_graph = procedure(1, g1, g2);
"""

main(input_code)
