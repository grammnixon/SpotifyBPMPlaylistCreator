import sys
import random
import math
import spotipy
import spotipy.util as util
from collections import OrderedDict
scope = 'user-library-modify playlist-modify-public'
username = 'grammnixon1'
redirectUri = 'http://localhost:8888/callback'
clientId = 'cd6af65dd90340288b2bd6b33dc33771'
clientSecret = '0ccc719218a3496e842c557700f5507c'
token = util.prompt_for_user_token(username, scope, client_id=clientId,client_secret = clientSecret, redirect_uri=redirectUri)
spotify = spotipy.Spotify(auth=token)


all_songs = OrderedDict()
playlist_array = []
song_playlist = []
song1_bucket = [] #90-110
song2_bucket = [] #60-70
song3_bucket = [] #75-85
song4_bucket = [] #90-126
song5_bucket = [] #80-90
song6_bucket = [] #60-70
song7_bucket = [] #45-60
song8_bucket = [] #85-110
song9_bucket = [] #80-90
song10_bucket = [] #70-90
song11_bucket = [] #45-65
song12_bucket = [] #90-126
playlist_bucket = []
playlist_ids = []

def show_all(tracks):
    ids = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        ids.append(track['id'])
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])
    try:
        all_features = spotify.audio_features(ids)
        tempo = [x['tempo'] for x in all_features]
        for i, item in enumerate(tracks['items']):
            track = item['track']
            print "   %s %s | Tempo:  %d" % (track['artists'][0]['name'], track['name'] , math.ceil(tempo[i]))
            track_id = track['id']
            all_songs[track_id]=math.ceil(tempo[i])
    except:
        print "Top playlist is empty! make sure to populate it!"
        sys.exit(1)
        

def show_tracks(tracks):
    tids = []
    total_sum = 0
    for i, item in enumerate(tracks['items']):
        track = item['track']
        tids.append(track['id'])
    features = spotify.audio_features(tids)
    for f in features:
         tempo = f['tempo']
        #print "THESE ARE THE FEATUERS:" + f
#    tempo = [y['tempo'] for y in features]
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %s %s | Tempo:  %d" % (track['artists'][0]['name'],
            track['name'], math.ceil(tempo[i]))
        track_id = track['id']
        all_songs[track_id]=math.ceil(tempo[i])

def create_list(dict):
    for key, value in dict.items():
        if ((value >=90) and (value <= 110)):
            song1_bucket.append(key)
        if ((value >= 60) and (value <= 70)):
            song2_bucket.append(key)
        if ((value >= 75) and (value <= 85)):
            song3_bucket.append(key)
        if ((value >= 90) and (value <= 126)):
            song4_bucket.append(key)
        if ((value >= 80) and (value <= 90)):
            song5_bucket.append(key)
        if ((value >= 60) and (value <= 70)):
            song6_bucket.append(key)
        if ((value >= 45) and (value <= 60)):
            song7_bucket.append(key)
        if ((value >= 85) and (value <= 110)):
            song8_bucket.append(key)
        if ((value >= 80) and (value <= 90)):
            song9_bucket.append(key)
        if ((value >= 70) and (value <= 90)):
            song10_bucket.append(key)
        if ((value >= 45) and (value <= 65)):
            song11_bucket.append(key)
        if ((value >= 90) and (value <= 126)):
            song12_bucket.append(key)
        else:
            new_value = value/2
            if ((new_value >=90) and (new_value <= 110)):
                song1_bucket.append(key)
            if ((new_value >= 60) and (new_value <= 70)):
                song2_bucket.append(key)
            if ((new_value >= 75) and (new_value <= 85)):
                song3_bucket.append(key)
            if ((new_value >= 90) and (new_value <= 126)):
                song4_bucket.append(key)
            if ((new_value >= 80) and (new_value <= 90)):
                song5_bucket.append(key)
            if ((new_value >= 60) and (new_value <= 70)):
                song6_bucket.append(key)
            if ((new_value >= 45) and (new_value <= 60)):
                song7_bucket.append(key)
            if ((new_value >= 85) and (new_value <= 110)):
                song8_bucket.append(key)
            if ((new_value >= 80) and (new_value <= 90)):
                song9_bucket.append(key)
            if ((new_value >= 70) and (new_value <= 90)):
                song10_bucket.append(key)
            if ((new_value >= 45) and (new_value <= 65)):
                song11_bucket.append(key)
            if ((new_value >= 90) and (new_value <= 126)):
                song12_bucket.append(key)
            
    print "======song1bucket====="
    for i in song1_bucket:
        print i
    print "======song2bucket====="
    for j in song2_bucket:
        print j
    print "======song3bucket====="
    for j in song3_bucket:
        print j
    print "======song4bucket====="
    for j in song4_bucket:
        print j
    print "======song5bucket====="
    for j in song5_bucket:
        print j
    print "======song6bucket====="
    for j in song6_bucket:
        print j
    print "======song7bucket====="
    for j in song7_bucket:
        print j
    print "======song8bucket====="
    for j in song8_bucket:
        print j
    print "======song9bucket====="
    for j in song9_bucket:
        print j
    print "======song10bucket====="
    for j in song10_bucket:
        print j
    print "======song11bucket====="
    for j in song11_bucket:
        print j
    print "======song12bucket====="
    for j in song12_bucket:
        print j

def amount_playlists():
    small_length = len(song1_bucket)
    if (len(song2_bucket) <= small_length):
        small_length = len(song2_bucket)
    if (len(song3_bucket) <= small_length):
        small_length = len(song3_bucket)
    if (len(song4_bucket) <= small_length):
        small_length = len(song4_bucket)
    if (len(song5_bucket) <= small_length):
        small_length = len(song5_bucket)
    if (len(song6_bucket) <= small_length):
        small_length = len(song6_bucket)
    if (len(song7_bucket) <= small_length):
        small_length = len(song7_bucket)
    if (len(song8_bucket) <= small_length):
        small_length = len(song8_bucket)
    if (len(song9_bucket) <= small_length):
        small_length = len(song9_bucket)
    if (len(song10_bucket) <= small_length):
        small_length = len(song10_bucket)
    if (len(song11_bucket) <= small_length):
        small_length = len(song11_bucket)
    if (len(song12_bucket) <= small_length):
        small_length = len(song12_bucket)

    return small_length
                
if token:
	playlists = spotify.user_playlists(username)
	for playlist in playlists['items']:
		if playlist['owner']['id'] == username:
			results = spotify.user_playlist(username, playlist['id'],
				fields="tracks,next")
			tracks = results['tracks']
			show_all(tracks)
			while tracks['next']:
				tracks = spotify.next(tracks)
				show_all(tracks)
        create_list(all_songs)
        for x in range (0, amount_playlists()):
            playlist_name = "CB_BPM_Playlist_" + str(x+1)
            spotify.user_playlist_create(username, playlist_name, public=True)
        new_playlists = spotify.user_playlists(username)
        for p in new_playlists['items']:
            if p['name'].startswith("CB_BPM_Playlist_"):
                playlist_ids.append(p['id'])
        for x in playlist_ids:
            print "PLAYLIST IDS:" + x
            print len(playlist_ids) 
        if (len(playlist_ids)-1 == 0):
            playlist_bucket.append(song1_bucket[random.randint(0,len(song1_bucket)-1)])
            playlist_bucket.append(song2_bucket[random.randint(0,len(song2_bucket)-1)])
            playlist_bucket.append(song3_bucket[random.randint(0,len(song3_bucket)-1)])
            playlist_bucket.append(song4_bucket[random.randint(0,len(song4_bucket)-1)])
            playlist_bucket.append(song5_bucket[random.randint(0,len(song5_bucket)-1)])
            playlist_bucket.append(song6_bucket[random.randint(0,len(song6_bucket)-1)])
            playlist_bucket.append(song7_bucket[random.randint(0,len(song7_bucket)-1)])
            playlist_bucket.append(song8_bucket[random.randint(0,len(song8_bucket)-1)])
            playlist_bucket.append(song9_bucket[random.randint(0,len(song9_bucket)-1)])
            playlist_bucket.append(song10_bucket[random.randint(0,len(song10_bucket)-1)])
            playlist_bucket.append(song11_bucket[random.randint(0,len(song11_bucket)-1)])
            playlist_bucket.append(song12_bucket[random.randint(0,len(song12_bucket)-1)])
            results = spotify.user_playlist_add_tracks(username, playlist_ids[0], playlist_bucket)
        else:
            for y in range (0, len(playlist_ids)-1):
                playlist_bucket.append(song1_bucket[y])
                playlist_bucket.append(song2_bucket[y])
                playlist_bucket.append(song3_bucket[y])
                playlist_bucket.append(song4_bucket[y])
                playlist_bucket.append(song5_bucket[y])
                playlist_bucket.append(song6_bucket[y])
                playlist_bucket.append(song7_bucket[y])
                playlist_bucket.append(song8_bucket[y])
                playlist_bucket.append(song9_bucket[y])
                playlist_bucket.append(song10_bucket[y])
                playlist_bucket.append(song11_bucket[y])
                playlist_bucket.append(song12_bucket[y])
                results = spotify.user_playlist_add_tracks(username, playlist_ids[y], playlist_bucket)
#        results = spotify.user_playlist_add_tracks(username, playlist_ids, playlist_bucket)
#        playlist_ids[:] = []
else:
	print "Can't get token for", username
