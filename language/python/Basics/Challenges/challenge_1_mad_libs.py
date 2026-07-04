"""
Write a story with some words missing

Roses are {colour}
Violets are {colour2}
Sugar are {adjective}
And so are you
"""

colour = input("Give me a colour: ")
colour2 = input("Give me another colour: ")
adjective = input("And an adjective: ")

story = f"""
Roses are {colour}
Violets are {colour2}
Sugar are {adjective}
And so are you"""

print(story)