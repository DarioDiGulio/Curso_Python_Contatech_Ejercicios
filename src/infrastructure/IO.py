from abc import abstractmethod, ABC


class IO(ABC):

    @abstractmethod
    def input(self, text, data_type=str):
        pass

    @abstractmethod
    def output(self, text):
        pass

    @staticmethod
    def parse_text(text, data_type):
        if data_type is int:
            entry = int(text)
        elif data_type is float:
            entry = float(text)
        else:
            entry = str(text)
        return entry
