lesson = {
    "title": "Lección 5: Condicionales (If / Else) - La Lógica de las Cláusulas Contractuales",
    "description": "Aprende a usar 'if' y 'else' para que tu programa tome decisiones, el equivalente a ejecutar una cláusula penal solo si se produce un incumplimiento.",
    "code": """# Se verifica el estado del pago de una factura
pago_recibido = False
dias_de_retraso = 35

# Se evalúa la condición principal
if pago_recibido == True:
    print("Estado: Pago recibido. Gracias.")
else:
    # Si la condición principal no se cumple, se evalúa esta otra
    print("Estado: Pago pendiente.")
    if dias_de_retraso > 30:
        print("Aviso: Se aplicará cláusula penal por demora superior a 30 días.")""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se definen variables booleanas y numéricas que representan los hechos del caso.",
            "why": "Las condiciones se basan en evaluar si una expresión es 'Verdadera' o 'Falsa'. Estas variables de estado son la materia prima para que el programa pueda tomar decisiones.",
            "appData": "Se utilizan como 'flags' o indicadores para segmentar datos. Por ejemplo, en una base de datos de clientes, podríamos tener una columna `ha_comprado_ultimo_mes` (True/False).",
            "appLaw": "Esta variable representa un 'hecho imponible' o una 'condición suspensiva'. Su valor (True/False) determina qué rama del razonamiento jurídico o contractual se debe seguir a continuación.",
            "state": {"globals": {"pago_recibido": False, "dias_de_retraso": 35}}
        },
        {
            "highlight": {"line": 6},
            "what": "La instrucción 'if' evalúa si la condición 'pago_recibido == True' es verdadera. En este caso, es falsa.",
            "why": "Este es el bloque de toma de decisiones más fundamental en programación. El código dentro del bloque 'if' SOLO se ejecutará si la condición se cumple.",
            "appData": "Se usa para todo: 'si las ventas superan el objetivo, enviar email de felicitación', 'si un dato es nulo, ignorarlo', etc.",
            "appLaw": "Es la transcripción literal de una condición legal o contractual. 'Si el arrendatario destina el inmueble a un uso distinto del pactado, entonces se resolverá el contrato'. El bloque 'if' contiene la consecuencia jurídica.",
            "state": {"io": {"log": ["Condición `pago_recibido == True` evaluada como Falso."]}}
        },
        {
            "highlight": {"line": 8},
            "what": "Como la condición del 'if' fue falsa, el programa salta y ejecuta el bloque 'else'.",
            "why": "El 'else' es la cláusula residual. Se ejecuta cuando la condición del 'if' NO se cumple. Asegura que el programa siempre tenga un camino a seguir, evitando la inacción o la ambigüedad.",
            "appData": "Proporciona un camino alternativo. 'Si el cliente es premium, aplicar descuento del 10%; si no (else), aplicar descuento del 5%'.",
            "appLaw": "Representa la consecuencia jurídica por defecto o subsidiaria. 'Si se entrega antes del día 5, se abona el precio íntegro; en caso contrario (else), se aplica una penalización'. Garantiza que haya una respuesta para cada escenario posible.",
            "state": {"io": {"out": ["Estado: Pago pendiente."]}},
        },
        {
            "highlight": {"line": 10},
            "what": "Dentro del 'else', se anida otro 'if' para comprobar si el retraso supera los 30 días. La condición es verdadera.",
            "why": "La lógica del mundo real raramente es binaria. A menudo, hay múltiples condiciones a evaluar. Los 'if' anidados permiten crear árboles de decisión tan complejos como sea necesario.",
            "appData": "Permite realizar segmentaciones más finas. 'Si el cliente es de España, y si además su compra supera los 100€, entonces ofrecer envío gratuito'.",
            "appLaw": "Refleja la complejidad de la argumentación jurídica, donde una norma general puede tener excepciones o sub-condiciones. 'El deudor responde con todos sus bienes, salvo (if) que sean inembargables, y si (if) además son bienes de primera necesidad, entonces se aplica un límite especial'.",
            "state": {"io": {"out": ["Estado: Pago pendiente.", "Aviso: Se aplicará cláusula penal por demora superior a 30 días."]}},
        }
    ]
}
