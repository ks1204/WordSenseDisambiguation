
from __future__ import division
import nltk
from nltk.book import *
from nltk.corpus import brown


def lexical_diversity(text):
	return len(text) / len(set(text)) 


sent1 = ['Call','me','Ismael','.']
print len(sent1)
print lexical_diversity(sent1)

sent2 = ['Call','me','Ismael','.','me','Kiran','please','science']
print len(sent2)
print '\n'
print lexical_diversity(sent2)

sent3 = ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']
print '\n'
sent4 = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
print '\n'
sent5 = ['Call','me','Ismael','.','me','Kiran','please','science']
print '\n'
sent6 = ['Call','me','Ismael','.','me','Kiran','please','science']
sent7 =['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
print '\n'
print sent2 + sent4
print '\n'
print text5[1:5]

#find words that are longer than the length of 15 characterss.
#set will not allow duplicates
Vocabulary = set(text1)
long_Words = [w for w in Vocabulary if len(w)>15]
print sorted(long_Words)

#find out the length of words that occur a lot in a text
[len(w) for w in text1]
fd= FreqDist([len(w) for w in text1])
print fd
print '\n'
print fd.keys()

x = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
y = sorted([w for w in set(x) if 'sh' in w and len(w) > 4])
print y

#This will tabulate data
news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can','could','may','might','must','will']
for m in modals:
    print m + ':', fdist[m]

news_texts = brown.words(categories='news')
fdist1 = nltk.FreqDist([w.lower() for w in news_texts])
modals1 = ['what','when','where','who','why']
for m in modals1:
    print m + ':',fdist1[m]

#tabulate the data
cfd= nltk.ConditionalFreqDist((genre,word)
                              for genre in brown.categories()
                              for word in brown.words(categories=genre))

genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genres,samples = modals)

