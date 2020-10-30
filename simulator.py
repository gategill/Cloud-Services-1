import time
import os
import argparse


class Argument:
    def __init__(self):
        self.program = None
        self.inputs = None
        
        self.parsed_args = self.parse_args()
        self.build_config()

    
    def parse_args(self):
        parser = argparse.ArgumentParser(description = "Simulator Configurations")

        parser.add_argument("-pr", "--set_program", nargs = "?", default = "hello_world.py", type = str)
        parser.add_argument("-in", "--set_inputs", nargs = "?", default = 1, type = int)
        return parser.parse_args()
        
    
    def build_config(self):
        self.program = self.parsed_args.set_program
        self.inputs = self.parsed_args.set_inputs



class Simulator:
    argument = Argument()
    
    def __init__(self):
        self.run_simulation()
       
        
        
    def get_path(self):
        return os.path.join(os.getcwd(), "generated times")
    
    
    def get_file_name(self):
        return self.get_path()
    
    
    def create_folder(self):
        if not os.path.exists(self.get_path()):
            os.mkdir(self.get_path())
        
        
    def run_simulation(self):
        self.create_folder()
        file_path = os.path.join(self.get_path(), "times_{}.txt".format(self.argument.program))
        times = open(file_path, "a")
        
        for i in range(self.argument.inputs):
            tic = time.time()
            #self.argument.program()
            print("Hello World")
            toc = time.time()
            
            time_passed = toc - tic
            times.write(str(time_passed) + "\n")
            
        times.close()
  


def main():
    Simulator()  
            
                
if __name__ == '__main__':
    main()