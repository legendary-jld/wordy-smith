import random

pronouns = ["i", "we"]
pronouns_reverse = ["me", "us"]
positive_verbs = ["love", "enjoy", "like"]
demand_verbs = ["tell", "show"]
general_nouns = ["website", "app"]
keywords = ["nutrition", "baseball"]
end_punctuation = [".","!"]

class phrase_generator:
    def __init__(self, pre_string):
        self.pre_string = pre_string

    def gen(self):
        arguments = {
            "pronouns": random.choice(pronouns),
            "pronouns_reverse": random.choice(pronouns_reverse),
            "positive_verbs": random.choice(positive_verbs),
            "demand_verbs": random.choice(demand_verbs),
            "general_nouns": random.choice(general_nouns),
            "keywords": random.choice(keywords),
            "end_punctuation": random.choice(end_punctuation)
        }
        return self.pre_string.format(**arguments).capitalize()

gen1 = phrase_generator("{pronouns} {positive_verbs} the {general_nouns}{end_punctuation}")
gen2 = phrase_generator("{pronouns} {positive_verbs} {keywords}{end_punctuation}")
gen3 = phrase_generator("{demand_verbs} {pronouns_reverse} more{end_punctuation}")
gen4 = phrase_generator("{demand_verbs} {pronouns_reverse} more about {keywords}{end_punctuation}")

generators = [ gen1, gen2, gen3, gen4 ]

def phrase_engine(cycles, generators):
    for index in range(0, cycles):
        cntr = "{0}".format(index).zfill(4)
        phrase = random.choice(generators).gen()
        print("{cntr}| {phrase}".format(cntr=cntr, phrase=phrase))
