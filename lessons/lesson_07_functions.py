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
            "appLaw": "Una función es la encarnación de un protocolo o procedimiento. En lugar de describir los pasos para crear un acta cada vez, se invoca la función 'generar_acta_de_evidencia', garantizando que el procedimiento se sigue siempre de la misma manera, sin errores ni omisiones.",
            "state": {"globals": {"generar_acta_de_evidencia": "<function>"}}
        },
        {
            "highlight": {"line": 17},
            "what": "Se 'llama' o 'invoca' a la función, pasándole los datos concretos de un contrato. La función ejecuta su código interno y devuelve el resultado, que se guarda en 'acta_contrato'.",
            "why": "Aquí se demuestra el poder de la reutilización. La misma 'plantilla' (la función) se utiliza con diferentes datos ('inputs') para producir diferentes resultados ('outputs').",
            "appData": "Se llama a la misma función de visualización (`crear_grafico()`) repetidamente con diferentes conjuntos de datos para generar todos los gráficos de un informe.",
            "appLaw": "Se aplica el mismo protocolo pericial ('generar_acta_de_evidencia') a diferentes pruebas del caso (un contrato, un email). La función garantiza la consistencia del procedimiento, un requisito fundamental para la validez de la prueba pericial.",
            "state": {"globals": {"acta_contrato": '{"documento": "Contrato_v1.pdf", "sha256": "..."}'}}
        },
        {
            "highlight": {"line": 18},
            "what": "Se vuelve a llamar a la misma función, pero esta vez con los datos de un correo electrónico.",
            "why": "Demuestra que una función bien diseñada es agnóstica a los datos específicos que procesa, siempre que cumplan el formato esperado. Esto la hace robusta y versátil.",
            "appData": "Una función `limpiar_texto()` puede aplicarse a cualquier texto, ya sea un tuit, la descripción de un producto o el capítulo de un libro.",
            "appLaw": "El mismo procedimiento legal se puede aplicar a diferentes 'hechos'. La función representa el 'procedimiento', y los argumentos que se le pasan son los 'hechos' del caso concreto.",
            "state": {"globals": {"acta_contrato": '{"documento": "Contrato_v1.pdf", "sha256": "..."}', "acta_email": '{"documento": "Email_importante.eml", "sha256": "..."}'}}
        },
        {
            "highlight": {"line": 20},
            "what": "Se imprimen los resultados generados por las llamadas a la función.",
            "why": "El programa principal recoge los 'outputs' de las funciones y puede continuar trabajando con ellos, en este caso, mostrándolos en pantalla.",
            "appData": "Los resultados de una función de análisis a menudo se convierten en el 'input' de la siguiente función en un pipeline de datos.",
            "appLaw": "Las actas generadas (los resultados de la función) ahora son 'evidencias' que pueden ser presentadas, almacenadas o enviadas, completando el flujo de trabajo pericial.",
            "state": {"io": {"out": ['{"documento": "Contrato_v1.pdf", "sha256": "..."}', '{"documento": "Email_importante.eml", "sha256": "..."}']}}
        }
    ]
}
