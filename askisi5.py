from os import remove
import json         #8a paro tin pliroforia se arxeia json kai 8a xeiristo ayta
import tweepy       #tweepy xrisimopoiontas to twitter api 8a mou dosei prosvasi
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize
from collections import Counter  #8a xrisimopoihso antikeimeno tipou counter kai pio sigkekrimena tin me8odo most_common gia na kano tin zwi mou pio eykoli
import re #epeleksa na kano tokenize ayta pou 8a paro me regular expressions, gia na min mplekso me listes kai strings kai splits-joins, in retrospect den ksero an htan kali epilogi
from nltk.corpus import stopwords #8a xrisimopoihso tin stopwords tou nltk paketou pou 8a filtrarei giro stis 153 agglikes lekseis kai kiriws sindesmous opws 'the','so','a', mias kai den mas fainontai toso 'interesting'
import string


def write_tweets(tweets, filename):
    with open(filename, 'a') as f:      #sinartisi pou 8a kaleitai gia na grafei ayta pou me endiaferoun se ena json arxeio me onoma to username pou me endiaferei
        json.dump(tweets._json, f)
        f.write('\n')
# edw prepei na simplirosete ta dika sas (mesa sta ' '):
consumer_key = 'YOUR CONSUMER KEY'  # consumer key
consumer_secret = 'YOUR CONSUMER SECRET'  # consumer secret
access_token = 'YOUR ACCESS TOKEN'  # access token
access_secret = 'YOUR ACCESS SECRET'  # access secret

auth = OAuthHandler(consumer_key, consumer_secret)                  #stin ousia edw dino prosvasi stin efarmogi mou sto twitter simfona me ta keys mou
auth.set_access_token(access_token, access_secret)                  #using the oAuth interface

api = tweepy.API(auth)                  #telos h metavliti api einai tora to access point mas

user_name = raw_input('dwse onoma xrhsth (xwris @) e.g.realDonaldTrump')      #diavazo onoma xristi pou me endiaferei
for status in tweepy.Cursor(api.user_timeline, screen_name=user_name, tweet_mode = 'extended').items(10):   #meso tis Cursor tou tweepy diavazo ta teleytaia 10 tweets se extended mode gia na ta paro plirws
    write_tweets(status, user_name+'.json')     #kalw tin write_tweets kai ta grafei se ena arxeio json


                                                    #tokenization and regexes hell
#prospa8o na ksexoriso emoticons, opou gia matia exw : h ;, mites - h katey8eian stomata o O D ) p P
emoticons_str = r"""
    (?:
        [:=;]                           
        [oO\-]? #
        [D\)\]\(\]/\\OpP]   
    )"""

#ksexorizo strings vasi:
regex_str = [
    emoticons_str,
    r'<[^>]+>',  #HTML tags
    r'(?:@[\w_]+)',  #@-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  #hashtags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  #URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  #numbers
    r"(?:[a-z'][a-z'\-_]+[a-z])",  #words with - kai '
    r'(?:[\w_]+)',  # ther words
    r'(?:\S)'  #otidipote allo
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):             #molis klh8ei h preprocess ta panta 8a einai tokenized simfona me ta regexes parapano
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
#with preprocess everything is tokenized, links, mentions, hastags, even emoticons

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via',u'\u2019']     #ftiaxno tin lista stop opou periexei ta stopwords pou anefera pio pano + ta simia stiksis + ta 'rt' kai 'via'
                                                                    #'rt' gia retweets kai 'via' gia mentions


filename = user_name + '.json'      #to onoma tou arxeiou pou eksartatai apo to username pou xrisimopoio
with open(filename, 'r') as f:      #anoigo to arxeio
    count_all = Counter()           #dimiourgo antikeimeno Counter pou 8a xrisimopoihso gia na vgalo katey8eian tis most_common lekseis
    for line in f:
        tweet = json.loads(line)                                                         #se ka8e grammi tou arxeiou json, pairno orous apo to pedio full_text
        terms_all = [term for term in preprocess(tweet['full_text']) if term not in stop]   #opou vriskontai ta tweets, efoson ta terms ayta den anoikoun stin lista stop
        count_all.update(terms_all)                                                         #kano update ton counter
    final_tuple = (count_all.most_common(1))                                                #dimiourgo mia tuple me tis most common lekseis kai poses fores emfanistikan
    print final_tuple[0][0]
#diagrafo to arxeio pou dimiourgi8ike, comment out gia na to kratisete kai na to deite
if f.closed:
    try:
        remove(filename)            #to exw se try giati yparxei periptosi to arxeio na exei meinei anoixto gia kapoion logo kai na petaksei exception
    except IOError:
        print "Unable to delete created file, maybe in use please do it manually."




