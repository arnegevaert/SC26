class Text:
    def insert(position: Position, text: str): ...
    def delete(start: Position, end: Position): ...
    def change_position(position: Position, num_chars: int): ...

class GUI:
    def backspace(self):
        self.text.delete(self.text.change_position(self.cursor, -1), self.cursor)

    def delete(self):
        self.text.delete(self.cursor, self.text.change_position(self.cursor, 1))
