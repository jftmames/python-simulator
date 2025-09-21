lesson = {
    "title": "Lección 4: Diccionarios y Conjuntos - El Expediente Organizado y los Intervinientes Únicos",
    "description": "Aprende a usar 'diccionarios' para crear registros estructurados (como un expediente con etiquetas) y 'conjuntos' para gestionar listas de elementos únicos (como las partes de un litigio).",
    "code": """# Un diccionario para estructurar la información de un expediente
expediente = {
    "numero": "PO-105/2024",
    "demandante": "Ana García",
    "demandado": "Global Tech S.L.",
    "cuantia": 25000.00
}

# Un conjunto (set) para identificar a todos los intervinientes únicos
partes_caso_A = ["Ana García", "Global Tech S.L.", "Perito Juan Pérez"]
partes_caso_B = ["Global Tech S.L.", "Consultoría Digital", "Ana García"]

intervinientes_unicos = set(partes_caso_A) | set(partes_caso_B)
print(intervinientes_unicos)""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se crea un 'diccionario', una estructura que almacena datos en pares 'clave: valor'.",
            "why": "Los diccionarios son la forma más natural de representar objetos o registros del mundo real que tienen propiedades con nombre. Son increíblemente legibles y eficientes para buscar datos por su clave.",
            "appData": "El formato JSON, que domina el intercambio de datos en la web, es una representación directa de los diccionarios de Python. Se usan para todo, desde configuraciones hasta resultados de APIs.",
            "appLaw": "Un diccionario es la estructura de datos perfecta para modelar un acta, una ficha de cliente o un expediente. La 'clave' (ej. 'demandante') es el campo, y el 'valor' (ej. 'Ana García') es el dato, eliminando la ambigüedad de tener datos sueltos.",
             "state": {"globals": {"expediente": "{'numero': 'PO-105/2024', 'demandante': 'Ana García', ...}"}}
        },
        {
            "highlight": {"line": 10},
            "what": "Se crean dos listas que representan a las partes de dos casos relacionados, con duplicados.",
            "why": "En el mundo real, los datos a menudo son redundantes. Una misma persona o empresa puede aparecer en múltiples contextos. El primer paso para consolidar información es tener los datos brutos.",
            "appData": "Es común tener múltiples fuentes de datos (ej. logs de ventas, registros de clientes) con información repetida que necesita ser consolidada.",
            "appLaw": "En un litigio complejo, una misma parte (ej. 'Ana García') puede figurar en varios escritos o expedientes. El objetivo es obtener una lista consolidada y única de todos los intervinientes.",
            "state": {"globals": {"partes_caso_A": "['Ana García', ...]", "partes_caso_B": "['Global Tech S.L.', ...]"}}
        },
        {
            "highlight": {"line": 13},
            "what": "Se convierten las listas en 'conjuntos' (sets) y se realiza una operación de 'unión' (`|`).",
            "why": "La característica principal de un 'conjunto' es que, por definición, no puede contener elementos duplicados. Al convertir una lista a conjunto, se eliminan automáticamente todas las repeticiones. La unión combina dos conjuntos en uno nuevo, manteniendo la unicidad.",
            "appData": "Es una operación fundamental para la limpieza de datos. Permite obtener los valores únicos de una columna, contar usuarios distintos o realizar operaciones de teoría de conjuntos (unión, intersección) entre diferentes segmentos de datos.",
            "appLaw": "Esta es una forma programática y a prueba de errores de determinar el conjunto total de partes personadas en un procedimiento. El resultado, `intervinientes_unicos`, es una lista depurada y sin duplicados, lista para ser utilizada en notificaciones o escritos.",
            "state": {"globals": {"intervinientes_unicos": "{'Ana García', 'Global Tech S.L.', 'Perito Juan Pérez', 'Consultoría Digital'}"}}
        },
        {
            "highlight": {"line": 14},
            "what": "Se muestra el resultado del conjunto, donde cada interviniente aparece una sola vez.",
            "why": "El resultado final demuestra el poder de los conjuntos para la deduplicación y consolidación de datos. El orden no está garantizado, porque la principal propiedad de un conjunto es la pertenencia, no la posición.",
            "appData": "El resultado de esta operación podría ser el input para un panel de control que muestre 'Total de Clientes Únicos' o 'Número de Productos Distintos Vendidos'.",
            "appLaw": "La salida de este programa podría generar la carátula de un escrito judicial: '...siendo partes en el presente procedimiento D. Perito Juan Pérez, Dña. Ana García, Global Tech S.L. ...'. La fiabilidad del listado está garantizada por la estructura de datos utilizada.",
            "state": {"io": {"out": ["{'Ana García', 'Global Tech S.L.', 'Perito Juan Pérez', 'Consultoría Digital'}"]}}
        }
    ]
}
