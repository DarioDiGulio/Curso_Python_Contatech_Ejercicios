from src.infrastructure.IO import IO


class IOStub(IO):
    def __init__(self):
        self.output_text = ''
        self.input_text: str = ''
        self.returns = 0

    def input(self, text, data_type=str):
        if self.input_text == '':
            self.input_text = text
        result = self.input_text.split(',')[self.returns]
        self.returns += 1
        return IO.parse_text(result, data_type)

    def output(self, text):
        if self.output_text != '':
            self.output_text += f'\n{text}'
        else:
            self.output_text = text
