All the programs to be tested are stored in the "programs" folder
Make sure the program has a main() function and a if __name__ == "__main__" condition
Use the hello_world.py as a template 
The simulation just runs the program as many times as required and records the time
It doesn't specify the input for the program, the program should have a way to do it itself
e.g., random.randint()



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

get_time_file():
Creates the name of the time text file based on the python file it's running and the number of iteration it's running
e.g., "hello_world.py__5"
And joins that name with the current path
Returns the text files' path

create_folder():
If the "generated times" folder already exists, it contains "old" data so it wil be deleted
Either way, a new empty folder is created

get_programs():
Returns a list of the programs to be run

The flow of run_simulation():
create "generated times" folder
for program:
	for num_iterations:
		for iteration: 
			run program
			record time
		record times, their mean and std to text file




