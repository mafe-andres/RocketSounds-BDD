Feature: Reproducción de Canciones
  Scenario: Reproducir una canción específica
    Given hay albumes y canciones cargadas
    When el usuario selecciona la canción "Titulo de la Cancion"
    Then el sistema debe reproducir la canción 
    And debe mostrar la información de la canción "Titulo de la Cancion", "Artista", "Album"