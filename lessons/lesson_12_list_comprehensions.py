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
            "appLaw": "Representa un proceso de revisión manual y secuencial. 'Para cada expediente de la estantería, compruebe si es de materia civil y si está en trámite. Si cumple ambas, apúntelo en esta nueva hoja'."
        },
        {
            "highlight": {"line": 16},
            "what": "Se define una 'list comprehension', que condensa toda la lógica del bucle anterior en una sola línea.",
            "why": "Las 'comprehensions' son una sintaxis más avanzada, declarativa y eficiente. Se leen casi como el lenguaje natural: 'dame el ID del expediente POR CADA expediente en la lista SI el expediente cumple estas condiciones'. Son preferidas por los programadores de Python por su brevedad y claridad.",
            "appData": "Es una herramienta extremadamente común en el análisis de datos para realizar transformaciones y filtros sobre listas de forma rápida y legible.",
            "appLaw": "Es el equivalente a dar una instrucción precisa y delegarla, en lugar de describir el proceso paso a paso. En lugar de un protocolo manual, es una 'orden ejecutiva': 'Obténgase un listado de los números de expediente de todos los procedimientos civiles en trámite'."
        },
        {
            "highlight": {"line": 17},
            "what": "La primera parte (`exp['id']`) especifica QUÉ queremos en la nueva lista.",
            "why": "Esto es la parte de la 'transformación'. No tenemos por qué quedarnos con el diccionario completo; podemos extraer solo la pieza de información que nos interesa (en este caso, el ID).",
            "appData": "Muy útil para extraer una sola columna de una lista de registros. 'Dame solo el email de cada usuario'.",
            "appLaw": "Permite generar listados específicos para un propósito concreto. No necesitamos toda la información del expediente, solo su identificador para una notificación."
        },
        {
            "highlight": {"line": 18},
            "what": "La parte central (`for exp in expedientes`) indica SOBRE QUÉ lista estamos trabajando.",
            "why": "Es el equivalente directo del `for ... in ...` del bucle tradicional. Define el origen de los datos.",
            "appData": "Es la fuente de datos para la transformación.",
            "appLaw": "Define el universo de discurso. 'De todos los expedientes existentes en este archivo...'"
        },
        {
            "highlight": {"line": 19},
            "what": "La parte final (`if ...`) establece la CONDICIÓN de filtrado.",
            "why": "Esta es la cláusula que deben cumplir los elementos para ser incluidos en el resultado. Es opcional; si se omite, se procesarían todos los elementos.",
            "appData": "Es la cláusula `WHERE` de una consulta SQL. '...donde la categoría sea 'libros' y el precio sea mayor de 20€'.",
            "appLaw": "'...siempre y cuando cumplan la doble condición de ser de materia civil Y estar en trámite'. Es la aplicación de los criterios de selección."
        }
    ]
}
