from behave import given, when, then
from main import login

@given('el usuario está en la página de inicio de sesión')
def step_usuario_en_pagina_inicio_sesion(context):
    context.users_data = [
        {"username": "usuario", "password": "contrasena"},
        {"username": "user2", "password": "pass2"}
    ]

@when('el usuario ingresa su nombre de usuario "{username}" y contraseña "{password}"')
def step_usuario_ingresa_credenciales(context, username, password):
    context.login_result = login(context.users_data, username, password)
    
@then('el usuario debe ser autenticado')
def step_usuario_autenticado(context):
    assert context.login_result is True, "Expected login to be successful but it failed."

@then('el sistema debe mostrar un mensaje de error "{message}"')
def step_then_login_fail(context, message):
    assert context.login_result is False, "Expected login to be unsuccessfull but it succedeed."


