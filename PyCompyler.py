from Lexer import Lexer

class PyCompiler:
    filename = ""
    extension = "splw"
    lexer = None
    _instance = None

    @staticmethod
    def getInstance():
        if PyCompiler._instance == None:
            PyCompiler('test_script')
        return PyCompiler._instance

    def __init__(self, filename: str):
        self.filename = filename
        PyCompiler._instance = self

    def run(self):
        raw_text = self.load()
        lexer = self.lexer = Lexer(raw_text)
        tokens = lexer.make_tokens()
        print(tokens)

    def load(self):
        raw_contents = open(self.filename+"."+self.extension,"r")
        raw_text = raw_contents.read()
        raw_contents.close()
        return raw_text

def main():
    compiler = PyCompiler("test_script")
    compiler.run()

if __name__ == "__main__":
    main()
