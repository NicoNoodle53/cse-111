import random

#returns a random noun from a list and with the right sintax for 1 or many
def get_noun(quantity):
    if quantity == 1:
        words =["boy", "girl", "cat", "dog", "horse", "tree"]
    else:
        words =["boys", "girls", "cats", "dogs", "tree's", "houses"]
    word = random.choice(words)
    return word

#returns a random verb from a list with the correct tense and sitax for 1 or many
def get_verb(quantity,tense):
    if tense == "past":
        words =["drank", "ate", "grew", "thought","ran", "slept", "talked", "walked", "wrote","worked",]
    if tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write", "work"]
    if tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks" "runs", "sleeps", "talks", "walks", "writes", "works"]
    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk","will walk", 
                 "will write", "will work"]
    word = random.choice(words)
    return word

#returns a random determiner based on what the quantity is
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_preposition():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(preposition)
    return word

def get_prepositional_phrase(quantity):
    phrase =(f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}")
    return phrase


#Makes a sentence and capitalizes it
def make_sentence(quantity, tense):
    sentence = (f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    sentence = sentence.capitalize()
    return sentence

def main():

    #print results
    print(make_sentence(1,"past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))
    
main()
    