import os
from playsound import playsound

class Player:
    def __init__(self, media_dir):
        self.media_dir = media_dir
        
    def play(self, media):
        for m in media:
            file_path = os.path.join(self.media_dir, m.get_file())
            # playsound(file_path)
            print(m)