Feature: Autenticación del Usuario
  Scenario: Iniciar sesión con credenciales correctas
    Given el usuario está en la página de inicio de sesión
    When el usuario ingresa su nombre de usuario "usuario" y contraseña "contrasena"
    Then el usuario debe ser autenticado

  Scenario: Iniciar sesión con credenciales incorrectas
    Given el usuario está en la página de inicio de sesión
    When el usuario ingresa su nombre de usuario "usuario_invalido" y contraseña "contraseña_incorrecta"
    Then el sistema debe mostrar un mensaje de error "Invalid username or password."
