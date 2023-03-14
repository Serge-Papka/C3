class animals():
    def __init__(self):
        self.Покрытие = "Кожа"


class cat(animals):
    pass
    # def __init__(self):
        # super.__init__()
    # pass


A = cat()
print(A.Покрытие)