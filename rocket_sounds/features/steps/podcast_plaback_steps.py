from behave import given, when, then
from unittest.mock import patch
from io import StringIO
from podcast import Podcast
from data import Data
from main import search_media
from player import Player
from podcast_episode import PodcastEpisode

def create_mock_data():
    podcast1 = Podcast(
        title="Podcast1",
        host="Anfitrion",
        publisher="Publisher1"
    )

    episode1 = PodcastEpisode(
        title="Titulo del Episodio",
        host="Anfitrion",
        podcast=podcast1,
        release_date="Fecha de Lanzamiento",
        duration=3600,
        episode_number=1,
        description="An in-depth discussion on the future of artificial intelligence.",
        guests=["Dr. Jane Doe", "Prof. Alan Turing"],
        file="episode1.mp3"
    )
    podcast1.add_episode(episode1)
    
    mock_data = Data()
    mock_data.podcasts = [podcast1]
    mock_data.podcast_episodes = [episode1]
    return mock_data

@given('hay series de podcasts y episodios disponibles')
def step_series_y_episodios_disponibles(context):
    context.mock_media = create_mock_data().podcast_episodes

@when('el usuario selecciona el episodio "{episode_title}"')
def step_usuario_selecciona_episodio(context, episode_title):
    context.selected_episode = search_media(episode_title, context.mock_media)

@then('el sistema debe reproducir el episodio')
def step_sistema_reproduce_episodio(context):
    assert context.selected_episode is not None
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        player = Player('mock_dir')
        player.play([context.selected_episode])
        context.printed_output = mock_stdout.getvalue()

@then('debe mostrar la información del episodio "{episode_title}", "{host}", "{release_date}"')
def step_sistema_reproduce_episodio(context, episode_title, host, release_date):
    assert episode_title in context.printed_output, f"Expected substring '{episode_title}' not found in {context.printed_output}."
    assert host in context.printed_output, f"Expected substring '{host}' not found in {context.printed_output}."
    assert release_date in context.printed_output, f"Expected substring '{release_date}' not found in {context.printed_output}."