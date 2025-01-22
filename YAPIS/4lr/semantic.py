import sys
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from generated.ExprParserListener import ExprParserListener
from generated.ExprParserVisitor import ExprParserVisitor
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4 import *
class SemanticError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"Semantic error at line {line}, column {column}: {message}")


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, value):
        self.symbols[name] = value

    def lookup(self, name):
        return self.symbols.get(name, None)

    def __repr__(self):
        return str(self.symbols)

class SymbolTable:
    def __init__(self):
        # Список для поддержания областей видимости
        self.scopes = [{}]  # Начинаем с глобальной области видимости

    def define(self, name, value):
        current_scope = self.scopes[-1]
        current_scope[name] = value

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def __repr__(self):
        return str(self.scopes)

class SemanticAnalyzer(ExprParserVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()

    def get_context_info(self, ctx):
        token = ctx.start
        return token.line, token.column

    def raise_error(self, message, ctx):
        line, column = self.get_context_info(ctx)
        raise SemanticError(message, line, column)

    def visitAnoun(self, ctx):
        try:
            if ctx.types():
                var_type = ctx.types().getText().upper()
                var_name = ctx.ID().getText()
                if self.symbol_table.lookup(var_name) is not None:
                    self.raise_error(f"Variable '{var_name}' already declared", ctx)
                self.symbol_table.define(var_name, var_type)

            elif ctx.GRAPH(): 
                graph_name = ctx.ID().getText()
                if self.symbol_table.lookup(graph_name) is not None:
                    self.raise_error(f"Graph '{graph_name}' already declared", ctx)
                self.symbol_table.define(graph_name, "GRAPH")
                
                for node in ctx.node():
                    node_name = node.getText()
                    if self.symbol_table.lookup(node_name) is None:
                        self.symbol_table.define(node_name, "NODE")
                for arc in ctx.arc():
                    arc_name = arc.getText()
                    if self.symbol_table.lookup(arc_name) is None:
                        self.symbol_table.define(arc_name, "ARC")

            elif ctx.ARC():
                arc_name = ctx.ID().getText()
                node1 = ctx.node(0).getText()
                node2 = ctx.node(1).getText()
                if (self.symbol_table.lookup(node1) is None or self.symbol_table.lookup(node2) is None) or (self.symbol_table.lookup(node1) != "NODE" or self.symbol_table.lookup(node2) != "NODE"):
                    self.raise_error(f"Undefined nodes in arc: {node1}, {node2}", ctx)
                self.symbol_table.define(arc_name, "ARC")

        except Exception as e:
            self.raise_error(f"Error processing declaration: {e}", ctx)

    def visitFunction(self, ctx):
        func_name = ctx.ID().getText()
        if self.symbol_table.lookup(func_name) is not None:
            self.raise_error(f"Function '{func_name}' already declared", ctx)
        self.symbol_table.define(func_name, "FUNCTION")
        for param in ctx.ID()[1:]:  
            self.symbol_table.define(param.getText(), "PARAM")

    def visitOperation(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        op = ctx.operation().getText()
        
        if op == "+" or op == "-" or op == "*":
            if (left != "GRAPH" or right != "GRAPH") and (left != "PARAM" or right != "PARAM"):
                self.raise_error(f"Operation '{op}' requires both operands to be graphs", ctx)
            return "GRAPH"
        elif op == "&" or op == "/" or op == "|":
            if left != "GRAPH" or right != "GRAPH":
                self.raise_error(f"Operation '{op}' requires both operands to be graphs", ctx)
            return "GRAPH"
        elif op == "and" or op == "or":
            if left != "BOOL" or right != "BOOL":
                self.raise_error(f"Logical operation '{op}' requires both operands to be booleans", ctx)
            return "BOOL"
        elif op == "==" or op == "!=" or op == "<" or op == ">" or op == "<=" or op == ">=":
            if left != "INT" or right != "INT":
                self.raise_error(f"Comparison operation '{op}' requires both operands to be integers", ctx)
            return "BOOL"

        return None
    
    def visitDef(self, ctx):
        func_name = ctx.ID(0).getText() 
        
        if self.symbol_table.lookup(func_name) is not None:
            self.raise_error(f"Function '{func_name}' is already defined", ctx)

        self.symbol_table.define(func_name, "FUNCTION")

        param_names = [param.getText() for param in ctx.ID()[1:]] 
        for param in param_names:
            
            self.symbol_table.define(param, "PARAM")

        self.symbol_table.enter_scope()  
        for stat in ctx.stat():
            self.visit(stat) 
        self.symbol_table.exit_scope() 


    def visitExpr(self, ctx):
        if ctx.ID(): 
            var_name = ctx.ID().getText()
            if self.symbol_table.lookup(var_name) is None:
                self.raise_error(f"Undefined variable: {var_name}", ctx)
            return self.symbol_table.lookup(var_name)

        elif ctx.operation():
            return self.visitOperation(ctx)

        elif ctx.INT():  
            return "INT"

        elif ctx.BREAK() or ctx.CONTINUE():  
            return "VOID"

        elif ctx.RETURN():  
            return self.visit(ctx.expr(0))


        elif ctx.func(): 
            func_name = ctx.func().ID().getText()
            if self.symbol_table.lookup(func_name) != "FUNCTION":
                self.raise_error(f"Undefined function: {func_name}", ctx)
            return "GRAPH"  

        return None

    def visitProgram(self, ctx):
        for child in ctx.getChildren():
            try:
                self.visit(child)
            except SemanticError as e:
                print(e)
        return None

def main(input_code):
    lexer = ExprLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()

    analyzer = SemanticAnalyzer()
    try:
        analyzer.visit(tree)
        print("Symbol table:", analyzer.symbol_table)
    except SemanticError as e:
        print(e)


input_code = """node e1; node e2; node e3; node e4;
arc a1 = < e1, e2>; arc a2 = < e3, e4>;
graph g1 = [nodes : (e1, e2, e3, e4), arcs : (a1, a2)];
graph g2 = [nodes : (e1, e2, e3, e4),  arcs : (<e1, e3>, <e2,e3>,<e3,e4>, <e4,e2> )];


function procedure (graph x, graph y){
    graph g;
    g = x + a1;
    return g;
}

result_graph = procedure (g1, g2);

"""

if __name__ == "__main__":
    main(input_code)
