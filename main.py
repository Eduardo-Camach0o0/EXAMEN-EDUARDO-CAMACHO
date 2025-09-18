from clases.areas import figuras1

def areaTrianguloMain():
    base = float(input("Ingrese su  base: "))
    altura = float(input("Ingrese su  altura: "))

    instacia = figuras1()

    instacia.areaTriangulo(base, altura)

    print (instacia.mostrarAreaTriangulo())

def areaRectanguloMain():
    base = float(input("Ingrese su  base: "))
    altura = float(input("Ingrese su  altura: "))

    instacia = figuras1()

    instacia.areaRectangulo(base, altura)

    print (instacia.mostrarAreaRectangulo())


areaTrianguloMain()

areaRectanguloMain()