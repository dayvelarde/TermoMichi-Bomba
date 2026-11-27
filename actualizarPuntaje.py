def actualizarPuntaje(posicionJugador, pescados, puntaje, puntosPorPescado=100):
    if posicionJugador in pescados:
        pescados.remove(posicionJugador)
        puntaje += puntosPorPescado
    return puntaje