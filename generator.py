import random

def weighted_value(value, weight):
    return [value for x in (range(0, weight)) ]


pronouns = ["i", "we"]
pronouns_reverse = ["me", "us"]
positive_verbs = ["love", "enjoy", "like"]
positive_adjectives = ["amazing", "great", "excellent", "well-written", "informative", "on point"]
demand_verbs = ["tell", "show", "teach", "write"]
general_nouns = ["website", "app", "blog", "article"]
keywords = ["nutrition", "baseball", "horses", "coffee"]
end_punctuation = [".","!", ""]

# accessory lists
greetings = ["hey", "hello", "hi", "nice", "thanks", "thank you"] + weighted_value(None, 24)

class phrase_generator:
    def __init__(self, pre_string, greeting=False):
        self.pre_string = pre_string
        self.greeting = greeting

    def gen(self):
        arguments = {
            "pronouns": random.choice(pronouns),
            "pronouns_reverse": random.choice(pronouns_reverse),
            "positive_verbs": random.choice(positive_verbs),
            "positive_adjectives": random.choice(positive_adjectives),
            "demand_verbs": random.choice(demand_verbs),
            "general_nouns": random.choice(general_nouns),
            "keywords": random.choice(keywords),
            "end_punctuation": random.choice(end_punctuation)
        }
        if self.greeting:
            prefix = random.choice(greetings)
            if prefix:
                prefix = prefix.capitalize() + random.choice(end_punctuation) + " "
            else:
                prefix = ""
        else:
            prefix = ""
        return prefix + self.pre_string.format(**arguments).capitalize()

gen1 = phrase_generator("{pronouns} {positive_verbs} the {general_nouns}{end_punctuation}", greeting=True)
gen2 = phrase_generator("{pronouns} {positive_verbs} {keywords}{end_punctuation}", greeting=True)
gen3 = phrase_generator("{demand_verbs} {pronouns_reverse} more{end_punctuation}", greeting=True)
gen4 = phrase_generator("{demand_verbs} {pronouns_reverse} more about {keywords}{end_punctuation}")
gen5 = phrase_generator("This {general_nouns} is {positive_adjectives}{end_punctuation}")

generators = [ gen1, gen2, gen3, gen4, gen5 ]

def phrase_engine(cycles, generators):
    for index in range(0, cycles):
        cntr = "{0}".format(index).zfill(4)
        phrase = random.choice(generators).gen()
        print("{cntr}| {phrase}".format(cntr=cntr, phrase=phrase))
