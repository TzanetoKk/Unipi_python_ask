import tweepy

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()


user = input("user:")
le3eis=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    le3eis.append(tweet.text)

lista=[]
for tweet in word_list:
    le3h = tweet.split()
    lista += le3h

def Sorting(lista):
    lista.sort(key=len)
    return lista

print(Sorting(lista))

symvola = '()[]{}.,:;=+-*/&~`|_#!@$%^<>\?'

results = []
for element in lista:
    temp = ""
    for ch in element:
        if ch not in symvola:
            temp += ch

    results.append(temp)

for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])