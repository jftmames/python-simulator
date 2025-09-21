lesson = {
    "title": "Lección 1: Sintaxis Básica y Variables",
    "description": "Entendiendo los cimientos: cómo Python almacena información y sigue instrucciones básicas, un concepto clave para la trazabilidad y la lógica contractual.",
    "code": """# Un perito asigna el número de caso a una variable
numero_de_caso = 101

# Se define el nombre del cliente
cliente = "Constructora S.A."

# Se verifica si el caso está activo (un booleano)
caso_activo = True

# Se crea un 'acta' simple usando un diccionario
acta_inicial = {
    "caso": numero_de_caso,
    "interviniente": cliente
}""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se asigna el valor '101' a una 'caja' etiquetada como 'numero_de_caso'.",
            "why": "Las variables son la forma fundamental de almacenar y referenciar datos. Sin ellas, no podríamos guardar información para usarla más tarde. Es como asignar un número de expediente a un caso para poder localizarlo.",
            "appData": "En análisis de datos, las variables guardan todo: desde tablas de datos importadas de un Excel hasta los resultados de un modelo estadístico.",
            "appLaw": "La correcta asignación de variables es la base de la trazabilidad. Una variable 'numero_de_caso' asegura que todas las operaciones posteriores se refieren inequívocamente a ese expediente, evitando ambigüedades."
        },
        {
            "highlight": {"line": 5},
            "what": "Se guarda el texto 'Constructora S.A.' en la variable 'cliente'.",
            "why": "Python distingue entre tipos de datos (números, texto, etc.). Esto evita errores, como intentar hacer operaciones matemáticas con un nombre. Es la diferencia entre un número de artículo del Código Penal y el texto del propio artículo.",
            "appData": "La limpieza y el tipado de datos es crucial. Asegurarse de que las fechas son fechas y el texto es texto es el primer paso en cualquier análisis.",
            "appLaw": "La tipificación es fundamental en Derecho. Un 'string' (texto) puede representar el nombre de una parte, mientras que un 'integer' (número) puede ser una cuantía. Confundirlos tendría consecuencias graves en un contrato inteligente."
        },
        {
            "highlight": {"line": 8},
            "what": "Se establece que la variable 'caso_activo' es 'Verdadero' (True).",
            "why": "Los booleanos (Verdadero/Falso) son la base de toda la lógica condicional. Permiten que un programa tome decisiones, como 'si el plazo ha vencido, entonces ejecuta el embargo'.",
            "appData": "Se usan constantemente para filtrar datos (ej. 'mostrar solo clientes activos') o para controlar el flujo de un algoritmo.",
            "appLaw": "Es la representación computacional de una condición jurídica. Una cláusula contractual puede estar 'activa' o 'inactiva' (True/False), y un programa puede actuar en consecuencia. Es la base de la automatización de contratos."
        },
        {
            "highlight": {"line": 11},
            "what": "Se crea una estructura de datos (diccionario) que agrupa información relacionada.",
            "why": "Los diccionarios permiten almacenar datos de forma estructurada con pares 'clave: valor'. Son increíblemente útiles para representar objetos del mundo real, como un expediente, un contrato o una persona.",
            "appData": "El formato JSON, el estándar de facto para el intercambio de datos en la web, es esencialmente una colección de diccionarios y listas.",
            "appLaw": "Un diccionario puede modelar perfectamente un asiento registral, un acta notarial o una ficha de evidencia, donde cada 'clave' (ej. 'sha256', 'custodio', 'timestamp') identifica un dato específico de forma inequívoca."
        }
    ]
}
