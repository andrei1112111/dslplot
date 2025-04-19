from antlr4 import *
import matplotlib.pyplot as plt

from dsplot.Gramar.generated.GraphPlotLexer import GraphPlotLexer
from dsplot.Gramar.generated.GraphPlotParser import GraphPlotParser
from dsplot.CodeGenerator import CodeGenerator


class Query:
    def __init__(self, query, variables=None):
        if variables is None:
            variables = {}

        self.plt = None
        self.__python_code = None

        self._query = query
        self._variables = variables
        self.__generator = CodeGenerator()

        self.__parse(query)

    def show(self):
        plt.show()

    def save(self, filename="output.png"):
        plt.savefig(filename)

    def code(self):
        return self.python_code

    def __execute_and_get_var(self, code_str, var_name='img'):
        local_vars = {}
        exec(code_str, self._variables, local_vars)

        return local_vars

    def __parse(self, input_code):
        input_stream = InputStream(input_code)
        lexer = GraphPlotLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GraphPlotParser(token_stream)
        tree = parser.parse()

        self.python_code = self.__generator.visit(tree)

        self.plt = self.__execute_and_get_var(self.python_code).get("plt", None)
