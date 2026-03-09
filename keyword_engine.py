import random

base = [
"dog","cat","coffee","desk","garden","bike",
"camping","fitness","kitchen","travel","pet"
]

mods = [
"holder","organizer","rack","stand","cart",
"kit","table","seat","bag","machine","feeder"
]

def generate_keywords(n=300):

    keywords=[]

    for i in range(n):

        k=random.choice(base)+" "+random.choice(mods)

        keywords.append(k)

    return keywords
