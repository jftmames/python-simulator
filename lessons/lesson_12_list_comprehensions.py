lesson = {
    "title": "Lección 12: List Comprehensions - Filtrando Evidencias de Forma Rápida y Elegante",
    "description": "Aprende una de las características más potentes y 'Pythónicas' de Python: una sintaxis compacta para crear una nueva lista a partir de otra, aplicando una condición y una transformación.",
    "code": """# Un listado de expedientes con su estado
expedientes = [
    {"id": "EXP-01", "materia": "civil", "estado": "archivado"},
    {"id": "EXP-02", "materia": "penal", "estado": "en trámite"},
    {"id": "EXP-03", "materia": "civil", "estado": "en trámite"},
    {"id": "EXP-04", "materia": "mercantil", "estado": "archivado"},
]

# Forma tradicional con un bucle 'for'
expedientes_civiles_activos_v1 = []
for exp in expedientes:
    if exp["materia"] == "civil" and exp["estado"] == "en trámite":
        expedientes_civiles_activos_v1.append(exp["id"])

# La misma operación con una 'list comprehension'
expedientes_civiles_activos_v2 = [
    exp["id"]
    for exp in expedientes
    if exp["materia"] == "civil" and exp["estado"] == "en trámite"
]

print(expedientes_civiles_activos_v2)""",
    "steps": [
        {
            "highlight": {"line": 10},
            "what": "Se utiliza un bucle 'for' tradicional para recorrer la lista, un 'if' para filtrar y 'append' para añadir los resultados a una nueva lista.",
            "why": "Esta es la forma estándar y más explícita de realizar la operación. Es perfectamente funcional y fácil de entender para un principiante, pero requiere varias líneas de código.",
            "appData": "Es el patrón básico para cualquier operación de filtrado o transformación de datos en una lista.",
            "appLaw": "Representa un proceso de revisión manual y secuencial. 'Para cada expediente de la estantería, compruebe si es de materia civil y si está en trámite. Si cumple ambas, apúntelo en esta nueva hoja'.",
            "state": {"globals": {"expedientes_civiles_activos_v1": ["EXP-03"]}}
        },
        {
            "highlight": {"line": 16},
            "what": "Se define una 'list comprehension', que condensa toda la lógica del bucle anterior en una sola línea.",
            "why": "Las 'comprehensions' son una sintaxis más avanzada, declarativa y eficiente. Se leen casi como el lenguaje natural: 'dame el ID del expediente POR CADA expediente en la lista SI el expediente cumple estas condiciones'. Son preferidas por los programadores de Python por su brevedad y claridad.",
            "appData": "Es una herramienta extremadamente común en el análisis de datos para realizar transformaciones y filtros sobre listas de forma rápida y legible.",
            "appLaw": "Es el equivalente a dar una instrucción precisa y delegarla, en lugar de describir el proceso paso a paso. En lugar de un protocolo manual, es una 'orden ejecutiva': 'Obténgase un listado de los números de expediente de todos los procedimientos civiles en trámite'.",
            "state": {
                "globals": {
                    "expedientes_civiles_activos_v1": ["EXP-03"],
                    "expedientes_civiles_activos_v2": ["EXP-03"]
                }
            }
        },
        {
            "highlight": {"line": 22},
            "what": "Se imprime el resultado de la 'list comprehension', que es idéntico al obtenido con el bucle tradicional.",
            "why": "Confirma que, aunque la sintaxis es diferente, el resultado lógico es el mismo. La 'list comprehension' es a menudo más rápida en ejecución, además de ser más corta de escribir.",
            "appData": "En el procesamiento de grandes volúmenes de datos, la eficiencia de las 'comprehensions' sobre los bucles 'for' puede ser significativa.",
            "appLaw": "Demuestra que diferentes métodos (uno manual/explícito, otro declarativo/eficiente) pueden llevar al mismo resultado válido. La elección de uno u otro depende de la claridad y la eficiencia requerida para la tarea.",
            "state": {
                "globals": {
                    "expedientes_civiles_activos_v1": ["EXP-03"],
                    "expedientes_civiles_activos_v2": ["EXP-03"]
                },
                "io": {"out": ["['EXP-03']"]}
            }
        }
    ]
}
