import time
import os
import argparse
import numpy as np
import shutil

class Argument:
    def __init__(self):
        self.iterations = None
        
        self.parsed_args = self.parse_args()
        self.build_config()

    
    def parse_args(self):
        parser = argparse.ArgumentParser(description = "Simulator Configurations")

        parser.add_argument("-ni", "--set_iterations", nargs = "+", required = True, default = 1, type = int,      
                            help = "Set number and sizes of iterations, required, eg -ni 1 5 10")
    
        return parser.parse_args()
        
    
    def build_config(self):
        self.iterations = self.parsed_args.set_iterations



class Simulator:

    argument = Argument()

    def __init__(self):
        self.run_simulation()
       
        
    def get_time_folder(self):
        return os.path.join(os.getcwd(), "generated times")
    
    
    def get_time_file(self, program, num_iterations):
        file_name =  "{}__{}_iterations.txt".format(program, num_iterations)
        file_path = os.path.join(self.get_time_folder(), file_name)
        return file_path


    def create_folder(self):
        if os.path.exists(self.get_time_folder()):
            shutil.rmtree(self.get_time_folder())
            
        os.mkdir(self.get_time_folder())
            
            
    def get_programs(self):
        program_folder = os.path.join(os.getcwd(), "programs")
        programs = os.listdir(program_folder)
        return programs


    def run_simulation(self):
        self.create_folder()

        for program in self.get_programs():
            time_list = []
            
            for num_iterations in list(self.argument.iterations):
                for iteration in range(num_iterations):
                    tic = time.time()
                    os.system(program) 
                    toc = time.time()
                    
                    time_passed = toc - tic
                    time_list.append(time_passed)
                    
                mean = np.mean(time_list)
                std = np.std(time_list)
                
                with open(self.get_time_file(program, num_iterations), "a") as time_txt:
                    time_txt.write(str(mean) + "\n")
                    time_txt.write(str(std) + "\n\n")
                    
                    for a_time in time_list:
                        time_txt.write(str(a_time) + "\n")
                    

def main():
    Simulator()  
            
                
if __name__ == "__main__":
    main()