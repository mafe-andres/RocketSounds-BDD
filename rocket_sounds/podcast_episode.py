from media import Media

class PodcastEpisode(Media):
    def __init__(self, title, host, podcast, release_date, duration, episode_number, description, guests, file):
        super().__init__(title, host, duration, file)
        self.podcast = podcast
        self.release_date = release_date
        self.episode_number = episode_number
        self.description = description
        self.guests = guests

    def __str__(self):
        return f"'{self.title}' hosted by {self.person}, Episode {self.episode_number} ({self.release_date})"

    def get_episode_info(self):
        return {
            "Title": self.title,
            "Host": self.host,
            "Podcast": self.podcast,
            "Release Date": self.release_date,
            "Duration": self.duration,
            "Episode Number": self.episode_number,
            "Description": self.description,
            "Guests": self.guests,
        }
        
    def get_file(self):
        return self.file