# input_processing.py
# Heemin Kang, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light_status = 'green'
        self.ped_status = 'no'
        self.veh_status = 'no'
        

    # The function update_status() updates the light, pedestrian, and vechicle status based on what the user inputs.
    #
    # Prompts the user to input changes for the light, pedestrian, or vehicle status, and updates
    # the respective attributes accordingly. 
    #
    # It takes the object of class Sensor as the argument and returns the current status and 
    # action message based on the updated values. 
    def update_status(self): # You may decide how to implement the arguments for this function
        update_option = ''
        while update_option != '0': #while the user does not select 0, the menu is repeated
            # if user input = 0, the program stops running
            update_option = input("Are changes detected in the vision input?\n\
Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end program: ") 
            try:   #runs the following code
                if update_option == '1': #if user input is 1, show prompt to change light color
                    while True:
                        light_change = input("What change has been identified?: ") 
                        # if the user input is green, yellow, red, update the light status and run the print_message function
                        # prints action message and current status
                        if(light_change in ['green', 'yellow', 'red']): 
                            self.light_status = light_change
                            print_message(self)
                            break #goes back to the menu option
                        # if the user input is not green, yellow, red, print "Invalid vision change"
                        # and go back to the menu option prompt
                        else:
                            print("Invalid vision change.")
                            print_message(self)
                            break #goes back to the menu option prompt
                    continue #continues the out while loop. Goes back to menu option prompt
                elif update_option == '2': #if user inputs 2, prompt to change the pedestrian status
                    while True: 
                        ped_change = input("What change has been identified?: ") 
                        # if the user input is yes or no, update the pedestrian status and run the print_message function
                        # prints action message and current status
                        if(ped_change in ['yes', 'no']): 
                            self.ped_status = ped_change
                            print_message(self)
                            break #goes back to the menu option
                        else:
                            print("Invalid vision change.")
                            print_message(self)
                            break #goes back to the menu option
                    continue #goes back to the menu option
                elif update_option == '3':
                    while True:
                        veh_change = input("What change has been identified?: ")
                        # if the user input is yes or no, update the vehicle status and run the print_message function
                        # prints action message and current status 
                        if(veh_change in ['yes', 'no']):
                            self.veh_status = veh_change
                            print_message(self)
                            break #goes back to the menu option
                        else:
                            print("Invalid vision change.")
                            print_message(self)
                            break #goes back to the menu option
                    continue #goes back to the menu option
                elif update_option == '0': #if user input is 0, end the program
                    break #breaks the first while loop, ending the program
                else: #raises the ValueError when selection is not 1, 2, 3, or 0
                    raise ValueError("selection is not 1, 2, 3, or 0.")
            except ValueError: #When ValueError is encountered, print the following line
                print("you must select either 1, 2, 3, or 0.\n")
        
         
# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
#
# This function prints the action message and the current status of the Sensor
# The parameter is sensor and the argument going to be passed is an object of the class Sensor
# It returns an action message ("Proceed", "Caution", or "STOP") based on the current light, pedestrian, and vehicle status
# It also prints the current status of the traffic light, pedestrian, and vehicle.
def print_message(sensor):
    if(sensor.light_status == 'green' and sensor.ped_status == 'no' and sensor.veh_status == 'no'):
        print("\nProceed")
    elif(sensor.light_status == 'yellow' and sensor.ped_status == 'no' and sensor.veh_status == 'no'):
        print("\nCaution")
    elif(sensor.light_status == 'red' or sensor.ped_status == 'yes' or sensor.veh_status == 'yes'):
        print("\nSTOP")
    print("\nLight = " + sensor.light_status + " , Pedestrian = " + sensor.ped_status + " , Vehicle = " + sensor.veh_status + " .\n")


# Complete the main function below
# The main function creates/initializes a Sensor object and calls the Sensor class methods,
# which updates and displays the sensor statuses based on user input
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    user_selection = Sensor() #creating a sensor object
    user_selection.update_status() #calling update_status() method 


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

