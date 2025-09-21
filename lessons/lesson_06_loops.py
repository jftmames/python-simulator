lesson = {
    "title": "Lección 6: Bucles - Procesando Expedientes en Masa y la Búsqueda Persistente",
    "description": "Descubre cómo los 'bucles' permiten repetir una acción sobre una colección de elementos (como revisar cada prueba de un listado) o insistir en una tarea hasta que se cumpla una condición (como en la 'minería' de criptomonedas).",
    "code": """pruebas = ["Contrato.pdf", "Email_confirmacion.eml", "Acta_notarial.docx"]

# Bucle 'for': para recorrer cada elemento de una lista conocida
for prueba in pruebas:
    print(f"Verificando integridad de: {prueba}")

# Bucle 'while': para repetir hasta que se cumpla una condición
intentos_restantes = 3
acceso_concedido = False
while intentos_restantes > 0 and not acceso_concedido:
    print(f"Intentando acceder al sistema cifrado... Quedan {intentos_restantes} intentos.")
    # Aquí iría la lógica de intento de acceso
    intentos_restantes -= 1
    # if exito: acceso_concedido = True""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se inicia un bucle 'for', que tomará cada elemento de la lista 'pruebas', uno por uno, y lo asignará a la variable 'prueba'.",
            "why": "El bucle 'for' es la herramienta perfecta para la automatización de tareas sobre un conjunto finito de elementos. Es determinista: se sabe de antemano cuántas veces se repetirá (una por cada elemento en la lista).",
            "appData": "Es el pan de cada día para cualquier analista: 'para cada fila en mi Excel, calcula el IVA', 'para cada cliente en mi base de datos, comprueba si está activo'.",
            "appLaw": "Automatiza un protocolo pericial. En lugar de verificar manualmente cada archivo, el bucle 'for' garantiza que el mismo procedimiento (ej. 'verificar integridad') se aplica de forma consistente y sin omisiones a todo el cuerpo de la prueba.",
            "state": {"globals": {"pruebas": ["Contrato.pdf", "Email_confirmacion.eml", "Acta_notarial.docx"]}, "io": {"out": ["Verificando integridad de: Contrato.pdf", "Verificando integridad de: Email_confirmacion.eml", "Verificando integridad de: Acta_notarial.docx"]}}
        },
        {
            "highlight": {"line": 8},
            "what": "Se inicializan las variables para un bucle 'while'. Este bucle continuará mientras queden intentos Y no se haya concedido el acceso.",
            "why": "A diferencia del 'for', el bucle 'while' se usa cuando no sabemos cuántas veces necesitamos repetir una acción. Se ejecuta 'mientras' una condición sea verdadera. Es ideal para simulaciones, esperas o procesos de prueba y error.",
            "appData": "Se usa para procesos que deben esperar un evento: 'mientras el servidor no responda, sigue intentando conectar', 'mientras la simulación no converja, sigue calculando'.",
            "appLaw": "Simula un escenario de insistencia o persistencia. Por ejemplo, un sistema intentando obtener una respuesta de un registro público online, o la propia 'minería' de Bitcoin, que es un gran bucle 'while' que se ejecuta 'mientras' no se encuentre la solución al puzzle.",
            "state": {"globals": {"intentos_restantes": 3, "acceso_concedido": False}}
        },
        {
            "highlight": {"line": 10},
            "what": "Dentro del bucle, se ejecuta la acción (imprimir el estado) y se actualiza la variable de control 'intentos_restantes'. (Iteración 1)",
            "why": "Es absolutamente crítico que dentro de un bucle 'while' algo cambie para que, eventualmente, la condición se vuelva falsa. Si no, se crearía un 'bucle infinito', un programa que nunca termina. Aquí, al restar 1 a los intentos, nos aseguramos de que el bucle tendrá fin.",
            "appData": "Actualizar el estado es clave. En un modelo de machine learning, en cada iteración se ajustan ligeramente los parámetros del modelo para acercarse a la solución.",
            "appLaw": "Representa el progreso dentro de un proceso. Cada intento consume un recurso (un intento). La gestión correcta del estado dentro del bucle evita que un proceso automatizado se quede bloqueado indefinidamente, lo que podría tener consecuencias graves (ej. bloquear un sistema).",
            "state": {"globals": {"intentos_restantes": 2, "acceso_concedido": False}, "io": {"out": ["Intentando acceder al sistema cifrado... Quedan 3 intentos."]}},
        },
        {
            "highlight": {"line": 10},
            "what": "El bucle se repite. Se ejecuta la acción e 'intentos_restantes' se reduce a 1. (Iteración 2)",
            "why": "La condición `intentos_restantes > 0` sigue siendo verdadera, por lo que el bucle continúa ejecutándose.",
            "appData": "Los bucles son la base de la iteración, un concepto fundamental para procesar colecciones de datos o ejecutar simulaciones.",
            "appLaw": "Demuestra la naturaleza persistente de ciertos procesos automatizados, que continúan intentando una acción hasta que se agotan los recursos (intentos) o se alcanza el objetivo.",
            "state": {"globals": {"intentos_restantes": 1, "acceso_concedido": False}, "io": {"out": ["Intentando acceder al sistema cifrado... Quedan 3 intentos.", "Intentando acceder al sistema cifrado... Quedan 2 intentos."]}},
        },
        {
            "highlight": {"line": 10},
            "what": "Última iteración. 'intentos_restantes' se reduce a 0. (Iteración 3)",
            "why": "En la siguiente comprobación, la condición `intentos_restantes > 0` será falsa, y el bucle terminará.",
            "appData": "Ilustra el final de un bucle 'while' cuando la condición de continuación deja de cumplirse.",
            "appLaw": "Representa el agotamiento de los intentos procesales o las oportunidades para realizar una acción, tras lo cual el proceso continúa por un camino diferente.",
            "state": {"globals": {"intentos_restantes": 0, "acceso_concedido": False}, "io": {"out": ["Intentando acceder al sistema cifrado... Quedan 3 intentos.", "Intentando acceder al sistema cifrado... Quedan 2 intentos.", "Intentando acceder al sistema cifrado... Quedan 1 intentos."]}},
        }
    ]
}
