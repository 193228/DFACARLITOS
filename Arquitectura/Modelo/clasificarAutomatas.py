from Arquitectura.Modelo.estructurarAutomatas import *
from Arquitectura.Modelo.Transicion import *

def clasificacionAutomata(automata):
    q0 = ""; Q = []; S = []; F = [];  D = []; bandera = "";

    for i in range(len(automata)):
            if automata[i][0:2] == 'q0':
                inicial = removeInicial(automata[i], 3)
                q0 = inicial
            elif automata[i][0] == 'Q':
                resultado= removeInicial(automata[i],2)
                Q = limpiarEstructurar(resultado)
            elif automata[i][0] == 'S':
                resultado= removeInicial(automata[i],2)
                S = limpiarEstructurar(resultado)
                S = set(S)
            elif automata[i][0] == 'F':
                resultado = removeInicial(automata[i], 2)
                F = limpiarEstructurar(resultado)
                F = set(F)
            elif automata[i][0] == 'D':
                resultado = removeInicial(automata[i], 2)
                found = re.search('{(.+?)}', resultado).group(1)
                if found.find("{") != -1:
                    print("AUTOMATA ES NO DETERMINISTA")
                    z = limpiarEstrucTND(resultado)
                    crearDiccionario(z,Q)
                    D = retornarDiccionario()
                    bandera = "no determinista"
                else:
                    print("AUTOMATA ES DETERMINISTA")
                    z = limpiarEstrucTD(resultado)
                    crearDiccionario(z, Q)
                    D = retornarDiccionario()
                    bandera = "determinista"

    return estructurarAutomata(Q,S,D,q0,F,bandera)

def estructurarAutomata(Q,S,D,q0,F,bandera):
    Q = set(Q)
    sistema = {"estados": Q, "lenguaje": S, "transiciones": D, "estadoInicial": q0, "estadosFinales": F, "tipo": bandera}
    print("IMPRIMO ",sistema)
    return sistema