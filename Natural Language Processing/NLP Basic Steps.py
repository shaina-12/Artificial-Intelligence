# to implement basic steps of nlp
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
def tokenization(tweet):
    tweet = tweet.lower()
    tokens = nltk.word_tokenize(tweet)
    return tokens
def stopwordsRemoval(tokens):
    sw = stopwords.words('english')
    sws=set(sw)
    remsw = [tok for tok in tokens if tok not in sws]
    return remsw
def stemming(remsw):
    ps = PorterStemmer()
    stems = []
    for rsw in remsw:
        stems.append(ps.stem(rsw))
    return stems
def lemmatization(remsw):
    wnl = WordNetLemmatizer()
    lemms = []
    for rsw in remsw:
        lemms.append(wnl.lemmatize(rsw))
    return lemms
tweet = """I’m amazed how often in practice, not only does a @huggingface NLP model solve your problem, but one of their public finetuned checkpoints, is good enough for the job. 
Both impressed, and a little disappointed how rarely I get to actually train a model that matters :("""
tokens = tokenization(tweet)
print('Tokens:',tokens)
print()
remsw = stopwordsRemoval(tokens)
print('Tokens which are not stopwords:',remsw)
print()
stems =  stemming(remsw)
print('Tokens after stemming:',stems)
print()
lemms = lemmatization(remsw)
print('Tokens after lemmatization:',lemms)