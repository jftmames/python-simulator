lesson = {
    "title": "Lección 18: Tipado Estático - El Contrato Formal que Obliga a Nuestros Datos",
    "description": "Aprende cómo el 'tipado estático' y librerías como Pydantic actúan como un contrato para tus datos, obligando a que la información cumpla una estructura y unos tipos predefinidos, evitando errores antes de que ocurran.",
    "code": """from pydantic import BaseModel, PositiveFloat, ValidationError

# Se define un 'modelo' de datos, que es como un contrato formal
class ActaEvidencia(BaseModel):
    id_expediente: str  # Debe ser un string, y es obligatorio
    cuantia_reclamada: PositiveFloat # Debe ser un número decimal y positivo
    custodio: str

# 1. Se crean datos válidos que cumplen el 'contrato'
datos_validos = {
    "id_expediente": "CIV-2025-987",
    "cuantia_reclamada": 12500.50,
    "custodio": "Perito Colegiado 123"
}
acta_valida = ActaEvidencia(**datos_validos) # Éxito

# 2. Se intenta crear un acta con datos inválidos
datos_invalidos = {"id_expediente": "CIV-2025-988", "cuantia_reclamada": -500} # Falta custodio, cuantía es negativa

try:
    ActaEvidencia(**datos_invalidos)
except ValidationError as e:
    print(e) # Pydantic genera un error claro y detallado""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se define una clase que hereda de 'BaseModel' de Pydantic. Cada atributo se 'tipa', es decir, se declara qué tipo de dato debe ser (`str`, `PositiveFloat`).",
            "why": "Esto es 'diseño por contrato'. En lugar de esperar a que un error ocurra en tiempo de ejecución, se definen las reglas de validación por adelantado. La clase 'ActaEvidencia' no es solo un contenedor, es un validador.",
            "appData": "Es fundamental para validar los datos que entran en un sistema, especialmente desde fuentes externas como una API. Garantiza que los datos tienen la forma y el tipo correctos antes de empezar a procesarlos.",
            "appLaw": "Es el equivalente a las cláusulas de definición y a los requisitos de forma de un contrato. El modelo 'ActaEvidencia' establece que para que un acta sea válida, DEBE tener un 'id_expediente' que sea texto, una 'cuantia' que sea un número positivo, y un 'custodio'. Si falta algo o el tipo es incorrecto, el 'contrato' es nulo (inválido)."
        },
        {
            "highlight": {"line": 14},
            "what": "Se crea una instancia del modelo pasándole un diccionario de datos que cumple con todas las reglas definidas.",
            "why": "Cuando los datos son correctos, Pydantic los valida, los convierte al tipo correcto si es necesario, y crea un objeto limpio y seguro con el que trabajar. El proceso es transparente y exitoso.",
            "appData": "Es el 'camino feliz' de la validación de datos. Los datos pasan el filtro y entran al sistema para ser procesados.",
            "appLaw": "Es la formalización de un acto jurídico que cumple todos los requisitos legales. El acta se crea con éxito porque los datos de entrada se ajustan a las 'cláusulas' definidas en el modelo."
        },
        {
            "highlight": {"line": 17},
            "what": "Se intenta crear una instancia con datos que violan las reglas: falta el campo 'custodio' y la 'cuantia' no es positiva.",
            "why": "Aquí se demuestra el poder de la validación. En lugar de crear un objeto con datos corruptos que podría causar errores impredecibles más adelante, Pydantic detiene el proceso inmediatamente.",
            "appData": "Esto previene la 'propagación de basura' (Garbage In, Garbage Out). Si los datos de entrada son incorrectos, el sistema los rechaza en la puerta en lugar de dejar que contaminen el resto del proceso.",
            "appLaw": "Es el equivalente a un registrador que deniega la inscripción de un documento por un defecto de forma insubsanable. El sistema detecta la invalidez de los datos de entrada y se niega a procesarlos, evitando la creación de un registro nulo o inválido."
        },
        {
            "highlight": {"line": 20},
            "what": "Pydantic no solo falla, sino que lanza una 'ValidationError' que contiene una descripción extremadamente clara y detallada de QUÉ ha fallado y DÓNDE.",
            "why": "Un buen sistema de validación no solo dice 'error', sino que explica por qué. Los mensajes de error de Pydantic son tan detallados que pueden ser mostrados directamente al usuario final o registrados en un log para una depuración rápida.",
            "appData": "Esto es crucial para construir APIs robustas. Si un usuario envía datos incorrectos, la API puede devolver un error 400 con el mensaje exacto de Pydantic, explicando qué campos son incorrectos.",
            "appLaw": "Es el equivalente a una providencia de subsanación de defectos clara y motivada. El sistema no solo rechaza el documento, sino que indica con precisión los motivos: 'Falta el nombre del custodio (campo obligatorio)' y 'La cuantía reclamada no puede ser negativa'. Esto permite a la parte corregir el error de forma eficiente."
        }
    ]
}
