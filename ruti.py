from kivy.config import Config
# filtros para que no se pixelee la imagen
Config.set('graphics', 'multisamples', '4')
Config.set('graphics', 'fullscreen', '0')    
Config.set('graphics', 'resizable', '1')     
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle
from kivy.metrics import sp
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.utils import platform

if platform == "android": #no sé si esto va acá o en build
    from android import AndroidActivity
    from jnius import autoclass

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity

    WindowManager = autoclass('android.view.WindowManager')
    activity.getWindow().addFlags(
        WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
    )


amarillo = (0.925, 0.882, 0.792, 1)   # ECE1CA , beige
azul = (0.192, 0.478, 0.831, 1)   # 317AD4 , azul
rojo = (0.831, 0.192, 0.192, 1)  # D43131 , rojo
tipografia = "fonts/InriaSerif-Regular.ttf"
medium_size = sp(25)
big_size = sp(35)

def ejercicio(nombre, duracion):
    return {
        "nombre": nombre,
        "preparacion": 3,
        "duracion": duracion,
        #"imagen": imagen
    }

MAINS_VERS_LE_CIEL = ejercicio("manos al cielo", 30,)
FLEXION_AVANT = ejercicio("flexión hacia adelante", 30)
FENTE_AVANT_DROIT = ejercicio("estocada frontal derecha", 30)
FENTE_AVANT_GAUCHE = ejercicio("estocada frontal izquierda", 30)
CHIEN_FACE_AU_CIEL = ejercicio("perro boca arriba", 30)
POSTURE_DU_ENFANT = ejercicio("postura del niño", 30)
CHIEN_TETE_EN_BAS = ejercicio("perro boca abajo", 30)
POSTURE_DU_GRAND_ANGLE = ejercicio("postura del gran ángulo", 30)
FLEXION_LATERALES_DYNAMIQUES = ejercicio("flexiones laterales dinámicas", 30)
CERCLES_AVEC_LES_BRAS = ejercicio("círculos con los brazos", 30)
BALANCEMENT_DE_BRAS = ejercicio("balanceo de brazos", 20)
TORSION_DU_TORSE = ejercicio("torsión del torso", 30)
ROULEMENTS_DU_COU = ejercicio("círculo con el cuello", 15)
CERCLES_DE_HANCHES = ejercicio("círculo con la cadera", 30)
FLEXION_DYNAMIQUE_DES_JAMBES_VERS_AVANT = ejercicio("flexión dinámica de las piernas", 45)
SCOOPS_POR_LES_IQUIO_JAMBIERS = ejercicio("estirar los isquiotibiales", 30,)
OUVRE_PORTE = ejercicio("apertura de puerta", 30,)
CERCLE_DE_TORSE_A_JAMBES_LARGES = ejercicio("cercle de torse à jambes larges", 30)
CALIN_DE_GENOUX = ejercicio("abrazo de rodillas", 30)
CERCLES_AVEC_LES_GENOUX = ejercicio("círculos con las rodillas", 30)
FLEXION_AVANT_NOCHE = ejercicio("flexión hacia adelante", 30)
GENOUX_A_LA_POITRINE = ejercicio("rodillas al pecho", 30)
BEBE_HEREUX = ejercicio("bébé hereux", 30)
PAPILLON_INCLINE = ejercicio("papillon incliné", 30)
TORSION_ALLONGEE_DROIT = ejercicio("torsion alongeé droit", 30)
TORSION_ALLONGEE_GAUCHE = ejercicio("torsion alongeé gauche", 30)
ESTIREMENT_DE_QUAD_DROIT = ejercicio("estirement des quad droit", 30)
ESTIREMENT_DE_QUAD_GAUCHE = ejercicio("estirement des quad gauche", 30)
JAMBES_CONTRE_LE_MUR = ejercicio("jambes contre le mur", 30)
JAMBES_GRAND_ANGLE_CONTRE_LE_MUR = ejercicio("jambes grand angle contre le mur",30)

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
        TORSION_DU_TORSE,
        ROULEMENTS_DU_COU,
        CERCLES_DE_HANCHES,
        FLEXION_DYNAMIQUE_DES_JAMBES_VERS_AVANT
    ],
    "mañana_dinamica_7": [
        FLEXION_LATERALES_DYNAMIQUES,
        CERCLES_AVEC_LES_BRAS,
        BALANCEMENT_DE_BRAS,
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
            font_size=big_size,
            color=azul,
            font_name=tipografia)

        #imagen
        #self.imagen = Image(
        #    size_hint=(1, 0.8), #40% del ancho
        #    allow_stretch=True, 
        #    keep_ratio=True, #no deforma el dibujo
        #    mipmap=True,
        #    pos_hint={"center_x": 0.5},
        #    opacity=0 #no visible al inicio
        #)

        self.layout.add_widget(self.label)

        #self.layout.add_widget(self.imagen, index=0) #index=1 es abajo del texto y arriba de los botones

        # botones de menú
        self.botones_menu = []

        for texto in [
            "mañana tranquila (5')",
            "mañana dinámica (4')",
            "mañana dinámica (7')",
            "noche",
        ]:
            boton = self.crear_boton(texto)
            self.botones_menu.append(boton)
            self.layout.add_widget(boton)

        self.boton_volver = Button(
            text="volver",
            size_hint=(None, None),
            size=(dp(280), dp(64)),
            pos_hint={"center_x": 0.5},
            background_normal="",
            background_color=azul,
            color=amarillo,
            font_name=tipografia,
            font_size=medium_size
        )

        self.boton_pausa = Button(
            text="pausar",
            size_hint=(None, None),
            size=(dp(280), dp(64)),
            pos_hint={"center_x": 0.5},
            background_normal="",
            background_color=azul,
            color=amarillo,
            font_name=tipografia,
            font_size=medium_size
        )

        self.boton_pausa.bind(on_press=self.toggle_pausa)
        self.pausado = False
        self.boton_volver.bind(on_press=self.volver_al_menu)
        return self.layout

    def ocultar_menu(self):
        for boton in self.botones_menu:
            if boton.parent:
                self.layout.remove_widget(boton)

    def mostrar_menu(self):
        for boton in self.botones_menu:
            if not boton.parent:
                self.layout.add_widget(boton)

        if self.boton_volver.parent:
            self.layout.remove_widget(self.boton_volver)

        self.label.text = "elegí una rutina"
        self.label.color = azul

    def actualizar_fondo(self, *args):
        self.fondo.size = self.layout.size
        self.fondo.pos = self.layout.pos

    def iniciar_rutina(self, nombre_rutina):
        self.ocultar_menu()

        if not self.boton_volver.parent:
            self.layout.add_widget(self.boton_volver)
        if not self.boton_pausa.parent:
            self.layout.add_widget(self.boton_pausa)
        
        self.boton_pausa.text = "pausar"
        self.pausado = False   
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

        #self.imagen.source = self.ejercicio_actual["imagen"]
        #self.imagen.opacity = 1  #hacer visible la imagen
        #self.imagen.reload()

        self.estado_timer = "preparacion"
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

        self.estado_timer = "ejercicio"
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
            size_hint=(0.8, None),
            height=dp(64),
            pos_hint={"center_x": 0.5},
            background_normal="",
            background_color=azul,
            color=amarillo,
            font_name=tipografia,
            font_size=medium_size
        )

        if texto == "mañana tranquila (5')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_tranquila"))

        if texto == "mañana dinámica (4')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_dinamica_4"))

        if texto == "mañana dinámica (7')":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("mañana_dinamica_7"))

        if texto == "noche":
            boton.bind(on_press=lambda instance: self.iniciar_rutina("noche"))


        return boton

    def volver_al_menu(self, instance):
        Clock.unschedule(self.cuenta_preparacion)
        Clock.unschedule(self.cuenta_ejercicio)
        self.pausado = False

        if self.boton_pausa.parent:
            self.layout.remove_widget(self.boton_pausa)

        self.mostrar_menu()

    def toggle_pausa(self, instance):
        if not self.pausado:
            # pausar
            if self.estado_timer == "preparacion":
                Clock.unschedule(self.cuenta_preparacion)
            elif self.estado_timer == "ejercicio":
                Clock.unschedule(self.cuenta_ejercicio)

            self.boton_pausa.text = "reanudar"
            self.pausado = True

        else:
            # reanudar
            if self.estado_timer == "preparacion":
                Clock.schedule_interval(self.cuenta_preparacion, 1)
            elif self.estado_timer == "ejercicio":
                Clock.schedule_interval(self.cuenta_ejercicio, 1)

            self.boton_pausa.text = "pausar"
            self.pausado = False

RutinaApp().run() 