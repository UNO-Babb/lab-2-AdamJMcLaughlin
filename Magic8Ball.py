print("Adam McLaughlin\n09/04/2025\nMagic8Ball")
print()
#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.

  print("Magic 8 Ball")

question = input("Ask the Magic 8 Ball a yes-or-no question: ")
print("\nThinking...\n")

  #Prompt the user for their question.

answers =["Hell No!","Hell Yeah!","Wish In One Hand And Shit In The Other.",
"Does A Bear Shit In The Woods","I Have A Headache","Don't Quit Your      Day Job",
"Please.","You Never Step In The Same River Twice","You Don't Find The Kundalini The Kundalini Finds You!",
"Dude...","Dude!","Ask Your Mom!","Ask Your Dad!","The Universe Approves",
"You Will Get Worms!!!","What Are You Asking Me!","Your Funny, Really!"]

  #Answer question randomly with one of the options from your earlier list.
length = len(answers)
r = random.random() * length
r = int(r)
 
print (r)
response = answers[r]
print (response)
