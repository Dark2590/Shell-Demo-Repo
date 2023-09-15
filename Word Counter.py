#Word Counter for a random paragraph
import string

para="""It was going to rain. The weather forecast didn't say that, but the steel plate in his hip did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better get outside and prepare.
There was nothing else to do. The deed had already been done and there was no going back. It now had been become a question of how they were going to be able to get out of this situation and escape."""

w_freq={}
#removes all punctuations. the two '' are placeholders. noramlly they would gove the string to be found and replaced.
translator=str.maketrans('', '', string.punctuation)
words=para.translate(translator).lower().split()
#Isolates each word and places it in a dictionary
for word in words:
    if word in w_freq:
        w_freq[word]+=1
    else:
        w_freq[word]=1
#sorts the dict to display the highest frequency words first
sw_freq=dict(sorted(w_freq.items(), key=lambda item:item[1], reverse=True))
print(sw_freq)
