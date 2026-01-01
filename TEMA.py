# ARCHIVO: TEMA.py

from UTILIDADES import validar_respuesta


class Tema:
    def __init__(self, id_tema: str, nombre_tema: str, requiere_diagnostico: bool = True):
        self.id_tema = id_tema
        self.nombre_tema = nombre_tema
        self.requiere_diagnostico = requiere_diagnostico
        self.cuestionario_diagnostico = []
        self.contenido_reforzamiento = []
        self.estado = "no_iniciado"
        self.prerequisitos = set()

    def asignar_cuestionario(self, preguntas: list) -> None:
        self.cuestionario_diagnostico = preguntas

    def asignar_reforzamiento(self, lecciones: list) -> None:
        self.contenido_reforzamiento = lecciones

    def asignar_prerequisitos(self, lista_ids_prerequisitos: list[str]) -> None:
        self.prerequisitos = set(lista_ids_prerequisitos)

    def actualizar_estado(self, nuevo_estado: str) -> None:
        estados_validos = ["no_iniciado", "en_reforzamiento",
                           "dominado_por_diagnostico", "completado_por_reforzamiento"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            print(f"ADVERTENCIA: Intento de asignar estado inválido: '{nuevo_estado}'")

    def realizar_diagnostico_rapido(self) -> float:
        print(f"\n--- Comprobando conocimientos de: {self.nombre_tema} ---")
        print("Veamos si ya dominas este tema o si necesitas un repaso.")

        if not self.cuestionario_diagnostico:
            print(f"ADVERTENCIA: No hay cuestionario de diagnóstico asignado para '{self.nombre_tema}'.")
            print("Se asumirá que se requiere reforzamiento (calificación 0.0).")
            return 0.0

        respuestas_correctas = 0
        total_preguntas = len(self.cuestionario_diagnostico)

        for i, datos_pregunta in enumerate(self.cuestionario_diagnostico):

            print(f"\nPregunta {i + 1}: {datos_pregunta['enunciado']}")
            respuesta_usuario = input("Escribe tu respuesta: ")

            respuesta_correcta = datos_pregunta['respuesta_correcta']

            if validar_respuesta(respuesta_usuario, respuesta_correcta):
                print("¡Correcto! 👍")
                respuestas_correctas += 1
            else:
                print(f"Incorrecto. La respuesta esperada era: {respuesta_correcta}")


        calificacion_final = (respuestas_correctas / total_preguntas) if total_preguntas > 0 else 0.0

        print(f"\n--- Fin del Diagnóstico ---")
        print(f"Resultado: {calificacion_final:.2f} ({respuestas_correctas} de {total_preguntas} correctas)")

        return calificacion_final

    def ejecutar_reforzamiento(self, carrera_usuario: str, leccion_idx: int = -1) -> str:
        """
        Ejecuta el curso de reforzamiento o una lección específica.
        Devuelve el estado final: "completado" o "leccion_terminada".
        """
        self.actualizar_estado("en_reforzamiento")

        # --- Lógica de una sola lección (Modo Admin) ---
        if leccion_idx != -1:
            try:
                leccion = self.contenido_reforzamiento[leccion_idx]
                print("\n" + "=" * 20 + f" LECCIÓN SELECCIONADA: {leccion_idx + 1} " + "=" * 20)
                self._ejecutar_leccion(leccion, carrera_usuario)
                print(f"✅ Lección {leccion_idx + 1} de '{self.nombre_tema}' finalizada.")
                return "leccion_terminada"
            except IndexError:
                print(f"❌ Error: El índice de lección {leccion_idx + 1} no existe.")
                return "error_leccion"

        # --- Flujo de Reforzamiento Completo (Modo Normal) ---
        print(f"\n--- Iniciando Curso de Reforzamiento de: {self.nombre_tema} ---")
        total_lecciones = len(self.contenido_reforzamiento)

        if total_lecciones == 0:
            print(f"ADVERTENCIA: No hay contenido de reforzamiento asignado para '{self.nombre_tema}'.")
            self.actualizar_estado("completado_por_reforzamiento")
            return "completado_por_reforzamiento"

        for i, leccion in enumerate(self.contenido_reforzamiento):
            print("\n" + "=" * 20 + f" Lección {i + 1}/{total_lecciones} " + "=" * 20)
            self._ejecutar_leccion(leccion, carrera_usuario)

        print(f"\n¡Felicidades! Has completado todas las lecciones de refuerzo de '{self.nombre_tema}'.")
        self.actualizar_estado("completado_por_reforzamiento")
        return "completado_por_reforzamiento"

    def _ejecutar_leccion(self, leccion: dict, carrera_usuario: str) -> None:
        """Contiene la lógica de ejecución de una lección individual, incluyendo
        la gestión de ejercicios principales y similares."""

        # Variables de control
        ejercicio_actual = leccion['ejercicio'].copy()

        # Cargar similares y mezclarlos (para que el orden no sea predecible)
        import random
        similares_pendientes = ejercicio_actual.get('similares', [])
        random.shuffle(similares_pendientes)

        # Usaremos esta variable para alternar entre el ejercicio principal y los similares
        ejercicio_en_curso = {
            "enunciado": ejercicio_actual['enunciado'],
            "respuesta_correcta": ejercicio_actual['respuesta_correcta'],
            "es_recuperacion": False
        }

        reintento_total = False  # Bandera para saber si ya se agotaron todos los intentos

        print(f"\nSubtema: {leccion['subtema_titulo']}")
        print(f"\nDefinición: {leccion['definicion']}")
        print("\n--- Ejemplo Resuelto ---")
        print(leccion['ejemplo_resuelto'])
        print("------------------------")

        # --- CICLO DE PREGUNTA Y RESPUESTA (MODIFICADO) ---
        while True:
            enunciado = ejercicio_en_curso['enunciado']
            respuesta_correcta = ejercicio_en_curso['respuesta_correcta']

            # Mensaje de contexto
            if ejercicio_en_curso['es_recuperacion']:
                prompt_prefix = "\n🔄 ¡Inténtalo de nuevo con un ejercicio similar! Resuelve: "
            elif reintento_total:
                # Si ya agotamos los similares, volvemos al principal con un mensaje de ánimo.
                prompt_prefix = "\n🛑 Pareces tener dificultades. Repasa la definición y resuelve: "
                reintento_total = False
            else:
                prompt_prefix = "\n¡Demuestra lo aprendido! Resuelve: "

            prompt_ejercicio = f"{prompt_prefix}{enunciado}: "
            respuesta_usuario = input(prompt_ejercicio)

            # 1. EVALUACIÓN
            if validar_respuesta(respuesta_usuario, respuesta_correcta):
                print("¡Excelente! Has entendido este punto. 👍 ¡Continuemos!")
                break  # Salir del ciclo while, la lección es un éxito

            # 2. EVALUACIÓN FALLIDA: Manejar reintento/similares
            else:
                print(f"❌ Incorrecto. La respuesta esperada era: {respuesta_correcta}")

                if similares_pendientes:
                    # Usar un ejercicio similar (Vida extra)
                    nuevo_ej = similares_pendientes.pop(0)

                    print("⚠️ Vamos a probar con un ejercicio diferente para reforzar.")

                    # Actualizar el ejercicio en curso al similar
                    ejercicio_en_curso['enunciado'] = nuevo_ej.get('pregunta', nuevo_ej.get('enunciado', ''))
                    ejercicio_en_curso['respuesta_correcta'] = nuevo_ej.get('respuesta_correcta',
                                                                            nuevo_ej.get('respuesta', ''))
                    ejercicio_en_curso['es_recuperacion'] = True

                else:
                    # Agotamos todos los intentos (Principal + Similares)
                    print("\n🛑 <b>Esto parece difícil.</b><br>")
                    print("Vuelve a intentarlo, lee atentamente la definición.")
                    print("Reiniciando la lección con el ejercicio principal.")

                    # Reiniciar el ciclo con el ejercicio principal original
                    ejercicio_en_curso = {
                        "enunciado": ejercicio_actual['enunciado'],
                        "respuesta_correcta": ejercicio_actual['respuesta_correcta'],
                        "es_recuperacion": False
                    }
                    # Recargar similares para el siguiente intento de la lección completa
                    similares_pendientes = ejercicio_actual.get('similares', [])
                    random.shuffle(similares_pendientes)
                    reintento_total = True  # Activar mensaje de "dificultad" en la siguiente iteración

        # --- Aplicación de la carrera (código original, solo aseguramos que el 'break' lo alcance) ---
        print("\n¿Por qué es importante esto para tu carrera?")
        if carrera_usuario in leccion['aplicaciones']:
            aplicacion = leccion['aplicaciones'][carrera_usuario]
            print(f"  - En Ing. {carrera_usuario.title()}:")
            print(f"    Uso: {aplicacion['uso']}")
            print(f"    Consecuencia de un error: {aplicacion['consecuencia_de_error']}")
        else:
            print("  - Aplicación general: Este es un concepto fundamental en todas las ingenierías.")

    def __repr__(self) -> str:
        diag_req = "SÍ" if self.requiere_diagnostico else "NO"

        return (f"<Tema ID: '{self.id_tema}' | "
                f"Nombre: '{self.nombre_tema}' | "
                f"Diag. Requerido: {diag_req} | "
                f"Estado: '{self.estado}'>")