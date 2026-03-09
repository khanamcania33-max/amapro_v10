import random

base_keywords = [
"dog","cat","fitness","kitchen","camping","travel",
"desk","home","garden","bike","coffee","pet"
]

modifiers = [
"holder","rack","organizer","kit","stand","bag",
"table","seat","feeder","light","cart","machine"
]

def generate_keywords(n=300):

    keywords = []

    for i in range(n):

        k = random.choice(base_keywords) + " " + random.choice(modifiers)

        keywords.append(k)

    return keywords