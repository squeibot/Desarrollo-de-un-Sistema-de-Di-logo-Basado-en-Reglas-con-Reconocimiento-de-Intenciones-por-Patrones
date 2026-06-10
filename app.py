from flask import Flask, render_template, request, jsonify
import re
import random
import datetime

app = Flask(__name__)

# =============================================================================
# NORMALIZACION
# =============================================================================

def limpiar_texto(texto):
    texto = texto.lower().strip()
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ñ': 'n', 'ç': 'c',
        '¿': '', '¡': '', '?': '', '!': '', '.': '', ',': '',
        ':': '', ';': '', '"': '', "'": '', '(': '', ')': ''
    }
    for orig, dest in reemplazos.items():
        texto = texto.replace(orig, dest)
    return texto.strip()

# =============================================================================
# HORA Y FECHA
# =============================================================================

def obtener_hora():
    ahora = datetime.datetime.now()
    hora = ahora.hour
    if hora < 12:
        periodo = "de la manana"
    elif hora < 19:
        periodo = "de la tarde"
    else:
        periodo = "de la noche"
    return ahora.strftime("%I:%M " + periodo).lstrip("0")

def obtener_fecha():
    ahora = datetime.datetime.now()
    return ahora.strftime("%d/%m/%Y")

# =============================================================================
# MEMORIA
# =============================================================================

class MemoriaConversacion:
    def __init__(self):
        self.usuario = {
            "nombre": None,
            "edad": None,
            "ciudad": None,
            "ocupacion": None
        }
    
    def obtener_nombre(self):
        return self.usuario["nombre"] if self.usuario["nombre"] else "amigo"

# =============================================================================
# INTENCIONES
# =============================================================================

INTENCIONES = [
    {
        "nombre": "preguntar_nombre",
        "patrones": [r"como me llamo", r"cual es mi nombre"],
        "respuestas": ["Te llamas {nombre}.", "Tu nombre es {nombre}."]
    },
    {
        "nombre": "preguntar_edad",
        "patrones": [r"cuantos anos tengo", r"que edad tengo"],
        "respuestas": ["Tienes {edad} anos.", "Tu edad es {edad}."]
    },
    {
        "nombre": "preguntar_ciudad",
        "patrones": [r"donde vivo", r"de donde soy"],
        "respuestas": ["Vives en {ciudad}.", "{ciudad}, correcto?"]
    },
    {
        "nombre": "guardar_nombre",
        "patrones": [r"me llamo ([a-z]+)", r"mi nombre es ([a-z]+)", r"soy ([a-z]+)$"],
        "respuestas": ["Encantado de conocerte, {nombre}.", "Hola {nombre}!"]
    },
    {
        "nombre": "guardar_edad",
        "patrones": [r"tengo (\d+) anos", r"mi edad es (\d+)", r"(\d+) anos"],
        "respuestas": ["{edad} anos. Gracias.", "Ya se que tienes {edad} anos."]
    },
    {
        "nombre": "guardar_ciudad",
        "patrones": [r"vivo en ([a-z]+)", r"soy de ([a-z]+)"],
        "respuestas": ["{ciudad} es interesante.", "Ah vives en {ciudad}."]
    },
    {
        "nombre": "guardar_ocupacion",
        "patrones": [r"soy (estudiante|programador|ingeniero|abogado|medico|profesor)"],
        "respuestas": ["{ocupacion} es respetable.", "Ser {ocupacion} es interesante."]
    },
    {
        "nombre": "saludo",
        "patrones": [r"hola", r"buenas", r"que tal", r"como estas"],
        "respuestas": ["Hola! Como estas?", "Buenas! Me alegra verte."]
    },
    {
        "nombre": "despedida",
        "patrones": [r"adios", r"chao", r"bye", r"hasta luego"],
        "respuestas": ["Adios! Fue un gusto.", "Chao! Vuelve cuando quieras."]
    },
    {
        "nombre": "hora",
        "patrones": [r"que hora es", r"dime la hora"],
        "respuestas": ["Son las {hora}.", "En este momento son las {hora}."]
    },
    {
        "nombre": "fecha",
        "patrones": [r"que fecha es", r"que dia es hoy"],
        "respuestas": ["Hoy es {fecha}.", "Estamos a {fecha}."]
    },
    {
        "nombre": "recomendar_libro",
        "patrones": [r"recomienda un libro", r"recomiendame un libro"],
        "respuestas": ["Te recomiendo Cien anos de soledad.", "Lee 1984 de Orwell."]
    },
    {
        "nombre": "recomendar_pelicula",
        "patrones": [r"recomienda una pelicula", r"recomiendame una pelicula"],
        "respuestas": ["Mira El Padrino.", "Te recomiendo Interestelar."]
    },
    {
        "nombre": "chiste",
        "patrones": [r"chiste", r"cuentame un chiste"],
        "respuestas": ["Por que los programadores confunden Halloween con Navidad? Porque Oct 31 = Dec 25."]
    },
    {
        "nombre": "ayuda",
        "patrones": [r"ayuda", r"help", r"que puedes hacer"],
        "respuestas": ["Puedo: saludar, recordar nombre/edad/ciudad, decir hora, recomendar libros y contar chistes."]
    },
    {
        "nombre": "no_entiendo",
        "patrones": [r".*"],
        "respuestas": ["No entendi eso. Escribe ayuda.", "No tengo respuesta para eso."]
    }
]

# =============================================================================
# RECONOCER INTENCION
# =============================================================================

def reconocer_intencion(texto, memoria):
    for intencion in INTENCIONES:
        for patron in intencion["patrones"]:
            match = re.search(patron, texto, re.IGNORECASE)
            if match:
                grupos = match.groups()
                datos = {}
                if intencion["nombre"] == "guardar_nombre" and grupos:
                    datos["nombre"] = grupos[0].capitalize()
                elif intencion["nombre"] == "guardar_edad" and grupos:
                    datos["edad"] = grupos[0]
                elif intencion["nombre"] == "guardar_ciudad" and grupos:
                    datos["ciudad"] = grupos[0].capitalize()
                elif intencion["nombre"] == "guardar_ocupacion" and grupos:
                    datos["ocupacion"] = grupos[0].capitalize()
                return intencion, datos, match
    return None, None, None

def generar_respuesta(intencion, datos, memoria):
    if not intencion:
        intencion = INTENCIONES[-1]
    
    if datos:
        for clave, valor in datos.items():
            if clave in memoria.usuario:
                memoria.usuario[clave] = valor
    
    respuesta = random.choice(intencion["respuestas"])
    respuesta = respuesta.replace("{nombre}", memoria.obtener_nombre())
    
    if memoria.usuario["edad"]:
        respuesta = respuesta.replace("{edad}", str(memoria.usuario["edad"]))
    else:
        respuesta = respuesta.replace("{edad}", "?")
    
    if memoria.usuario["ciudad"]:
        respuesta = respuesta.replace("{ciudad}", memoria.usuario["ciudad"])
    else:
        respuesta = respuesta.replace("{ciudad}", "?")
    
    if memoria.usuario["ocupacion"]:
        respuesta = respuesta.replace("{ocupacion}", memoria.usuario["ocupacion"])
    else:
        respuesta = respuesta.replace("{ocupacion}", "?")
    
    respuesta = respuesta.replace("{hora}", obtener_hora())
    respuesta = respuesta.replace("{fecha}", obtener_fecha())
    
    return respuesta

# =============================================================================
# SESIONES
# =============================================================================

sesiones = {}

# =============================================================================
# RUTAS WEB
# =============================================================================

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    session_id = data.get('session_id', 'default')
    
    if session_id not in sesiones:
        sesiones[session_id] = MemoriaConversacion()
    
    memoria = sesiones[session_id]
    
    palabras_salida = {"salir", "adios", "chao", "bye", "exit"}
    if limpiar_texto(mensaje) in palabras_salida:
        nombre = memoria.obtener_nombre()
        respuesta = f"Hasta luego {nombre}. Fue un gusto."
        del sesiones[session_id]
        return jsonify({"respuesta": respuesta, "finalizar": True})
    
    texto_limpio = limpiar_texto(mensaje)
    intencion, datos, _ = reconocer_intencion(texto_limpio, memoria)
    respuesta = generar_respuesta(intencion, datos, memoria)
    
    return jsonify({"respuesta": respuesta, "finalizar": False})

# =============================================================================
# INICIAR
# =============================================================================

if __name__ == '__main__':
    print("=" * 50)
    print("  RegexBot Pro - Servidor Web")
    print("  Abre: http://localhost:5000")
    print("  Ctrl + C para cerrar")
    print("=" * 50)
    app.run(debug=True, host='localhost', port=5000)