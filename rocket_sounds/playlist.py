class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        
    def complete_playlist(self, titles, media):
        self.playlist = []
        for title in titles:
            for m in media:
                if title == m.title:
                    self.playlist.append(m)
                    
    def add_media(self, media):
        self.playlist.append(media)