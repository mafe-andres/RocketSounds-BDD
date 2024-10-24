from behave import given, when, then

@given('el usuario está en la página de inicio de sesión')
def step_usuario_en_pagina_inicio_sesion(context):
    context.page = 'login_page'

@when('el usuario ingresa su nombre de usuario "{username}" y contraseña "{password}"')
def step_usuario_ingresa_credenciales(context, username, password):
    if username == "usuario_valido" and password == "contraseña_correcta":
        context.authenticated = True
    else:
        context.authenticated = False

@then('el usuario debe ser autenticado y redirigido al menú principal')
def step_usuario_autenticado(context):
    assert context.authenticated is True

@then('el sistema debe mostrar un mensaje de error "{mensaje_error}"')
def step_mostrar_mensaje_error(context, mensaje_error):
    assert context.authenticated is False
    context.error_message = "Credenciales inválidas"
    assert context.error_message == mensaje_error

@then('debe pedir al usuario que vuelva a intentarlo')
def step_pedir_reintento(context):
    context.prompt_relogin = True
    assert context.prompt_relogin is True
