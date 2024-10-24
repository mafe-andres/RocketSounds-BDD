from behave import given, when, then

@given('hay series de podcasts y episodios disponibles')
def step_series_y_episodios_disponibles(context):
    context.available_podcasts = {'Título del Episodio': {'anfitrion': 'Anfitrión', 'fecha_lanzamiento': 'Fecha de Lanzamiento'}}

@when('el usuario selecciona el episodio "{episode_title}"')
def step_usuario_selecciona_episodio(context, episode_title):
    context.selected_episode = context.available_podcasts.get(episode_title)

@then('el sistema debe reproducir el episodio')
def step_sistema_reproduce_episodio(context):
    assert context.selected_episode is not None

@then('debe mostrar la información del episodio "{episode_title}", "Anfitrión", "Fecha de Lanzamiento"')
def step_mostrar_informacion_episodio(context, episode_title):
    episode_info = context.available_podcasts.get(episode_title)
    assert episode_info is not None
    assert episode_info['anfitrion'] == 'Anfitrión'
    assert episode_info['fecha_lanzamiento'] == 'Fecha de Lanzamiento'
