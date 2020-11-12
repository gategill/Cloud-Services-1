All the programs to be tested are stored in the "programs" folder
Make sure the program has a main() function and a if __name__ == "__main__" condition
Use the hello_world.py as a template 
The simulatorjust runs the program as many times as required and records the time
It doesn't specify the input for the program, the program should have a way to do it itself
e.g., random.randint()

The "generated times" folder holds the text files for the simulation
Each time_text is saved with the name of the file and the number of iterations specified
e.g., "hello_world.py__5_iterations"
The first first row is the mean of the times
The second row is the standard deviation of the times
All the rest are individual runtimes for each iteration  


Argument Class:
The argparse module lets us specify inputs for a python file from the CMD

In the cmd, you specify the the number of iterations you want to run each program
e.g., >> python simulator.py -ni 1 5 10
This will run programA 1 time and record the times, then it will run programA 5 times and record the times, ...
Then it will run programB 1 time and record the results, ...
(This feature might be overkill, idk) 



Simulator Class:
The idea is that for each iteration, we run program and record the time it takes to execute
The runtimes are logged to a text file

get_time_folder(): 
Returns the path of the "generated times" folder which holds the time data

get_time_file(program, num_iterations):
Creates the name of the time text file based on the python file it's running and the number of iteration it's running
e.g., "hello_world.py__5_iterations"
And joins that name with the current path
Returns the text files' path

create_folder():
If the "generated times" folder already exists, it contains "old" data so it wil be deleted
Either way, a new and empty folder is created

get_program_names():
Returns a list of program names to be run
e.g., ["programA.py", ...]

get_program_path(program_name):
Given the name of a program as input it returns the program's path 

The flow of run_simulator():
create "generated times" folder
for program:
	for num_iterations:
		for iteration: 
			run program
			record time
		record times to text file



Run Simulator on Docker:

I have moved the dockerfiles and rquirments.txt into the simulator file and updated the CMD variable to run the
simulator.

To run a container on the docker files you must be in the simulator folder on your terminal

ie. pythontest/simulator

Then run the following to build and then run:

		docker build -t NameOfImage .
		(eg. docker build -t simtest/test1 .)

		docker run NameOfImage
		(eg. docker run simtest/test1)

NOTE:
NameOfImage is anything you want to call your image, it will only matter on your machine.
Docker convention is to use name/version but doesnt matter here really
