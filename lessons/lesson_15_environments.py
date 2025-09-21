lesson = {
    "title": "Lección 15: Entornos Virtuales - Aislando el 'Expediente' Técnico de Cada Caso",
    "description": "Descubre por qué se usan los entornos virtuales para evitar conflictos de dependencias. Es el equivalente a tener una carpeta separada y autocontenida para las herramientas de cada caso, asegurando que un caso no interfiere con otro.",
    "code": """# --- En la terminal, fuera de Python ---

# 1. Crear un entorno virtual llamado 'venv_caso_101'
# python -m venv venv_caso_101

# 2. Activar el entorno (entrar en la 'burbuja' aislada)
# En Windows: .\\venv_caso_101\\Scripts\\activate
# En Mac/Linux: source venv_caso_101/bin/activate

# 3. Instalar librerías específicas para este caso
# (venv_caso_101) > pip install pandas=="1.5.3"
# (venv_caso_101) > pip install "cryptography<40.0"

# 4. Desactivar el entorno (salir de la 'burbuja')
# (venv_caso_101) > deactivate""",
    "steps": [
        {
            "highlight": {"line": 4},
            "what": "Se ejecuta un comando en la terminal para crear una nueva carpeta que contendrá un entorno virtual.",
            "why": "Un entorno virtual es una copia aislada de Python. Permite tener múltiples proyectos en el mismo ordenador, cada uno con su propio conjunto de librerías y versiones, sin que entren en conflicto entre sí.",
            "appData": "Es una práctica obligatoria en la ciencia de datos profesional. Cada proyecto tiene su propio entorno para garantizar que los análisis sean 100% reproducibles.",
            "appLaw": "Es el principio de 'aislamiento del caso'. Imagina que un perito usa una herramienta de software versión 1.0 para el Caso A. Años después, para el Caso B, necesita la versión 3.0. Sin entornos virtuales, instalar la 3.0 podría romper la capacidad de reproducir el análisis del Caso A. Un entorno virtual 'congela' las herramientas de cada caso.",
            "state": {"io": {"log": ["Comando ejecutado: python -m venv venv_caso_101"]}}
        },
        {
            "highlight": {"line": 7},
            "what": "Se 'activa' el entorno. La terminal cambia para mostrar el nombre del entorno activo.",
            "why": "Activar un entorno es como 'entrar' en la carpeta de un caso específico. A partir de este momento, cualquier herramienta de Python que se instale o ejecute lo hará dentro de esta 'burbuja' aislada, sin afectar al sistema principal ni a otros proyectos.",
            "appData": "Antes de empezar a trabajar en un proyecto, el primer paso es siempre activar su entorno virtual correspondiente.",
            "appLaw": "Es el acto de 'abrir el expediente' técnico. El perito se asegura de que está trabajando con el conjunto de herramientas correcto y específico para el caso en cuestión, evitando la contaminación cruzada.",
            "state": {"io": {"log": ["Entorno 'venv_caso_101' activado."]}}
        },
        {
            "highlight": {"line": 11},
            "what": "Dentro del entorno activo, se instalan versiones específicas de las librerías necesarias para el proyecto.",
            "why": "Aquí reside el poder de los entornos. Podemos instalar una versión antigua de una librería (`pandas=='1.5.3'`) para un proyecto que la requiere, sin desinstalar la versión más moderna que podamos necesitar para otro. El operador `==` fija la versión exacta.",
            "appData": "La reproducibilidad es la piedra angular de la ciencia. Fijar las versiones de las librerías garantiza que un análisis realizado hoy producirá exactamente el mismo resultado dentro de cinco años.",
            "appLaw": "Esto es fundamental para la impugnación o contra-peritaje. Un segundo perito debe poder recrear el entorno técnico exacto del primero para verificar sus conclusiones. Un `requirements.txt` (el archivo que lista las dependencias) es el equivalente a la lista de material del laboratorio.",
            "state": {"io": {"log": ["Instalando pandas==1.5.3...", "Instalando cryptography<40.0..."]}}
        },
        {
            "highlight": {"line": 14},
            "what": "Se 'desactiva' el entorno para volver a la configuración global del sistema.",
            "why": "Es el acto de 'cerrar' el expediente. Al salir del entorno, volvemos a tener acceso a las herramientas del sistema principal, dejando la 'burbuja' del proyecto intacta y lista para ser reactivada cuando volvamos a trabajar en él.",
            "appData": "Permite cambiar de un proyecto a otro de forma limpia y segura. `deactivate`, `cd ../otro_proyecto`, `source venv_otro_proyecto/bin/activate`.",
            "appLaw": "Asegura que el trabajo realizado en un caso no 'contamina' inadvertidamente el siguiente. Es una medida de higiene y organización profesional indispensable para garantizar la integridad y reproducibilidad de la prueba pericial digital.",
            "state": {"io": {"log": ["Entorno desactivado."]}}
        }
    ]
}
