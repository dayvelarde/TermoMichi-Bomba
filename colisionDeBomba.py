def colisionDeBomba(posicionJugador, bombas):
    if posicionJugador in bombas:
        bombas.remove(posicionJugador)
        return True
    return False
