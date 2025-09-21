lesson = {
    "title": "Lección 16: Gestores de Paquetes (Pip) - El Inventario de Herramientas del Perito",
    "description": "Aprende qué es 'pip', el gestor de paquetes de Python, y cómo se usa el archivo 'requirements.txt' para listar todas las herramientas externas de un proyecto. Es el equivalente a adjuntar un listado del software exacto usado en una pericia.",
    "code": """# --- En la terminal, dentro de un entorno virtual activado ---

# 1. Instalar una librería externa (ej. para análisis de datos)
# pip install pandas

# 2. Instalar una librería para trabajar con PDFs
# pip install pypdf2

# 3. Generar un 'inventario' de todas las librerías instaladas
# pip freeze > requirements.txt

# --- Contenido del archivo requirements.txt generado ---
# pandas==2.2.1
# pypdf2==3.0.1
# numpy==1.26.4
# ... (y otras dependencias que se instalan automáticamente)""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se usa el comando 'pip install' para descargar e instalar una librería desde un repositorio público (PyPI).",
            "why": "El ecosistema de Python es inmenso gracias a las miles de librerías de terceros que resuelven problemas específicos. 'pip' es la herramienta estándar para instalar estas librerías en nuestro entorno de trabajo.",
            "appData": "Es el primer paso en casi cualquier proyecto de datos: `pip install pandas matplotlib scikit-learn` para obtener las herramientas de análisis, visualización y machine learning.",
            "appLaw": "Un perito puede necesitar herramientas especializadas que no vienen con Python por defecto (ej. para analizar metadatos de un archivo o para procesar un formato de log específico). 'pip' es el mecanismo para instalar estas herramientas de forma controlada."
        },
        {
            "highlight": {"line": 10},
            "what": "El comando 'pip freeze' genera una lista de todas las librerías y sus versiones exactas instaladas en el entorno actual.",
            "why": "Este comando es la clave para la reproducibilidad. Al guardar esta lista en un archivo (por convención, `requirements.txt`), cualquier otra persona puede recrear tu entorno de trabajo exacto ejecutando `pip install -r requirements.txt`.",
            "appData": "Compartir un `requirements.txt` es una práctica obligatoria en proyectos colaborativos. Asegura que todos los miembros del equipo están usando las mismas versiones de las herramientas, evitando errores sutiles.",
            "appLaw": "El archivo `requirements.txt` es una pieza fundamental de la cadena de custodia técnica. Adjuntado a una pericial, permite a un contra-perito (o al propio juzgado) replicar el entorno del análisis con total fidelidad para verificar los resultados. Es la máxima garantía de transparencia y reproducibilidad."
        },
        {
            "highlight": {"line": 13},
            "what": "El archivo `requirements.txt` contiene una línea por cada librería, con su nombre y la versión exacta (`==`).",
            "why": "Fijar la versión con `==` es crucial. Una nueva versión de una librería podría cambiar su comportamiento y, potencialmente, alterar el resultado de un análisis. Fijar la versión 'congela' el estado del software en el tiempo.",
            "appData": "Evita el problema de 'en mi máquina sí funciona'. Garantiza que el código se ejecutará igual hoy, mañana o dentro de tres años.",
            "appLaw": "Garantiza la inmutabilidad del análisis. El perito puede afirmar con total certeza que el resultado de su informe se obtuvo con una versión específica de una herramienta, protegiéndose contra futuras actualizaciones que pudieran poner en duda sus conclusiones originales."
        }
    ]
}
