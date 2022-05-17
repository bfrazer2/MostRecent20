import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util

username = "22q2xgqzky6a2zzsvpc3a2pma"
scope = "playlist-modify-private"
client_id = ""
client_secret = ""
redirect_uri = ""

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


sp = spotipy.Spotify(auth=token)

most_recent_20 = "33hHpD2547qf39434V8QEo"
literally_everything = "2Z4gcXJCAWMgSDeynAzg2r"

class GetPlaylistTracks:
    
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.track_list = []
        self.uri_list = []
    
    def get_playlist_items(self):
        results = sp.playlist_items(self.playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
  
        for idx, item in enumerate(tracks[-20:]):
            track = item['track']
            self.track_list.append(track['name'])
            self.uri_list.append(track['uri'])

class URIid:
    
    def __init__(self, playlist_id1, track_list1, uri_list1, playlist_id2, track_list2, uri_list2):
        self.playlist_id1 = playlist_id1
        self.track_list1 = track_list1
        self.uri_list1 = uri_list1
        self.playlist_id2 = playlist_id2
        self.track_list2 = track_list2
        self.uri_list2 = uri_list2
        self.uris_to_add = []
        self.uris_to_remove = []
        
    def get_uris_to_add(self):
        for song in self.track_list1:
            if song not in self.track_list2:
                index = self.track_list1.index(song)
                self.uris_to_add.append(self.uri_list1[index])
    
    def get_uris_to_remove(self):
        for song in self.track_list2:
            if song not in self.track_list1:
                index = self.track_list2.index(song)
                self.uris_to_remove.append(self.uri_list2[index])
                
    def add_uris(self):
        for uri in self.uris_to_add:
            sp.playlist_add_items(self.playlist_id2, [uri])
    
    def remove_uris(self):
        for uri in self.uris_to_remove: 
            sp.playlist_remove_all_occurrences_of_items(self.playlist_id2, [uri])
        
