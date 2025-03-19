class SuperArray:
    def __init__(self, lim_inf, lim_sup):
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.array = [0 for i in range(lim_inf, lim_sup)]

    def set(self, index, value):
        if index < self.lim_inf or index >= self.lim_sup: raise Exception("Invalid index")
        self.array[index] = value
        
    def get(self, index):
        if index < self.lim_inf or index >= self.lim_sup: raise Exception("Invalid index")
        return self.array[index]