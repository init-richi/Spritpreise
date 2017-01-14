import os, json, requests
import datetime, time

class fetch(object):

    def sprit(self, api_key, latitude, longitude, radius, type):


        dTime = str(datetime.datetime.now())[:-10]
        api_url = 'https://creativecommons.tankerkoenig.de/json/list.php?lat=%s&lng=%s&rad=%s&type=%s&apikey=%s' % (latitude, longitude, radius, type, api_key)



        req = requests.get(api_url)
        return req.json()


    def news(self, api_key, time, source):

        api_url = "https://newsapi.org/v1/articles?source=%s&publishedAt=%s=latest&apiKey=%s" % (source, time, api_key)
        req = requests.get(api_url)
        return req.json()
