import random

# topic question dictionaries
historical =  {
        "Who was President of France during WWII": "Charles de Gaulle",
        "Who was Aristotle": "philosopher",
        "What Midwestern US city got the nickname, 'Porkopolis' in the 19th century": "politician",
        "Charles Darwin proped his Theory of Evolution by ________ ________": "natural selection",
        "What is the world’s oldest writing system?": "Cuneiform",
        "By marrying Prince Rainier, what nation did Grace Kelly became princess of?": "Monaco",
        "What beauty brand started out by selling books?": "Avon",
        "Who was the queen of France during the French Revolution?": "Marie Antoinette",
        "Which company manufactured the film for NASA’s Apollo 11 moon mission?": "Kodak",
        "Who was Edgar Allan Poe": "author",
        "Who was Wolfgang Amadeus Mozart": "musician",
        "Where was Christmas first celebrated?": "Rome",
        "What is the other name for the celebration 'Fat Tuesday'": "Mardi Gras",
        "Who was Jesse Owen": "athlete",
        "Which country were the 1992 Winter Olympic Games held in?": "France",
        "What country presented the US with a gift of cherry trees in 1912?": "Japan",
        "Who was Oscar Wilde": "author",
        "An attempt to delay Senate action on a bill by debate, procedural motions, or obstructive actions.": "filibuster",
        "In the Chinese zodiac, with which of the five elements is the snake associated?": "fire",
        "What was the original name of New York City?": "New Amsterdam",
        }

popculture = {
    "What show featured the five orphaned Salinger siblings?": "Party of Five",
    "Who voices the character of Bart Simpson on the TV show 'The Simpsons'?": "Nancy Cartwright",
    "What was the mailman's name on the show 'Seinfeld'?": "Newman",
    "Which 1990 dance craze gave the Digital Underground their biggest hit?": "The Humpty Hump",
    "What singer holds the record for most Grammy nominations?": "Beyonce",
    "What weather phenomenon swept Dorothy Gale to the Land of Oz?": "tornado",
    "Who holds the record for winning the most Oscars?": "Walt Disney",
    "What's the title (in English) of the longest movie ever made": "The Innocence",
    "What animal did Britney Spears  carry on her shoulders during a performance?": "snake",
    "What actor has played a superhero in the most movies?": "Robert Downey, Jr.",
}

science = {
    "What kind of scientist was Luther Burbank?": "botanist",
    "What gas becomes a superfluid when cooled to absolute zero?": "helium",
    "What is the most common form of stalactites?": "speleothems",
    "What does a manometer measure?": "pressure",
    "How many horns does the average African black rhino have?": "2",
    "What is the very bottom soil horizon called?": "bedrock",
    "Coal is predominantly made up of which element?": "carbon",
    "What connects a flower buds to its stem?": "sepal",
    "What does a coleopterist study?": "beetles",
    "How many pi bonds in a triple bond?": "2",
    "What does TNT stand for?": "trinitrotoluene",
    "760 milimeters of Mercury (mmHg) is equal to _ atmospheres?": "1",
    "Which element has the chemical symbol Pt?": "platinum",
    "What is the most abundant gas in the Earth's atmosphere?": "nitrogen",
    "How many plates comprise the surface of the Earth?": "7",
    "How many brains does an octopus have?": "9",
    "What does USB stand for?": "universal serial bus",
    "What is the study of mushrooms called?": "mycology",
}

whoisanswerbank = ["king", "queen", "president", "explorer", "scientist", "author", "politician", "philosopher"]
useranswers = []
# create empy list to append user's answers to 

print("---------------------------------- 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚛𝚒𝚟𝚒𝚊! ----------------------------------")
quiz_type = input("Choose your trivia topic! History (h), pop culture (p), science (s), or mix (m) ")
number = int(input("How many questions would you like to be asked? "))
#get user specifications for topic and quiz length

#function to merge 3 topic dictionaries for "mix" topic
def Merge(historical, science, popculture):
	result = historical | science | popculture
	return result

#assign questions as the correct dictionary depending on what topic user selected
if quiz_type.lower() == "h" or quiz_type.lower() == "historical":
    questions = historical
    print("Answer bank for 'Who is ____' questions \n" , whoisanswerbank)
elif quiz_type.lower() == "s" or quiz_type.lower() == "science":
    questions = science
elif quiz_type.lower() == "p" or quiz_type.lower() == "pop culture":
    questions = popculture
    print("Answer bank for 'Who is ____' questions \n" , whoisanswerbank)
elif quiz_type.lower() == "m" or quiz_type.lower() == "mix":
    questions = Merge(historical, science, popculture)
    print("Answer bank for 'Who is ____' questions \n" , whoisanswerbank)
else:
    print("Please choose from the given quiz types.")
    exit()

# loop through quetion set using for loop; number is the value user inputed for the number of questions they wanted to be asked
def askquestions(number, questions, useranswers):
    score = 0      #initialize score as 0
    i = 0          #initialize i as 0
    while i < number:          
        x = random.choice(list(questions.keys()))
        print("➥ Question: " + x)
        answer = input("    Your answer: ")
        useranswers.append(answer)    #append the user's answer to the empty list
        if answer.lower() == questions[x].lower():
            print("    Correct! \n")
            score += 1     #add 1 to score if answer is correct
        else:
            print("    Incorrect")
            print("    The correct answer was" , questions[x], "\n")
        i += 1      #increment by 1
    print(f"\nYou answered {score} questions correctly out of {number}")



askquestions(number, questions, useranswers)


#Option for user to get a list of their answers
def quizreciept():
    receipt = input("Would you like a reciept of your quiz answers? ")
    if receipt.lower() == "yes" or receipt.lower() == "y":
        print(useranswers)      
    elif receipt.lower() == "no" or receipt.lower() == "n":
        print("Alright, thank you for playing!")
    else:
        print("Please enter either 'yes' or 'no'.")
quizreciept()