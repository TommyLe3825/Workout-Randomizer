#Random workout to do
import random #need to use this library to use choice


dice1 = ["1 Min Wall Sit", "Water Break", "20 Triceps Dips", "15 Jump Squats", "20 Burpees", "30 Russian Twists", 
"30 Bicycle Crunches", "30 Walking Lunges", "30 Sec Side Plank x 2", "30 Mountain Climbers", "15 Jump Lunges"]
word = random.choice(dice1)
print("Your first workout will be: ")
print(word)

dice2input = input("Do you want to do second dice as well? Y/N ") #getting input

if dice2input == 'Y' or dice2input == 'y':
    dice2 = ["15 Lateral Lunges", "30 Jumping Jacks", "15 Push Ups", "Water Break", "15 Burpees", "20 Mountain Climbers",
    "15 Supermans", "15 Floor Dips", "15 Sumo Squats", "30 sec Side Planks x 2", "15 Skaters", "15 Bicycle Cruches"]
    word1 = random.choice(dice2)
    print(word1)
else:
    print("Alright, stay safe and have a nice day!")
    exit
    
