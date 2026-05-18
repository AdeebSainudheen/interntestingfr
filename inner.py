class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)  # Output: Outer Class

inner = outer.Inner() 
print(inner.name)  # Output: Inner Class