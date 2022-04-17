# export SPOTIPY_CLIENT_ID='848cb28237744e39bdcb7b766996d9dd'
# export SPOTIPY_CLIENT_SECRET='6aae92519fb9458eb741925f9b999991'

import spotipy, json 
from string import ascii_uppercase

''' To fetch distinct artists name, ID, and image if exist, with alpha order.'''

auth_manager = spotipy.oauth2.SpotifyClientCredentials(requests_timeout=20)
sp = spotipy.Spotify(auth_manager=auth_manager)

''' To fetch distinct artists name, ID, and image if exist, with alpha order.'''

# data = {}
# data['Artists'] = []

# for letter in ascii_uppercase:
#   for i in range(20):
#       try:
#           s = sp.search(q=letter, limit=50, offset=(50*i), type= "artist") 

#           for i in range(len(s['artists']['items'])):
#               try:
#                   s['artists']['items'][i]['images'][0]['url']
#                   image = s['artists']['items'][i]['images'][0]['url']
#               except:
#                   image = 'no_image'

#               artist = {
#                           'name' : s['artists']['items'][i]['name'],
#                           'id' : s['artists']['items'][i]['id'],
#                           'image_url' : image
#                       }

#               if artist not in data['Artists']:
#                   data['Artists'].append(artist)
#       except:
#           continue 

# with open('artists_backup.txt', 'w') as f:
#   json.dump(data, f, indent= 4)



""" To fetch top artists songs """

artists_info = {}

with open('artists.txt','r') as f:
    r = json.loads(f.read())
    for i in r['Artists']:
        artists_info[i['name']] = i['id']

# num = 0
songs = {}

f = open('songs.txt', 'w') 

f.write('{')

for name in artists_info:
    artist_name = name
    songs[artist_name] = [] # add a key to the album name ? if top song does not exists ?

    f.write(f'\n\t"{name}": [,')

    s = sp.artist_top_tracks(artist_id= artists_info[artist_name])

    for track in s['tracks'][:10]:
        # f.write(track['name']+"\n")
        f.write(",\n\t\t\t\"{}\"".format( track['name'] ))
        
    f.write("\n\t\t],")

    # break

    # try :
    #     s = sp.artist_top_tracks(artist_id= artists_info[artist_name])
        
    #     for i in range(len(s['tracks'])):
    #         album_id = s["tracks"][i]['album']['id']
    #         album_track = sp.album_tracks(album_id, limit=50, offset=0, market=None)

    #         for i in range(len(album_track['items'])):
    #             # print(album_track['items'][i]['name'])
    #             songs[artist_name].append(album_track['items'][i]['name'])
    #             # print(songs[artist_name])
    #             f.write(",\n\t\t\t\"{}\"".format( album_track['items'][i]['name'] ))

    #     f.write("\n\t\t],")

    # except: # to catch the name
    #     last_artist = name 
    #     with open('arch.txt', 'w') as r:
    #         r.write('the last name is ' + name)

# f.write("\n}")
# f.close()


# with open('songs.txt', 'w') as f:
#   json.dump(songs, f, indent= 4)
        
    













    
# class Spotifyy:
#   def __init__(self):
#       auth_manager = spotipy.oauth2.SpotifyClientCredentials(requests_timeout=20)
#       sp = spotipy.Spotify(auth_manager=auth_manager)

#   def fetch_distinct_artist(self, filename):
#       # data = {}
#       # data['Artists'] = []

#       # for letter in ascii_uppercase:
#       #   for i in range(20):
#       #       try:
#       #           s = self.sp.search(q=letter, limit=50, offset=(50*i), type= "artist") 

#       #           for i in range(len(s['artists']['items'])):
#       #               try:
#       #                   s['artists']['items'][i]['images'][0]['url']
#       #                   image = s['artists']['items'][i]['images'][0]['url']
#       #               except:
#       #                   image = 'no_image'

#       #               artist = {
#       #                           'name' : s['artists']['items'][i]['name'],
#       #                           'id' : s['artists']['items'][i]['id'],
#       #                           'image_url' : image
#       #                       }

#       #               if artist not in data['Artists']:
#       #                   data['Artists'].append(artist)
#       #       except:
#       #           continue 

#       # with open(filename, 'w') as f:
#       #   json.dump(data, f, indent= 4)


#   def fetch_artists_songs(self, filename2):
#       artists_info = {}

#       with open('artists.txt','r') as f:
#           r = json.loads(f.read())
#           for i in r['Artists']:
#               artists_info[i['name']] = i['id']

#       # num = 0
#       songs = {}

#       for name in artists_info:
#           artist_name = name
#           songs[artist_name] = [] # add a key to the album name ? if top song does not exists ?
#           try :
#               s = self.sp.artist_top_tracks(artist_id= artists_info[artist_name])

#               ''' I have to organize the data so every artists appear 
#               with the top songs or list of all songs in a given album '''

#               # with open('songs.txt', 'w') as f:
#               # print(artist_name, end= ' ')
#               # print(len(s['tracks']))
#               # print()

#               for i in range(len(s['tracks'])):
#                   album_id = s["tracks"][i]['album']['id']
#                   album_track = self.sp.album_tracks(album_id, limit=50, offset=0, market=None)   
#                   for i in range(len(album_track['items'])):
#                       # print(album_track['items'][i]['name'])
#                       songs[artist_name].append(album_track['items'][i]['name'])
#           except: # to catch the name
#               last_artist = name 
#               with open('arch.txt', 'w') as f:
#                   f.write('the last name is ' + name)
#           # if num == 5:
#           #   break
#           # else:
#           #   num +=1

#       with open(filename2, 'w') as f:
#           json.dump(songs, f, indent= 4)
        


