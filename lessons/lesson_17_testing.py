lesson = {
    "title": "Lección 17: Testing - La Validación Cruzada del Código Pericial",
    "description": "Aprende el concepto de 'testing' o pruebas unitarias. Consiste en escribir código que comprueba automáticamente que otro código funciona como se espera. Es la forma de demostrar la fiabilidad y corrección de una herramienta.",
    "code": """# --- En un archivo llamado 'calculadora_indemnizaciones.py' ---
def calcular_interes_simple(principal, tasa, dias):
    # Fórmula: Principal * (Tasa / 365) * Días
    if principal < 0 or tasa < 0 or dias < 0:
        raise ValueError("Los valores no pueden ser negativos")
    return principal * (tasa / 365) * dias

# --- En un archivo de pruebas llamado 'test_calculadora.py' ---
from calculadora_indemnizaciones import calcular_interes_simple

def test_calculo_normal():
    # Se comprueba que para un caso simple, el resultado es el esperado
    assert calcular_interes_simple(1000, 0.05, 365) == 50.0

def test_valores_negativos():
    # Se comprueba que la función falla correctamente si se le dan datos inválidos
    try:
        calcular_interes_simple(-1000, 0.05, 365)
    except ValueError:
        assert True # Si se lanza el error esperado, la prueba es un éxito""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se define una función que contiene una lógica de negocio importante (el cálculo de un interés).",
            "why": "Este es el 'sujeto' de la prueba. Es una pieza de código cuya corrección es crítica. Un error en esta función podría tener consecuencias económicas.",
            "appData": "Podría ser una función que calcula una métrica de negocio, que limpia una columna de datos o que transforma un formato de fecha.",
            "appLaw": "Representa una pieza de lógica que implementa una regla jurídica o contractual. La correcta implementación de esta fórmula es fundamental para la validez de la conclusión (ej. la cuantía de la indemnización)."
        },
        {
            "highlight": {"line": 9},
            "what": "Se crea un archivo separado para las pruebas. Se importa la función que se quiere probar.",
            "why": "El código de las pruebas vive separado del código de la aplicación. Esto mantiene el proyecto organizado. Cada prueba es un 'caso de uso' que verifica un comportamiento específico.",
            "appData": "Los proyectos de software serios tienen una carpeta `tests/` con una estructura que replica la del código fuente.",
            "appLaw": "Las pruebas son el equivalente a una 'validación cruzada' o a un 'caso de control' en una investigación. Se diseñan escenarios específicos para verificar que el 'protocolo' (la función) se comporta como se espera en cada situación."
        },
        {
            "highlight": {"line": 12},
            "what": "La instrucción 'assert' comprueba si una condición es verdadera. Si lo es, la prueba pasa. Si es falsa, la prueba falla y se reporta un error.",
            "why": "'Assert' es el corazón del testing. Es una afirmación rotunda: 'Yo afirmo que el resultado de esta operación DEBE SER este valor'. Si la afirmación no es cierta, algo está roto en el código.",
            "appData": "Una suite de tests puede tener miles de 'asserts' que verifican cada pequeño detalle del comportamiento de un sistema.",
            "appLaw": "Es una declaración jurada sobre el comportamiento del código. El programador (o perito) no solo escribe el código, sino que también escribe una serie de afirmaciones que demuestran su corrección ante casos concretos y verificables."
        },
        {
            "highlight": {"line": 15},
            "what": "Se diseña una prueba para un 'caso límite' o 'caso de error'. La prueba verifica que la función falla de la manera esperada (lanzando un 'ValueError').",
            "why": "Probar que el código funciona con datos correctos es solo la mitad del trabajo. Es igualmente importante probar que gestiona los datos incorrectos de forma segura y predecible, sin romperse de forma inesperada.",
            "appData": "Se prueban casos como inputs nulos, formatos incorrectos, números fuera de rango, etc., para asegurar la robustez del programa.",
            "appLaw": "Demuestra la diligencia debida del perito o desarrollador. No solo se ha considerado el 'camino feliz', sino que se han previsto y gestionado los posibles escenarios de error. Esto aumenta enormemente la confianza en la fiabilidad de la herramienta."
        }
    ]
}
