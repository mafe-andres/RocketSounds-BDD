Feature: Reproducción de Episodios de Podcast
  Scenario: Reproducir un episodio de podcast específico
    Given el usuario ha iniciado sesión
    And hay series de podcasts y episodios disponibles
    When el usuario selecciona el episodio "Título del Episodio"
    Then el sistema debe reproducir el episodio
    And debe mostrar la información del episodio "Título del Episodio", "Anfitrión", "Fecha de Lanzamiento"