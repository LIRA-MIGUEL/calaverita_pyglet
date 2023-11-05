import pyglet

# Cargar una imagen
img = pyglet.image.load("logo3.jpg")

# Obtener las dimensiones de la imagen
ventana_ancho = img.width
ventana_alto = img.height

new_window = pyglet.window.Window(width=ventana_ancho, height=ventana_alto)

# Resto de tu código...

# Crea una etiqueta para el texto largo
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

text_label = pyglet.text.Label(
    texto_largo,
    font_name='Arial',
    font_size=12,
    x=new_window.width // 2,
    y=new_window.height // 2,
    anchor_x='center',  # Centra horizontalmente
    anchor_y='bottom',  # Centra verticalmente
    multiline=True,
    width=new_window.width - 20,
    color=(0, 0, 0, 255)
)


label = pyglet.text.Label(
    '',
    font_name='Arial',
    font_size=16,
    x=new_window.width // 2,
    y=new_window.height // 2,
    anchor_x='center',  # Centra horizontalmente
    anchor_y='bottom',  # Centra verticalmente
    color=(0, 0, 0, 255)
)


music = pyglet.resource.media('music.mp3')
music.play()

# Evento para cerrar la ventana
@new_window.event
def on_close():
    pyglet.app.exit()

@new_window.event
def on_draw():
    new_window.clear()
    img.blit(0, 0)  # Dibuja la imagen en la ventana
    text_label.draw()  # Dibuja el texto largo
    label.draw()

pyglet.app.run()
