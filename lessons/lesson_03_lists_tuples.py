lesson = {
    "title": "Lección 3: Listas y Tuplas - El Expediente Modificable vs. Hechos Probados Inmutables",
    "description": "Aprende la diferencia entre una 'lista' (un conjunto de pruebas que puede crecer) y una 'tupla' (una secuencia de hechos que, una vez declarada, no puede cambiar).",
    "code": """# Una lista de pruebas presentadas, que puede ser modificada
pruebas_presentadas = ["Contrato original", "Correo electrónico del 22 de Sep"]

# Se añade una nueva prueba al expediente
pruebas_presentadas.append("Acta notarial de entrega")

# Una tupla con los hechos probados de una sentencia: inmutables
hechos_probados = ("Incumplimiento contractual", "Lucro cesante acreditado")

# Intentar modificar un hecho probado generaría un error.
# hechos_probados[0] = "Cumplimiento parcial" # <-- Esto es imposible y daría error""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se crea una 'lista', que es una colección ordenada y modificable de elementos.",
            "why": "Las listas son una de las estructuras más versátiles. Permiten agrupar elementos relacionados y cambiar el grupo dinámicamente: añadir, eliminar o modificar elementos.",
            "appData": "Las listas son omnipresentes en el análisis de datos para almacenar columnas de una tabla, series de tiempo o los resultados de una encuesta.",
            "appLaw": "Una lista es el símil perfecto para el inventario de pruebas de un caso. A medida que avanza la investigación, se pueden añadir ('append') nuevas pruebas o retirar las que han sido desestimadas.",
            "state": {"globals": {"pruebas_presentadas": ["Contrato original", "Correo electrónico del 22 de Sep"]}}
        },
        {
            "highlight": {"line": 5},
            "what": "Se utiliza el método 'append' para añadir un nuevo elemento al final de la lista.",
            "why": "Esta es la operación fundamental para hacer crecer una colección de datos. Demuestra la 'mutabilidad' de las listas: su contenido puede cambiar después de su creación.",
            "appData": "En un proceso de recolección de datos, cada nuevo dato (ej. una venta, un tuit) se añade a una lista para su posterior procesamiento.",
            "appLaw": "Este acto es análogo a la aportación de una nueva prueba documental al expediente judicial. La lista 'pruebas_presentadas' se actualiza para reflejar el estado actual y completo del material probatorio.",
            "state": {"globals": {"pruebas_presentadas": ["Contrato original", "Correo electrónico del 22 de Sep", "Acta notarial de entrega"]}}
        },
        {
            "highlight": {"line": 8},
            "what": "Se crea una 'tupla', que es una colección ordenada pero inmutable de elementos.",
            "why": "La inmutabilidad es una garantía de seguridad. Cuando tienes datos que NUNCA deben cambiar (como unas coordenadas, una fecha clave o una versión de un software), usas una tupla para protegerlos contra modificaciones accidentales.",
            "appData": "Las tuplas se usan a menudo como claves en los diccionarios porque, al ser inmutables, garantizan que la clave nunca cambiará.",
            "appLaw": "Una tupla representa perfectamente los 'hechos probados' de una sentencia firme. Son una declaración definitiva que no puede ser alterada. Su inmutabilidad en el código refleja la inmutabilidad y seguridad jurídica del concepto que representa.",
            "state": {"globals": {"hechos_probados": ("Incumplimiento contractual", "Lucro cesante acreditado")}}
        },
        {
            "highlight": {"line": 11},
            "what": "Se muestra un intento comentado de modificar la tupla, lo cual es imposible.",
            "why": "Este es el punto clave de la lección. Python protege activamente las tuplas contra cualquier intento de modificación, lanzando un error. Esta protección es la razón de ser de las tuplas.",
            "appData": "Si un analista necesita garantizar que una configuración o un conjunto de parámetros iniciales no se modifiquen durante la ejecución de un largo proceso, los almacenará en una tupla.",
            "appLaw": "Esto es una barrera técnica contra la alteración de datos críticos. Un smart contract podría usar una tupla para almacenar las condiciones esenciales del acuerdo (ej. el precio y el objeto), asegurando que ni siquiera un error en el código pueda modificarlas.",
            "state": {"io": {"log": ["Intentar `hechos_probados[0] = ...` causaría un TypeError."]}}
        }
    ]
}
