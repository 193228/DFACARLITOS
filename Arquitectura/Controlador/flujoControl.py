import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from Arquitectura.Modelo.archivoTxt import *
from Arquitectura.Modelo.clasificarAutomatas import *
from Arquitectura.Modelo.Automatas import *

aux = ['']
enlaceGraphviz = "https://graphviz.org/download/"

def abrirExplorador():
    aux.clear()
    automataCargado = leerArchivo()
    automata = clasificacionAutomata(automataCargado) #aca ya esta
    aux.append(automata)


def analizarCadena(ventana):
    ventana.tablaTransiciones.setRowCount(0)
    cadena = ventana.textEdit.toPlainText()
    automataLeido = aux[0]
    if len(cadena)!=0 and automataLeido["tipo"] == "determinista" or automataLeido["tipo"] == "no determinista":
        if automataLeido["tipo"] == "determinista":
            try:
                afd = generarAutomataDeterminista(automataLeido)
                automata = VisualDFA(afd)
                #fd = automata.show_diagram(cadena)
                #fd.render('Automatas/AutomataGenerado.gv', view=True)
                yu = automata.input_check(cadena)
                procesoAutomata(yu, ventana, automataLeido)
            except:
                PyQt5.QtWidgets.QMessageBox.about(None, "Error", "Se leyo el automata finito determinista, pero no coincide con el lenguaje\nLimpiando la tabla")
                pass
        elif automataLeido["tipo"] == "no determinista":
            try:
                afn = generarAutomataNoDeterminista(automataLeido)
                d = VisualNFA(afn);
                automata = VisualNFA.eliminate_lambda(d)
                #nd = automata.show_diagram(cadena)
                #nd.render('Automatas/AutomataGenerado.gv', view=True)
                yu = automata.input_check(cadena)
                procesoAutomata(yu, ventana, automataLeido)
            except:
                PyQt5.QtWidgets.QMessageBox.about(None, "Error", "Se leyo el automata finito no determinista, pero no coincide con el lenguaje\nLimpiando la tabla")
                pass
    else:
        PyQt5.QtWidgets.QMessageBox.about(None, "Verifique","La cadena se encuentra vacia o no se reconocio el automata")

def creacionDataframe(pasos, dataframe):
    df = pd.DataFrame({
        "pasos": pasos,
        "estadoActual": dataframe.iloc[:, 0],
        "simboloEntrada": dataframe.iloc[:, 1],
        "nuevoEstado": dataframe.iloc[:, 2]
    })
    return df

def tablaAutomata(ventana, dataframe):
    pasos = np.array(dataframe["pasos"])
    actual = np.array(dataframe["estadoActual"])
    entrada = np.array(dataframe["simboloEntrada"])
    nuevo = np.array(dataframe["nuevoEstado"])

    dato = int(dataframe.size / 4)
    ventana.tablaTransiciones.setRowCount(dato)
    tablerow = 0

    for i in range(dato):
        ventana.tablaTransiciones.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(pasos[i])))
        ventana.tablaTransiciones.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(actual[i])))
        ventana.tablaTransiciones.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(entrada[i])))
        ventana.tablaTransiciones.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(nuevo[i])))
        tablerow += 1


def procesoAutomata(automata,ventana,lista):
    x = automata.columns
    x = x[0][0]

    if x == "[Rejected]":
        ventana.tipoCadena.setText("Cadena Invalida")
    else:
        ventana.tipoCadena.setText("Cadena Aceptada")

    if lista["tipo"] == "determinista":
        ventana.tipoAutomata.setText("Automata Finito Determinista")
    else:
        ventana.tipoAutomata.setText("Automata Finito No Determinista")

    pasos = automata.index.values  # dataframe
    df = creacionDataframe(pasos, automata)
    tablaAutomata(ventana, df)
