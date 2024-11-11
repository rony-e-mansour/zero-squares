class Cell:

    def __init__(self, type=None, color=None, top_cell=None):
        self.type = type
        self.color = color
        self.top_cell = top_cell

    def __str__(self):

        if self.type == "wall":
            return "🔳"
        elif self.type == "mixed":
            if (self.color == "red" and self.top_cell.color == "blue") or (
                self.top_cell.color == "red" and self.color == "blue"
            ):
                return "🟪"
            elif (self.color == "red" and self.top_cell.color == "green") or (
                self.top_cell.color == "red" and self.color == "green"
            ):
                return "🟫"
            elif (self.color == "green" and self.top_cell.color == "blue") or (
                self.top_cell.color == "green" and self.color == "blue"
            ):
                return "🟨"
            else:
                return "❌"

        elif self.type == "empty":
            return "🔲"

        elif self.type == None:
            return "  "

        elif self.type == "goal":
            if self.color == "red":
                return "🟥"
            elif self.color == "blue":
                return "🟦"
            elif self.color == "green":
                return "🟩"
            elif self.color == "orange":
                return "🟧"
            else:
                return "❌"

        elif self.type == "player":
            if self.color == "red":
                return "🔴"
            elif self.color == "blue":
                return "🔵"
            elif self.color == "green":
                return "🟢"
            elif self.color == "orange":
                return "🟠"
            else:
                return "❌"

        else:
            return "⬜"

    def __repr__(self):
        return self.__str__()
