lesson = {
    "title": "Lección 13: Expresiones Regulares (RegEx) - El Bisturí para Encontrar Patrones en Textos Legales",
    "description": "Aprende a usar 'expresiones regulares', un mini-lenguaje especializado en la búsqueda y extracción de patrones de texto. Es la herramienta más potente para tareas como anonimizar documentos o extraer fechas.",
    "code": """import re

texto_contrato = "El presente acuerdo se firma el 22/09/2025. El NIF del arrendador es 12345678A y el del arrendatario es Y9876543B."

# Se define un 'patrón' para encontrar fechas en formato dd/mm/yyyy
patron_fecha = r"\\d{2}/\\d{2}/\\d{4}"
fechas_encontradas = re.findall(patron_fecha, texto_contrato)

# Se define un patrón más complejo para encontrar NIFs/NIEs
patron_nif = r"[XYZ\\d]?\\d{7}[A-Z]"
nifs_encontrados = re.findall(patron_nif, texto_contrato)

# Se usa 're.sub' para anonimizar (reemplazar) los NIFs
texto_anonimizado = re.sub(patron_nif, "[NIF OCULTO]", texto_contrato)

print(f"Fechas: {fechas_encontradas}")
print(f"NIFs: {nifs_encontrados}")
print(f"Texto anonimizado: {texto_anonimizado}")""",
    "steps": [
        {
            "highlight": {"line": 6},
            "what": "Se define un 'patrón' de expresión regular. `\\d` significa 'un dígito' y `{2}` significa 'exactamente dos veces'. El patrón busca 'dos dígitos, barra, dos dígitos, barra, cuatro dígitos'.",
            "why": "Las expresiones regulares son un lenguaje para describir patrones de texto. En lugar de buscar un texto exacto, se busca una 'forma' o 'estructura'. Esto permite encontrar todas las fechas de un documento, sin importar cuáles sean los números.",
            "appData": "Se usan para validar formatos de datos (ej. si un email tiene la forma 'texto@texto.dominio'), para limpiar texto o para extraer información de logs no estructurados.",
            "appLaw": "Es una herramienta pericial de primer orden para el análisis de grandes volúmenes de texto. Permite, por ejemplo, extraer todas las menciones a un número de cuenta bancaria, a una matrícula o a una fecha en miles de documentos de forma automática."
        },
        {
            "highlight": {"line": 7},
            "what": "La función `re.findall` busca TODAS las apariciones del patrón en el texto y las devuelve en una lista.",
            "why": "Es la función de 'búsqueda'. Recorre el texto completo y extrae todos los fragmentos que coinciden con la descripción del patrón.",
            "appData": "Permite 'cosechar' datos de texto no estructurado, como extraer todos los hashtags de una lista de tuits.",
            "appLaw": "Permite a un investigador o perito realizar un 'discovery' electrónico: encontrar todas las ocurrencias de un término, fecha o identificador clave dentro de un cuerpo masivo de documentos (ej. correos electrónicos, contratos)."
        },
        {
            "highlight": {"line": 10},
            "what": "Se define un patrón más complejo: `[XYZ\\d]?` significa 'una X, Y, Z o un dígito, opcionalmente'. `\\d{7}` son siete dígitos. `[A-Z]` es una letra mayúscula.",
            "why": "Los patrones pueden ser tan complejos como sea necesario para describir con precisión lo que se busca. Este patrón es capaz de encontrar tanto NIFs de españoles como NIEs de extranjeros.",
            "appData": "La complejidad de los patrones permite extraer información muy específica de textos complejos, como los resultados de un análisis médico de un informe en texto plano.",
            "appLaw": "La precisión del patrón es clave para evitar 'falsos positivos'. Un patrón bien definido asegura que solo se extrae la información relevante (ej. NIFs) y no otros números que puedan parecerse."
        },
        {
            "highlight": {"line": 14},
            "what": "La función `re.sub` busca todas las apariciones del patrón y las REEMPLAZA por un nuevo texto.",
            "why": "Además de buscar, las expresiones regulares son extremadamente potentes para modificar texto. `re.sub` es la base de cualquier proceso de anonimización o seudonimización.",
            "appData": "Se usa para limpiar datos, por ejemplo, eliminando caracteres extraños, o para estandarizar formatos (ej. convertir todas las variantes de fechas a un único formato YYYY-MM-DD).",
            "appLaw": "Esta es la implementación técnica directa de los principios de minimización de datos y privacidad por defecto del RGPD. Antes de entregar un conjunto de documentos en un procedimiento, se puede usar `re.sub` para 'tachar' u 'ocultar' sistemáticamente toda la información personal identificable."
        }
    ]
}
