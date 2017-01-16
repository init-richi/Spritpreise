#
#    Wirtten by Richard Mietz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import datetime, os
import json, requests


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


jsonConfig = open('config.json', 'r')
jsonConfigData = json.load(jsonConfig)

# parse config.json to vars

# general settings :

genSaveSprit = jsonConfigData['general']['saveDirSprit']
genSaveNews = jsonConfigData['general']['saveDirNews']

##################

# sprit_api vars :

spritKey = jsonConfigData['config_spritpreise']['api_key_sprt']    # STR
spritLat = jsonConfigData['config_spritpreise']['latitude']        # STR
spritLng = jsonConfigData['config_spritpreise']['longitude']       # STR
spritRad = jsonConfigData['config_spritpreise']['radius']          # STR
spritType = jsonConfigData['config_spritpreise']['type']           # STR
spritSlp = jsonConfigData['config_spritpreise']['sleep_time']     # INT 

###################

# news_api vars :

newsKey = jsonConfigData['config_news']['api_key_nws'] #STR
newsSources = jsonConfigData['config_news']['sources'] #STR

###################




    if os.path.exists('Data/' + genSaveSprit):
        pass
    else:
        os.mkdir('Data/' + genSaveSprit)


    dTime = str(datetime.datetime.now())[:-10]
    with open('Data/' + genSaveSprit  + '/sprit_' + dTime + '.json', 'w') as spritFile:
        json.dump(fetch().sprit(spritKey,spritLat,spritLng,spritRad,spritType), spritFile, ensure_ascii=False, indent=4, sort_keys=True)

    if datetime.datetime.now().time() >= datetime.time(23, 55): #if end of day download news
        if os.path.exists('Data/' + genSaveNews):
            pass
        else:
            os.mkdir('Data/' + genSaveNews)

        for item in newsSources: #for every source download .json
            with open('Data/' + genSaveNews + '/news_' + dTime +'_' + item + '.json', 'w') as newsFile:
                json.dump(fetch().news(newsKey,str(datetime.datetime.now())[:10], item), newsFile, ensure_ascii=False, indent=4, sort_keys=True)

    time.sleep(spritSlp)
