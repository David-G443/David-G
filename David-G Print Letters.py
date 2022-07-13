#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Letter_c():
    """Prints the letter C in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_c="";
    #defines the amount of space for the letter to be printed
    for row in range(0,7):
        for column in range(0,7):
            #defines where the * sign will go, with every other spot being allocated a space
            if ((column == 1 and row != 0 and row != 6)
            or (column == 5 and row !=0 and row != 2 and row != 3 and row != 4 and row != 6)
            or ((row == 0 or row == 6) and column > 1 and column < 5)):
               Letter_c+="*"
            else:
              Letter_c+= " "
        Letter_c+= "\n"
    return Letter_c
LetterC=Letter_c()



def Letter_o():
    """Prints the letter O in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_o="";
    for row in range(0,7):
        for column in range(0,7):
            if ((column == 1 and row != 0 and row != 6)
            or (column == 5 and row !=0 and row != 6)
            or ((row == 0 or row == 6) and column > 1 and column < 5)):
               Letter_o+="*"
            else:
              Letter_o+= " "
        Letter_o+= "\n"
    return Letter_o
LetterO=Letter_o()


def Letter_l():
    """Prints the letter L in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_l="";
    for row in range(0,7):
        for column in range(0,7):
            if ((column == 1)
            or ((row == 6) and column > 0 and column < 6)):
                Letter_l+="*"
            else:
              Letter_l+= " "
        Letter_l+= "\n"
    return Letter_l
LetterL=Letter_l()


def Letter_d():
    """Prints the letter D in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_d="";
    for row in range(0,7):
        for column in range(0,7):
            if ((column == 1)
            or (column == 5 and row != 0 and row != 1 and row != 5 and row !=6)
            or ((row == 1 or row == 5) and column > 3 and column < 5)
            or ((row == 0 or row == 6) and column > 1 and column < 4)):
                Letter_d+="*"
            else:
              Letter_d+= " "
        Letter_d+= "\n"
    return Letter_d
LetterD=Letter_d()


def Letter_h():
    """Prints the letter H in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_h="";
    for row in range(0,7):
        for column in range(0,7):
            if ((column == 1 or column == 5)
            or ((row == 3) and column > 0 and column < 6)):
                Letter_h+="*"
            else:
              Letter_h+= " "
        Letter_h+= "\n"
    return Letter_h
LetterH=Letter_h()
    

def Letter_t():
    """Prints the letter T in a seven by seven grid, marking the outline with * and everything else
    with spaces"""
    Letter_t="";
    for row in range(0,7):
        for column in range(0,7):
            if ((column == 3)
            or ((row == 0) and column > 0 and column < 6)):
                Letter_t+="*"
            else:
              Letter_t+= " "
        Letter_t+= "\n"
    return Letter_t
LetterT=Letter_t()


def cold():
    """Prints the word cold in a seven by 28 grid, marking the outline with * and everything else
    with spaces"""
    cold="";
    for row in range(0,7):
        for column in range(0,28):
            if ((column == 1 and row != 0 and row != 6)
            or (column == 5 and row !=0 and row != 2 and row != 3 and row != 4 and row != 6)
            or ((row == 0 or row == 6) and column > 1 and column < 5)
            or (column == 8 and row != 0 and row != 6)
            or (column == 12 and row !=0 and row != 6)
            or ((row == 0 or row == 6) and column > 8 and column < 12)
            or (column == 15)
            or ((row == 6) and column > 14 and column < 20)
            or (column == 22)
            or (column == 26 and row != 0 and row != 1 and row != 5 and row !=6)
            or ((row == 1 or row == 5) and column > 24 and column < 26)
            or ((row == 0 or row == 6) and column > 22 and column < 25)): 
               cold+="*"
            else:
              cold+= " "
        cold+= "\n"
    return cold
wordCold=cold()


def hot():
    """Prints the word hot in a seven by 21 grid, marking the outline with * and everything else
    with spaces"""
    hot="";
    for row in range(0,7):
        for column in range(0,21):
            if ((column == 1 or column == 5)
            or ((row == 3) and column > 0 and column < 6)
            or (column == 8 and row != 0 and row != 6)
            or (column == 12 and row !=0 and row != 6)
            or ((row == 0 or row == 6) and column > 8 and column < 12)
            or (column == 17)
            or ((row == 0) and column > 14 and column < 20)):
                hot+="*"
            else:
                hot+=" "
        hot+= "\n"
    return hot
wordHot=hot()


def Print_value():
    """If input is valid prints in letters in 7*7, cold in 7*28 and hot in 7*21 grid
    unless END is entered which ends the program"""
    while True:
        User_input=input("Please enter only values of C, O, L, D, H, T, COLD, HOT and end ")
        #if the user inputs a letter (case sensitive) it will print the associated 7*7 letter by calling the function
        if  User_input == "C":
            print(LetterC)
        elif User_input == "O":
            print(LetterO)
        elif User_input == "L":
            print(LetterL)
        elif User_input == "D":
            print(LetterD)
        elif User_input == "H":
            print(LetterH)
        elif User_input == "T":
            print(LetterT)
        #if the words cold or hot are inputed (case sensitive) it will print the associated 7*28 or 7*21 word by calling the function
        elif User_input == "COLD":
            print(wordCold)
        elif User_input == "HOT":
            print(wordHot)
        #when "END" is inputed (case in-sensitve) at any point in time, it will end the function and print "The program has ended"
        elif User_input.upper() == "END":
            print("The program has ended")
            break
        #if a appropriate value is not inputed this validation claim will print "Please enter a correct value"
        else:
            print("Please enter a correct value")  
        
Print_value()


# In[ ]:




