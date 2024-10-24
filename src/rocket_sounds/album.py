class Album:
    def __init__(self, title, artist, release_year, label, tracks=None):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.label = label
        self.tracks = tracks if tracks is not None else []

    def add_track(self, track):
        self.tracks.append(track)

    def get_album_info(self):
        return {
            "Title": self.title,
            "Artist": self.artist,
            "Release Year": self.release_year,
            "Label": self.label,
            "Number of Tracks": len(self.tracks),
            "Tracks": [track.get_song_info() for track in self.tracks]
        }

    def __str__(self):
        return f"Album: '{self.title}' by {self.artist} ({self.release_year})"
    