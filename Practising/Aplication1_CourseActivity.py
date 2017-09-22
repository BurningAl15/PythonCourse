import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if(w in data):
        return data[w]
    elif(len(get_close_matches(w,data.keys()))>0):
        yn= input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w,data.keys())[0])
        if(yn=="Y"):
            return data[get_close_matches(w,data.keys())[0]]
        elif(yn=="N"):
            c=input("Did you mean any of this options? " + str(get_close_matches(w,data)))
            return data[get_close_matches(c,data.keys())[0]]
    else:
        a="There's an error, the word is not in the database dude."
        return a

#while(True):
word=input("Enter word: ")
print(translate(word))

#for k,v in data.items():
#    print(k)

a=SequenceMatcher(None,"rain","rain").ratio()
b=get_close_matches("rainn",["help","pyramid","rain"])
#print(type(b))
