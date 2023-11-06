# Importar la biblioteca Pyglet
import pyglet

# Cargar una imagen llamada "logo3.jpg"
img = pyglet.image.load("logo4.jpg")

# Obtener las dimensiones de la imagen
ventana_ancho = img.width
ventana_alto = img.height

# Crear una nueva ventana con las dimensiones de la imagen
new_window = pyglet.window.Window(width=ventana_ancho, height=ventana_alto)

# Crear una etiqueta de texto largo
texto_largo = """
Todo ya comienza en un solo día 
festivo del día de muertos hablamos 
o del Halloween para los amigos 
este día enaltecemos las tradiciones
no hay clases que dicha menos para los 
Programadores. Es un día de fiesta ya 
que recordamos a los que ya no están,
pero los únicos que no celebran 
son los programadores esos tienen que 
chambear. Los alumnos trabajando y 
trabajando se la pasan, los maestros 
No los dejan descansar. Trabajen,
trabajen están, ya que el Hackathon está por 
empezar apúrenle muchachos si no
quieren reprobar hay dios mío el hackathon
ya está llegando, y la catrina 
está esperando, ya no hay salvación, 
después del hackathon nos vamos al panteón.
"""

# Crear una etiqueta de texto largo para mostrar en la ventana
text_label = pyglet.text.Label(
    texto_largo,
    font_name='Arial',
    font_size=12,
    x=new_window.width // 2,
    y=new_window.height // 2,
    anchor_x='center',  # Centra horizontalmente
    anchor_y='center',  # Centra verticalmente
    multiline=True,  # Permite texto en varias líneas
    width=new_window.width - 20,  # Ancho del área de texto
    color=(0, 0, 255, 255)  # Color del texto (negro)
)

# Crear una etiqueta de texto vacía para mostrar en la ventana
label = pyglet.text.Label(
    '',
    font_name='Arial',
    font_size=16,
    x=new_window.width // 2,
    y=new_window.height // 2,
    anchor_x='center',  # Centra horizontalmente
    anchor_y='center',  # Centra verticalmente
    color=(0, 0, 255, 255)  # Color del texto (negro)
)

# Cargar y reproducir un archivo de música llamado "music.mp3"
music = pyglet.resource.media('music.mp3')
music.play()

# Definir un evento para cerrar la ventana
@new_window.event
def on_close():
    pyglet.app.exit()

# Definir un evento de dibujo en la ventana
@new_window.event
def on_draw():
    new_window.clear()  # Borra el contenido anterior de la ventana
    img.blit(0, 0)  # Dibuja la imagen en la ventana en la posición (0, 0)
    text_label.draw()  # Dibuja el texto largo
    label.draw()  # Dibuja la etiqueta de texto vacía

# Iniciar la aplicación Pyglet y mantener la ventana abierta
pyglet.app.run()
