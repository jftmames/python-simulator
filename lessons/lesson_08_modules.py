lesson = {
    "title": "Lección 8: Módulos - Usando las 'Leyes' del Código y Organizando Nuestro Despacho",
    "description": "Descubre cómo 'importar' funcionalidades ya hechas (módulos 'built-in' como el 'Código Penal' de Python) y cómo organizar tu propio código en diferentes archivos (módulos 'custom').",
    "code": """# 1. Importar un módulo 'built-in' (incluido en Python)
import json
import datetime

# 2. Importar una función de nuestro propio módulo 'custom'
# (Imaginemos que tenemos un archivo llamado 'protocolos_periciales.py')
from protocolos_periciales import generar_acta_de_evidencia

# Se usan las herramientas importadas
timestamp_actual = datetime.datetime.now().isoformat()
acta = generar_acta_de_evidencia("Contrato_v2.pdf", b"...", timestamp_actual)

print(acta)""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se importa el módulo 'json', que contiene herramientas para trabajar con el formato JSON.",
            "why": "Python viene con una 'biblioteca estándar' de módulos que resuelven problemas muy comunes. No tienes que reinventar la rueda. 'Importar' es como decir 'en este escrito, voy a aplicar las normas del Código de Comercio'.",
            "appData": "Módulos como 'csv', 'math', 'os' o 'datetime' son la base para la manipulación de archivos, cálculos matemáticos y gestión de fechas en casi cualquier script de análisis de datos.",
            "appLaw": "El uso de módulos estándar ('built-in') es una buena práctica pericial. Demuestra que se están utilizando herramientas probadas y aceptadas por la comunidad, no código 'casero' de dudosa fiabilidad."
        },
        {
            "highlight": {"line": 6},
            "what": "Se importa una función específica ('generar_acta_de_evidencia') de un módulo nuestro ('protocolos_periciales').",
            "why": "A medida que un proyecto crece, es insostenible tener todo el código en un solo archivo. Los módulos personalizados nos permiten organizar el código por temática (ej. un archivo para funciones de peritaje, otro para la gestión de clientes), haciendo el proyecto mantenible.",
            "appData": "Un proyecto de ciencia de datos se organiza en módulos: uno para la carga de datos (`data_loader.py`), otro para la limpieza (`data_cleaner.py`), otro para el modelado (`model.py`), etc.",
            "appLaw": "Es el equivalente a organizar un despacho de abogados por especialidades. En lugar de tener a todos los abogados haciendo de todo en un gran espacio, se crean departamentos (mercantil, penal, procesal). Cada módulo (`.py`) es un departamento con sus propias funciones y responsabilidades."
        },
        {
            "highlight": {"line": 9},
            "what": "Se utiliza una función del módulo 'datetime' para obtener la fecha y hora actual.",
            "why": "Una vez importado, podemos usar las herramientas del módulo como si fueran nuestras. Esto nos da acceso a funcionalidades muy potentes (como el manejo preciso de fechas y zonas horarias) con muy poco esfuerzo.",
            "appData": "El manejo de series temporales es una disciplina en sí misma. El módulo 'datetime' es la puerta de entrada para analizar datos a lo largo del tiempo.",
            "appLaw": "El sellado de tiempo ('timestamping') es crucial para la validez de una prueba digital. Demuestra cuándo se realizó una acción (ej. la creación del acta). Usar un módulo estándar para esto garantiza la precisión y fiabilidad de la fecha."
        },
        {
            "highlight": {"line": 10},
            "what": "Se llama a la función que importamos de nuestro propio módulo.",
            "why": "Este es el resultado final de una buena organización. El archivo principal (`app.py`) se vuelve muy legible. Su trabajo es orquestar y llamar a las herramientas especializadas que ha importado de otros módulos.",
            "appData": "El script principal de un pipeline de datos se dedica a llamar a las funciones de los diferentes módulos en el orden correcto: `cargar()`, `limpiar()`, `analizar()`, `visualizar()`.",
            "appLaw": "Demuestra una estructura de trabajo profesional y escalable. Un perito puede desarrollar una biblioteca de 'protocolos' en sus propios módulos y luego importarlos en cada caso concreto según las necesidades, asegurando consistencia y eficiencia."
        }
    ]
}
