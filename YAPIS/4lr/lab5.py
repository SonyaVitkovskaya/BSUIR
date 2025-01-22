import sys
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from generated.ExprParserListener import ExprParserListener
from generated.ExprParserVisitor import ExprParserVisitor
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4 import *
from collections import deque

def depth_first_search(graph, start_node, end_node):

    visited, path, found = set(), [], False

    def dfs(node):
        nonlocal found
        if found: return
        if node == end_node:
            found = True
            return
        visited.add(node)
        for arc in graph.arcs:
            if arc[0] == node and arc[1] not in visited:
                path.append(arc)
                dfs(arc[1])
                if found: return
                path.pop() 

    dfs(start_node)

    if not found:
        print( "No path exists")
        return "GRAPH", Graph()

    nodes_in_path = {start_node, end_node}.union(node for arc in path for node in arc)
    return  "GRAPH", Graph(nodes=nodes_in_path, arcs=path)

def breadth_first_search(graph, start_node, end_node):
    queue, visited = deque([(start_node, [])]), set() 

    while queue:
        current_node, path = queue.popleft()
        if current_node in visited: continue
        visited.add(current_node)

        if current_node == end_node:
            nodes_in_path = {start_node, end_node}.union(node for arc in path for node in arc)
            return "GRAPH", Graph(nodes=nodes_in_path, arcs=path)

        for arc in graph.arcs:
            if arc[0] == current_node and arc[1] not in visited:
                queue.append((arc[1], path + [arc]))

    print ("No path exists")
    return "GRAPH", Graph()


def shortest_path(graph, start_node, end_node):
    import heapq
    queue = [(0, start_node, [])]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0

    while queue:
        cost, current_node, path = heapq.heappop(queue)

        if current_node == end_node:
            nodes_in_path = {start_node, end_node}.union(node for arc in path for node in arc)
            return Graph(nodes=nodes_in_path, arcs=path)

        for arc in graph.arcs:
            if arc[0] == current_node:
                next_node = arc[1]
                new_cost = cost + 1 

                if new_cost < distances[next_node]:
                    distances[next_node] = new_cost
                    heapq.heappush(queue, (new_cost, next_node, path + [arc]))

    print ("No path exists")
    return "GRAPH", Graph()


class SemanticError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"Semantic error at line {line}, column {column}: {message}")

class Graph:
    def __init__(self, nodes=None, arcs=None):
        self.nodes = nodes if nodes else set()
        self.arcs = arcs if arcs else []

    def __repr__(self):
        return f"Graph(nodes={self.nodes}, arcs={self.arcs})"

    def __add__(self, other):
        if not isinstance(other, Graph):
            raise TypeError("Can only add two Graph objects")
        return Graph(self.nodes | other.nodes, self.arcs | other.arcs)

    def __and__(self, other):
        if not isinstance(other, Graph):
            raise TypeError("Can only intersect two Graph objects")
        return Graph(self.nodes & other.nodes, self.arcs & other.arcs)

    def __sub__(self, other):
        if not isinstance(other, Graph):
            raise TypeError("Can only subtract two Graph objects")
        return Graph(self.nodes - other.nodes, self.arcs - other.arcs)

    def __truediv__(self, other):
        if not isinstance(other, Graph):
            raise TypeError("Can only perform symmetric difference on Graph objects")
        return Graph(self.nodes ^ other.nodes, self.arcs ^ other.arcs)

    def __mul__(self, other):
        if not isinstance(other, Graph):
            raise TypeError("Can only perform product on two Graph objects")
        return Graph(self.nodes, self.arcs)

class SymbolTable:
    def __init__(self):
        self.nodes = set()
        self.arcs = {}
        self.scopes = [{}] 

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
        self.values = {}
        self.functions = {'depth_first_search':[('search_graph', 'GRAPH'), ('start_node', 'NODE'), ('end_node', 'NODE')], 
                          'breadth_first_search': [('search_graph', 'GRAPH'), ('start_node', 'NODE'), ('end_node', 'NODE')], 
                          'shortest_path':[('search_graph', 'GRAPH'), ('start_node', 'NODE'), ('end_node', 'NODE')]}
        self.function_bodies = {} 

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
                if var_type == "NODE": self.symbol_table.nodes.add(var_name)
                if var_type == "ARC": self.symbol_table.arcs[var_name] = None
                self.symbol_table.define(var_name, var_type)
                self.values[var_name] = var_name
                print(f"Declaring a variable {var_name}, type {var_type}")

            elif ctx.TYPE_INT():  
                var_name = ctx.ID().getText() 
                value = ctx.INT().getText() 
                if self.symbol_table.lookup(var_name) is not None: print(f"Rewriting {var_name}")
                self.symbol_table.define(var_name, "INT")
                try:
                    self.values[var_name] = int(value)
                except Exception as e:
                    self.raise_error("Not int", ctx)

            elif ctx.GRAPH(): 
                graph_name = ctx.ID().getText()
                if self.symbol_table.lookup(graph_name) is not None: self.raise_error(f"Graph '{graph_name}' already declared", ctx)
                self.symbol_table.define(graph_name, "GRAPH")
                new_graph = Graph()
                self.values[graph_name] = new_graph
                print(f"Declaring a variable {graph_name}, type GRAPH")

                graph_nodes, graph_arcs = set(), []

                if ctx.node(): 
                    for node in ctx.node():
                        node_name = node.getText()
                        if self.symbol_table.lookup(node_name) is None: self.raise_error(f"Node '{node_name}' is not declared", ctx)
                        graph_nodes.add(node_name)
            
                    for arc in ctx.arc():
                        node1, node2, arc_name = "", "", ""
                        if arc.node(): 
                            arc_name = arc.ID().getText()
                            node1 = arc.node(0).getText()
                            node2 = arc.node(1).getText()
                            if (self.symbol_table.lookup(node1) != "NODE" or self.symbol_table.lookup(node2) != "NODE"): self.raise_error(f"Undefined nodes in arc: {node1}, {node2}", ctx)
                            self.symbol_table.define(arc_name, "ARC")
                            self.symbol_table.arcs[arc_name] = [node1, node2]
                        else: 
                            arc_name = arc.ID().getText()
                            if self.symbol_table.lookup(arc_name) is None: self.raise_error(f"Arc '{arc_name}' is not declared", ctx)
                            [node1, node2] = self.symbol_table.arcs[arc_name]

                        if (not node1 in graph_nodes or not node2 in graph_nodes): self.raise_error(f"Undefined nodes for this graph in arc: {node1}, {node2}", ctx)
                        graph_arcs.append([node1, node2])

                    changed_graph = Graph(graph_nodes, graph_arcs)
                    self.values[graph_name] = changed_graph
                    print(f"Defining the value of {graph_name} {graph_nodes} {graph_arcs}")

                if ctx.expr():
                    type_, value = self.visitExpr(ctx.expr())
                    self.values[graph_name] = value
                    print(f"Defining the value of {graph_name} = {value}")
   
            elif ctx.ARC():
                arc_name = ctx.ID().getText()
                node1 = ctx.node(0).getText()
                node2 = ctx.node(1).getText()
                if (self.symbol_table.lookup(node1) is None or self.symbol_table.lookup(node2) is None) or (self.symbol_table.lookup(node1) != "NODE" or self.symbol_table.lookup(node2) != "NODE"):
                    self.raise_error(f"Undefined nodes in arc: {node1}, {node2}", ctx)
                self.symbol_table.define(arc_name, "ARC")
                self.symbol_table.arcs[arc_name] = [node1, node2]
                self.values[arc_name] = [node1, node2]

        except Exception as e:
            self.raise_error(f"Error processing declaration: {e}", ctx)

    def visitDef(self, ctx):
        func_name = ctx.ID(0).getText()

        if func_name in self.functions:
            self.raise_error(f"Function '{func_name}' already declared", ctx)

        param_names = [param.getText() for param in ctx.ID()[1:]]
        param_types = [ptype.getText().upper() for ptype in ctx.types()]

        if len(param_names) != len(param_types):
            self.raise_error(f"Function '{func_name}' parameter names and types mismatch", ctx)

        self.functions[func_name] = list(zip(param_names, param_types))
        self.function_bodies[func_name] = ctx

    def visitExpr(self, ctx, id = ""):
        if ctx.ID():
            var_name = ctx.ID().getText()
            var_type = self.symbol_table.lookup(var_name)
            if var_type is None:
                self.raise_error(f"Undefined variable: {var_name}", ctx)
            return var_type, self.values[var_name]
        
        if ctx.RETURN():
            if not ctx.expr(): self.raise_error("Return statement must have an expression", ctx)
            type_, self.return_value = self.visitExpr(ctx.expr(0)) 
            return type_, self.return_value
             
        elif ctx.INT():
            return "INT", int(ctx.INT().getText())

        elif ctx.operation():
            return self.visitOperation(ctx)

        elif ctx.func():
            func_name = ctx.func().ID().getText() if ctx.func().ID()  else ctx.func().or_func().getText()
            if func_name not in self.functions: self.raise_error(f"Undefined function: {func_name}", ctx)
        
            param_types = self.functions[func_name]
            args = ctx.func().expr()

            if len(param_types) != len(args): self.raise_error(f"Function '{func_name}' expects {len(param_types)} arguments, got {len(args)}", ctx)

            self.symbol_table.enter_scope()
            for (param_name, param_type), arg in zip(param_types, args):
                arg_type, arg_value = self.visit(arg)
                if arg_type != param_type: self.raise_error(f"Argument type mismatch for parameter '{param_name}', expected {param_type}, got {arg_type}", ctx)
                self.symbol_table.define(param_name, param_type)
                self.values[param_name] = arg_value
                print(f"Defining the value of parametr {param_name} = {arg_value}")

            if func_name == 'depth_first_search': return depth_first_search(self.values["search_graph"], self.values["start_node"], self.values["end_node"])
            elif func_name == 'breadth_first_search': return breadth_first_search(self.values["search_graph"], self.values["start_node"], self.values["end_node"])
            elif func_name == 'shortest_path': return shortest_path(self.values["search_graph"], self.values["start_node"], self.values["end_node"])

            function_body = self.function_bodies[func_name]

            self.return_value = None
            for stat in function_body.stat():
                self.visitStat(stat)
                if self.return_value:
                    return "", self.return_value

            self.symbol_table.exit_scope()

        return None, None

    def visitOperation(self, ctx):
        left_type, left = self.visit(ctx.expr(0))
        right_type, right = self.visit(ctx.expr(1))
        if ctx.ID():
            var_name = ctx.ID().getText()
            var_type = self.symbol_table.lookup(var_name)
            if var_type is None: self.raise_error(f"Undefined variable: {var_name}", ctx)
            return var_type
        
        if (left_type != "GRAPH" and left_type != "NODE") or (right_type != "GRAPH" and right_type!= "NODE"): self.raise_error(f"Operation requires both operands to be graphs", ctx)
        
        op = ctx.operation().getText()        

        if op == "+": new_graph = Graph(left.nodes | right.nodes, left.arcs + right.arcs)
        elif op ==  "-": new_graph = Graph(self.values[left].nodes - self.values[right].nodes, [arc for arc in self.values[left].arcs if not arc in self.values[right].arcs ])
        elif op == "/": new_graph = Graph(self.values[left].nodes ^ self.values[right].nodes, [arc for arc in (self.values[right].arcs + self.values[left].arcs) if not arc in self.values[left].arcs and not arc in self.values[right].arcs])
        elif op == "&": new_graph = Graph(self.values[left].nodes & self.values[right].nodes, [arc for arc in self.values[right].arcs if arc in self.values[left].arcs ])

        return "GRAPH", new_graph

    def visitProgram(self, ctx):
        for child in ctx.getChildren():
            if isinstance(child, ExprParser.DefContext):
                self.visitDef(child)

        for child in ctx.getChildren():
            try:
                if not isinstance(child, ExprParser.DefContext):
                    self.visit(child)
            except SemanticError as e:
                print(e)
        return None
    
    def visitStat(self, ctx):
        try:
            if ctx.ID() and ctx.expr():
                var_name = ctx.ID().getText()
                if self.symbol_table.lookup(var_name) is None: self.raise_error(f"Undefined variable '{var_name}'", ctx)
                
                value_type, value = self.visitExpr(ctx.expr(), var_name)
                expected_type = self.symbol_table.lookup(var_name)
                
                if value_type != expected_type: self.raise_error(f"Type mismatch: variable '{var_name}' is of type {expected_type}, but the expression evaluates to type {value_type}", ctx)
                print(f"Value of {var_name}: {value}")
                self.values[var_name] = value
                return None
            
            else:
                for child in ctx.getChildren():
                    if isinstance(child, ExprParser.DefContext):
                        self.visitDef(child)
                for child in ctx.getChildren():
                    try:
                        if not isinstance(child, ExprParser.DefContext):
                            self.visit(child)
                    except SemanticError as e:
                        print(e)
                return None
            
        except Exception as e:
            self.raise_error(f"Error processing statement: {e}", ctx)

def main():
    if len(sys.argv) == 1: input_file = "example_code.txt"
    else: input_file = sys.argv[1]
    print(input_file)
    input_code = FileStream(input_file)

    lexer = ExprLexer(input_code)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()

    analyzer = SemanticAnalyzer()
    try:
        analyzer.visit(tree)
        
    except SemanticError as e:
        print(e)

    #print(analyzer.values)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()