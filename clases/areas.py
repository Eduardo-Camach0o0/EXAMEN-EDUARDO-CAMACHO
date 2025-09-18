class figuras1:

    def __init__(self):
        self.areaTr = 0
        self.areaRec = 0
        return 
    
    def areaTriangulo(self, base, altura):
        self.areaTr = (base*altura)/2
        return 
    
    def mostrarAreaTriangulo(self):
        return f"El área del tringulo dado es: {self.areaTr}"
    
    def areaRectangulo(self, base, altura):
        self.areaRec = (base*altura)
        return 

    def mostrarAreaRectangulo(self):
        return f"El área del rectangulo dado es: {self.areaRec}"

