lesson = {
    "title": "Lección 14: Lambdas - Creando 'Mini-Funciones' al Vuelo para Ordenar y Filtrar",
    "description": "Descubre las funciones 'lambda', que son pequeñas funciones anónimas de una sola línea, y cómo se usan con funciones de 'orden superior' como `sorted` para personalizar operaciones complejas.",
    "code": """# Una lista de diccionarios representando transacciones
transacciones = [
    {"id": "A", "cuantia": 500.0, "fecha": "2025-09-23"},
    {"id": "B", "cuantia": 150.0, "fecha": "2025-09-22"},
    {"id": "C", "cuantia": 800.0, "fecha": "2025-09-24"},
]

# Se ordena la lista usando una función 'lambda' como clave
# La 'lambda' le dice a 'sorted' que debe fijarse en el valor de la 'cuantia'
transacciones_ordenadas = sorted(
    transacciones,
    key=lambda tx: tx["cuantia"],
    reverse=True
)

print(transacciones_ordenadas)""",
    "steps": [
        {
            "highlight": {"line": 9},
            "what": "Se utiliza la función 'sorted', que es una función de 'orden superior' porque puede aceptar otra función como argumento (el parámetro 'key').",
            "why": "Las funciones de orden superior son una característica de lenguajes de programación avanzados. Permiten un alto grado de personalización. En lugar de tener una única forma de ordenar, `sorted` nos permite decirle EXACTAMENTE cuál es el criterio de ordenación.",
            "appData": "Funciones como `sorted`, `map`, `filter` son fundamentales en el paradigma de la programación funcional, muy utilizado en el procesamiento de grandes volúmenes de datos.",
            "appLaw": "Representa la capacidad de aplicar un criterio jurídico específico a un conjunto de hechos. La ley puede establecer un criterio general de prelación de créditos, pero un juez puede aplicar un criterio específico ('key') basado en las circunstancias del caso.",
            "state": {"globals": {"transacciones": [{"id": "A", "cuantia": 500.0, "fecha": "2025-09-23"}, {"id": "B", "cuantia": 150.0, "fecha": "2025-09-22"}, {"id": "C", "cuantia": 800.0, "fecha": "2025-09-24"}]}}
        },
        {
            "highlight": {"line": 10},
            "what": "Se define una función 'lambda'. `lambda tx: tx['cuantia']` es una mini-función que, para una transacción `tx` dada, devuelve el valor de su `cuantia`.",
            "why": "Las lambdas son una forma de crear funciones pequeñas y de un solo uso sin la necesidad de definirlas formalmente con `def`. Son perfectas para usarlas como 'ayudantes' o 'criterios' para otras funciones como `sorted`.",
            "appData": "Se usan constantemente en la librería 'pandas' para realizar operaciones sobre columnas. Por ejemplo, `df.apply(lambda x: x * 1.21)` para aplicar el IVA a toda una columna de precios.",
            "appLaw": "Una lambda es la expresión de un criterio simple y directo. Es como decirle a un asistente: 'Para ordenar estos expedientes, no mires el número, no mires el nombre, solo mírame la cuantía'. Esa instrucción ('solo mírame la cuantía') es la función lambda.",
            "state": {"globals": {"transacciones": "[...]", "transacciones_ordenadas": "[...]" }, "io": {"log": ["sorted() está usando la lambda para mirar la 'cuantia' de cada elemento."]}}
        },
        {
            "highlight": {"line": 15},
            "what": "La ejecución de `sorted` crea una nueva lista ordenada de mayor a menor cuantía.",
            "why": "La función `sorted` no modifica la lista original, sino que devuelve una copia ordenada. Esto es un principio de seguridad para evitar la modificación accidental de los datos originales.",
            "appData": "Este es un paso fundamental en cualquier análisis exploratorio de datos: ordenar los datos según diferentes variables para identificar patrones, valores atípicos o tendencias.",
            "appLaw": "La salida de esta operación podría ser un anexo para un informe concursal, mostrando los créditos ordenados por su cuantía para determinar el orden de pago. La fiabilidad del orden está garantizada por la lógica del código.",
            "state": {
                "globals": {
                    "transacciones": [{"id": "A", "cuantia": 500.0, "fecha": "2025-09-23"}, {"id": "B", "cuantia": 150.0, "fecha": "2025-09-22"}, {"id": "C", "cuantia": 800.0, "fecha": "2025-09-24"}],
                    "transacciones_ordenadas": [{"id": "C", "cuantia": 800.0, "fecha": "2025-09-24"}, {"id": "A", "cuantia": 500.0, "fecha": "2025-09-23"}, {"id": "B", "cuantia": 150.0, "fecha": "2025-09-22"}]
                },
                "io": {"out": ["[{'id': 'C', 'cuantia': 800.0, ...}, {'id': 'A', 'cuantia': 500.0, ...}, {'id': 'B', 'cuantia': 150.0, ...}]"]}
            }
        }
    ]
}
