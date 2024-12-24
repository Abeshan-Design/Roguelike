class Action:
    pass




class Escape(Action):
    pass




class Movement(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy