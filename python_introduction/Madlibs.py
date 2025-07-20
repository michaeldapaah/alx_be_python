# Madlib Game# This program allows users to create a madlib by filling in words for a story template.
noun = input("Enter a noun: ")
pronoun = input("Enter a pronoun (he/she/they): ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
emotion = input("Enter an emotion: ")

weather = input("What's the weather like today(sunny, rainy, cloudy)? ").lower()

story = f"""On a {adjective} day, {pronoun} went to the zoo. {pronoun} saw a {adjective} {noun} {verb} from the trees. Then, {pronoun} spotted a {adjective} {noun} lounging in the sun.  What a wild and {adjective} experience!"""

if weather == "sunny":
    story += f" The sun was {verb} brightly, making everything look even more {adjective}."
elif weather == "rainy":
    story += f" The rain added a refreshing touch to the day, making the {noun} more playful."
elif weather == "cloudy":
    story += f" The clouds created a perfect backdrop for the {noun}, making them look even more majestic."


print(story)