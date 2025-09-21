lesson = {
    "title": "Lección 11: Herencia - Del 'Contrato' Genérico al 'Contrato de Arras' Específico",
    "description": "Aprende cómo una clase puede 'heredar' las propiedades y comportamientos de otra. Esto permite crear clases especializadas (un Contrato de Arras) a partir de una plantilla general (un Contrato), evitando repetir código.",
    "code": """class DocumentoLegal:
    def __init__(self, id_doc, partes):
        self.id = id_doc
        self.partes = partes

    def notificar_partes(self):
        print(f"Notificando a: {', '.join(self.partes)}")

# La clase 'Contrato' hereda de 'DocumentoLegal'
class Contrato(DocumentoLegal):
    def anular_contrato(self):
        print(f"El contrato {self.id} ha sido anulado.")

# Se crea un objeto de la clase especializada
contrato_arras = Contrato("ARR-2024-45", ["Comprador X", "Vendedor Y"])

# Puede usar métodos de su propia clase...
contrato_arras.anular_contrato()

# ...y también métodos de la clase 'padre' de la que hereda
contrato_arras.notificar_partes()""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Se define una clase 'padre' o 'base' llamada 'DocumentoLegal', con las propiedades comunes a cualquier documento.",
            "why": "Este es el principio de abstracción. Identificamos las características comunes (todo documento legal tiene un ID y partes) y las ponemos en una clase general. Esto crea una base sólida y reutilizable.",
            "appData": "Podríamos tener una clase base `Visualizacion` y clases hijas como `GraficoDeBarras` o `GraficoCircular` que heredan sus propiedades.",
            "appLaw": "Representa una categoría jurídica general. Por ejemplo, la categoría de 'Contratos' en el Código Civil establece unas reglas generales que luego se aplican y especializan en compraventas, arrendamientos, etc."
        },
        {
            "highlight": {"line": 9},
            "what": "Se define una clase 'hija' llamada 'Contrato' que hereda de 'DocumentoLegal'. La herencia se indica con los paréntesis: `class Contrato(DocumentoLegal):`.",
            "why": "La herencia permite que la clase 'Contrato' adquiera automáticamente todos los atributos (`id`, `partes`) y métodos (`notificar_partes`) de 'DocumentoLegal' sin tener que reescribirlos. A esto se le llama el principio 'DRY' (Don't Repeat Yourself - No te repitas).",
            "appData": "Esto permite crear jerarquías lógicas de objetos, haciendo el código más organizado y fácil de extender.",
            "appLaw": "Es el concepto de especialidad de la norma. Un 'Contrato de Arras' (clase hija) es, ante todo, un 'Contrato' (clase padre), y por tanto le aplican todas las normas generales de los contratos, además de sus reglas específicas."
        },
        {
            "highlight": {"line": 15},
            "what": "Se crea un objeto de la clase 'Contrato'. Aunque no hemos definido un `__init__` en 'Contrato', puede usar el de su clase padre 'DocumentoLegal'.",
            "why": "La herencia es automática. El objeto `contrato_arras` busca primero los métodos en su propia clase (`Contrato`) y, si no los encuentra, sube por la jerarquía para buscarlos en su clase padre (`DocumentoLegal`).",
            "appData": "Facilita enormemente la creación de variantes de un objeto. Puedes crear 10 tipos de gráficos diferentes heredando de una clase base y solo necesitarás programar lo que es único para cada uno.",
            "appLaw": "Un contrato de arras, por el hecho de ser un contrato, ya nace con las propiedades de 'partes' e 'identificador', heredadas de la definición general de documento legal."
        },
        {
            "highlight": {"line": 21},
            "what": "El objeto `contrato_arras` puede usar tanto los métodos definidos en su propia clase (`anular_contrato`) como los que ha heredado (`notificar_partes`).",
            "why": "Esto demuestra el poder y la flexibilidad de la herencia. Los objetos hijos tienen lo mejor de ambos mundos: la funcionalidad común del padre y su propia funcionalidad especializada.",
            "appData": "Permite construir sistemas complejos de forma modular y jerárquica, donde cada pieza se especializa en una tarea sin perder las capacidades de la base.",
            "appLaw": "Es la aplicación práctica de la teoría de los tipos contractuales. Todo contrato de arras puede ser 'anulado' (su especialidad), pero también debe permitir 'notificar a las partes' (su característica general como documento legal)."
        }
    ]
}
