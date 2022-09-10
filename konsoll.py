#
# Sjekk versjoner av installerte biblioteker
# Kurset brukte v2.0.0 av dash og v1.0.0 av dash_bootstrap_components

import dash
dash.__version__

import dash_bootstrap_components as dbc
dbc.__version__

#
# Enkle funksjonskall: motivasjon for "Hei Dash"
#
navn = "Geir Arne"
navn

def si_hei(navn):
    print(f"Hei {navn}")

si_hei("Geir Arne")
si_hei("Kristin")
navn  # Variable innenfor en funksjon forstyrrer ikke variable utenfor


#
# Modellering
#

def befolkning(start, vekstrate, antall_tidssteg=20):
    """Enkel eksponensiell befolkningsmodell"""
    tidsserie = []
    
    nå = start
    for tidssteg in range(antall_tidssteg):
        tidsserie.append(nå)
        nå = nå + nå * vekstrate
    
    return tidsserie

befolkning(100, 0.10)


def befolkning(start, vekstrate, maks, antall_tidssteg=20):
    """Befolkningsmodell med ressursknapphet"""
    tidsserie = []
    
    nå = start
    for tidssteg in range(antall_tidssteg):
        tidsserie.append(nå)
        nå = nå + nå * vekstrate * (1 - nå/maks)
    
    return tidsserie

befolkning(100, 0.10, 200)
