class Ensemble():
    def __init__(self, type, period):
        # self.name = name
        self.type = type
        self.period = period
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.type, self.period)
    def definitions(self):
        print(f"Classical ensembles from the {self.period} period include the {self.type}")

group = Ensemble('Orchestra', 'Romantic')
group.definitions()
