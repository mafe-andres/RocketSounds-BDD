import json
from album import Album
from song import Song
from podcast import Podcast
from podcast_episode import PodcastEpisode

class Data:
    def __init__(self):
        self.podcasts = []
        self.podcast_episodes = []
        self.album = []
        self.songs = []
        
    def load_podcasts(self, file_path):
        with open(file_path) as file:
            podcast_data = json.load(file)
        
        podcast_list = []
        podcast_episodes_list = []
        for series_data in podcast_data['podcast_series']:
            podcast = Podcast(
                title=series_data['title'],
                host=series_data.get('host') or series_data.get('hosts'),
                publisher=series_data['publisher']
            )
            
            for episode_data in series_data['episodes']:
                episode = PodcastEpisode(
                    title=episode_data['title'],
                    host=episode_data['host'],
                    podcast=podcast,
                    release_date=episode_data['release_date'],
                    duration=episode_data['duration'],
                    episode_number=episode_data['episode_number'],
                    description=episode_data['description'],
                    guests=episode_data['guests'],
                    file=episode_data['file']
                )
                podcast.add_episode(episode)
                podcast_episodes_list.append(episode)
            
            podcast_list.append(podcast)
        
        self.podcasts = podcast_list
        self.podcast_episodes = podcast_episodes_list
 
    def load_music(self, file_path):
        with open(file_path) as file:
            music_data = json.load(file)

        album_list = []
        songs_list = []
        for music_data in music_data['albums']:
            album = Album(
                title=music_data['title'],
                artist=music_data['artist'],
                release_year=music_data['release_year'],
                label=music_data['label']
            )
            
            for track_data in music_data['tracks']:
                track = Song(
                    title=track_data['title'],
                    artist=track_data['artist'],
                    album=album,
                    duration=track_data['duration'],
                    track_number=track_data['track_number'],
                    writers=track_data['writers'],
                    producers=track_data['producers'],
                    lyrics=track_data['lyrics'],
                    file=track_data['file']
                )
                songs_list.append(track)
                album.add_track(track)
            
            album_list.append(album)
            
        self.album = album_list
        self.songs = songs_list
