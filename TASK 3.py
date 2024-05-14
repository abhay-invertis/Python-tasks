score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to Quiz night! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name))

#Question1
print("""what is the most used languages in computer science?
1. c programming
2. python 
3. java
4. javascript """)

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("""what is the capital of india’?
1. punjab
2. delhi
3. haryana
4. U P  """)

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 2")