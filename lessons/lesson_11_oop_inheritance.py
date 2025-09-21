lesson = {
    "title": "Lección 10: Clases y Objetos - Creando la 'Plantilla' de un Contrato",
    "description": "Introducción a la Programación Orientada a Objetos (OOP). Aprende a crear 'clases' (plantillas) para modelar conceptos del mundo real, como un 'Contrato', y luego a crear 'objetos' (instancias específicas) a partir de ellas.",
    "code": """# Se define una 'clase', que es la plantilla para crear contratos
class Contrato:
    def __init__(self, id_contrato, partes, objeto):
        self.id = id_contrato
        self.partes = partes
        self.objeto = objeto
        self.firmado = False  # Por defecto, un contrato no está firmado

    def firmar_contrato(self):
        # Este es un 'método' que cambia el estado del objeto
        self.firmado = True
        print(f"El contrato {self.id} ha sido firmado.")

# Se crea un 'objeto' (una instancia específica) a partir de la clase
contrato_alquiler = Contrato(
    id_contrato="ALQ-2025-01",
    partes=["Arrendador A", "Arrendatario B"],
    objeto="Vivienda sita en C/ Falsa, 123"
)

# Se invoca un método del objeto
contrato_alquiler.firmar_contrato()
print(f"Estado de firma: {contrato_alquiler.firmado}")""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se define una 'clase' llamada 'Contrato' usando la palabra clave 'class'.",
            "why": "Una clase es un plano o una plantilla. No es un contrato en sí, sino la definición de QUÉ es un contrato: qué propiedades tiene (sus 'atributos') y qué cosas puede hacer (sus 'métodos').",
            "appData": "En análisis de datos, podrías tener una clase `Cliente` con atributos como `nombre`, `id`, `fecha_de_alta` y métodos como `calcular_antiguedad()`.",
            "appLaw": "Una clase es el equivalente a la definición legal de una figura jurídica. La clase 'Contrato' define las características esenciales que todo contrato debe tener (partes, objeto, etc.), tal y como lo haría el Código Civil.",
            "state": {"globals": {"Contrato": "<class 'Contrato'>"}}
        },
        {
            "highlight": {"line": 15},
            "what": "Se crea una 'instancia' u 'objeto' de la clase 'Contrato'. 'contrato_alquiler' es un contrato específico y real.",
            "why": "Este es el paso de la plantilla a la realidad. Usando el plano (la clase `Contrato`), creamos una entidad concreta y única con sus propios datos. Podemos crear miles de objetos 'Contrato' diferentes a partir de la misma clase.",
            "appData": "A partir de la clase `Cliente`, creamos miles de objetos, uno por cada cliente en nuestra base de datos, cada uno con su propio nombre, ID, etc.",
            "appLaw": "Es la diferencia entre la definición abstracta de 'contrato de compraventa' en la ley y 'el contrato de compraventa específico firmado entre A y B el día X'. `contrato_alquiler` es este último.",
            "state": {
                "globals": {
                    "Contrato": "<class 'Contrato'>",
                    "contrato_alquiler": "<Contrato object with id='ALQ-2025-01'>"
                }
            }
        },
        {
            "highlight": {"line": 22},
            "what": "Se 'invoca' el método 'firmar_contrato' sobre el objeto 'contrato_alquiler'.",
            "why": "Ahora que tenemos un objeto concreto, podemos pedirle que realice las acciones para las que fue diseñado. La llamada al método ejecuta el código definido en la clase, pero lo hace en el contexto de este objeto específico.",
            "appData": "Se le pide a un objeto `grafico_ventas` que se dibuje a sí mismo (`grafico_ventas.mostrar()`).",
            "appLaw": "Este es el acto de firmar el contrato específico que hemos creado. La acción modifica el estado interno de 'contrato_alquiler' (su atributo `firmado` ahora es `True`), pero no afectaría a ningún otro objeto de contrato que pudiera existir.",
            "state": {
                "globals": {
                    "Contrato": "<class 'Contrato'>",
                    "contrato_alquiler": "<Contrato object with id='ALQ-2025-01', firmado=True>"
                },
                "io": {"out": ["El contrato ALQ-2025-01 ha sido firmado."]}
            }
        },
        {
            "highlight": {"line": 23},
            "what": "Se imprime el atributo 'firmado' del objeto para verificar que su estado ha cambiado.",
            "why": "Demuestra que la acción (el método) ha tenido un efecto persistente sobre el estado del objeto. El objeto ahora 'recuerda' que ha sido firmado.",
            "appData": "Después de ejecutar un `datos.limpiar()`, se comprueba el estado de los datos para verificar que la limpieza se ha realizado correctamente.",
            "appLaw": "Es la constatación del cambio de estado jurídico. El contrato ha pasado de estar 'pendiente' a 'perfeccionado', y este nuevo estado puede ser consultado y tendrá efectos para futuras operaciones.",
            "state": {
                "globals": {
                    "Contrato": "<class 'Contrato'>",
                    "contrato_alquiler": "<Contrato object with id='ALQ-2025-01', firmado=True>"
                },
                "io": {
                    "out": [
                        "El contrato ALQ-2025-01 ha sido firmado.",
                        "Estado de firma: True"
                    ]
                }
            }
        }
    ]
}
