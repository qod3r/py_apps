class DefaultList(list):
    def __init__(self, default_value=5):
        super().__init__(self)
        self.default = default_value
    
    def __getitem__(self, idx):
        try:
            return super().__getitem__(idx)
        except IndexError:
            return self.default


a = DefaultList('a number')
a.extend([1, 2, 3, 4])

print(a)
print(f"a[2]: {a[2]}")
print(f"a[-1]: {a[-1]}")
print(f"a[1000]: {a[1000]}")
    

