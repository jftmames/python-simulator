lesson = {
    "title": "Lección 9: Excepciones - El Plan de Contingencia para Imprevistos Procesales",
    "description": "Aprende a usar 'try' y 'except' para gestionar errores de forma controlada. Es el equivalente a tener un plan B o un procedimiento de subsanación cuando una operación falla.",
    "code": """# Se intenta abrir un archivo de prueba que podría no existir
ruta_prueba = "evidencia_adjunta.pdf"

try:
    # Intenta ejecutar este bloque de código "peligroso"
    with open(ruta_prueba, "rb") as f:
        contenido = f.read()
    print(f"Éxito: El archivo '{ruta_prueba}' ha sido leído correctamente.")

except FileNotFoundError:
    # Si y solo si ocurre un error de 'Archivo No Encontrado', se ejecuta este bloque
    print(f"ERROR: No se pudo encontrar el archivo '{ruta_prueba}'.")
    print("Acción: Se deja constancia en el acta y se notifica al juzgado.")

print("El programa continúa su ejecución de forma controlada.")""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se inicia un bloque 'try', que delimita una sección de código que podría fallar.",
            "why": "Hay operaciones que son inherentemente arriesgadas porque dependen de factores externos: acceder a un archivo (puede no existir), conectar a una red (puede estar caída), etc. El bloque 'try' es una declaración de intenciones: 'voy a intentar hacer esto, pero estoy preparado para que falle'.",
            "appData": "Cualquier proceso que lea datos de una fuente externa (un archivo, una API, una base de datos) debe estar envuelto en un bloque 'try' para manejar posibles errores de conexión o formato.",
            "appLaw": "Es el equivalente a iniciar un acto procesal que tiene riesgo de defecto. Por ejemplo, al presentar una demanda, se 'intenta' cumplir todos los requisitos, pero se está preparado para recibir una providencia de 'subsanación de defectos'.",
            "state": {"globals": {"ruta_prueba": "evidencia_adjunta.pdf"}}
        },
        {
            "highlight": {"line": 10},
            "what": "Se define un bloque 'except' que 'captura' un tipo de error específico: 'FileNotFoundError'.",
            "why": "Este es el plan de contingencia. El código dentro de este bloque NO se ejecuta en condiciones normales. Solo se activa si el error especificado ('FileNotFoundError') ocurre dentro del bloque 'try'. Permite dar una respuesta controlada al fallo en lugar de que el programa entero se colapse.",
            "appData": "Permite crear programas robustos. Si falla la lectura de un archivo, en lugar de parar, el programa puede registrar el error en un log y continuar procesando los demás archivos.",
            "appLaw": "Esto es un procedimiento de subsanación. Si el 'try' es presentar la prueba y falla porque 'el archivo no se encuentra', el 'except' es el procedimiento a seguir: 'se haga constar por diligencia del Letrado de la Administración de Justicia y se requiera a la parte para que lo aporte'.",
            "state": {
                "globals": {"ruta_prueba": "evidencia_adjunta.pdf"},
                "io": {
                    "log": ["Ocurrió un FileNotFoundError dentro del bloque 'try'."],
                    "out": [
                        "ERROR: No se pudo encontrar el archivo 'evidencia_adjunta.pdf'.",
                        "Acción: Se deja constancia en el acta y se notifica al juzgado."
                    ]
                }
            }
        },
        {
            "highlight": {"line": 15},
            "what": "El programa continúa ejecutándose después del bloque try/except.",
            "why": "Esta es la principal ventaja del manejo de excepciones. Un error en una parte del programa no provoca un fallo catastrófico. El error se gestiona, se registra, y el programa sigue adelante. Es la diferencia entre un sistema frágil y uno resiliente.",
            "appData": "Un pipeline de datos que procesa millones de registros no puede permitirse fallar por un solo registro mal formado. Lo captura, lo reporta y sigue con el resto.",
            "appLaw": "La nulidad de una prueba no tiene por qué invalidar todo el procedimiento. El sistema jurídico está diseñado para aislar y gestionar los fallos (errores procesales, pruebas ilícitas) sin detener por completo la maquinaria de la justicia. El manejo de excepciones es el mismo principio aplicado al código.",
            "state": {
                "globals": {"ruta_prueba": "evidencia_adjunta.pdf"},
                "io": {
                    "out": [
                        "ERROR: No se pudo encontrar el archivo 'evidencia_adjunta.pdf'.",
                        "Acción: Se deja constancia en el acta y se notifica al juzgado.",
                        "El programa continúa su ejecución de forma controlada."
                    ]
                }
            }
        }
    ]
}
