from src.infrastructure.IO import IO


class IOStub(IO):
    def __init__(self):
        self.outputText = ''
        self.inputText: str = ''
        self.returns = 0

    def input(self, text, data_type=str):
        if self.inputText == '':
            self.inputText = text
        result = self.inputText.split(',')[self.returns]
        self.returns += 1
        return IO.parse_text(result, data_type)

    def output(self, text):
        if self.outputText != '':
            self.outputText += f'\n{text}'
        else:
            self.outputText = text
