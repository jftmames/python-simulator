lesson = {
    "title": "Lección 7: Funciones - Encapsulando un Protocolo Pericial Reutilizable",
    "description": "Aprende a crear 'funciones', que son como plantillas para realizar tareas. Esto permite empaquetar un procedimiento complejo (como 'generar un acta de evidencia') en un solo comando reutilizable y fiable.",
    "code": """import hashlib
import json

# Se define una función que encapsula el protocolo de creación de un acta
def generar_acta_de_evidencia(id_documento, contenido_bytes):
    # 1. Calcular el hash
    h = hashlib.sha256(contenido_bytes)
    huella = h.hexdigest()

    # 2. Construir el acta
    acta = {
        "documento": id_documento,
        "sha256": huella
    }
    # 3. Devolver el resultado
    return json.dumps(acta)

# Se utiliza la función para dos documentos diferentes
acta_contrato = generar_acta_de_evidencia("Contrato_v1.pdf", b"Contenido del contrato...")
acta_email = generar_acta_de_evidencia("Email_importante.eml", b"Cuerpo del email...")

print(acta_contrato)
print(acta_email)""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se define un bloque de código reutilizable llamado 'generar_acta_de_evidencia' usando la palabra clave 'def'. Esta 'función' acepta dos 'argumentos' o 'inputs': un identificador y el contenido del documento.",
            "why": "Las funciones son el pilar de la programación estructurada. Permiten agrupar un conjunto de pasos lógicos bajo un solo nombre. Esto reduce la duplicación de código, facilita el mantenimiento y hace el programa mucho más legible.",
            "appData": "Todo el análisis de datos se basa en funciones: una para limpiar los datos, otra para entrenar un modelo, otra para generar un gráfico. Cada una tiene una responsabilidad única.",
            "appLaw": "Una función es la encarnación de un protocolo o procedimiento. En lugar de describir los pasos para crear un acta cada vez, se invoca la función 'generar_acta_de_evidencia', garantizando que el procedimiento se sigue siempre de la misma manera, sin errores ni omisiones."
        },
        {
            "highlight": {"line": 6},
            "what": "Dentro de la función, se realizan las operaciones necesarias, como calcular el hash y construir el diccionario del acta.",
            "why": "La lógica interna de la función está 'encapsulada'. El usuario de la función no necesita saber los detalles de cómo funciona por dentro, solo qué 'inputs' necesita y qué 'output' producirá. Es el principio de abstracción.",
            "appData": "Cuando usas una función de una librería (ej. `modelo.fit()`), no necesitas saber el complejo algoritmo matemático que hay detrás, solo confías en que hará su trabajo.",
            "appLaw": "Un abogado no necesita entender los detalles criptográficos de SHA-256. Solo necesita saber que la función 'generar_acta_de_evidencia' implementa un procedimiento pericialmente válido. La función abstrae la complejidad técnica."
        },
        {
            "highlight": {"line": 14},
            "what": "La instrucción 'return' especifica cuál es el resultado o 'output' que la función devuelve al programa principal.",
            "why": "Una función no solo 'hace' cosas, sino que a menudo 'produce' un resultado que puede ser almacenado en una variable y utilizado más adelante. 'Return' es la forma de entregar ese resultado.",
            "appData": "Una función puede devolver un número, un texto, una tabla de datos completa o un modelo entrenado. El 'return' es lo que hace que las funciones sean piezas componibles en un flujo de trabajo más grande.",
            "appLaw": "El valor de retorno es el producto del protocolo. En este caso, el 'acta en formato JSON' es el entregable final del procedimiento pericial encapsulado en la función."
        },
        {
            "highlight": {"line": 17},
            "what": "Se 'llama' o 'invoca' a la función, pasándole los datos concretos de un contrato.",
            "why": "Aquí se demuestra el poder de la reutilización. La misma 'plantilla' (la función) se utiliza con diferentes datos ('inputs') para producir diferentes resultados ('outputs').",
            "appData": "Se llama a la misma función de visualización (`crear_grafico()`) repetidamente con diferentes conjuntos de datos para generar todos los gráficos de un informe.",
            "appLaw": "Se aplica el mismo protocolo pericial ('generar_acta_de_evidencia') a diferentes pruebas del caso (un contrato, un email). La función garantiza la consistencia del procedimiento, un requisito fundamental para la validez de la prueba pericial."
        }
    ]
}
