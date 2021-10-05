import PyQt5

def abroExplorador():
    ruta = PyQt5.QtWidgets.QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileName()", "","*.txt")
    return str(ruta[0]).join(ruta[0])

def leerArchivo():
    automata= []
    path = abroExplorador()

    if path:
        with open(path,encoding="utf-8") as f:
            lines = f.readlines()
        lines = [x.strip() for x in lines]
        lines = list(filter(None, lines))
        for i in range(len(lines)):
            x = lines[i].replace(" ", "")
            automata.append(x)
    else:
        PyQt5.QtWidgets.QMessageBox.about(None, "Error", "No cargo un archivo TXT")
        pass

    return automata
