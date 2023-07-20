import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
# Empty list to build later
WORDS = []

# Code snippets are keys, English phrases are values.
# English phrase syntax modified from Shaw for consistency.
PHRASES = {
    "class %%%(%%%):":
      "Make a class %%% that is-a %%%.",
    "class %%%(object): def __init__(self, ***)" :
      "class %%% has-a __init__ that takes params self, ***.",
    "class %%%(object): def ***(self, @@@)":
      "class %%% has-a function *** that takes params self, @@@.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the function *** and call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the attribute *** and set it to '***'."
}

# do they want to drill phrases first
# Remember that script name is always argv[0].
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # word must be stripped of trailing '\n' and converted from bytes to str.
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    # Draw random sample from WORDS for each '%%%' and '***' in snippet.
    # Will result in empty lists depending on the snippet.
    # BUG: random words could be repeated in same snippet. (OK but bad style?)
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    # Empty lists to build later.
    results = []
    param_names = []

    # This loop will run no or 1 iteration depending on snippet.
    for i in range(0, snippet.count("@@@")):
        # Draw between 1 and 3 parameters.
        param_count = random.randint(1,3)
        # join() will not add ', ' if param_count = 1
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # iterate once for snippet and once for phrase
    for sentence in snippet, phrase:
        # This copy of sentence seems unnecessary based on testing.
        result = sentence[:]

        # Iterate over class_names, other_names, and param_names. . .
        # replacing the placeholders with randomly drawn words.
        # '1' arg. in replace() means only one placeholder per iteration.

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        # Put replaced snippet and phrase strings in list to be returned.
        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        # Keeps the snippet order from being repeated every time.
        random.shuffle(snippets)
        
        # Loop over the PHRASES dictionary.
        for snippet in snippets:
            phrase = PHRASES[snippet]
            # Placeholders in PHRASES get populated with random words.
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                # Swap the order so English phrase comes first.
                question, answer = answer, question
            
            print(question)
            
            input("      > ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
