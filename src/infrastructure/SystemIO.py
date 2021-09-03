from src.infrastructure.IO import IO


class SystemIO(IO):
    def input(self, text, data_type=str):
        entry = input(f"{text}\n")
        return IO.parse_text(entry, data_type)

    def output(self, text):
        print(text)
