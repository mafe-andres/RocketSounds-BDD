Feature: Reproducción de Contenido de Forma Aleatoria
  Scenario: Reproducir contenido aleatoriamente
    Given el usuario ha iniciado sesión
    And hay canciones y episodios de podcast disponibles
    When el usuario elige reproducir contenido de forma aleatoria
    Then el sistema debe mezclar todas las canciones y episodios de podcast
    And debe reproducirlos de manera aleatoria
    And debe mostrar el archivo multimedia que se está reproduciendo con su "Título", "Creador" y "Duración"
