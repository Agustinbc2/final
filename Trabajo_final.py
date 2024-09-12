from trabajo_final2 import activar_vacaciones
class Alumno:
    def __init__(self, nombre, humor, color_de_pelo, color_de_ojos, altura):
        self.nombre = nombre
        self.humor = humor
        self.color_de_pelo = color_de_pelo
        self.color_de_ojos = color_de_ojos
        self.altura = altura
        self.preparacion_para_examen = False
        self.estudio = 0
        self.cansancio = True
        self.en_vacaciones=False
        
    def estudiar(self, horas):
        if self.cansancio:
            horas -= 1
            print(f"{self.nombre} está cansado y pierde una hora de estudio.")
        
        horas = max(horas, 0)
        self.estudio += horas
        print(f"{self.nombre} ha estudiado {horas} horas. Total acumulado: {self.estudio} horas.")
        
        if self.estudio >= 5:
            self.preparacion_para_examen = True
            print(f"{self.nombre} ahora está preparado para el examen.")
        else:
            self.preparacion_para_examen = False
            print(f"{self.nombre} aún no está preparado para el examen.")
        
    def mostrar_estado(self):
        print(f"Preparación para examen: {self.preparacion_para_examen}")
        print(f"Horas de estudio: {self.estudio}")
        print(f"Cansancio: {self.cansancio}")
        print(f"Humor: {self.humor}")
        
    def descansar(self):
        self.cansancio = False
        print(f"{self.nombre} ha dormido y ahora está descansado.")
        
    def tomar_examen(self):
        if self.preparacion_para_examen:
            self.humor = "Feliz"
            print(f"{self.nombre} aprobó el examen y está feliz.")
            self.en_vacaciones=activar_vacaciones(self.nombre)
        else:
            self.humor = "Enojado/Frustrado"
            print(f"{self.nombre} desaprobó el examen y está enojado")



Alumno1=Alumno("jose","neutro","rubio","azules",1.73)
Alumno1.descansar()
Alumno1.estudiar(5)
Alumno1.mostrar_estado()

Alumno1.tomar_examen()



        
            
            
        
        
        