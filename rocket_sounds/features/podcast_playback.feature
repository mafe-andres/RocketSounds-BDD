Feature: Reproducción de Episodios de Podcast
  Scenario: Reproducir un episodio de podcast específico
    Given hay series de podcasts y episodios disponibles
    When el usuario selecciona el episodio "Titulo del Episodio"
    Then el sistema debe reproducir el episodio
    And debe mostrar la información del episodio "Titulo del Episodio", "Anfitrion", "Fecha de Lanzamiento"