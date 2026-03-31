from time import *
import random as r

print(time())

def load_sentences():
    with open("sentence.txt", "r") as f:
        sentences = [line.strip() for line in f if line.strip()]
    return sentences


def mistake(partest,usertest):
    error=0
    part_words = partest.split()          
    user_words = usertest.split()         

    for i in range(min(len(part_words), len(user_words))):   
        if part_words[i] != user_words[i]:
            error= error + 1

    error += abs(len(part_words) - len(user_words))   
    return error


def speed_time(time_s,time_e,userinput):
    time_delay= time_e - time_s
    time_R= round(time_delay,2)
    words = len(userinput.split())        
    speed= (words/time_R)*60             
    return round(speed)


sentences = load_sentences()


while True:
    ck= input("Ready to Test : Yes/No : ")
    if ck== "Yes":
    
       
        test1= r.choice(sentences)

        print("*****Typing speed*****")
        print(test1)
        print()
        print()
        time_1= time()
        testinput=input(" Enter : ")
        time_2= time()

        print('Speed : ', speed_time(time_1,time_2,testinput),"WPM") 
        print("Error : ", mistake(test1,testinput))  
    
    elif ck== 'No':
        print("Thank You")
        break
    else:
        print("Wrong Input")