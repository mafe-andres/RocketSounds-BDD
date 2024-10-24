class Media:
    def __init__(self, title, person, duration, file):
        self.title = title
        self.person = person
        self.duration = duration
        self.file = file
        
    def play(self):
        print(f'{self.title} by {self.person} is playing. Duration: {self.duration}')
        