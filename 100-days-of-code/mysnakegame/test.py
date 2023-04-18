class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segment = []
        print("hello world")
        for pos in self.position:
            print(pos)

class Anaconda(Snake):
    def __init__(self):
        super().__init__()


joy = Anaconda()
