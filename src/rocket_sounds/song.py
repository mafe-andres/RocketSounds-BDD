from media import Media

class Song(Media):
    def __init__(self, title, artist, album, duration, track_number, writers, producers, lyrics, file):
        super().__init__(title, artist, duration, file)
        self.album = album
        self.track_number = track_number
        self.writers = writers
        self.producers = producers
        self.lyrics = lyrics

    def __str__(self):
        return f"'{self.title}' by {self.person} from the album '{self.album}')"

    def get_song_info(self):
        return {
            "Title": self.title,
            "Artist": self.artist,
            "Album": self.album,
            "Duration": self.duration,
            "Track Number": self.track_number,
            "Writers": self.writers,
            "Producers": self.producers,
            "Lyrics": self.lyrics,
        }
        
    def get_file(self):
        return self.file