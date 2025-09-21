lesson = {
    "title": "Lección 2: Tipos de Datos (Texto, Números y Lógica)",
    "description": "Exploramos la diferencia entre una cuantía (número), el texto de una cláusula (string) y una condición contractual (booleano). Entender esta distinción es clave para evitar ambigüedades y programar lógica jurídica precisa.",
    "code": """# 1. El plazo en días para una apelación (un número entero)
plazo_dias = 15

# 2. El porcentaje de interés de demora (un número decimal)
interes_demora = 0.035

# 3. El nombre del demandado (una cadena de texto)
demandado = "Inversiones Globales S.L."

# 4. Se verifica si la prueba ha sido admitida (un valor lógico)
prueba_admitida = True

# Se usan los datos para generar un resumen
resumen = f"El demandado {demandado} tiene un plazo de {plazo_dias} días."
print(resumen)""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se almacena el número 15 en la variable 'plazo_dias'. Este es un tipo de dato 'integer' (entero).",
            "why": "Los números enteros se usan para cantidades que no pueden tener decimales, como días, unidades o el número de un artículo de una ley. Son precisos y se usan para contar.",
            "appData": "En análisis de datos, las columnas de 'edad', 'número de hijos' o 'días de antigüedad' se representan como enteros para realizar cálculos exactos.",
            "appLaw": "Un plazo procesal es un ejemplo perfecto de un entero. Son 15 días, no 15.5. Usar el tipo de dato correcto (entero) refleja la naturaleza indivisible del concepto jurídico y evita errores de cálculo.",
            "state": {"globals": {"plazo_dias": 15}}
        },
        {
            "highlight": {"line": 5},
            "what": "Se guarda el número 0.035 en 'interes_demora'. Este es un tipo 'float' (decimal).",
            "why": "Los 'floats' son necesarios cuando se requiere precisión decimal. Son indispensables para cualquier cálculo financiero, estadístico o científico.",
            "appData": "Se usan para representar probabilidades, porcentajes, precios, o cualquier medida que no sea una unidad contable entera.",
            "appLaw": "El cálculo de intereses, la distribución de porcentajes en una herencia o el cálculo de una indemnización con céntimos requieren el uso de decimales. Un error de redondeo por usar un tipo incorrecto podría tener consecuencias económicas significativas.",
            "state": {"globals": {"plazo_dias": 15, "interes_demora": 0.035}}
        },
        {
            "highlight": {"line": 8},
            "what": "Se asigna el texto 'Inversiones Globales S.L.' a la variable 'demandado'. Este es un tipo 'string' (cadena de texto).",
            "why": "Los strings se usan para almacenar cualquier tipo de información textual: nombres, direcciones, párrafos de texto, etc. Son la forma de representar el lenguaje humano en un programa.",
            "appData": "El análisis de texto (NLP), la minería de opiniones o la clasificación de documentos se basan enteramente en la manipulación y el análisis de strings.",
            "appLaw": "El texto de una cláusula contractual, el nombre de las partes, el contenido de una declaración testifical o el cuerpo de una ley son 'strings'. La integridad y literalidad del texto es a menudo un punto central de la argumentación jurídica.",
            "state": {"globals": {"plazo_dias": 15, "interes_demora": 0.035, "demandado": "Inversiones Globales S.L."}}
        },
        {
            "highlight": {"line": 11},
            "what": "Se establece la variable 'prueba_admitida' como 'True' (Verdadero). Este es un tipo 'boolean' (booleano).",
            "why": "Los booleanos solo pueden tener dos valores: Verdadero o Falso. Son el pilar de la toma de decisiones en la programación. Cualquier pregunta de 'sí o no' se responde con un booleano.",
            "appData": "Se usan para crear filtros (ej. `clientes_activos == True`), para indicar el resultado de una prueba, o para controlar bucles y condicionales.",
            "appLaw": "Representa el cumplimiento o incumplimiento de una condición jurídica: ¿es válido el contrato? (True/False), ¿ha prescrito la acción? (True/False), ¿se ha admitido la prueba? (True/False). La lógica de un smart contract se basa enteramente en evaluar condiciones booleanas.",
            "state": {"globals": {"plazo_dias": 15, "interes_demora": 0.035, "demandado": "Inversiones Globales S.L.", "prueba_admitida": True}}
        },
        {
            "highlight": {"line": 14},
            "what": "Se combinan variables de texto y número en una nueva cadena de texto para crear un resumen.",
            "why": "Este es un ejemplo de 'composición'. Los programas raramente trabajan con un solo tipo de dato a la vez. Lo habitual es combinar y transformar datos para generar informes, notificaciones o documentos.",
            "appData": "La generación de informes dinámicos, la creación de visualizaciones con títulos personalizados o la exportación de datos a formatos legibles son tareas de composición.",
            "appLaw": "Es el equivalente a redactar un auto o una notificación judicial, donde se combinan datos estructurados (nombre del demandado, número de expediente, plazos) en un documento narrativo coherente y legible.",
            "state": {"globals": {"resumen": "El demandado Inversiones Globales S.L. tiene un plazo de 15 días."}, "io": {"out": ["El demandado Inversiones Globales S.L. tiene un plazo de 15 días."]}}
        }
    ]
}
