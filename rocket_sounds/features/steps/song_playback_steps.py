from behave import given, when, then
from unittest.mock import patch
from io import StringIO
from song import Song
from album import Album
from data import Data
from player import Player
from main import search_media

def create_mock_data():
    album1 = Album(
        title="Album",
        artist="The Rockers",
        release_year=2021,
        label="RockLabel"
    )

    song1 = Song(
        title="Titulo de la Cancion",
        artist="Artista",
        album=album1,
        duration=300,
        track_number=1,
        writers=["Rocky Stone", "Jim Beat"],
        producers=["Rocky Stone"],
        lyrics="We will, we will rock you...",
        file="rock_anthem.mp3"
    )
    album1.add_track(song1)
    
    mock_data = Data()
    mock_data.albums = [album1]
    mock_data.songs = [song1]
    return mock_data

@given('hay albumes y canciones cargadas')
def step_series_y_episodios_disponibles(context):
    context.mock_media = create_mock_data().songs

@when('el usuario selecciona la canción "{song_title}"')
def step_usuario_selecciona_episodio(context, song_title):
    context.selected_song = search_media(song_title, context.mock_media)

@then('el sistema debe reproducir la canción')
def step_sistema_reproduce_episodio(context):
    assert context.selected_song is not None
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        player = Player('mock_dir')
        player.play([context.selected_song])
        context.printed_output = mock_stdout.getvalue()

@then('debe mostrar la información de la canción "{song_title}", "{artista}", "{album}"')
def step_sistema_reproduce_episodio(context, song_title, artista, album):
    assert song_title in context.printed_output, f"Expected substring '{song_title}' not found in {context.printed_output}."
    assert artista in context.printed_output, f"Expected substring '{artista}' not found in {context.printed_output}."
    assert album in context.printed_output, f"Expected substring '{album}' not found in {context.printed_output}."