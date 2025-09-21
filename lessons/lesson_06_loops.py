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
            "highlight": {"line": 1},
            "what": "Se crea una lista de documentos que representan las pruebas de un caso.",
            "why": "El objetivo es tener una colección de elementos sobre la cual podamos realizar una operación repetitiva. Los bucles necesitan algo que 'recorrer' o iterar.",
            "appData": "En el mundo de los datos, esta podría ser una lista de archivos a procesar, una lista de URLs a descargar o una columna de una tabla con miles de registros.",
            "appLaw": "Representa el conjunto de documentos o evidencias que un perito necesita analizar de forma sistemática. La tarea (verificar integridad) es la misma para cada uno."
        },
        {
            "highlight": {"line": 4},
            "what": "Se inicia un bucle 'for', que tomará cada elemento de la lista 'pruebas', uno por uno, y lo asignará a la variable 'prueba'.",
            "why": "El bucle 'for' es la herramienta perfecta para la automatización de tareas sobre un conjunto finito de elementos. Es determinista: se sabe de antemano cuántas veces se repetirá (una por cada elemento en la lista).",
            "appData": "Es el pan de cada día para cualquier analista: 'para cada fila en mi Excel, calcula el IVA', 'para cada cliente en mi base de datos, comprueba si está activo'.",
            "appLaw": "Automatiza un protocolo pericial. En lugar de verificar manualmente cada archivo, el bucle 'for' garantiza que el mismo procedimiento (ej. 'verificar integridad') se aplica de forma consistente y sin omisiones a todo el cuerpo de la prueba."
        },
        {
            "highlight": {"line": 8},
            "what": "Se inicializan las variables para un bucle 'while'. Este bucle continuará mientras queden intentos Y no se haya concedido el acceso.",
            "why": "A diferencia del 'for', el bucle 'while' se usa cuando no sabemos cuántas veces necesitamos repetir una acción. Se ejecuta 'mientras' una condición sea verdadera. Es ideal para simulaciones, esperas o procesos de prueba y error.",
            "appData": "Se usa para procesos que deben esperar un evento: 'mientras el servidor no responda, sigue intentando conectar', 'mientras la simulación no converja, sigue calculando'.",
            "appLaw": "Simula un escenario de insistencia o persistencia. Por ejemplo, un sistema intentando obtener una respuesta de un registro público online, o la propia 'minería' de Bitcoin, que es un gran bucle 'while' que se ejecuta 'mientras' no se encuentre la solución al puzzle."
        },
        {
            "highlight": {"line": 11},
            "what": "Dentro del bucle, se ejecuta la acción (imprimir el estado) y se actualiza una de las variables de control ('intentos_restantes').",
            "why": "Es absolutamente crítico que dentro de un bucle 'while' algo cambie para que, eventualmente, la condición se vuelva falsa. Si no, se crearía un 'bucle infinito', un programa que nunca termina. Aquí, al restar 1 a los intentos, nos aseguramos de que el bucle tendrá fin.",
            "appData": "Actualizar el estado es clave. En un modelo de machine learning, en cada iteración se ajustan ligeramente los parámetros del modelo para acercarse a la solución.",
            "appLaw": "Representa el progreso dentro de un proceso. Cada intento consume un recurso (un intento). La gestión correcta del estado dentro del bucle evita que un proceso automatizado se quede bloqueado indefinidamente, lo que podría tener consecuencias graves (ej. bloquear un sistema)."
        }
    ]
}
