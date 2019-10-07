#a baby asking question not ending until the anwser starts with just because
from random import choice 

questions= ["why is the sky blue? ", "why is there a face on the moon? ","why are the cock shouting? "] # a list of questions
question =choice (questions) # to choose any random question from the list questions
answer = input(question).strip().lower()
while answer!="just because":
    answer = input("why? ").strip().lower()

print("Oh... okay")