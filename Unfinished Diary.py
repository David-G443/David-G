empty_list=[]

def priority_input():
    """Obtains user input for the priority of the appointment and returns error if not 'High' or 'Low' """
    while True:
        priority=input("Please enter the priority, only values of High or Low: ")
        if priority.upper() == "HIGH":
            #assigns 'High' to variable if input is high (case insensitive)
            global high
            high=("High")
            start_input()
            break
        elif priority.upper() == "LOW":
            #assigns 'Low' to variable if input is low (case insensitive)
            global low
            high=("Low")
            start_input()
            break
            # if input is not high or low returns error
        else:
            print("Please enter only values of High or Low.")


def date_input():
    """Obtains user input for the date of the appointment and returns error if day isnt valid for month,
    if the month isnt between 1 to 12 and if the year is less than 2022 or greater than 9999"""
    while True:
        date=input("Please input the date e.g. 20/03/2022 or end to end the program: ")
        #obtains date input or end input
        if date.upper()=="END":
            heading = 'Priority    | Date      | Start | End | Subject |'
            line = '+' + '-'*40 + '-'*13 + '+'

            print(line)
            print (heading)
            print(line)
            #once the user is finished adding entries the table is created
            break
        #splits the days months and years and assigns them to variable as integers
        dd,mm,yy=date.split('/')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        global date_str
        if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
            max1=31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            max1=30
        elif(yy%4==0 and yy%100!=0 or yy%400==0):
            max1=29
        else:
            max1=28
        #date validation, validates if days months and years are correct
        if(mm<1 or mm>12):
            print("Only enter valid months between 1 and 12.")
            return date_input()
            break
        elif(dd<1 or dd>max1):
            print("Please input a valid day for the applicable month.")
            return date_input()
            break
        elif(yy<2022 or yy>9999):
            print("Please input a year between 2022 and 9999.")
            return date_input()
            break
        elif(dd==max1 and mm!=12):
            date_str=date
            priority_input()
            break
        else:
            date_str=date
            priority_input()
            break
        
def start_input():
    """Obtains user input for the start time of the appointment and returns error if not lower than '7'
    and greater than '21' """
    while True:
        global int_start
        global start
        start_time=input("Please only enter start time, from 7 and 22: ")
        int_start=int(start_time)
        #start time validation, checks if input is equal to or greater than 7 or lower than 22. Else it returns an error
        if 7<=int_start<=21:
            start=start_time
            end_input()
            break
        else:
            print("Please enter a value greater than 7 or lower than 22.")
            return start_input()
            break
        
def end_input():
    """Obtains user input for the end time of the appointment and returns error if lower than or equal to
    start time or greater than '22' """
    while True:
        global end
        end_time=input("Please only enter end time,including and from 7 and 22: ")
        int_end=int(end_time)
        #end time validation ensure input is between 7 and 22 and greater than start time
        if int_end<=int_start:
            print("End time cannot be lower than or equal to start time.")
            return end_input()
            break
        if 7<=int_end<=22:
            end=end_time
            description_input()
            break
        else:
            print("Please enter a value greater than or equal to 7 or lower than or equal to 22.")
            return end_input()
            break
        
def description_input():
    """Obtains user input for the description of the appointment and returns error if empty or
    or greater than or equal to '30' """
    while True:
        global des
        description=input("Please enter a decription below equal to or below 30 characters: ")
        #validates description length and ensures the description is not empty
        des_length=len(description)-1
        int_des_length=int(des_length)
        if int_des_length<0:
            print("This input cannot be empty.")
            return description_input()
            break
        elif int_des_length<=30:
            des=description
            break        
        else:
            print("Enter a description below 30 characters.")
    date_input()
    appointmentList=high+";"+date_str+";"+start+";"+end+";"+des
    empty_list.append(appointmentList)
    showRecord()
           
            
def showRecord():
    
    line = '+' + '-'*40 + '-'*13 + '+'
    print(high+"         |"+date_str+" |"+start+"      |"+end+"   |"+des)
    print(line)
# This function pulls the global variables and placees them into a table         
                  
date_input()
#Calls the date_input function to begin the program

def sort(program, char):
   
    char_list = []
    other_list = []
    for priority in program:
        if priority==("High"):
            char_list.append(priority)
        else:
            other_list.append(priority)
    return sorted(char_list) + sorted(other_list)

def remove_duplicate(appointment):
   
    unique = []
    for repeat in appointment:
        if repeat not in unique:
            unique.append(repeat)
            
    return unique

