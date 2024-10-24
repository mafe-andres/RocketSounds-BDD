Feature: Reproducción de Canciones
  Scenario: Reproducir una canción específica
    Given el usuario ha iniciado sesión
    And hay álbumes y canciones cargadas
    When el usuario selecciona la canción "Título de la Canción"
    Then el sistema debe reproducir la canción And debe mostrar la información de la canción "Título de la Canción", "Artista", "Álbum"