from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from keras.models import model_from_json
from keras import backend as K
import re
import numpy
import h5py
import tweepy
import requests
#import xlrd
import array
#import xlwt
import matplotlib.pyplot as plt
import json




class final:
    def __init__(self,name):
         self.name=name

    def sentiment(self):
        tweetsnum= 100
        vocabnum = 3000

        query =self.name
        query = query + " -filter:retweets"
        '''GETTING TWEETS'''

        ckey = 'MK1RukvjEJOKABP1bV46WNTNP'
        csecret = '328rvizTjSjiZj9uZE3J9m4h5CeMxw2aeRufoBF4ynCEjEBkLd'
        atoken = '1095575987155169280-K8uV6nmsIv8mQqndvNy53NiDKUMyhs'
        asecret = 'Mm6mOVilWSF6GcVeBpslOt3fRR7xR6IENLTE0gnLAnXub'

        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        api = tweepy.API(auth)
        tweets_arr=[]


        p=0

        #workbook = xlwt.Workbook(encoding="ascii")
        #worksheet = workbook.add_sheet('My Worksheet')
        for status in tweepy.Cursor(api.search,q=query ,lang ='en', tweet_mode='extended').items(tweetsnum):
            tweethead = "https://publish.twitter.com/oembed?url=https://twitter.com/"
            tweet2 = "/status/"
            tweets_arr.append(status.full_text)
            id = status.id_str
            user = status.user.screen_name
            tweethead = tweethead + user + tweet2 + id
            if p==0:
                r = requests.get(tweethead)
                x = r.json()
                blockcode1 = x['html']
                print("P=",str(p))
            if p == 1:
                r = requests.get(tweethead)
                x = r.json()
                blockcode2 = x['html']
                print("P=", str(p))
            if p==2:
                r = requests.get(tweethead)
                x = r.json()
                blockcode3 = x['html']
                print("P=",str(p))
            p = p + 1

            #worksheet.write(i, 5, label=status.text)

            #workbook.save('apex.xls')
        blockcode = [blockcode1, blockcode2, blockcode3]
        print(tweets_arr)

        '''DISPLAYING TWEETS ON WEBSITE'''
        f = open("displaytweets.txt", "w",encoding="utf8",errors='ignore')
        for i in range(5):
            try:
                f.write("(" + str(i+1) + ") ")
                f.writelines(tweets_arr[i])
                f.write(" ")
                f.write('\n\n\n')

            except UnicodeEncodeError:
                pass

        f.close()
        tweetsnum = len(tweets_arr)



        '''PREPROCESSING'''
        ps = PorterStemmer()
        file = open("stemporttweets.txt","w")
        x = ["?", "#", "!", ".", ",", ":", ";", "/", "-", "(", ")", "*", "_", "&"]
        print("Loaded")
        for z in range(tweetsnum):
            new_text = tweets_arr[z]
            new_text = re.sub(r"http\S+", ' ', new_text)
            new_text = re.sub(r"@\S+", ' ', new_text)
            new_text = new_text.lower()
            for i in range(5):
                new_text = new_text.replace(x[i], " ")
            words = word_tokenize(new_text)
            for w in words:
                try:
                    file.write(ps.stem(w))
                except UnicodeEncodeError:
                    pass
                file.write(" ")
            file.write('\n')
            print(((z/tweetsnum)*100), "%", end="\r")
        file.close()
        print("Completed successfully!")


        fSent = open('stemporttweets.txt', 'r')
        fWord = open('D:\\Sentimental\\static\\sentimental\\vocab_final.txt', 'r')
        X = numpy.zeros((tweetsnum, vocabnum+1), dtype=numpy.int)


        for i in range(tweetsnum):
            text = fSent.readline()
            arr = text.split(" ")
            for j in range(vocabnum):
                k = 0
                vocab = fWord.readline()
                while k < len(arr):
                    if arr[k].replace('\n', '') == vocab.replace('\n', ''):
                        X[i, j] = 1
                    k=k+1
            print("Negative Processing:", (i/tweetsnum)*100, "% done", end="\r")
            fWord.seek(0, 0)

        X[0, vocabnum] = 1


        print("Compressing...")
        with h5py.File("tweettesting.hdf5", "w") as f:
            dset = f.create_dataset("default", data=X, dtype='i1', compression="gzip", compression_opts=4)
        print("Completed!")



        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

        validate = h5py.File("tweettesting.hdf5", "r")

        A = validate["default"]

        X = A[:tweetsnum, :3000]

        # evaluate loaded model on test data
        Y=loaded_model.predict(X)

        i=0
        for i in range(tweetsnum):
            if Y[i] >= 0.5:
                Y[i] = 1

            else:
                Y[i] = 0


        count1 = numpy.count_nonzero(Y)
        print("Positive: "+str(count1))
        count0 = tweetsnum - count1
        print("Negative: "+str(count0))
        print("Percent Positive: "+str(count1*100/tweetsnum))

        labels="Positive","Negative"
        sizes=[count1,count0]
        colors=['#cdf900','#ff1a1a']
        explode=(0.1,0)

        plt.pie(sizes,explode=explode,labels=labels,colors=colors,
            autopct='%1.1f%%',shadow= True ,startangle=0)
        plt.axis("equal")

        plt.savefig("D:\Sentimental\static\sentimental\piechart.png",bbox_inches="tight",pad_inches=0)
        plt.close()

        plt.rcdefaults()
        objects = ("Positive", "Negative")
        y_pos = numpy.arange(len(objects))
        performance = [count1, count0]
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No of tweets')
        plt.xlabel('Result')
        plt.savefig("D:\Sentimental\static\sentimental\\barchart.png",bbox_inches="tight",pad_inches=0)
        plt.close()
        K.clear_session()
        print(blockcode)
        return blockcode