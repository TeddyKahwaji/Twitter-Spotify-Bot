import json
import requests
import os
from Refresher import Refresh

USER_ID = os.environ.get("USER_ID")


class SpotifyAPIContainer:
    def __init__(self):
        self.user_id = USER_ID
        self.spotify_token = ""
        self.checkerSet = set()
        self.playlist_id = "2hG55i5eClTfIwuH68VJFn"

    def addSongsToPlaylist(self, songList):
        print("ADDING SONGS TO PLAYLIST")
        query = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
        songList = list(filter(lambda e: e not in self.checkerSet, songList))

        requests_body = json.dumps({
            "uris": songList,
        })
        response = requests.post(query, requests_body, headers=self.header)
        response_json = response.json()
        for song in songList:
            if song not in self.checkerSet:
                self.checkerSet.add(song)

    def refreshToken(self):
        print("REFERSHING TOKEN")
        refresher = Refresh()
        self.spotify_token = refresher.refresh()
        self.header = {"Content-Type": "application/json",
                       "Authorization": f"Bearer {self.spotify_token}"}
