class Todo:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item): 
        self.items.append(item)

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}')"

    def __str__(self):
       return self.name 
    
    def __len__(self):
        pass