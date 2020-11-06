import time
import os
import argparse
import numpy as np
import shutil
import subprocess


class Argument:
    def __init__(self):
        self.iterations = None
        
        self.parsed_args = self.parse_args()
        self.build_config()

    
    def parse_args(self):
        parser = argparse.ArgumentParser(description = "Simulator Configurations")

        parser.add_argument("-ni", "--set_iterations", nargs = "+", required = True, default = 1, type = int,      
                            help = "Set number and sizes of iterations, required, e.g., -ni 1 5 10")
    
        return parser.parse_args()
        
    
    def build_config(self):
        self.iterations = self.parsed_args.set_iterations


class Simulator:
    argument = Argument()


    def __init__(self):
        self.run_simulator()
       
        
    def get_time_folder(self):
        return os.path.join(os.getcwd(), "generated_times")
    
    
    def get_time_file(self, program, num_iterations):
        file_name = "{}__{}_iterations.txt".format(program, num_iterations)
        file_path = os.path.join(self.get_time_folder(), file_name)
        return file_path


    def create_folder(self):
        if os.path.exists(self.get_time_folder()):
            shutil.rmtree(self.get_time_folder())
            
        os.mkdir(self.get_time_folder())
            
    
    def get_program_names(self):
        programs_folder = os.path.join(os.getcwd(), "programs")
        program_names = os.listdir(programs_folder)
        return program_names
    
                
    def get_program_path(self, program_name):
        programs_folder = os.path.join(os.getcwd(), "programs")
        program_path = os.path.join(programs_folder, program_name) 
        return program_path
    
    
    def run_simulator(self):
        self.create_folder()

        for program_name in self.get_program_names():
            for num_iterations in list(self.argument.iterations): # let know
                time_list = []
                
                for iteration in range(num_iterations):
                    tic = time.time()
                    program_path = self.get_program_path(program_name)
                    subprocess.call(["python", program_path])
                    toc = time.time()
                    
                    time_passed = toc - tic
                    time_list.append(time_passed)
                    
                mean = np.mean(time_list)
                std = np.std(time_list)
                
                with open(self.get_time_file(program_name, num_iterations), "a") as time_txt:
                    time_txt.write(str(mean) + "\n")
                    time_txt.write(str(std) + "\n\n")
                    
                    for a_time in time_list:
                        time_txt.write(str(a_time) + "\n")
                    

def main():
    Simulator()  
            
                
if __name__ == "__main__":
    main()