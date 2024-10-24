from behave import given, when, then

@given('el usuario ha iniciado sesión')
def step_usuario_ha_iniciado_sesion(context):
    context.logged_in = True

@given('hay álbumes y canciones cargadas')
def step_albumes_y_canciones_cargadas(context):
    context.available_songs = {'Título de la Canción': {'artista': 'Artista', 'album': 'Álbum'}}

@when('el usuario selecciona la canción "{song_title}"')
def step_usuario_selecciona_cancion(context, song_title):
    assert context.logged_in is True
    context.selected_song = context.available_songs.get(song_title)

@then('el sistema debe reproducir la canción')
def step_sistema_reproduce_cancion(context):
    assert context.selected_song is not None

@then('debe mostrar la información de la canción "{song_title}", "Artista", "Álbum"')
def step_mostrar_informacion_cancion(context, song_title):
    song_info = context.available_songs.get(song_title)
    assert song_info is not None
    assert song_info['artista'] == "Artista"
    assert song_info['album'] == "Álbum"
    
@then('el sistema debe reproducir la canción And debe mostrar la información de la canción "Título de la Canción", "Artista", "Álbum"')
def step_impl(context):
    song_info = context.selected_song  # Simulating that the song was selected
    assert song_info['title'] == "Título de la Canción"
    assert song_info['artist'] == "Artista"
    assert song_info['album'] == "Álbum"
    
    # Simulate the song playback (this can be a mock or actual function)
    context.song_playing = True
    assert context.song_playing  # Verify that the song is being played
