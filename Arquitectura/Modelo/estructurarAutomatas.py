import re
import itertools

def limpiarEstructurar(cadena):
    try:
        found = re.search('{(.+?)}', cadena).group(1)
        variable = found.split(',')
        '''for i in range(len(variable)):
            if variable[i] == "ɛ" or variable[i] == "λ":
                variable[i]= ""'''
        return variable
    except AttributeError:
        pass

def limpiarEstrucTD(str):
    d = []
    result = re.findall('\(.*?\)',str)
    for i in range(len(result)):
        resultado = result[i][result[i].find('(')+1:result[i].find(')')]
        n = resultado.split(',')
        n[1] = n[1].replace(" ", "")
        if n[1] == "ɛ" or n[1] == "λ": #funciona pero hay que saber bien el digito
            n[1] = ""
        d.append(n)
    return d

def limpiarEstrucTND(str):
    d = []
    result = re.findall('\(.*?\)',str)
    for i in range(len(result)):
        t = []
        resultado = result[i][result[i].find('(')+1:result[i].find(')')]
        found = re.search('{(.+?)}', resultado).group(1)
        s = found.split(',')
        for j in range(len(s)):
            s[j]= s[j].replace(" ", "")
        n = resultado.split(',')
        t.append(n[0].replace(" ", ""))
        n[1]=n[1].replace(" ", "")
        if n[1]=="ɛ"or n[1]=="λ": #funciona pero hay que saber bien el digito
            n[1]=""
        t.append(n[1])
        t.append(s)
        d.append(t)
    return d

def remove_char(cadena,inicio,fin):
    return cadena[ inicio:len(cadena) - fin]

def removeInicial(cadena,inicio):
    return cadena[inicio:]