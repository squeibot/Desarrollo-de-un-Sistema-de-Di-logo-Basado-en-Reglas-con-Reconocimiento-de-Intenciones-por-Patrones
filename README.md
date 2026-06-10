## DESCRIPCIÓN DEL PROYECTO

Este proyecto es un sistema de diálogo que permite a un usuario conversar con un programa por medio de texto. El programa lee lo que el usuario escribe y responde automáticamente. No utiliza machine learning ni redes neuronales. Funciona con reglas escritas a mano por el programador.

El usuario escribe un mensaje. El programa limpia el texto: lo convierte a minúsculas, le quita acentos y elimina signos de puntuación. Luego compara el texto con una lista de patrones predefinidos. Si encuentra una coincidencia, responde con un mensaje que también estaba predefinido. Si no encuentra ninguna coincidencia, responde pidiendo al usuario que reformule su pregunta.

El bot puede saludar, despedirse, guardar el nombre del usuario, guardar su edad, guardar su ciudad, guardar su profesión, responder preguntas sobre los datos que guardó, decir la hora actual, decir la fecha actual, recomendar libros, recomendar películas y contar chistes. Todo esto ocurre en menos de 0.1 segundos.

---

## CONCEPTOS QUE USA EL PROYECTO

Aunque el proyecto es simple, aplica varios conceptos fundamentales que se estudian en sistemas conversacionales.

El primer concepto es el reconocimiento de intenciones. Cada mensaje del usuario tiene una intención, que es lo que el usuario quiere lograr. Por ejemplo, si el usuario escribe "hola", su intención es saludar. Si escribe "me llamo Juan", su intención es presentarse. El programa clasifica cada mensaje en una categoría de intención usando los patrones que el programador escribió.

El segundo concepto es la extracción de entidades. Las entidades son los datos importantes dentro de un mensaje. Por ejemplo, en "me llamo Juan", la entidad es "Juan" (el nombre). En "tengo 20 años", la entidad es "20" (la edad). En "vivo en Madrid", la entidad es "Madrid" (la ciudad). El programa extrae estas entidades usando grupos de captura en las expresiones regulares y las guarda en la memoria.

El tercer concepto es el sistema basado en reglas. Es un enfoque clásico donde se escriben reglas del tipo "si ocurre esto, entonces haz aquello". El programa tiene una lista de reglas. Cada regla tiene un patrón y una respuesta. Si el patrón coincide con el mensaje del usuario, se activa la respuesta. Es un sistema determinista: las mismas entradas siempre producen las mismas salidas.

El cuarto concepto es la memoria conversacional o contexto. El programa necesita recordar información de turnos anteriores para usarla después. Por ejemplo, si el usuario dice "me llamo Juan", el programa debe recordar que el usuario se llama Juan para poder responder "Te llamas Juan" más tarde. El programa guarda el nombre, la edad, la ciudad y la ocupación en una clase de memoria y los mantiene durante toda la conversación.

El quinto concepto es el ciclo percepción-acción. El programa percibe su entorno a través del texto que escribe el usuario. Luego procesa ese texto para entender la intención y extraer entidades. Finalmente actúa generando una respuesta. Es el mismo ciclo que siguen los agentes conversacionales: percibir, procesar, actuar.

El sexto concepto es el procesamiento de lenguaje natural básico. El programa hace tareas simples de procesamiento de texto: normalización (convertir a minúsculas, quitar acentos, eliminar signos), tokenización implícita (separar palabras) y reconocimiento de patrones. Son los primeros pasos para que una máquina entienda lenguaje humano.

El séptimo concepto es la respuesta por defecto o fallback. Cuando el programa no entiende lo que el usuario escribió, tiene una respuesta predeterminada. En este caso, responde "No entendí eso. Escribe ayuda para ver mis comandos". Esto evita que el programa se quede sin responder y le da una pista al usuario sobre cómo continuar.

---

## QUÉ PUEDE HACER EL BOT

Cuando el usuario escribe "hola", el bot responde "Hola como estas".

Cuando el usuario escribe "me llamo Camilo", el bot responde "Encantado de conocerte Camilo" y guarda el nombre.

Cuando el usuario escribe "tengo 20 años", el bot responde "20 años gracias" y guarda la edad.

Cuando el usuario escribe "vivo en Sincelejo", el bot responde "Sincelejo es interesante" y guarda la ciudad.

Cuando el usuario escribe "soy ingeniero", el bot responde "Ingeniero es respetable" y guarda la profesión.

Cuando el usuario escribe "como me llamo", el bot responde "Te llamas Camilo" usando el nombre que guardó antes.

Cuando el usuario escribe "cuantos años tengo", el bot responde "Tienes 20 años" usando la edad que guardó antes.

Cuando el usuario escribe "donde vivo", el bot responde "Vives en Sincelejo" usando la ciudad que guardó antes.

Cuando el usuario escribe "que hora es", el bot responde con la hora actual del sistema.

Cuando el usuario escribe "recomiendame un libro", el bot recomienda un libro de una lista que tiene guardada.

Cuando el usuario escribe "chiste", el bot cuenta un chiste de una lista que tiene guardada.

Cuando el usuario escribe "ayuda", el bot muestra la lista de comandos disponibles.

Cuando el usuario escribe "adios", el bot se despide y la conversación termina.

---

## REQUISITOS PARA QUE FUNCIONE

Para ejecutar este proyecto necesitas tener Python 3.8 o superior instalado en tu computadora. También necesitas Flask, que es una biblioteca de Python para crear la interfaz web. Necesitas Visual Studio Code o cualquier editor de texto. Cualquier computadora moderna funciona, no se necesita hardware especial.

---

## ESTRUCTURA DE ARCHIVOS

Tu carpeta del proyecto debe tener esta estructura. Una carpeta llamada PROYECTO BOOTCAMP. Dentro de ella, un archivo llamado app.py. Dentro de ella también, una carpeta llamada templates (todo en minúsculas). Dentro de la carpeta templates, un archivo llamado chat.html. La carpeta templates es obligatoria porque Flask la necesita para encontrar la interfaz web.

---

## INSTALACIÓN PASO A PASO

Primero, instala Python. Ve a python.org y descarga la versión más reciente. Durante la instalación, marca la opción "Add Python to PATH". Esto es muy importante. Si no lo marcas, después no funcionará.

Segundo, verifica que Python se instaló bien. Abre la terminal de Windows o la terminal de VS Code. Escribe python --version. Debe mostrar la versión de Python.

Tercero, instala Flask. En la misma terminal, escribe pip install flask. Espera a que termine la instalación. Verás un mensaje que dice "Successfully installed flask".

Cuarto, verifica que Flask se instaló. Escribe pip show flask. Debe mostrar información del paquete.

---

## EJECUCIÓN PASO A PASO

Primero, abre Visual Studio Code. Luego abre la carpeta del proyecto: Archivo, Abrir carpeta, selecciona PROYECTO BOOTCAMP.

Segundo, abre la terminal en VS Code. Puedes ir al menú Terminal y hacer clic en Nueva terminal. También puedes usar el atajo Ctrl + ` (la tecla de la tilde, al lado del número uno).

Tercero, en la terminal escribe python app.py y presiona Enter. Verás un mensaje que dice "Running on http://localhost:5000". Eso significa que el servidor inició correctamente. No cierres esta terminal. El servidor debe quedarse abierto.

Cuarto, abre tu navegador web. Puede ser Chrome, Edge o Firefox. En la barra de direcciones, escribe http://localhost:5000 y presiona Enter.

Quinto, verás la interfaz del chat. Escribe un mensaje y presiona Enter o haz clic en el botón Enviar. El bot te responderá.

---

## CÓMO DETENER EL SERVIDOR

Cuando termines de usar el chat, ve a la terminal de VS Code. Presiona las teclas Ctrl y C al mismo tiempo. El servidor se detendrá. Puedes cerrar VS Code.

---

## SOLUCIÓN DE PROBLEMAS

Si la terminal dice que python no se reconoce, significa que Python no está instalado correctamente o no marcaste la opción "Add Python to PATH". Reinstala Python y marca esa opción.

Si la terminal dice "No module named flask", significa que Flask no está instalado. Ejecuta pip install flask.

Si la página del navegador no carga, verifica que la URL sea http://localhost:5000. No uses https, solo http.

Si dentro del chat aparece "Error de conexión", significa que el servidor no está corriendo. Verifica que la terminal sigue abierta y que el mensaje "Running on http://localhost:5000" apareció.

Si el bot responde "No entendi eso", significa que escribiste algo que no está en sus reglas. Escribe exactamente los comandos que están en la lista. Usa minúsculas y no uses acentos.

Si el puerto 5000 está ocupado por otro programa, puedes cambiar el puerto. Abre app.py, busca donde dice port=5000 y cámbialo a port=5001. Luego abre el navegador en http://localhost:5001.

---

## QUÉ HACE CADA ARCHIVO

app.py es el servidor. Contiene las reglas de reconocimiento, las respuestas del bot, la memoria para guardar nombre y edad, y el código que recibe los mensajes desde la web.

chat.html es la interfaz. Es la ventana que el usuario ve. Contiene el diseño del chat, los colores, las burbujas de mensajes y el código JavaScript que envía los mensajes al servidor.

templates es la carpeta que Flask necesita para encontrar chat.html. Si esta carpeta no existe o se llama diferente, el proyecto no funciona.

conversaciones_log.json se crea automáticamente. Guarda todo el historial de la conversación. Puedes abrirlo con cualquier editor de texto.

---

## CONCLUSIÓN

Este proyecto es un sistema de diálogo funcional que aplica conceptos básicos de sistemas conversacionales como reconocimiento de intenciones, extracción de entidades, memoria de contexto y respuesta por defecto. Es rápido, predecible y fácil de modificar. Demuestra que se puede construir un asistente conversacional sin necesidad de machine learning, usando solo reglas y expresiones regulares.
