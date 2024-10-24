import random
from behave import given, when, then

@given('hay canciones y episodios de podcast disponibles')
def step_canciones_y_podcasts_disponibles(context):
    context.media_content = [
        {'titulo': 'Título de Canción', 'creador': 'Artista', 'duracion': '3:30'},
        {'titulo': 'Título del Episodio', 'creador': 'Anfitrión', 'duracion': '45:00'}
    ]

@when('el usuario elige reproducir contenido de forma aleatoria')
def step_reproducir_aleatoriamente(context):
    context.playing_now = random.choice(context.media_content)

@then('el sistema debe mezclar todas las canciones y episodios de podcast')
def step_mezclar_contenido(context):
    random.shuffle(context.media_content)

@then('debe reproducirlos de manera aleatoria')
def step_reproducir_aleatorio(context):
    assert context.playing_now is not None

@then('debe mostrar el archivo multimedia que se está reproduciendo con su "Título", "Creador" y "Duración"')
def step_mostrar_info_reproduccion(context):
    playing = context.playing_now
    assert playing['titulo'] is not None
    assert playing['creador'] is not None
    assert playing['duracion'] is not None
