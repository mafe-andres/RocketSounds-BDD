class Podcast:
    def __init__(self, title, host, publisher, episodes=None):
        self.title = title
        self.host = host
        self.publisher = publisher
        self.episodes = episodes if episodes is not None else []

    def add_episode(self, episode):
        self.episodes.append(episode)

    def get_podcast_info(self):
        return {
            "Title": self.title,
            "Host": self.host,
            "Publisher": self.publisher,
            "Number of Episodes": len(self.episodes),
            "Episodes": [episode.get_episode_info() for episode in self.episodes]
        }

    def __str__(self):
        return f"Podcast: '{self.title}' hosted by {self.host} ({self.genre})"