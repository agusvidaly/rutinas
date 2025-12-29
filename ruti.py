from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle

amarillo = (0.925, 0.882, 0.792, 1)   # ECE1CA , beige
azul = (0.192, 0.478, 0.831, 1)   # 317AD4 , azul
rojo = (0.831, 0.192, 0.192, 1)  # D43131 , rojo

def ejercicio(nombre, duracion):
    return {
        "nombre": nombre,
        "preparacion": 3,
        "duracion": duracion
    }

MAINS_VERS_LE_CIEL = ejercicio("mains vers le ciel", 30)
FLEXION_AVANT = ejercicio("flexion avant", 30)
FENTE_AVANT_DROIT = ejercicio("fente avant droit", 30)
FENTE_AVANT_GAUCHE = ejercicio("fente avant gauche", 30)
CHIEN_FACE_AU_CIEL = ejercicio("chien face au ciel", 30)
POSTURE_DU_ENFANT = ejercicio("posture du enfant", 30)
CHIEN_TETE_EN_BAS = ejercicio("chien tête en bas", 30)
POSTURE_DU_GRAND_ANGLE = ejercicio("posture du grand angle", 30)
FLEXION_LATERALES_DYNAMIQUES = ejercicio("flexions latérales dynamiques", 30)
CERCLES_AVEC_LES_BRAS = ejercicio("cercles avec les bras", 30)
BALANCEMENT_DE_BRAS = ejercicio("balancement de bras", 30)
BONS_MATINS = ejercicio("bons matins", 30)
TORSION_DU_TORSE = ejercicio("torsion du torse", 30)
ROULEMENTS_DU_COU = ejercicio("roulements du cou", 30)
CERCLES_DE_HANCHES = ejercicio("cercles de hanches", 30)
FLEXION_DYNAMIQUE_DES_JAMBES_VERS_AVANT = ejercicio("flexion dynamique des jambes vers l'avant", 30)
SCOOPS_POR_LES_IQUIO_JAMBIERS = ejercicio("scoops por les iquio-jambiers", 30)
OUVRE_PORTE = ejercicio("ouvre porte", 30)
CERCLE_DE_TORSE_A_JAMBES_LARGES = ejercicio("cercle de torse à jambes larges", 30)
CALIN_DE_GENOUX = ejercicio("câlin de genoux", 30)
CERCLES_AVEC_LES_GENOUX = ejercicio("cercles avec les genoux", 30)
POSTURE_DE_LA_CIGOGNE = ejercicio("posture de la cigogne", 45)
GENOUX_A_LA_POITRINE = ejercicio("genoux à la poitrine", 45)
BEBE_HEREUX = ejercicio("bébé hereux", 45)
PAPILLON_INCLINE = ejercicio("papillon incliné", 60)
TORSION_ALLONGEE_DROIT = ejercicio("torsion alongeé droit", 60)
TORSION_ALLONGEE_GAUCHE = ejercicio("torsion alongeé gauche", 60)
ESTIREMENT_DE_QUAD_DROIT = ejercicio("estirement des quad droit", 60)
ESTIREMENT_DE_QUAD_GAUCHE = ejercicio("estirement des quad gauche", 60)
JAMBES_CONTRE_LE_MUR = ejercicio("jambes contre le mur", 60)
JAMBES_GRAND_ANGLE_CONTRE_LE_MUR = ejercicio("jambes grand angle contre le mur", 60)

RUTINAS = {
    "mañana_tranquila": [
        MAINS_VERS_LE_CIEL,
        FLEXION_AVANT,
        FENTE_AVANT_DROIT,
        FENTE_AVANT_GAUCHE,
        POSTURE_DU_ENFANT,
        CHIEN_FACE_AU_CIEL,
        CHIEN_TETE_EN_BAS,
        POSTURE_DU_GRAND_ANGLE,
        MAINS_VERS_LE_CIEL
    ],

    "mañana_dinamica_4": [
        FLEXION_LATERALES_DYNAMIQUES,
        CERCLES_AVEC_LES_BRAS,
        BALANCEMENT_DE_BRAS,
        BONS_MATINS,
        TORSION_DU_TORSE,
        ROULEMENTS_DU_COU,
        CERCLES_DE_HANCHES,
        FLEXION_DYNAMIQUE_DES_JAMBES_VERS_AVANT
    ],
    "mañana_dinamica_7": [
        FLEXION_LATERALES_DYNAMIQUES,
        CERCLES_AVEC_LES_BRAS,
        BALANCEMENT_DE_BRAS,
        BONS_MATINS,
        TORSION_DU_TORSE,
        ROULEMENTS_DU_COU,
        CERCLES_DE_HANCHES,
        SCOOPS_POR_LES_IQUIO_JAMBIERS,
        OUVRE_PORTE,
        FLEXION_DYNAMIQUE_DES_JAMBES_VERS_AVANT,
        CERCLE_DE_TORSE_A_JAMBES_LARGES,
        CALIN_DE_GENOUX,
        CERCLES_AVEC_LES_GENOUX
    ],
    "noche": [
        POSTURE_DE_LA_CIGOGNE,
        CHIEN_FACE_AU_CIEL,
        POSTURE_DU_ENFANT,
        GENOUX_A_LA_POITRINE,
        BEBE_HEREUX,
        PAPILLON_INCLINE,
        TORSION_ALLONGEE_DROIT,
        TORSION_ALLONGEE_GAUCHE,
        ESTIREMENT_DE_QUAD_DROIT,
        ESTIREMENT_DE_QUAD_GAUCHE,
        JAMBES_CONTRE_LE_MUR,
        JAMBES_GRAND_ANGLE_CONTRE_LE_MUR,
    ]
}

class RutinaApp(App):

    def build(self):

        #sonido
        self.sonido = SoundLoader.load("la.mp3")

        #layout principal
        self.layout = BoxLayout(
            orientation="vertical",
            spacing=25,
            padding=40)

        #fondo
        with self.layout.canvas.before:
            Color(*amarillo)
            self.fondo = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self.actualizar_fondo, pos=self.actualizar_fondo)

        #texto central
        self.label = Label(
            text="elegí una rutina",
            font_size=30,
            color=azul,
            font_name="fonts/InriaSerif-Regular.ttf"
        )

        self.layout.add_widget(self.label)

        #botones
        for texto in ["mañana tranquila (5')", "mañana dinámica (4')", "mañana dinámica (7')", "noche", "salir"]:
            self.layout.add_widget(self.crear_boton(texto))

        return self.layout

    def actualizar_fondo(self, *args):
        self.fondo.size = self.layout.size
        self.fondo.pos = self.layout.pos

    def iniciar_rutina(self, nombre_rutina):
        self.rutina_actual = RUTINAS[nombre_rutina]
        self.indice_ejercicio = 0
        self.iniciar_ejercicio()

    def iniciar_ejercicio(self):
        if self.indice_ejercicio >= len(self.rutina_actual):
            self.label.text = "rutina terminada"
            return

        self.ejercicio_actual = self.rutina_actual[self.indice_ejercicio]
        self.nombre_actual = self.ejercicio_actual["nombre"]
        self.preparacion = self.ejercicio_actual["preparacion"]
        self.duracion = self.ejercicio_actual["duracion"]

        self.label.color = rojo
        self.tiempo = self.preparacion
        self.label.text = f"{self.nombre_actual}\n{self.tiempo}"

        Clock.schedule_interval(self.cuenta_preparacion, 1)


    def actualizar_label_preparacion(self):
        self.label.text = (
            f"{self.ejercicio_actual['nombre']}\n"
            f"{self.tiempo}"
        )
        self.label.color = rojo

    def cuenta_preparacion(self, dt):
        self.tiempo -= 1

        if self.sonido:
            self.sonido.play()

        if self.tiempo <= 0:
            Clock.unschedule(self.cuenta_preparacion)
            self.comenzar_ejercicio()
            return False
        
        self.label.text = f"{self.nombre_actual}\n{self.tiempo}"

    def comenzar_ejercicio(self):
        ejercicio = self.rutina_actual[self.indice_ejercicio]

        self.tiempo = ejercicio["duracion"]
        self.label.color = azul
        self.label.text = f"{self.nombre_actual}\n{self.tiempo}"

        Clock.schedule_interval(self.cuenta_ejercicio, 1)

     
    def actualizar_label_ejercicio(self):
        self.label.text = (
            f"{self.ejercicio_actual['nombre']}\n"
            f"{self.tiempo}"
        )
        self.label.color = azul

    def cuenta_ejercicio(self, dt):
        self.tiempo -= 1

        if self.tiempo <= 0:
            Clock.unschedule(self.cuenta_ejercicio)
            self.indice_ejercicio += 1
            self.iniciar_ejercicio()
            return False
        self.label.text = f"{self.nombre_actual}\n{self.tiempo}"


    def crear_boton(self, texto):
        boton = Button(
            text=texto,
            size_hint=(None, None),
            size=(276, 53),
            pos_hint={"center_x": 0.5, "center_y": 0.5}, #centrar el botón
            background_normal="",
            background_color=azul,
            color=amarillo, 
            font_name="fonts/InriaSerif-Regular.ttf",
            font_size=25
        )

        if texto == "mañana tranquila (5')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_tranquila"))

        if texto == "mañana dinámica (4')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_dinamica_4"))

        if texto == "mañana dinámica (7')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_dinamica_7"))

        if texto == "noche":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("noche"))

        if texto == "Salir":
            boton.bind(on_press=lambda x: App.get_running_app().stop())

        return boton


RutinaApp().run() 