class Hello_World:
    def __init__(self, i):
        self.i = i
        self.do_it()
        
        
    def do_it(self):
        print("hello world \n"*self.i)
        
hello = Hello_World(7)