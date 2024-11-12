import random
from behave import given, when, then
from unittest.mock import patch, MagicMock
from io import StringIO
from podcast import Podcast
from podcast_episode import PodcastEpisode
from song import Song
from album import Album
from data import Data
from main import shuffle

def create_mock_data():
    podcast1 = Podcast(
        title="Podcast1",
        host="Anfitrion",
        publisher="Publisher1"
    )

    episode1 = PodcastEpisode(
        title="Titulo del Episodio 1",
        host="Anfitrion",
        podcast=podcast1,
        release_date="Fecha de Lanzamiento",
        duration=3600,
        episode_number=1,
        description="An in-depth discussion on the future of artificial intelligence.",
        guests=["Dr. Jane Doe", "Prof. Alan Turing"],
        file="episode1.mp3"
    )
    
    episode2 = PodcastEpisode(
        title="Titulo del Episodio 2",
        host="Anfitrion",
        podcast=podcast1,
        release_date="Fecha de Lanzamiento",
        duration=3600,
        episode_number=1,
        description="An in-depth discussion on the future of artificial intelligence.",
        guests=["Dr. Jane Doe", "Prof. Alan Turing"],
        file="episode1.mp3"
    )
    
    album1 = Album(
        title="Album",
        artist="The Rockers",
        release_year=2021,
        label="RockLabel"
    )

    song1 = Song(
        title="Titulo de la Cancion 1",
        artist="Artista",
        album=album1,
        duration=300,
        track_number=1,
        writers=["Rocky Stone", "Jim Beat"],
        producers=["Rocky Stone"],
        lyrics="We will, we will rock you...",
        file="rock_anthem.mp3"
    )
    
    song2 = Song(
        title="Titulo de la Cancion 2",
        artist="Artista",
        album=album1,
        duration=300,
        track_number=1,
        writers=["Rocky Stone", "Jim Beat"],
        producers=["Rocky Stone"],
        lyrics="We will, we will rock you...",
        file="rock_anthem.mp3"
    )
    mock_data = Data()
    mock_data.podcasts = [podcast1]
    mock_data.podcast_episodes = [episode1, episode2]
    mock_data.albums = [album1]
    mock_data.songs = [song1, song2]
    return mock_data

@given('hay canciones y episodios de podcast disponibles')
def step_canciones_y_podcasts_disponibles(context):
    mock_data = create_mock_data()
    context.mock_media = mock_data.songs + mock_data.podcasts

@when('el usuario elige reproducir contenido de forma aleatoria')
def step_reproducir_aleatoriamente(context):
    pass 

@then('el sistema debe mezclar todas las canciones y episodios de podcast')
def step_mezclar_contenido(context):
    context.original_media = context.mock_media
    context.mock_player = MagicMock()
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        shuffle(context.mock_media, context.mock_player)
        context.printed_output = mock_stdout.getvalue()

@then('debe reproducirlos de manera aleatoria')
def step_reproducir_aleatorio(context):
    context.mock_player.play.assert_called_once_with(context.original_media)