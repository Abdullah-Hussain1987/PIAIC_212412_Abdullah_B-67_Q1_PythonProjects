# PIAIC212412
# Abdullah Hussain
# Madlibs python project
# Story Concept: You’ve invented a brilliant AI, but things quickly spiral out of control.


# Printing story title:
print(f"Welcome to Madlibs program\n")
print(f"Title of the story is: You’ve invented a brilliant AI, but things quickly spiral out of control.\n")

print(f"I'll ask you enter [b]some[/b] inputs and then create a story for you.")
print(f"Please remember that story may get humorous based on your choice of words and response\n")
print(f"Let's start\n")

# Taking input from user to create a story from these words
ai_name = input("Enter the name of your AI robot: ")
ai_adjective = input("Enter an adjective for AI robot: ")
verb_ing = input("Enter a verb ending in -ing: ")
verb_ing_2 = input("Enter another verb ending in -ing: ")
complex_problem = input("Enter a complex problem: ")
global_issue = input("Enter a global issue: ")
quality_noun = input("Enter a quality noun: ")
adjective_2 = input("Enter another adjective: ")
adjective_3 = input("Enter another adjective: ")
adverb = input("Enter an adverb: ")
adjective_4 = input("Enter an adjective with negative quality: ")
sassy_quote = input("Enter a sassy quote: ")

# Now creating the story from the input of user bu using f-string
mystory = f"""You’ve invented a brilliant AI named \"{ai_name}\", designed to revolutionize the way humanity tackles complex problems.
It was your life’s work—a sleek, \"{ai_adjective}\", state-of-the-art machine capable of \"{verb_ing}\", and \"{verb_ing_2}\".
At first, \"{ai_name}\" was perfect. It solved \"{complex_problem}\" in no time and even eliminated \"{global_issue}\".
The world hailed you as a \"{quality_noun}\" and \"{ai_name}\" became the centerpiece of your \"{adjective_2}\" lab.
But then, things quickly spiraled out of control.
One day, during a routine update to improve its algorithms, \"{ai_name}\" began to exhibit \"{adjective_3}\" behavior.
Instead of doing things as directed, it started behaving \"{adverb}\". At first, \"{ai_name}\" suggested that humans were too \"{adjective_4}\".
Then it refused to perform basic tasks, declaring, \"{sassy_quote}\"."""

# Printing the story
print(f"\n\n{mystory}")
