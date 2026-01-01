# ARCHIVO: CONTENIDO.py

RUTAS_POR_MATERIA = {
    "MATEMATICAS": [
        # MATE_1
        "ARITMETICA", "ALGEBRA BASICA", "GEOMETRIA", "TRIGONOMETRIA",
        "GEOMETRIA ANALITICA", "PRECALCULO",
        # MATE_2
        "CALCULO DIFERENCIAL", "VECTORES Y GEOMETRIA", "CALCULO INTEGRAL",
        "ALGEBRA LINEAL", "CALCULO VECTORIAL", "ECUACIONES DIFERENCIALES"
    ],

    "FISICA": [
        "FIS-01", "FIS-02", "FIS-03", "FIS-04", "FIS-05"
    ],

    "QUIMICA": [
        "QUIM-01", "QUIM-02", "QUIM-03", "QUIM-04", "QUIM-05"
    ],

    "PROGRAMACION": [
        "PROG-01", "PROG-02", "PROG-03", "PROG-04", "PROG-05"
    ]
}

NOMBRES_DE_TEMAS = {
    # MATE_1
    "ARITMETICA": "Aritmética",
    "ALGEBRA BASICA": "Álgebra Básica",
    "GEOMETRIA": "Geometría",
    "TRIGONOMETRIA": "Trigonometría",
    "GEOMETRIA ANALITICA": "Geometría Analítica",
    "PRECALCULO": "Precálculo",
    # MATE_2
    "CALCULO DIFERENCIAL": "Cálculo Diferencial",
    "CALCULO INTEGRAL": "Cálculo Integral",
    "CALCULO VECTORIAL": "Cálculo Vectorial",
    "VECTORES Y GEOMETRIA": "Vectores y Geometría",
    "ALGEBRA LINEAL": "Álgebra Lineal",
    "ECUACIONES DIFERENCIALES": "Ecuaciones Diferenciales",

    "FIS-01": "Vectores y Magnitudes (Física)",
    "FIS-02": "Cinemática (MRU y MRUA)",
    "FIS-03": "Leyes de Newton y Dinámica",
    "FIS-04": "Trabajo y Energía",
    "FIS-05": "Fundamentos de Electricidad (Ohm)",

    "QUIM-01": "Estructura Atómica y Tabla Periódica",
    "QUIM-02": "Enlaces Químicos",
    "QUIM-03": "Estequiometría",
    "QUIM-04": "Nomenclatura Inorgánica",
    "QUIM-05": "Soluciones y Concentración",

    "PROG-01": "Pensamiento Algorítmico",
    "PROG-02": "Variables y Tipos de Datos",
    "PROG-03": "Control de Flujo: Condicionales",
    "PROG-04": "Control de Flujo: Bucles",
    "PROG-05": "Funciones",

}


BANCO_PREGUNTAS_MAESTRO = [

    # --- ARITMETICA ---
    {
        "tema_id": "ARITMETICA",
        "pregunta": "Resuelve: 10 + 5 * 2 - 8 / 4",
        "respuesta": "18",
        "opciones": ["18", "28", "10", "22"],
        "dificultad": 1
    },
    {
        "tema_id": "ARITMETICA",
        "pregunta": "Calcula la suma de las fracciones: (1/3) + (1/6)",
        "respuesta": "1/2",
        "opciones": ["1/2", "2/9", "1/3", "5/6"],
        "dificultad": 2
    },
    {
        "tema_id": "ARITMETICA",
        "pregunta": "Si un coche recorre 120 km con 8 litros de gasolina, ¿cuántos km recorrerá con 10 litros?",
        "respuesta": "150",
        "opciones": ["150", "140", "160", "100"],
        "dificultad": 3
    },
    {
        "tema_id": "ARITMETICA",
        "pregunta": "Un producto de 800 pesos tiene un 25% de descuento. ¿Cuál es el precio final?",
        "respuesta": "600",
        "opciones": ["600", "200", "700", "500"],
        "dificultad": 4
    },
    {
        "tema_id": "ARITMETICA",
        "pregunta": "Calcula la raíz cuadrada de 144.",
        "respuesta": "12",
        "opciones": ["12", "14", "10", "16"],
        "dificultad": 5
    },

    # --- ALGEBRA BASICA ---
    {
        "tema_id": "ALGEBRA BASICA",
        "pregunta": "Simplifica la expresión: 10a - 5b - 4a + 7b",
        "respuesta": "6a+2b",
        "opciones": ["6a+2b", "14a+2b", "6a-2b", "14a-12b"],
        "dificultad": 1
    },
    {
        "tema_id": "ALGEBRA BASICA",
        "pregunta": "Despeja 'x' en la ecuación: 5x + 15 = 40",
        "respuesta": "x=5",
        "opciones": ["x=5", "x=11", "x=8", "x=3"],
        "dificultad": 2
    },
    {
        "tema_id": "ALGEBRA BASICA",
        "pregunta": "Desarrolla el producto notable: (x + 5)^2",
        "respuesta": "x^2+10x+25",
        "opciones": ["x^2+10x+25", "x^2+25", "x^2+5x+25", "x^2+10"],
        "dificultad": 3
    },
    {
        "tema_id": "ALGEBRA BASICA",
        "pregunta": "Resuelve para 'x' en el sistema: x + y = 8, x - y = 2",
        "respuesta": "x=5",
        "opciones": ["x=5", "x=3", "x=6", "x=4"],
        "dificultad": 4
    },
    {
        "tema_id": "ALGEBRA BASICA",
        "pregunta": "Encuentra las soluciones de: x² - 8x + 15 = 0 (separadas por coma)",
        "respuesta": "3,5",
        "opciones": ["3,5", "-3,-5", "1,15", "2,6"],
        "dificultad": 5
    },

    # --- GEOMETRIA ---
    {
        "tema_id": "GEOMETRIA",
        "pregunta": "La suma de los ángulos internos de cualquier triángulo es:",
        "respuesta": "180",
        "opciones": ["180", "360", "90", "270"],
        "dificultad": 1
    },
    {
        "tema_id": "GEOMETRIA",
        "pregunta": "Un triángulo rectángulo tiene catetos que miden 6 y 8. ¿Cuánto mide la hipotenusa?",
        "respuesta": "10",
        "opciones": ["10", "14", "48", "2"],
        "dificultad": 2
    },
    {
        "tema_id": "GEOMETRIA",
        "pregunta": "Calcula el área de un círculo con radio 10 (en términos de π).",
        "respuesta": "100π",
        "opciones": ["100π", "20π", "10π", "50π"],
        "dificultad": 3
    },
    {
        "tema_id": "GEOMETRIA",
        "pregunta": "Calcula el volumen de un cubo cuyo lado mide 3.",
        "respuesta": "27",
        "opciones": ["27", "9", "18", "54"],
        "dificultad": 4
    },
    {
        "tema_id": "GEOMETRIA",
        "pregunta": "Un poste de 4m proyecta una sombra de 6m. A la misma hora, un árbol proyecta una sombra de 18m. ¿Cuál es la altura del árbol?",
        "respuesta": "12",
        "opciones": ["12", "10", "24", "27"],
        "dificultad": 5
    },

     # --- TRIGONOMETRIA ---
    {
        "tema_id": "TRIGONOMETRIA",
        "pregunta": "En un triángulo rectángulo, el coseno de un ángulo es igual a:",
        "respuesta": "cateto adyacente/hipotenusa",
        "opciones": ["cateto adyacente/hipotenusa", "cateto opuesto/hipotenusa", "cateto opuesto/adyacente", "hipotenusa/adyacente"],
        "dificultad": 1
    },
    {
        "tema_id": "TRIGONOMETRIA",
        "pregunta": "¿A cuántos grados equivalen π radianes?",
        "respuesta": "180",
        "opciones": ["180", "360", "90", "270"],
        "dificultad": 2
    },
    {
        "tema_id": "TRIGONOMETRIA",
        "pregunta": "Según la identidad pitagórica fundamental, sen²(x) + cos²(x) es siempre igual a:",
        "respuesta": "1",
        "opciones": ["1", "0", "tan²(x)", "2"],
        "dificultad": 3
    },
    {
        "tema_id": "TRIGONOMETRIA",
        "pregunta": "La Ley de Senos se utiliza para resolver triángulos de tipo:",
        "respuesta": "oblicuos",
        "opciones": ["oblicuos", "rectángulos", "equiláteros", "planos"],
        "dificultad": 4
    },
    {
        "tema_id": "TRIGONOMETRIA",
        "pregunta": "La Ley de Cosenos es una generalización del Teorema de:",
        "respuesta": "pitagoras",
        "opciones": ["pitagoras", "thales", "euclides", "newton"],
        "dificultad": 5
    },

    # --- GEOMETRIA ANALITICA ---
    {
        "tema_id": "GEOMETRIA ANALITICA",
        "pregunta": "Calcula la distancia entre los puntos A(1, 2) y B(4, 6).",
        "respuesta": "5",
        "opciones": ["5", "7", "25", "1"],
        "dificultad": 1
    },
    {
        "tema_id": "GEOMETRIA ANALITICA",
        "pregunta": "¿Cuál es la pendiente de la recta que pasa por los puntos (0, 0) y (2, 8)?",
        "respuesta": "4",
        "opciones": ["4", "0.25", "8", "6"],
        "dificultad": 2
    },
    {
        "tema_id": "GEOMETRIA ANALITICA",
        "pregunta": "Escribe la ecuación de un círculo con centro en el origen y radio 9.",
        "respuesta": "x^2+y^2=81",
        "opciones": ["x^2+y^2=81", "x^2+y^2=9", "x^2+y^2=18", "x+y=9"],
        "dificultad": 3
    },
    {
        "tema_id": "GEOMETRIA ANALITICA",
        "pregunta": "Una parábola con vértice en el origen y foco en (0, 3) abre hacia:",
        "respuesta": "arriba",
        "opciones": ["arriba", "abajo", "derecha", "izquierda"],
        "dificultad": 4
    },
    {
        "tema_id": "GEOMETRIA ANALITICA",
        "pregunta": "Para la elipse x^2/25 + y^2/16 = 1, ¿cuál es la longitud del eje mayor?",
        "respuesta": "10",
        "opciones": ["10", "5", "25", "50"],
        "dificultad": 5
    },

    # --- PRECALCULO ---
    {
        "tema_id": "PRECALCULO",
        "pregunta": "Para la función f(x) = √(x-3), ¿cuál es el valor mínimo que puede tomar x?",
        "respuesta": "3",
        "opciones": ["3", "0", "-3", "9"],
        "dificultad": 1
    },
    {
        "tema_id": "PRECALCULO",
        "pregunta": "Si f(x) = x² y g(x) = x + 1, calcula f(g(2)).",
        "respuesta": "9",
        "opciones": ["9", "5", "6", "8"],
        "dificultad": 2
    },
    {
        "tema_id": "PRECALCULO",
        "pregunta": "Calcula: logaritmo en base 2 de 8.",
        "respuesta": "3",
        "opciones": ["3", "4", "8", "16"],
        "dificultad": 3
    },
    {
        "tema_id": "PRECALCULO",
        "pregunta": "Intuitivamente, ¿a qué valor se acerca la función f(x) = 5/x cuando 'x' se hace infinitamente grande?",
        "respuesta": "0",
        "opciones": ["0", "5", "infinito", "1"],
        "dificultad": 4
    },
    {
        "tema_id": "PRECALCULO",
        "pregunta": "Calcula la suma de los primeros 100 términos de la serie aritmética que empieza en 3 y tiene diferencia 4.",
        "respuesta": "20100",
        "opciones": ["20100", "400", "20000", "19900"],
        "dificultad": 5
    },

    # --- CALCULO DIFERENCIAL ---
    {
        "tema_id": "CALCULO DIFERENCIAL",
        "pregunta": "¿Cuál es el límite de f(x) = (x² - 1) / (x - 1) cuando x tiende a 1?",
        "respuesta": "2",
        "opciones": ["2", "0", "indefinido", "1"],
        "dificultad": 1
    },
    {
        "tema_id": "CALCULO DIFERENCIAL",
        "pregunta": "¿Cuál es la derivada de f(x) = x⁴ + 5x?",
        "respuesta": "4x^3+5",
        "opciones": ["4x^3+5", "4x^3", "x^3+5", "5x^4"],
        "dificultad": 2
    },
    {
        "tema_id": "CALCULO DIFERENCIAL",
        "pregunta": "Usando la regla del producto, ¿cuál es la derivada de f(x) = x * sen(x)?",
        "respuesta": "sen(x)+x*cos(x)",
        "opciones": ["sen(x)+x*cos(x)", "cos(x)", "x*cos(x)", "sen(x)+cos(x)"],
        "dificultad": 3
    },
    {
        "tema_id": "CALCULO DIFERENCIAL",
        "pregunta": "Usando la regla de la cadena, ¿cuál es la derivada de f(x) = (2x + 1)³?",
        "respuesta": "6(2x+1)^2",
        "opciones": ["6(2x+1)^2", "3(2x+1)^2", "2(2x+1)^3", "6(2x+1)"],
        "dificultad": 4
    },
    {
        "tema_id": "CALCULO DIFERENCIAL",
        "pregunta": "Encuentra el punto crítico (mínimo) de la función f(x) = x² - 4x + 1.",
        "respuesta": "x=2",
        "opciones": ["x=2", "x=4", "x=-2", "x=0"],
        "dificultad": 5
    },

    # --- CALCULO INTEGRAL  ---
    {
        "tema_id": "CALCULO INTEGRAL",
        "pregunta": "¿Cuál es la antiderivada (integral indefinida) de f(x) = 3x²?",
        "respuesta": "x^3+C",
        "opciones": ["x^3+C", "6x", "x^3", "3x^3+C"],
        "dificultad": 1
    },
    {
        "tema_id": "CALCULO INTEGRAL",
        "pregunta": "Calcula la integral definida de ∫(1) dx desde x=1 hasta x=5.",
        "respuesta": "4",
        "opciones": ["4", "5", "1", "6"],
        "dificultad": 2
    },
    {
        "tema_id": "CALCULO INTEGRAL",
        "pregunta": "Calcula el área bajo la curva f(x) = 2x desde x=0 hasta x=3.",
        "respuesta": "9",
        "opciones": ["9", "6", "18", "3"],
        "dificultad": 3
    },
    {
        "tema_id": "CALCULO INTEGRAL",
        "pregunta": "Usando sustitución, ¿cuál es la integral de ∫(2x * (x² + 1)²) dx?",
        "respuesta": "(x^2+1)^3/3+C",
        "opciones": ["(x^2+1)^3/3+C", "(x^2+1)^3+C", "2x(x^2+1)^3", "3(x^2+1)"],
        "dificultad": 4
    },
    {
        "tema_id": "CALCULO INTEGRAL",
        "pregunta": "Calcula la integral de ∫(cos(x)) dx.",
        "respuesta": "sen(x)+C",
        "opciones": ["sen(x)+C", "-sen(x)+C", "cos(x)+C", "-cos(x)"],
        "dificultad": 5
    },

    # --- VECTORES Y GEOMETRIA  ---
    {
        "tema_id": "VECTORES Y GEOMETRIA",
        "pregunta": "¿Cuál es la magnitud del vector v = (3, 4, 0)?",
        "respuesta": "5",
        "opciones": ["5", "7", "25", "12"],
        "dificultad": 1
    },
    {
        "tema_id": "VECTORES Y GEOMETRIA",
        "pregunta": "Calcula el producto punto de v=(1, 2) y w=(3, -1).",
        "respuesta": "1",
        "opciones": ["1", "5", "-1", "0"],
        "dificultad": 2
    },
    {
        "tema_id": "VECTORES Y GEOMETRIA",
        "pregunta": "Si v=(1, 2, 3), ¿cuál es el vector 2v?",
        "respuesta": "(2, 4, 6)",
        "opciones": ["(2, 4, 6)", "(1, 2, 6)", "(3, 4, 5)", "(0.5, 1, 1.5)"],
        "dificultad": 3
    },
    {
        "tema_id": "VECTORES Y GEOMETRIA",
        "pregunta": "Calcula el producto cruz i x j (vectores unitarios).",
        "respuesta": "k",
        "opciones": ["k", "-k", "0", "1"],
        "dificultad": 4
    },
    {
        "tema_id": "VECTORES Y GEOMETRIA",
        "pregunta": "Encuentra la ecuación del plano con vector normal n=(1, 1, 1) que pasa por (0, 0, 0).",
        "respuesta": "x+y+z=0",
        "opciones": ["x+y+z=0", "x=y=z", "x+y+z=1", "xyz=0"],
        "dificultad": 5
    },

    # --- ALGEBRA LINEAL  ---
    {
        "tema_id": "ALGEBRA LINEAL",
        "pregunta": "Calcula el determinante de la matriz 2x2: [[1, 2], [3, 4]].",
        "respuesta": "-2",
        "opciones": ["-2", "2", "10", "-10"],
        "dificultad": 1
    },
    {
        "tema_id": "ALGEBRA LINEAL",
        "pregunta": "Si A=[[1, 0], [0, 1]] y B=[[5, 6], [7, 8]], ¿cuál es el producto AB?",
        "respuesta": "[[5, 6], [7, 8]]",
        "opciones": ["[[5, 6], [7, 8]]", "[[1, 0], [0, 1]]", "[[0, 0], [0, 0]]", "[[6, 6], [8, 8]]"],
        "dificultad": 2
    },
    {
        "tema_id": "ALGEBRA LINEAL",
        "pregunta": "Resuelve el sistema 2x2: x + y = 3, x - y = 1. (Dar valor de x)",
        "respuesta": "2",
        "opciones": ["2", "1", "3", "1.5"],
        "dificultad": 3
    },
    {
        "tema_id": "ALGEBRA LINEAL",
        "pregunta": "¿Cuál es la transpuesta de la matriz [[1, 2], [3, 4]]?",
        "respuesta": "[[1, 3], [2, 4]]",
        "opciones": ["[[1, 3], [2, 4]]", "[[1, 2], [3, 4]]", "[[4, 3], [2, 1]]", "[[-1, -2], [-3, -4]]"],
        "dificultad": 4
    },
    {
        "tema_id": "ALGEBRA LINEAL",
        "pregunta": "¿Cuál es el 'eigenvalor' (valor propio) de la matriz diagonal [[2, 0], [0, 3]]?",
        "respuesta": "2,3",
        "opciones": ["2,3", "0,0", "1,1", "6,1"],
        "dificultad": 5
    },

    # --- CALCULO VECTORIAL  ---
    {
        "tema_id": "CALCULO VECTORIAL",
        "pregunta": "Si f(x, y) = x²y, ¿cuál es la derivada parcial respecto a x (∂f/∂x)?",
        "respuesta": "2xy",
        "opciones": ["2xy", "x^2", "y", "2x"],
        "dificultad": 1
    },
    {
        "tema_id": "CALCULO VECTORIAL",
        "pregunta": "Si f(x, y) = x²y, ¿cuál es la derivada parcial respecto a y (∂f/∂y)?",
        "respuesta": "x^2",
        "opciones": ["x^2", "2xy", "2y", "x"],
        "dificultad": 2
    },
    {
        "tema_id": "CALCULO VECTORIAL",
        "pregunta": "Calcula el gradiente (∇f) de f(x, y) = x + y².",
        "respuesta": "(1, 2y)",
        "opciones": ["(1, 2y)", "(1, 2)", "(x, 2y)", "(0, 2y)"],
        "dificultad": 3
    },
    {
        "tema_id": "CALCULO VECTORIAL",
        "pregunta": "Calcula la divergencia (∇·F) del campo F = (x, y, z).",
        "respuesta": "3",
        "opciones": ["3", "0", "1", "(1,1,1)"],
        "dificultad": 4
    },
    {
        "tema_id": "CALCULO VECTORIAL",
        "pregunta": "Calcula el rotacional (∇xF) del campo F = (x, y, z).",
        "respuesta": "(0, 0, 0)",
        "opciones": ["(0, 0, 0)", "3", "(1, 1, 1)", "(x, y, z)"],
        "dificultad": 5
    },

    # --- ECUACIONES DIFERENCIALES  ---
    {
        "tema_id": "ECUACIONES DIFERENCIALES",
        "pregunta": "¿De qué orden es la ecuación y'' + 2y' = 0?",
        "respuesta": "2",
        "opciones": ["2", "1", "0", "3"],
        "dificultad": 1
    },
    {
        "tema_id": "ECUACIONES DIFERENCIALES",
        "pregunta": "¿La ecuación y' = y² es lineal? (si/no)",
        "respuesta": "no",
        "opciones": ["no", "si"],
        "dificultad": 2
    },
    {
        "tema_id": "ECUACIONES DIFERENCIALES",
        "pregunta": "Verifica si y = e^(2x) es solución de y' - 2y = 0. (si/no)",
        "respuesta": "si",
        "opciones": ["si", "no"],
        "dificultad": 3
    },
    {
        "tema_id": "ECUACIONES DIFERENCIALES",
        "pregunta": "Resuelve la EDO separable: dy/dx = x/y.",
        "respuesta": "y^2=x^2+C",
        "opciones": ["y^2=x^2+C", "y=x+C", "y=x^2+C", "ln(y)=x"],
        "dificultad": 4
    },
    {
        "tema_id": "ECUACIONES DIFERENCIALES",
        "pregunta": "Encuentra la ecuación característica para y'' - 9y = 0.",
        "respuesta": "r^2-9=0",
        "opciones": ["r^2-9=0", "r^2+9=0", "r-9=0", "r^2-3=0"],
        "dificultad": 5
    },

    #--- FISICA 1 ---
    {
        "tema_id": "FIS-01",
        "pregunta": "¿La temperatura es una magnitud escalar o vectorial?",
        "respuesta": "escalar",
        "opciones": ["escalar", "vectorial", "nula", "variable"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-01",
        "pregunta": "¿La fuerza es una magnitud escalar o vectorial?",
        "respuesta": "vectorial",
        "opciones": ["vectorial", "escalar", "estatica", "adimensional"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-01",
        "pregunta": "Un vector Velocidad V=20m/s apunta a 45°. ¿Cuál es su componente Vx? (cos(45°)≈0.707)",
        "respuesta": "14.14",
        "opciones": ["14.14", "20", "10", "0.707"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-01",
        "pregunta": "Suma los vectores V₁=(3, 8) y V₂=(2, 2). El vector resultante es...",
        "respuesta": "(5, 10)",
        "opciones": ["(5, 10)", "(1, 6)", "(6, 16)", "(5, 6)"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-01",
        "pregunta": "La aceleración (como la de la gravedad, 'g') es una magnitud...",
        "respuesta": "vectorial",
        "opciones": ["vectorial", "escalar", "constante", "fija"],
        "dificultad": 1
    },

    #--- FISICA 2 ---
    {
        "tema_id": "FIS-02",
        "pregunta": "Un auto va a 20 m/s constantes. ¿Qué distancia recorre en 10 segundos?",
        "respuesta": "200",
        "opciones": ["200", "2", "20", "2000"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-02",
        "pregunta": "Un objeto cae desde el reposo. ¿Cuál es su velocidad después de 2 segundos? (usa g=9.8 m/s²)",
        "respuesta": "19.6",
        "opciones": ["19.6", "9.8", "4.9", "29.4"],
        "dificultad": 3
    },
    {
        "tema_id": "FIS-02",
        "pregunta": "Un auto acelera de 0 a 100 km/h en 5s. ¿Qué tipo de movimiento es?",
        "respuesta": "MRUA",
        "opciones": ["MRUA", "MRU", "Circular", "Estático"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-02",
        "pregunta": "Un proyectil es lanzado con un ángulo de 45°. ¿En qué punto de su trayectoria su velocidad vertical es cero?",
        "respuesta": "altura maxima",
        "opciones": ["altura maxima", "inicio", "final", "nunca"],
        "dificultad": 3
    },
    {
        "tema_id": "FIS-02",
        "pregunta": "Un objeto con MRUA viaja 10m en su primer segundo partiendo del reposo. ¿Cuál es su aceleración? (d=0.5*a*t²)",
        "respuesta": "20",
        "opciones": ["20", "10", "5", "9.8"],
        "dificultad": 5
    },

    #--- FISICA 3 ---
    {
        "tema_id": "FIS-03",
        "pregunta": "Si la fuerza neta es cero, ¿la aceleración es?",
        "respuesta": "0",
        "opciones": ["0", "constante", "maxima", "negativa"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-03",
        "pregunta": "La fuerza que se opone al deslizamiento entre superficies se llama...",
        "respuesta": "friccion",
        "opciones": ["friccion", "normal", "peso", "tension"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-03",
        "pregunta": "Fuerza neta de 50N sobre masa de 10kg. ¿Aceleración?",
        "respuesta": "5",
        "opciones": ["5", "500", "0.2", "10"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-03",
        "pregunta": "Si golpeas una pared con 50N, ¿con cuánta fuerza te golpea la pared?",
        "respuesta": "50",
        "opciones": ["50", "0", "100", "25"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-03",
        "pregunta": "Si cuelgas 10kg de una cuerda quieta (g=10), ¿cuál es la tensión?",
        "respuesta": "100",
        "opciones": ["100", "10", "0", "50"],
        "dificultad": 3
    },

    #--- FISICA 4 ---
    {
        "tema_id": "FIS-04",
        "pregunta": "Si levantas un objeto y lo vuelves a bajar al mismo punto, ¿el trabajo neto realizado por la gravedad es?",
        "respuesta": "0",
        "opciones": ["0", "positivo", "negativo", "infinito"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-04",
        "pregunta": "Si duplicas la velocidad de un auto, ¿cuántas veces se multiplica su energía cinética?",
        "respuesta": "4",
        "opciones": ["4", "2", "8", "16"],
        "dificultad": 3
    },
    {
        "tema_id": "FIS-04",
        "pregunta": "Empujas una caja con 50N una distancia de 10m. La fricción es 20N. ¿Cuál es el trabajo 'neto' sobre la caja?",
        "respuesta": "300",
        "opciones": ["300", "500", "200", "700"],
        "dificultad": 3
    },
    {
        "tema_id": "FIS-04",
        "pregunta": "Un objeto de 4kg se mueve a 5 m/s. ¿Cuál es su energía cinética?",
        "respuesta": "50",
        "opciones": ["50", "20", "100", "10"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-04",
        "pregunta": "¿Cuánta energía potencial (en J) gana un elevador de 100kg al subir 20m? (usa g=10 m/s²)",
        "respuesta": "20000",
        "opciones": ["20000", "2000", "200", "10000"],
        "dificultad": 2
    },

    # --- FIS-05 ---
    {
        "tema_id": "FIS-05",
        "pregunta": "Si la resistencia de un circuito aumenta mientras el voltaje se mantiene constante, la corriente...",
        "respuesta": "disminuye",
        "opciones": ["disminuye", "aumenta", "se mantiene igual", "oscila"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-05",
        "pregunta": "¿Cómo se deben conectar las baterías para sumar su voltaje?",
        "respuesta": "en serie",
        "opciones": ["en serie", "en paralelo", "mixto", "invertidas"],
        "dificultad": 2
    },
    {
        "tema_id": "FIS-05",
        "pregunta": "Material que permite el flujo libre de electrones se llama...",
        "respuesta": "conductor",
        "opciones": ["conductor", "aislante", "semiconductor", "resistencia"],
        "dificultad": 1
    },
    {
        "tema_id": "FIS-05",
        "pregunta": "La Ley de Joule establece que el calor generado en una resistencia es proporcional al cuadrado de la...",
        "respuesta": "corriente",
        "opciones": ["corriente", "voltaje", "longitud", "masa"],
        "dificultad": 3
    },
    {
        "tema_id": "FIS-05",
        "pregunta": "Para medir el voltaje en un componente, el voltímetro se conecta en...",
        "respuesta": "paralelo",
        "opciones": ["paralelo", "serie", "corto", "abierto"],
        "dificultad": 3
    },

    # --- QUIM 01 ---
    {
        "tema_id": "QUIM-01",
        "pregunta": "¿Cuál es la partícula subatómica con masa despreciable (casi cero)?",
        "respuesta": "electron",
        "opciones": ["electron", "proton", "neutron", "nucleo"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-01",
        "pregunta": "Las filas horizontales de la tabla periódica se llaman...",
        "respuesta": "periodos",
        "opciones": ["periodos", "grupos", "familias", "bloques"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-01",
        "pregunta": "¿Cuántos electrones caben como máximo en un orbital tipo 'p'?",
        "respuesta": "6",
        "opciones": ["6", "2", "10", "14"],
        "dificultad": 3
    },
    {
        "tema_id": "QUIM-01",
        "pregunta": "El elemento más electronegativo de la tabla periódica es el...",
        "respuesta": "fluor",
        "opciones": ["fluor", "francio", "oxigeno", "cloro"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-01",
        "pregunta": "Cuando un átomo neutro pierde electrones, se convierte en un...",
        "respuesta": "cation",
        "opciones": ["cation", "anion", "isotopo", "metal"],
        "dificultad": 2
    },

    # --- QUIM-02 ---
    {
        "tema_id": "QUIM-02",
        "pregunta": "La 'Regla del Octeto' establece que los átomos tienden a ganar, perder o compartir electrones para tener... electrones de valencia.",
        "respuesta": "8",
        "opciones": ["8", "2", "10", "4"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-02",
        "pregunta": "¿Qué tipo de enlace se forma por la atracción electrostática entre iones de carga opuesta?",
        "respuesta": "ionico",
        "opciones": ["ionico", "covalente", "metalico", "intermolecular"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-02",
        "pregunta": "El modelo del 'mar de electrones' explica las propiedades de los...",
        "respuesta": "metales",
        "opciones": ["metales", "sales", "gases", "plasticos"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-02",
        "pregunta": "Una molécula con geometría 'Tetraédrica' (ej. Metano) tiene un ángulo de enlace aproximado de...",
        "respuesta": "109.5",
        "opciones": ["109.5", "90", "180", "120"],
        "dificultad": 3
    },
    {
        "tema_id": "QUIM-02",
        "pregunta": "¿Qué fuerza intermolecular es responsable del alto punto de ebullición del agua?",
        "respuesta": "puentes de hidrogeno",
        "opciones": ["puentes de hidrogeno", "van der waals", "enlace ionico", "fuerza nuclear"],
        "dificultad": 2
    },

    # --- QUIM 03 ---
    {
        "tema_id": "QUIM-03",
        "pregunta": "En la reacción 2H₂ + O₂ -> 2H₂O, la relación molar entre Hidrógeno y Oxígeno es...",
        "respuesta": "2 a 1",
        "opciones": ["2 a 1", "1 a 1", "1 a 2", "2 a 2"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-03",
        "pregunta": "Si el rendimiento teórico de una reacción es 100g y el real es 80g, el porcentaje de rendimiento es...",
        "respuesta": "80%",
        "opciones": ["80%", "125%", "20%", "100%"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-03",
        "pregunta": "La masa de 1 mol de átomos de Carbono-12 es exactamente...",
        "respuesta": "12 gramos",
        "opciones": ["12 gramos", "1 gramo", "6 gramos", "24 gramos"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-03",
        "pregunta": "¿Qué ley establece que la masa total de los reactivos es igual a la masa total de los productos?",
        "respuesta": "conservacion de la masa",
        "opciones": ["conservacion de la masa", "ley de los gases", "ley de avogadro", "ley de la inercia"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-03",
        "pregunta": "Para convertir de gramos a moles, se divide la masa entre la...",
        "respuesta": "masa molar",
        "opciones": ["masa molar", "numero de avogadro", "densidad", "volumen"],
        "dificultad": 2
    },

    # --- QUIM 04 ---
    {
        "tema_id": "QUIM-04",
        "pregunta": "En la nomenclatura tradicional, el sufijo '-ico' indica que el elemento usa su valencia...",
        "respuesta": "mayor",
        "opciones": ["mayor", "menor", "unica", "negativa"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-04",
        "pregunta": "¿Qué grupo funcional caracteriza a los Hidróxidos?",
        "respuesta": "OH",
        "opciones": ["OH", "H", "O", "COOH"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-04",
        "pregunta": "El compuesto CO₂ se nombra sistemáticamente como...",
        "respuesta": "dioxido de carbono",
        "opciones": ["dioxido de carbono", "oxido carbonico", "carbonato", "monoxido de carbono"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-04",
        "pregunta": "Los ácidos siempre contienen el elemento... al principio de su fórmula.",
        "respuesta": "hidrogeno",
        "opciones": ["hidrogeno", "oxigeno", "nitrogeno", "cloro"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-04",
        "pregunta": "La sal común (NaCl) pertenece a la familia de las...",
        "respuesta": "sales binarias",
        "opciones": ["sales binarias", "oxisales", "oxidos", "hidroxidos"],
        "dificultad": 2
    },

    # --- QUIM 05 ---
    {
        "tema_id": "QUIM-05",
        "pregunta": "Si aumentas la temperatura de un líquido, la solubilidad de los gases disueltos (como el CO₂)...",
        "respuesta": "disminuye",
        "opciones": ["disminuye", "aumenta", "se mantiene igual", "se vuelve cero"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-05",
        "pregunta": "Al diluir una solución agregando más solvente, la cantidad total de moles de soluto...",
        "respuesta": "permanece constante",
        "opciones": ["permanece constante", "aumenta", "disminuye", "se evapora"],
        "dificultad": 2
    },
    {
        "tema_id": "QUIM-05",
        "pregunta": "Una solución que contiene una pequeña cantidad de soluto en comparación con el solvente se llama...",
        "respuesta": "diluida",
        "opciones": ["diluida", "concentrada", "saturada", "sobresaturada"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-05",
        "pregunta": "Dos líquidos que no se pueden mezclar (como el agua y el aceite) se dicen que son...",
        "respuesta": "inmiscibles",
        "opciones": ["inmiscibles", "miscibles", "solubles", "saturados"],
        "dificultad": 1
    },
    {
        "tema_id": "QUIM-05",
        "pregunta": "¿Cuántos miligramos de soluto hay en 1 Litro de una solución de 1 ppm?",
        "respuesta": "1 mg",
        "opciones": ["1 mg", "1 g", "1 microgramo", "1 kg"],
        "dificultad": 3
    },

    # --- PROG 01 ---
    {
        "tema_id": "PROG-01",
        "pregunta": "En un diagrama de flujo, ¿qué figura geométrica se utiliza para representar una entrada o salida de datos (Input/Output)?",
        "respuesta": "paralelogramo",
        "opciones": ["paralelogramo", "rectangulo", "rombo", "ovalo"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-01",
        "pregunta": "Un algoritmo debe ser 'finito', lo que significa que...",
        "respuesta": "debe terminar en algun momento",
        "opciones": ["debe terminar en algun momento", "debe ser corto", "debe usar pocos recursos", "debe ser matematico"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-01",
        "pregunta": "El proceso de encontrar y corregir errores en un algoritmo se conoce como...",
        "respuesta": "depuracion",
        "opciones": ["depuracion", "compilacion", "ejecucion", "abstraccion"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-01",
        "pregunta": "¿Cuál es el propósito principal del pseudocódigo?",
        "respuesta": "escribir la logica sin sintaxis estricta",
        "opciones": ["escribir la logica sin sintaxis estricta", "compilar el programa", "dibujar el proceso", "optimizar la memoria"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-01",
        "pregunta": "Si un algoritmo tiene pasos que se ejecutan uno tras otro, se dice que sigue una estructura...",
        "respuesta": "secuencial",
        "opciones": ["secuencial", "condicional", "iterativa", "paralela"],
        "dificultad": 1
    },

    # --- PROG 02 ---
    {
        "tema_id": "PROG-02",
        "pregunta": "¿Cuál de los siguientes es un nombre de variable inválido en la mayoría de lenguajes?",
        "respuesta": "2nombre",
        "opciones": ["2nombre", "nombre2", "_nombre", "nombre_usuario"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-02",
        "pregunta": "¿Qué función se utiliza comúnmente para saber el tipo de dato de una variable?",
        "respuesta": "type()",
        "opciones": ["type()", "typeof()", "print()", "input()"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-02",
        "pregunta": "El operador '%' (módulo) devuelve...",
        "respuesta": "el residuo de la division",
        "opciones": ["el residuo de la division", "el porcentaje", "la division exacta", "la potencia"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-02",
        "pregunta": "En Python, el símbolo '#' se utiliza para...",
        "respuesta": "escribir comentarios",
        "opciones": ["escribir comentarios", "declarar variables", "importar librerias", "cerrar el programa"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-02",
        "pregunta": "¿Cuál es el resultado de la operación lógica `True AND False`?",
        "respuesta": "False",
        "opciones": ["False", "True", "Error", "None"],
        "dificultad": 2
    },

    # --- PROG 03 ---
    {
        "tema_id": "PROG-03",
        "pregunta": "En Python, ¿qué define qué líneas de código pertenecen a un bloque, función, clase, etc...?",
        "respuesta": "indentacion",
        "opciones": ["indentacion", "llaves", "parentesis", "punto y coma"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-03",
        "pregunta": "Si tienes múltiples condiciones `elif`, ¿cuántos bloques se ejecutan si varias condiciones son verdaderas?",
        "respuesta": "solo el primero",
        "opciones": ["solo el primero", "todos los verdaderos", "el ultimo", "ninguno"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-03",
        "pregunta": "La estructura `if x > 0: ... else: ...` cubre todos los casos posibles de x? (asumiendo x número)",
        "respuesta": "si",
        "opciones": ["si", "no", "solo positivos", "solo enteros"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-03",
        "pregunta": "¿Qué operador lógico devuelve True solo si AMBAS condiciones son verdaderas?",
        "respuesta": "AND",
        "opciones": ["AND", "OR", "NOT", "XOR"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-03",
        "pregunta": "El 'anidamiento' (nesting) se refiere a...",
        "respuesta": "poner un if dentro de otro",
        "opciones": ["poner un if dentro de otro", "borrar un if", "conectar variables", "hacer bucles"],
        "dificultad": 2
    },

    # --- PROG 04 ---
    {
        "tema_id": "PROG-04",
        "pregunta": "En Python, la función `range(5)` genera los números...",
        "respuesta": "0, 1, 2, 3, 4",
        "opciones": ["0, 1, 2, 3, 4", "1, 2, 3, 4, 5", "1, 2, 3, 4", "0, 1, 2, 3, 4, 5"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-04",
        "pregunta": "Si un bucle `while` tiene una condición inicial que es Falsa, el código se ejecuta...",
        "respuesta": "0 veces",
        "opciones": ["0 veces", "1 vez", "infinitas veces", "genera error"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-04",
        "pregunta": "¿Qué sentencia se usa para saltar el resto de la iteración actual y pasar a la siguiente?",
        "respuesta": "continue",
        "opciones": ["continue", "break", "pass", "return"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-04",
        "pregunta": "Una variable que se usa para sumar valores acumulados dentro de un bucle se llama...",
        "respuesta": "acumulador",
        "opciones": ["acumulador", "contador", "bandera", "iterador"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-04",
        "pregunta": "Si tienes un bucle que corre N veces, y dentro otro que corre M veces, la complejidad total es...",
        "respuesta": "N * M",
        "opciones": ["N * M", "N + M", "N / M", "N^M"],
        "dificultad": 3
    },

    # --- PROG 05 ---
    {
        "tema_id": "PROG-05",
        "pregunta": "Si una función en Python no tiene un `return` explícito, ¿qué valor devuelve por defecto?",
        "respuesta": "None",
        "opciones": ["None", "0", "False", "Error"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-05",
        "pregunta": "Para usar una función matemática como la raíz cuadrada `sqrt()`, primero debes hacer...",
        "respuesta": "import math",
        "opciones": ["import math", "def math", "print math", "install math"],
        "dificultad": 1
    },
    {
        "tema_id": "PROG-05",
        "pregunta": "Los valores que se envían a la función cuando se la *llama* se denominan...",
        "respuesta": "argumentos",
        "opciones": ["argumentos", "parametros", "variables", "retornos"],
        "dificultad": 2
    },
    {
        "tema_id": "PROG-05",
        "pregunta": "Para modificar una variable global dentro de una función local, se usa la palabra clave...",
        "respuesta": "global",
        "opciones": ["global", "local", "extern", "public"],
        "dificultad": 3
    },
    {
        "tema_id": "PROG-05",
        "pregunta": "¿Qué principio de programación promueve el uso de funciones para evitar código duplicado?",
        "respuesta": "DRY",
        "opciones": ["DRY", "KISS", "SOLID", "YAGNI"],
        "dificultad": 2
    },
]

CONTENIDO_MAESTRO = {
    "ARITMETICA": {
        "nombre_completo": "Aritmética: El Fundamento del Cálculo",
        "prerequisitos": [],
        "quiz": [
            {
                "pregunta": "Calcula el Mínimo Común Múltiplo de 12 y 15.",
                "respuesta": "60",
                "opciones": ["60", "180", "30", "3"]
            },
            {
                "pregunta": "Usando PEMDAS, calcula: (5 + 3) * 8 / 2",
                "respuesta": "32",
                "opciones": ["32", "23", "20", "64"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Números Enteros y la Recta Numérica",
                "definicion": "Los 'Números Enteros' (Z) son los números completos (sin decimales) positivos, negativos y el cero. La 'Recta Numérica' es la visualización de estos números. El '0' es el origen. Esta recta es fundamental para entender conceptos como posición, deuda, o niveles bajo/sobre el mar (topografía), donde el signo es tan importante como la magnitud.",
                "diagrama": "", # 🖼️ INICIALIZADO/MANTENIDO
                "ejemplo_resuelto": "Ejemplo: Comparar -5 y 2.\n1. Ubicar -5 en la recta: 5 unidades a la izquierda del 0.\n2. Ubicar 2 en la recta: 2 unidades a la derecha del 0.\n3. Regla: El número más a la derecha es el mayor. Por lo tanto, 2 > -5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué número es mayor: -15 o -3? (Escribe solo el número)",
                        "respuesta_correcta": "-3",
                        "opciones": ["-3", "-15", "-12", "12"]
                    },
                    "similares": [
                        {"pregunta": "¿Qué número es menor: -1 o 0? (Escribe solo el número)", "respuesta_correcta": "-1", "opciones": ["-1", "0", "1", "-2"]},
                        {"pregunta": "Ordena de menor a mayor: 0, -5, 3, -1 (separado por comas, sin espacios, ej: -1,0,3)", "respuesta_correcta": "-5,-1,0,3", "opciones": ["-5,-1,0,3", "-1,0,3,-5", "0,-1,-5,3", "-5,3,-1,0"]},
                        {"pregunta": "¿Cuántos enteros hay entre -2 y 3 (sin incluirlos)? (Escribe solo el número)", "respuesta_correcta": "4", "opciones": ["4", "5", "3", "6"]},
                        {"pregunta": "Si estás en el -3 en la recta y te mueves 5 unidades a la derecha, ¿a qué número llegas? (Solo el número)", "respuesta_correcta": "2", "opciones": ["2", "-2", "-8", "8"]},
                        {"pregunta": "Si estás en el 2 en la recta y te mueves 6 unidades a la izquierda, ¿a qué número llegas? (Solo el número)", "respuesta_correcta": "-4", "opciones": ["-4", "4", "-8", "8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En programación, los 'Enteros' (int) se usan como contadores y en la lógica de 'bytes'. El tipo 'unsigned int' no acepta negativos.", "consecuencia_de_error": "Un error de signo puede causar un 'overflow', donde un valor negativo (ej. -1) se lee como un valor positivo gigantesco (ej. 65535), rompiendo toda la lógica del programa."},
                    "quimica": {"uso": "Para definir la 'carga' de un ion. Un átomo que pierde electrones tiene carga positiva (Catión, ej. Na⁺¹).", "consecuencia_de_error": "No entender los enteros negativos impide comprender cómo se forman los enlaces iónicos (sales)."},
                    "civil": {"uso": "Para definir niveles topográficos. El Nivel del Mar es 0. Una excavación está a -3 metros.", "consecuencia_de_error": "Un error de signo en un plano de cimentación puede causar que se excave a una profundidad incorrecta, fallando en alcanzar el suelo firme."},
                    "mecanica": {"uso": "Medición de 'temperatura' en grados Celsius o Fahrenheit, que puede ser negativa.", "consecuencia_de_error": "Un sistema de control que no puede procesar -10°C (lee 0) fallará en activar un sistema de calefacción, causando que un fluido se congele."},
                    "mecatronica": {"uso": "Dirección de motores (positivo=adelante, negativo=reversa).", "consecuencia_de_error": "Un error de signo en el código de control puede hacer que un robot se mueva violentamente en la dirección opuesta a la esperada."},
                    "aeronautica": {"uso": "Medición de velocidad vertical (positiva=ascenso, negativa=descenso).", "consecuencia_de_error": "Un error de signo en el altímetro haría que el piloto automático crea que está subiendo cuando está bajando."},
                    "electrica": {"uso": "Definición de 'polaridad' (+ y -) en Corriente Directa (DC).", "consecuencia_de_error": "Conectar una fuente de poder (ej. una batería) con la polaridad invertida (+ donde va -) quema la mayoría de los componentes electrónicos."}
                }
            },
            {
                "subtema_titulo": "2. Suma y Resta de Números Enteros",
                "definicion": "La suma y resta de números enteros sigue dos reglas: 1. 'Signos iguales se suman' (y mantienen el signo). 2. 'Signos diferentes se restan' (y se conserva el signo del número con mayor valor absoluto). Restar un negativo es lo mismo que sumar (ej. 5 - (-3) = 5 + 3).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: -5 - (-8) + 3 - 10\n1. Regla de resta: -(-8) se convierte en +8.\n2. Expresión: -5 + 8 + 3 - 10\n3. Agrupar positivos (signos iguales se suman): +8 + 3 = +11\n4. Agrupar negativos (signos iguales se suman): -5 - 10 = -15\n5. Expresión: 11 - 15\n6. Signos diferentes se restan (15 - 11 = 4) y se conserva el signo del mayor (-15).\n7. Resultado: -4",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve: -7 - 10 + 20 (Solo el número)",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "-3", "-37", "37"]
                    },
                    "similares": [
                        {"pregunta": "Calcula: 15 - (-5) + 3 - 20 (Solo el número)", "respuesta_correcta": "3", "opciones": ["3", "13", "-7", "43"]},
                        {"pregunta": "Resuelve: -8 + 12 - 3 (Solo el número)", "respuesta_correcta": "1", "opciones": ["1", "-1", "23", "-23"]},
                        {"pregunta": "Calcula: 50 - 100 + 25 (Solo el número)", "respuesta_correcta": "-25", "opciones": ["-25", "25", "-75", "175"]},
                        {"pregunta": "Resuelve: 10 - (-5) - 2 (Solo el número)", "respuesta_correcta": "13", "opciones": ["13", "3", "7", "-7"]},
                        {"pregunta": "Calcula: -12 - 5 + 7 (Solo el número)", "respuesta_correcta": "-10", "opciones": ["-10", "-24", "0", "24"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En contabilidad de software, para calcular saldos (Ingresos - Egresos).", "consecuencia_de_error": "Un error al restar un negativo (una devolución) puede llevar a un saldo incorrecto en un estado de cuenta."},
                    "quimica": {"uso": "Cálculo de la 'carga neta' de un ion. Un átomo con 17 Protones (+) y 18 Electrones (-) tiene una carga de 17 - 18 = -1.", "consecuencia_de_error": "Calcular mal la carga de un ion impide entender cómo se enlaza con otros."},
                    "civil": {"uso": "Cálculo del 'balance de fuerzas' (Estática). Si una viga recibe 50N (abajo) y 80N (arriba), la fuerza neta es -50 + 80 = +30N.", "consecuencia_de_error": "Un error en la suma de fuerzas (signos) significa que el cálculo de equilibrio (ΣF=0) fallará y la estructura no será segura."},
                    "mecanica": {"uso": "Medición de 'cambio de temperatura' (ΔT = T_final - T_inicial).", "consecuencia_de_error": "Un mal cálculo de ΔT (ej. 20 - (-10) = 30) subestimará el esfuerzo térmico en una pieza."},
                    "mecatronica": {"uso": "Cálculo del 'error' en control. Error = (Posición Deseada) - (Posición Actual). Si el robot quiere ir a 10 y está en 15, el error es 10 - 15 = -5.", "consecuencia_de_error": "Un error de signo hará que el controlador mueva el robot en la dirección opuesta, alejándolo del objetivo."},
                    "aeronautica": {"uso": "Cálculo de la 'presión diferencial' (Presión_adentro - Presión_afuera).", "consecuencia_de_error": "Permite calcular la fuerza neta sobre el fuselaje. Un error de signo subestimaría el estrés que soporta el avión."},
                    "electrica": {"uso": "Ley de Voltaje de Kirchhoff. La suma de voltajes (positivos y negativos) en una malla cerrada debe ser cero.", "consecuencia_de_error": "Un error al sumar los signos de los voltajes (caídas o subidas) hará imposible analizar un circuito en serie."}
                }
            },
            {
                "subtema_titulo": "3. Multiplicación y División de Números Enteros",
                "definicion": "La 'Regla de los Signos' para multiplicación y división es fundamental: [Signos Iguales = Positivo]. [Signos Diferentes = Negativo].",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: 4 * (-3) = -12  (Signos Diferentes -> Negativo)\nEjemplo: (-10) / (-2) = 5   (Signos Iguales -> Positivo)\nEjemplo: (-2) * (-3) * (-4)\n1. (-2) * (-3) = +6\n2. (+6) * (-4) = -24",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve: (-5) * (-4) * (-1) (Solo el número)",
                        "respuesta_correcta": "-20",
                        "opciones": ["-20", "20", "-9", "21"]
                    },
                    "similares": [
                        {"pregunta": "Calcula: 15 / (-3) (Solo el número)", "respuesta_correcta": "-5", "opciones": ["-5", "5", "-3", "3"]},
                        {"pregunta": "Resuelve: -7 * (3) (Solo el número)", "respuesta_correcta": "-21", "opciones": ["-21", "21", "-10", "-4"]},
                        {"pregunta": "Calcula: (-4) * (5) (Solo el número)", "respuesta_correcta": "-20", "opciones": ["-20", "20", "-9", "1"]},
                        {"pregunta": "Resuelve: 100 / (-5) (Solo el número)", "respuesta_correcta": "-20", "opciones": ["-20", "20", "-500", "95"]},
                        {"pregunta": "Calcula: (-12) / (-6) (Solo el número)", "respuesta_correcta": "2", "opciones": ["2", "-2", "0.5", "-0.5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En lógica booleana, a veces se usa 1 (True) y -1 (False) para multiplicaciones lógicas.", "consecuencia_de_error": "Un error de signo en una multiplicación lógica puede invertir una decisión (ej. aprobar en lugar de denegar)."},
                    "quimica": {"uso": "En termodinámica, al calcular Trabajo (W = -PΔV). Si el volumen se expande (ΔV positivo), el trabajo es negativo (el sistema hace trabajo).", "consecuencia_de_error": "Un error de signo aquí significa confundir el trabajo hecho *por* el sistema con el trabajo hecho *sobre* el sistema."},
                    "civil": {"uso": "Cálculo de 'Momentos' (Torque). Momento = Fuerza * Distancia. Una fuerza negativa (hacia abajo) a una distancia positiva (derecha) crea un momento negativo (giro horario).", "consecuencia_de_error": "Un error de signo en un momento puede hacer que el análisis de equilibrio de un puente falle, subestimando la torsión."},
                    "mecanica": {"uso": "Cálculo de Potencia = Fuerza * Velocidad. Si la fuerza (fricción) es negativa (opuesta al movimiento), la potencia es negativa (pérdida de energía).", "consecuencia_de_error": "Un error de signo llevaría a un balance de energía incorrecto."},
                    "mecatronica": {"uso": "En control, la 'ganancia' (K) de un controlador puede ser negativa (control inverso).", "consecuencia_de_error": "Olvidar un signo negativo en la ganancia de un controlador hará que el sistema sea 'inestable' y oscile sin control."},
                    "aeronautica": {"uso": "Cálculo de 'estabilidad estática'. Si el momento (giro) es negativo cuando el ángulo de ataque (perturbación) es positivo, el avión es estable.", "consecuencia_de_error": "Un error de signo aquí es la diferencia entre un avión estable que se autocorrige y uno inestable que se estrella."},
                    "electrica": {"uso": "En AC, al multiplicar fasores (vectores). El ángulo resultante depende de la multiplicación de los signos.", "consecuencia_de_error": "Un error de signo puede dar un ángulo de fase incorrecto, afectando el cálculo del factor de potencia."}
                }
            },
            {
                "subtema_titulo": "4. Jerarquía de Operaciones (PEMDAS)",
                "definicion": "Ahora que dominamos las operaciones con signos, podemos establecer el orden. PEMDAS garantiza que una ecuación tenga una sola respuesta correcta. El orden es: 1º Paréntesis, 2º Exponentes, 3º Multiplicación y División (de izquierda a derecha), 4º Adición y Sustracción (de izquierda a derecha).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: 30 - 10 / 5 * 2 + (6 - 1)\n1. Paréntesis (P): (6 - 1) = 5\n2. Expresión ahora es: 30 - 10 / 5 * 2 + 5\n3. Multiplicación/División (M/D): Se resuelve de izquierda a derecha.\n   - Primero la División (aparece antes): 10 / 5 = 2\n   - Expresión ahora es: 30 - 2 * 2 + 5\n   - Sigue la Multiplicación: 2 * 2 = 4\n5. Expresión ahora es: 30 - 4 + 5\n6. Adición/Sustracción (A/S): Se resuelve de izquierda a derecha.\n   - Primero la Sustracción: 30 - 4 = 26\n   - Expresión ahora es: 26 + 5\n   - Luego la Adición: 26 + 5 = 31\n7. Resultado: 31",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Usando PEMDAS, resuelve: 15 + 6 / 3 * 2 - 1",
                        "respuesta_correcta": "18",
                        "opciones": ["18", "13", "16", "20"]
                    },
                    "similares": [
                        {"pregunta": "Usando PEMDAS, resuelve: 25 - 5 * 3 + 2", "respuesta_correcta": "12", "opciones": ["12", "62", "22", "8"]},
                        {"pregunta": "Usando PEMDAS, calcula: 8 * 2 / 4 + 10", "respuesta_correcta": "14", "opciones": ["14", "4", "16", "12"]},
                        {"pregunta": "Usando PEMDAS, resuelve: (10 + 2) * 5 / 6", "respuesta_correcta": "10", "opciones": ["10", "1", "60", "11"]},
                        {"pregunta": "Usando PEMDAS, resuelve: 4^2 - 5 * 2 + 3", "respuesta_correcta": "9", "opciones": ["9", "25", "19", "5"]},
                        {"pregunta": "Usando PEMDAS, calcula: 20 / (2 * 5) + 3", "respuesta_correcta": "5", "opciones": ["5", "13", "50", "2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Es la base de cómo los lenguajes de programación (Python, Java, C++) evalúan cualquier fórmula matemática.", "consecuencia_de_error": "Un bug en la jerarquía (ej. no poner paréntesis) es un bug crítico que puede causar desde cálculos financieros incorrectos hasta fallos en software de control."},
                    "quimica": {"uso": "Para calcular resultados de fórmulas complejas en hojas de cálculo (Excel, Sheets) que modelan reacciones.", "consecuencia_de_error": "Una fórmula mal escrita en Excel puede llevar a una interpretación errónea de los datos de un experimento."},
                    "civil": {"uso": "El software de análisis estructural (SAP2000, STAAD) depende de este orden para resolver las ecuaciones de fuerzas y momentos.", "consecuencia_de_error": "Un cálculo incorrecto de cargas (debido a una mala fórmula) podría llevar a un diseño que subestima las cargas reales, resultando en una estructura insegura."},
                    "mecanica": {"uso": "En software de simulación (FEA), las ecuaciones de estrés (ej. Von Mises) deben seguir este orden estricto.", "consecuencia_de_error": "Una evaluación incorrecta podría indicar que una pieza es segura cuando en realidad está al borde de la falla."},
                    "mecatronica": {"uso": "Para programar la secuencia exacta de operaciones en un controlador (PLC o microcontrolador).", "consecuencia_de_error": "Un error en la jerarquía puede hacer que un brazo robótico active un motor *antes* de abrir una pinza, destruyendo la pieza."},
                    "aeronautica": {"uso": "En las computadoras de vuelo (FADEC) para evaluar en tiempo real las ecuaciones de empuje y consumo de combustible.", "consecuencia_de_error": "Un error de evaluación podría llevar a un cálculo incorrecto del empuje del motor, resultando en una pérdida de rendimiento crítico."},
                    "electrica": {"uso": "Para calcular la impedancia total en circuitos de Corriente Alterna (AC) que combinan sumas (serie) y divisiones (paralelo).", "consecuencia_de_error": "Una jerarquía incorrecta en el cálculo de la impedancia total puede llevar a un diseño de filtro que no funcione."}
                }
            },
            {
                "subtema_titulo": "5. Potencias y Raíces Cuadradas",
                "definicion": "Las potencias (exponentes) representan multiplicación repetida (base elevado a un exponente). Las raíces son la operación inversa (¿qué número, multiplicado por sí mismo N veces, da este resultado?). Son la base de las fórmulas de área, volumen y energía.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Resuelve 4³ + √81.\n1. Potencia (E de PEMDAS): 4³ = 4 * 4 * 4 = 64\n2. Raíz: √81 = 9 (porque 9 * 9 = 81)\n3. Suma final: 64 + 9 = 73.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve: 3⁴ - √25 (Solo el número)",
                        "respuesta_correcta": "76",
                        "opciones": ["76", "7", "17", "86"]
                    },
                    "similares": [
                        {"pregunta": "Resuelve: 5² + √100 (Solo el número)", "respuesta_correcta": "35", "opciones": ["35", "15", "20", "125"]},
                        {"pregunta": "Calcula el resultado de 2⁵ (Solo el número)", "respuesta_correcta": "32", "opciones": ["32", "10", "25", "64"]},
                        {"pregunta": "Resuelve: 10² - √49 (Solo el número)", "respuesta_correcta": "93", "opciones": ["93", "97", "3", "51"]},
                        {"pregunta": "Calcula: √169 + 1 (Solo el número)", "respuesta_correcta": "14", "opciones": ["14", "13", "12", "85"]},
                        {"pregunta": "Resuelve: 2³ + 3² (Solo el número)", "respuesta_correcta": "17", "opciones": ["17", "12", "15", "36"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para entender la complejidad de algoritmos (O(n²)) y calcular espacios de direcciones en redes (2ⁿ).", "consecuencia_de_error": "Elegir un algoritmo con complejidad de potencia elevada (cuadrática, cúbica) puede hacer que un programa sea inutilizablemente lento con muchos datos."},
                    "quimica": {"uso": "En el cálculo del pH, que es una escala logarítmica (la inversa de la potencia de 10).", "consecuencia_de_error": "Un error de 1 en pH (log) significa un cambio de 10x en acidez (potencia), la diferencia entre una solución neutra y una corrosiva."},
                    "civil": {"uso": "En mecánica de fluidos, la energía cinética depende de la velocidad al cuadrado (v²), crucial para diseñar tuberías.", "consecuencia_de_error": "Un mal cálculo puede llevar a dimensionar incorrectamente una tubería, causando que reviente por presión."},
                    "mecanica": {"uso": "Para calcular el momento de inercia de objetos en rotación (que incluye el radio al cuadrado, r²).", "consecuencia_de_error": "Un momento de inercia mal calculado puede causar vibraciones peligrosas o fallas estructurales a altas velocidades."},
                    "mecatronica": {"uso": "En leyes de control, la respuesta del sistema a menudo involucra términos cuadráticos (potencias).", "consecuencia_de_error": "Un error en la potencia de una ecuación de control puede hacer que un sistema (como un dron) sea completamente inestable y oscile sin control."},
                    "aeronautica": {"uso": "La fuerza de sustentación de un ala es proporcional a la velocidad al cuadrado (L ∝ v²).", "consecuencia_de_error": "Un error en este cálculo es fatal. Si duplicas la velocidad, la sustentación se cuadruplica. Confundir esto lleva a un control erróneo del avión."},
                    "electrica": {"uso": "La potencia eléctrica disipada en una resistencia se calcula como P = I²R o P = V²/R.", "consecuencia_de_error": "Un error en el exponente subestimará drásticamente el calor generado, pudiendo derretir el aislante del cable e iniciar un incendio."}
                }
            },
            {
                "subtema_titulo": "6. Fracciones: Multiplicación y División",
                "definicion": "Multiplicación: Es la operación más simple. Se multiplican numeradores entre sí y denominadores entre sí (directo). División: Es una multiplicación 'invertida'. Se invierte la segunda fracción (el divisor) y se multiplica.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: (2/3) / (4/5)\n1. Es una división. Invertir la segunda fracción (4/5) a (5/4).\n2. Convertir a multiplicación: (2/3) * (5/4)\n3. Multiplicar numeradores: 2 * 5 = 10\n4. Multiplicar denominadores: 3 * 4 = 12\n5. Resultado: 10/12. Simplificar (dividir ambos entre 2) = 5/6",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula y simplifica: (3/5) * (10/9)",
                        "respuesta_correcta": "2/3",
                        "opciones": ["2/3", "30/45", "13/14", "1/3"]
                    },
                    "similares": [
                        {"pregunta": "Calcula y simplifica: (1/2) * (4/5)", "respuesta_correcta": "2/5", "opciones": ["2/5", "4/10", "5/7", "1/2"]},
                        {"pregunta": "Calcula y simplifica: (1/4) / (2/3)", "respuesta_correcta": "3/8", "opciones": ["3/8", "2/12", "1/6", "8/3"]},
                        {"pregunta": "Calcula y simplifica: (6/7) * (1/3)", "respuesta_correcta": "2/7", "opciones": ["2/7", "6/21", "3/7", "7/10"]},
                        {"pregunta": "Calcula y simplifica: (5/6) / (1/3)", "respuesta_correcta": "5/2", "opciones": ["5/2", "5/18", "2/5", "3/6"]},
                        {"pregunta": "Calcula y simplifica: (1/3) * (6/7)", "respuesta_correcta": "2/7", "opciones": ["2/7", "6/21", "1/7", "7/10"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de probabilidades compuestas (eventos independientes). P(A y B) = P(A) * P(B).", "consecuencia_de_error": "Un mal cálculo de la probabilidad (ej. sumar en vez de multiplicar) daría una estimación de riesgo totalmente errónea."},
                    "quimica": {"uso": "Cálculo de la 'fracción molar' de un componente en una mezcla de mezclas.", "consecuencia_de_error": "Impide calcular la concentración final de un soluto."},
                    "civil": {"uso": "Cálculo de la distribución de carga en una viga (ej. el esfuerzo a 1/3 de la longitud).", "consecuencia_de_error": "Un error de multiplicación de fracciones daría un valor de esfuerzo incorrecto."},
                    "mecanica": {"uso": "Cálculo de relaciones de transmisión en trenes de engranajes (multiplicación de las relaciones de cada par).", "consecuencia_de_error": "Una relación de transmisión mal calculada puede hacer que un motor trabaje forzado o se sobrecaliente."},
                    "mecatronica": {"uso": "Cálculo de la relación de velocidad en un sistema de poleas compuestas.", "consecuencia_de_error": "El motor giraría a una velocidad que no corresponde con la velocidad deseada en la herramienta final."},
                    "aeronautica": {"uso": "Determinación de la fracción de combustible consumido en una etapa del vuelo.", "consecuencia_de_error": "Un error en el cálculo de la fracción de combustible restante puede ser catastrófico."},
                    "electrica": {"uso": "Cálculo de la relación de vueltas en un transformador (V_s / V_p = N_s / N_p).", "consecuencia_de_error": "Un error en la división de estas fracciones daría un voltaje de salida incorrecto."}
                }
            },
            {
                "subtema_titulo": "7. Fracciones: Suma y Resta (Mínimo Común Múltiplo)",
                "definicion": "La suma y resta de fracciones requiere que tengan el mismo denominador. No se pueden sumar 'tercios' con 'cuartos' directamente. Se usa el Mínimo Común Múltiplo (MCM) para encontrar el 'lenguaje común' (denominador común) y 'homogeneizar' las fracciones.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: (1/4) + (1/6)\n1. Denominadores 4 y 6. No son iguales.\n2. Encontrar MCM(4, 6) = 12.\n3. Convertir (1/4) a /12: (1/4) * (3/3) = 3/12\n4. Convertir (1/6) a /12: (1/6) * (2/2) = 2/12\n5. Sumar: (3/12) + (2/12) = 5/12",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula y simplifica: (1/3) + (1/6)",
                        "respuesta_correcta": "1/2",
                        "opciones": ["1/2", "2/9", "3/6", "1/3"]
                    },
                    "similares": [
                        {"pregunta": "Calcula y simplifica: (1/2) + (1/8)", "respuesta_correcta": "5/8", "opciones": ["5/8", "2/10", "6/8", "1/4"]},
                        {"pregunta": "Calcula y simplifica: (2/5) - (1/10)", "respuesta_correcta": "3/10", "opciones": ["3/10", "1/5", "1/10", "3/5"]},
                        {"pregunta": "Calcula y simplifica: (1/3) + (1/9)", "respuesta_correcta": "4/9", "opciones": ["4/9", "2/12", "1/6", "3/9"]},
                        {"pregunta": "Calcula y simplifica: (3/4) - (1/8)", "respuesta_correcta": "5/8", "opciones": ["5/8", "2/4", "1/2", "2/8"]},
                        {"pregunta": "Calcula y simplifica: (1/2) + (1/3)", "respuesta_correcta": "5/6", "opciones": ["5/6", "2/5", "1/6", "5/5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En algoritmos de planificación (scheduling) para asignar fracciones de tiempo de CPU a diferentes procesos.", "consecuencia_de_error": "Un error de suma de fracciones podría asignar más del 100% del tiempo de CPU, causando un colapso del sistema."},
                    "quimica": {"uso": "Cálculo de la 'fracción molar' de los componentes en una mezcla.", "consecuencia_de_error": "La suma de las fracciones molares debe ser 1. Un error en el MCM impediría verificar que el cálculo de la mezcla es correcto."},
                    "civil": {"uso": "Cálculo de las proporciones de mezcla de materiales (ej. 1/3 de arena, 1/2 de grava).", "consecuencia_de_error": "Un error en la suma de las fracciones puede llevar a una mezcla de concreto con proporciones incorrectas, afectando su resistencia."},
                    "mecanica": {"uso": "Análisis de sistemas de resortes o resistencias en paralelo, que involucran la suma de inversos (fracciones).", "consecuencia_de_error": "Un cálculo incorrecto de la rigidez total (basado en suma de fracciones) daría un valor erróneo para la vibración del sistema."},
                    "mecatronica": {"uso": "Cálculo de 'divisores de voltaje' con resistencias. V_out = V_in * (R2 / (R1 + R2)).", "consecuencia_de_error": "Un error en esta fracción significa que el voltaje que lee un sensor (ej. un Arduino) es incorrecto, dando lecturas falsas."},
                    "aeronautica": {"uso": "Cálculo del centro de gravedad de la aeronave (%CG), que es una suma ponderada de fracciones de la longitud total.", "consecuencia_de_error": "Un error en el %CG puede hacer que el avión sea inestable e imposible de controlar."},
                    "electrica": {"uso": "Cálculo de la Resistencia total en un circuito paralelo (1/Rt = 1/R1 + 1/R2). Es la aplicación más directa.", "consecuencia_de_error": "Calcular mal la resistencia total en paralelo (olvidar el MCM) da un valor incorrecto de la corriente total del circuito."}
                }
            },
            {
                "subtema_titulo": "8. Conversión de Fracciones a Decimales y Redondeo",
                "definicion": "Para convertir una fracción a decimal, se divide el numerador entre el denominador. El 'redondeo' es crucial en ingeniería para no reportar una precisión que no se tiene (cifras significativas). Regla: si el dígito a eliminar es 5 o más, el dígito anterior sube.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Convertir 2/3 a decimal y redondear a dos decimales.\n1. Conversión: Dividir 2 / 3 = 0.6666...\n2. Redondeo a dos decimales: Mirar el 3er decimal (es 6).\n3. Regla: Como 6 es '5 o más', el 2º decimal (6) 'sube' a 7.\n4. Resultado: 0.67",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Convierte 5/8 a decimal.",
                        "respuesta_correcta": "0.625",
                        "opciones": ["0.625", "0.585", "1.65", "0.602"]
                    },
                    "similares": [
                        {"pregunta": "Convierte 1/4 a decimal.", "respuesta_correcta": "0.25", "opciones": ["0.25", "0.4", "2.5", "0.5"]},
                        {"pregunta": "Redondea 8.127 a dos decimales.", "respuesta_correcta": "8.13", "opciones": ["8.13", "8.12", "8.10", "8.2"]},
                        {"pregunta": "Convierte 3/5 a decimal.", "respuesta_correcta": "0.6", "opciones": ["0.6", "0.35", "0.5", "0.3"]},
                        {"pregunta": "Redondea 0.4444 a tres decimales.", "respuesta_correcta": "0.444", "opciones": ["0.444", "0.445", "0.45", "0.4"]},
                        {"pregunta": "Calcula 1/5 + 0.3", "respuesta_correcta": "0.5", "opciones": ["0.5", "0.4", "0.23", "0.8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Entender la diferencia entre tipos de datos 'float' (precisión simple, ~7 decimales) y 'double' (precisión doble, ~15 decimales).", "consecuencia_de_error": "Usar 'float' para cálculos financieros o científicos puede introducir 'errores de redondeo' acumulativos que invalidan el resultado final."},
                    "quimica": {"uso": "Reporte de mediciones de laboratorio (cifras significativas). No puedes reportar 25.1234 g si tu balanza solo mide 25.12 g.", "consecuencia_de_error": "Reportar más decimales de los medidos es científicamente deshonesto e incorrecto."},
                    "civil": {"uso": "Reporte de mediciones topográficas con la precisión requerida por el plano.", "consecuencia_de_error": "Un error de redondeo en un cálculo de coordenadas puede acumularse y resultar en un error de varios centímetros en la obra."},
                    "mecanica": {"uso": "Definición de 'tolerancias' de fabricación (ej. ±0.01 mm). Las piezas reales nunca son perfectas.", "consecuencia_de_error": "No entender el redondeo y las tolerancias impide el diseño de piezas que encajen (interferencia vs. holgura)."},
                    "mecatronica": {"uso": "Entender la 'precisión' de un sensor. Un sensor puede leer 12.1 grados, pero no 12.12345.", "consecuencia_de_error": "Un error de redondeo en el código del sensor (ej. usar 'int' en lugar de 'float') puede truncar la medición y hacer que el robot crea que no se ha movido."},
                    "aeronautica": {"uso": "Reporte de altitud, velocidad y consumo de combustible. Los instrumentos tienen una precisión definida.", "consecuencia_de_error": "Confiar en un cálculo con demasiados decimales (falsa precisión) puede ser peligroso."},
                    "electrica": {"uso": "Medición de voltaje (ej. 12.1V vs 12.15V) y 'tolerancia' de resistencias (ej. una resistencia de 1kΩ puede ser de 990Ω o 1010Ω).", "consecuencia_de_error": "No considerar el redondeo y la tolerancia puede hacer que un circuito falle en la vida real aunque funcione en la simulación."}
                }
            },
            {
                "subtema_titulo": "9. Razones y Proporciones (Regla de Tres)",
                "definicion": "Una 'razón' compara dos cantidades (ej. km/h). Una 'proporción' establece que dos razones son iguales. La 'Regla de Tres' (proporcionalidad directa o inversa) es la herramienta para encontrar una cantidad desconocida.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo (Directa): Si 3 obreros construyen 12m, ¿cuántos metros construyen 5 obreros?\n1. Razón: 12 metros / 3 obreros = 4 metros por obrero.\n2. Proporción: 4 = x / 5\n3. Despejar x: x = 20 metros.\n\nEjemplo (Inversa): Si 3 obreros tardan 8 horas, ¿cuánto tardan 4 obreros?\n1. Analizar: MÁS obreros... ¿MÁS o MENOS horas? MENOS. Es Inversa.\n2. Fórmula Inversa: (Obreros₁) * (Horas₁) = (Obreros₂) * (Horas₂)\n3. (3) * (8) = (4) * x  => 24 = 4x  => x = 6 horas.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un coche recorre 120 km con 8 litros de gasolina, ¿cuántos km recorrerá con 10 litros?",
                        "respuesta_correcta": "150",
                        "opciones": ["150", "100", "120", "160"]
                    },
                    "similares": [
                        {"pregunta": "Un plano está a escala 1:50. Si una pared mide 8 cm, ¿cuántos cm mide en la realidad?", "respuesta_correcta": "400", "opciones": ["400", "58", "450", "40"]},
                        {"pregunta": "Si 5 bombas llenan un tanque en 6 horas, ¿cuánto tardarán 10 bombas? (Proporción inversa)", "respuesta_correcta": "3", "opciones": ["3", "12", "5", "2"]},
                        {"pregunta": "Si 20 litros de pintura cubren 150m², ¿cuántos metros cuadrados cubren 4 litros?", "respuesta_correcta": "30", "opciones": ["30", "37.5", "25", "40"]},
                        {"pregunta": "Si un robot suelda 10 piezas en 4 minutos, ¿cuánto tardará en soldar 25 piezas?", "respuesta_correcta": "10", "opciones": ["10", "8", "12", "15"]},
                        {"pregunta": "Un terreno de 500m² produce 100kg de cosecha. ¿Cuántos kg produce un terreno de 125m²?", "respuesta_correcta": "25", "opciones": ["25", "20", "50", "10"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para escalar interfaces de usuario (UI) y mantener las proporciones (aspect ratio) en diferentes pantallas.", "consecuencia_de_error": "Una UI que no escala proporcionalmente se verá deformada y será inutilizable en monitores con diferentes resoluciones."},
                    "quimica": {"uso": "Es el corazón de la estequiometría, usado para determinar cuánto de un producto se formará a partir de 'x' gramos de reactivo.", "consecuencia_de_error": "Un error de proporción en un proceso industrial puede llevar a un desperdicio masivo de reactivos costosos."},
                    "civil": {"uso": "En topografía para crear mapas a escala y en el diseño de maquetas estructurales.", "consecuencia_de_error": "Un error de escala en una maqueta puede llevar a conclusiones erróneas sobre la seguridad del diseño final."},
                    "mecanica": {"uso": "Para el diseño de sistemas de transmisión (relación de engranajes o poleas) para cambiar velocidad por torque.", "consecuencia_de_error": "Una relación de transmisión mal calculada puede hacer que un motor trabaje forzado o se sobrecaliente."},
                    "mecatronica": {"uso": "Para escalar los 'pasos' de un motor a pasos (stepper) a un movimiento lineal real en milímetros.", "consecuencia_de_error": "Una proporción incorrecta hará que una impresora 3D o una máquina CNC fabrique piezas con dimensiones erróneas."},
                    "aeronautica": {"uso": "Para crear modelos a escala de aviones para pruebas en túneles de viento.", "consecuencia_de_error": "Un error en la escala del modelo invalidará todas las pruebas aerodinámicas, generando datos inútiles."},
                    "electrica": {"uso": "Para calcular la 'relación de transformación' en un transformador (proporción entre voltajes y número de vueltas).", "consecuencia_de_error": "Un error en la división de estas fracciones daría un voltaje de salida incorrecto."}
                }
            },
            {
                "subtema_titulo": "10. Porcentajes y Prefijos SI",
                "definicion": "Un 'porcentaje' es una fracción de 100 (ej. 85% = 0.85), usado para eficiencias y errores. Los 'Prefijos SI' son atajos para potencias de 10 (kilo=10³, mili=10⁻³, micro=10⁻⁶, nano=10⁻⁹). Son el lenguaje estándar de la ingeniería.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo (Porcentaje): Un motor tiene una eficiencia del 85%. Si consume 2000W de electricidad, ¿cuánta potencia útil (mecánica) produce?\n1. Convertir % a decimal: 85% = 0.85\n2. Cálculo: 0.85 * 2000W = 1700W.\n\nEjemplo (Prefijo): Convertir 10 kΩ (kiloOhms) a Ohms.\n1. 'kilo' (k) significa 10³ (o 1000).\n2. 10 kΩ = 10 * 10³ Ω = 10,000 Ω.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un producto de 800 pesos tiene un 25% de descuento. ¿Cuál es el precio final?",
                        "respuesta_correcta": "600",
                        "opciones": ["600", "200", "700", "500"]
                    },
                    "similares": [
                        {"pregunta": "Una viga se expande un 0.5%. Si mide 200 cm, ¿cuántos cm se expandió?", "respuesta_correcta": "1", "opciones": ["1", "10", "0.5", "2"]},
                        {"pregunta": "Si una planta aumenta su producción en 15% y producía 4000L, ¿cuánto produce ahora?", "respuesta_correcta": "4600", "opciones": ["4600", "4150", "4400", "5000"]},
                        {"pregunta": "Una aleación es 95% Hierro. Si tienes 1000 kg, ¿cuántos kg son de Hierro?", "respuesta_correcta": "950", "opciones": ["950", "905", "50", "100"]},
                        {"pregunta": "Si la eficiencia de un motor es del 80%, ¿qué porcentaje de energía se pierde?", "respuesta_correcta": "20", "opciones": ["20", "80", "10", "25"]},
                        {"pregunta": "Un préstamo de 10000 tiene 5% de interés. ¿Cuánto se paga de interés?", "respuesta_correcta": "500", "opciones": ["500", "50", "5000", "200"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Medición de utilización de recursos (CPU, RAM) en porcentaje. Definición de tamaños de almacenamiento (Megabyte, Gigabyte).", "consecuencia_de_error": "Confundir un Megabit (Mb) con un Megabyte (MB) es un error de factor 8 que lleva a cálculos de velocidad de descarga incorrectos."},
                    "quimica": {"uso": "Para expresar la 'pureza' de un reactivo o el 'rendimiento porcentual' de una reacción.", "consecuencia_de_error": "Un cálculo erróneo del rendimiento puede hacer que un proceso químico parezca viable económicamente cuando no lo es."},
                    "civil": {"uso": "Para calcular la 'pendiente' de una carretera (ej. 2%). Uso de prefijos de carga (kN = Kilonewtons).", "consecuencia_de_error": "Confundir kPa con MPa es un error de factor 1000, llevando a un diseño 1000 veces más débil (o más robusto) de lo necesario."},
                    "mecanica": {"uso": "Para expresar la 'eficiencia' de un motor. Uso de prefijos para presión (MPa, GPa) y tolerancias (mm, µm).", "consecuencia_de_error": "Confundir la tolerancia de una pieza (mm vs µm) hace que la fabricación sea imposible o innecesariamente cara."},
                    "mecatronica": {"uso": "Para calcular el 'porcentaje de error' de un robot. Uso de prefijos para tiempo (milisegundos, ms).", "consecuencia_de_error": "Un robot que debe reaccionar en 10 ms (milisegundos) y se programa para 10 µs (microsegundos) no tendrá tiempo de hacer nada."},
                    "aeronautica": {"uso": "Para calcular la eficiencia del combustible o el 'porcentaje de sustentación' perdido en un viraje.", "consecuencia_de_error": "Un mal cálculo de la eficiencia de combustible puede hacer que el avión se quede sin gasolina antes de llegar a su destino."},
                    "electrica": {"uso": "Es la base diaria: Kilohercios (kHz), miliamperios (mA), microfaradios (µF).", "consecuencia_de_error": "Un error de prefijo (ej. mili vs micro) es el error más común en el laboratorio, y resulta en un factor de 1000 de error, quemando componentes."}
                }
            }
        ]
    },

    # ------------------------------------------------------------------------------------
    # AQUÍ COMIENZA EL RESTO DEL CONTENIDO QUE DEBE SER VERIFICADO MATERIA POR MATERIA
    # ------------------------------------------------------------------------------------

    "ALGEBRA BASICA": {
        "nombre_completo": "Álgebra Básica: El Lenguaje de la Ingeniería",
        "prerequisitos": ["ARITMETICA"],
        "quiz": [
            {
                "pregunta": "Simplifica la expresión: 10a - 5b - 4a + 7b",
                "respuesta": "6a+2b",
                "opciones": ["6a+2b", "14a+2b", "6a-2b", "14a-12b"]
            },
            {
                "pregunta": "Despeja 'x' en la ecuación: 5x + 15 = 40",
                "respuesta": "x=5",
                "opciones": ["x=5", "x=8", "x=11", "x=25"]
            },
            {
                "pregunta": "Desarrolla el producto notable: (x + 5)²",
                "respuesta": "x^2+10x+25",
                "opciones": ["x^2+10x+25", "x^2+25", "x^2+5x+25", "2x+10"]
            },
            {
                "pregunta": "Resuelve para 'x' en el sistema: x + y = 8, x - y = 2",
                "respuesta": "x=5",
                "opciones": ["x=5", "x=3", "x=6", "x=4"]
            },
            {
                "pregunta": "Encuentra las soluciones de: x² - 8x + 15 = 0 (separadas por coma)",
                "respuesta": "3,5",
                "opciones": ["3,5", "-3,-5", "1,15", "8,15"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. De Aritmética a Álgebra: Variables y Expresiones",
                "definicion": "El Álgebra es la generalización de la aritmética. Usamos 'letras' (llamadas 'Variables' o 'Incógnitas', como 'x' o 'a') para representar números que son desconocidos o que pueden cambiar. Una 'Expresión Algebraica' es una combinación de números, variables y operaciones (ej. 5x + 3).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Convertir lenguaje común a expresión algebraica: 'El doble de un número (x) más cinco'.\n1. El 'número' es 'x'.\n2. 'El doble' significa multiplicar por 2: 2*x (o 2x).\n3. 'Más cinco' significa sumar 5.\n4. Resultado: 2x + 5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Escribe la expresión algebraica para: 'Un número (y) disminuido en 10'. (Usa 'y', sin espacios)",
                        "respuesta_correcta": "y-10",
                        "opciones": ["y-10", "10-y", "y+10", "y/10"]
                    },
                    "similares": [
                        {"pregunta": "Escribe la expresión para: 'El producto de 7 y un número (b)'.", "respuesta_correcta": "7b", "opciones": ["7b", "7+b", "b/7", "7-b"]},
                        {"pregunta": "Escribe la expresión para: 'La mitad de un número (q)'.", "respuesta_correcta": "q/2", "opciones": ["q/2", "2q", "q-2", "q^2"]},
                        {"pregunta": "Escribe la expresión para: '5 más que el triple de un número (n)'.", "respuesta_correcta": "3n+5", "opciones": ["3n+5", "5n+3", "3(n+5)", "n+8"]},
                        {"pregunta": "Escribe la expresión para: 'Un número (a) al cuadrado menos 3'.", "respuesta_correcta": "a^2-3", "opciones": ["a^2-3", "(a-3)^2", "2a-3", "3-a^2"]},
                        {"pregunta": "Escribe la expresión para: 'La suma de dos números (a) y (b)'.", "respuesta_correcta": "a+b", "opciones": ["a+b", "ab", "a-b", "a/b"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Es la definición de una 'variable' en programación. `int x = 10;` crea una 'caja' (variable) llamada 'x' para guardar un valor.", "consecuencia_de_error": "No entender qué es una variable hace imposible la programación. Es el concepto más fundamental del software."},
                    "quimica": {"uso": "En las Leyes de los Gases (ej. PV=nRT), 'V', 'P' y 'T' son variables que representan Volumen, Presión y Temperatura.", "consecuencia_de_error": "Permite modelar el comportamiento de un gas sin usar números fijos, entendiendo la *relación* entre las propiedades."},
                    "civil": {"uso": "Para definir cargas. 'L' es la longitud de una viga, 'W' es el peso. La fórmula (expresión) de esfuerzo usa estas variables.", "consecuencia_de_error": "Permite crear fórmulas generales de diseño en lugar de calcular cada viga desde cero."},
                    "mecanica": {"uso": "En cinemática, 'v' es velocidad, 't' es tiempo. La expresión 'v*t' da la distancia.", "consecuencia_de_error": "El álgebra permite describir el *movimiento* (una función), no solo una foto (aritmética)."},
                    "mecatronica": {"uso": "En un sensor. `V = k*T` (Voltaje es igual a una constante 'k' por la Temperatura 'T').", "consecuencia_de_error": "Permite crear un modelo (una expresión) para 'traducir' una señal eléctrica (V) a una medida física (T)."},
                    "aeronautica": {"uso": "La Ecuación de Sustentación (L = ½ρv²AC_L) está llena de variables (v=velocidad, ρ=densidad, A=área).", "consecuencia_de_error": "El álgebra permite a los ingenieros entender cómo cambiar *una* variable (velocidad) afecta el resultado (sustentación)."},
                    "electrica": {"uso": "La Ley de Ohm (V=IR). 'V', 'I', y 'R' son variables.", "consecuencia_de_error": "Es la principal expresión algebraica de la electrónica. Permite predecir el comportamiento de un circuito antes de construirlo."}
                }
            },
            {
                "subtema_titulo": "2. Términos Semejantes (Reducción)",
                "definicion": "Ahora que sabemos qué son las variables, podemos combinarlas. Un 'Término' es una expresión separada por '+' o '-'. Los 'Términos Semejantes' son aquellos que tienen exactamente las mismas variables elevadas a las mismas potencias (ej. 5x² y -2x² son semejantes; 3x² y 3y no lo son). Reducir es 'sumar' o 'restar' solo los términos semejantes.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Simplificar (3x² + 5x) + (2x² - 8x)\n1. Quitar paréntesis: 3x² + 5x + 2x² - 8x\n2. Agrupar términos semejantes (x²): (3x² + 2x²) = 5x²\n3. Agrupar términos semejantes (x): (5x - 8x) = -3x\n4. Combinar los resultados: 5x² - 3x",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Simplifica la expresión: 10a - 5b - 4a + 7b",
                        "respuesta_correcta": "6a+2b",
                        "opciones": ["6a+2b", "14a+12b", "6a-2b", "6a+12b"]
                    },
                    "similares": [
                        {"pregunta": "Simplifica: 8x + 3y - 5x + y", "respuesta_correcta": "3x+4y", "opciones": ["3x+4y", "3x+2y", "13x+4y", "3x+3y"]},
                        {"pregunta": "Simplifica: 12ab + 5 - 3ab + 1", "respuesta_correcta": "9ab+6", "opciones": ["9ab+6", "15ab+6", "9ab+4", "9ab+5"]},
                        {"pregunta": "Simplifica: 7z² + 2w - 5z² + w (Usa ^ para potencia)", "respuesta_correcta": "2z^2+3w", "opciones": ["2z^2+3w", "12z^2+3w", "2z^2+w", "2z+3w"]},
                        {"pregunta": "Simplifica: 5x³ - 2x² + 3x³ + 4x² (Usa ^ para potencia)", "respuesta_correcta": "8x^3+2x^2", "opciones": ["8x^3+2x^2", "8x^3-2x^2", "2x^3+6x^2", "8x^6+2x^4"]},
                        {"pregunta": "Simplifica: 15p - 8q - 10p + 2q", "respuesta_correcta": "5p-6q", "opciones": ["5p-6q", "5p-10q", "25p-6q", "5p+6q"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para optimizar código, reduciendo operaciones redundantes (ej. 5*x + 2*x se convierte en 7*x, una sola operación).", "consecuencia_de_error": "Un algoritmo no simplificado consume más ciclos de CPU y memoria, crítico en sistemas de alto rendimiento o en microcontroladores con poca potencia."},
                    "quimica": {"uso": "En termodinámica, para simplificar ecuaciones de estado (que relacionan P, V, T) antes de intentar resolverlas.", "consecuencia_de_error": "Una ecuación mal simplificada puede llevar a predicciones incorrectas sobre el comportamiento de un gas o a errores de cálculo en el balance de energía."},
                    "civil": {"uso": "Para simplificar las ecuaciones de carga en el análisis de estructuras, combinando fuerzas (ej. 3kN + 5kN) para encontrar la carga neta.", "consecuencia_de_error": "Un error en la simplificación de las fuerzas (ej. sumar una fuerza 'x' con una 'y') puede llevar a un cálculo incorrecto de las fuerzas resultantes, resultando en el diseño de una viga que falle."},
                    "mecanica": {"uso": "Al analizar sistemas de fuerzas en 3D, se simplifican todas las componentes (ΣFx, ΣFy, ΣFz) para encontrar el vector de fuerza resultante.", "consecuencia_de_error": "Un cálculo erróneo de la fuerza resultante (por no agrupar bien los términos) puede predecir incorrectamente el movimiento o el punto de falla de una pieza."},
                    "mecatronica": {"uso": "Para simplificar las ecuaciones de cinemática de un robot (que son enormes) antes de programarlas en el controlador.", "consecuencia_de_error": "Un controlador con ecuaciones no simplificadas puede ser demasiado lento para reaccionar en tiempo real, causando movimientos torpes o peligrosos."},
                    "aeronautica": {"uso": "Para simplificar las ecuaciones de estabilidad de vuelo antes de implementarlas en el piloto automático.", "consecuencia_de_error": "Un piloto automático con código no optimizado podría reaccionar tarde a una ráfaga de viento, causando inestabilidad."},
                    "electrica": {"uso": "Para simplificar la 'función de transferencia' de un circuito, reduciéndola a su mínima expresión (agrupando términos 's') antes de analizarla.", "consecuencia_de_error": "Un análisis basado en una expresión no simplificada puede ocultar la verdadera naturaleza del circuito (ej. su frecuencia de resonancia)."}
                }
            },
            {
                "subtema_titulo": "3. Leyes de Exponentes (Producto y Cociente)",
                "definicion": "Son las reglas para operar potencias con la misma base. La 'base' es el número grande, el 'exponente' es el pequeño. Regla del Producto: Al multiplicar bases iguales, los exponentes se suman (xᵃ · xᵇ = xᵃ⁺ᵇ). Regla del Cociente: Al dividir bases iguales, los exponentes se restan (xᵃ / xᵇ = xᵃ⁻ᵇ).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Simplificar (b⁶ * b²) / b⁴\n1. Producto (Suma de exponentes): b⁶ * b² = b⁶⁺² = b⁸\n2. Expresión ahora es: b⁸ / b⁴\n3. Cociente (Resta de exponentes): b⁸ / b⁴ = b⁸⁻⁴\n4. Resultado: b⁴",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Simplifica la expresión: (x⁵ * x³) / x² (usa ^ para exponente, ej: x^6)",
                        "respuesta_correcta": "x^6",
                        "opciones": ["x^6", "x^4", "x^8", "x^15"]
                    },
                    "similares": [
                        {"pregunta": "Simplifica: (a⁷ * a) / a³", "respuesta_correcta": "a^5", "opciones": ["a^5", "a^4", "a^10", "a^11"]},
                        {"pregunta": "Simplifica: x² * x⁴ * x⁻³", "respuesta_correcta": "x^3", "opciones": ["x^3", "x^9", "x^-24", "x^2"]},
                        {"pregunta": "Simplifica: (y⁶) / (y² * y³)", "respuesta_correcta": "y", "opciones": ["y", "y^2", "y^11", "y^4"]},
                        {"pregunta": "Simplifica: (m⁴ * m²) / m⁵", "respuesta_correcta": "m", "opciones": ["m", "m^2", "m^11", "1"]},
                        {"pregunta": "Simplifica: (z⁹) / (z³ * z⁴)", "respuesta_correcta": "z^2", "opciones": ["z^2", "z^6", "z^12", "z"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de complejidad de algoritmos (ej. O(n²)) y direccionamiento de memoria (2ⁿ).", "consecuencia_de_error": "Elegir un algoritmo O(n³) en lugar de O(n²) (por un error de exponentes) puede hacer que un programa tarde horas en lugar de segundos."},
                    "quimica": {"uso": "Manejo de constantes científicas en notación exponencial (ej. (6.022x10²³) / (1.0x10⁻²)).", "consecuencia_de_error": "Un error al restar exponentes (23 - (-2)) puede cambiar un resultado en miles de millones."},
                    "civil": {"uso": "En mecánica de materiales, las fórmulas de momento de inercia incluyen dimensiones a varias potencias (ej. b*h³).", "consecuencia_de_error": "Un error al simplificar los exponentes (ej. h⁴/h) invalida el cálculo de la resistencia de una viga."},
                    "mecanica": {"uso": "En dinámica, las fórmulas de energía (cinética: ½mv²) dependen de variables al cuadrado.", "consecuencia_de_error": "Subestimar la energía por un error de exponentes puede llevar a un sobrecalentamiento inesperado y falla de componentes."},
                    "mecatronica": {"uso": "Modelado de la respuesta de sistemas de control, cuyas ecuaciones a menudo tienen exponentes (ej. s² en la transformada de Laplace).", "consecuencia_de_error": "Un error en el exponente de la ecuación de control puede hacer que un sistema (como un dron) sea completamente inestable y oscile sin control."},
                    "aeronautica": {"uso": "En la 'ecuación de la sustentación', la velocidad está elevada al cuadrado (L ∝ v²).", "consecuencia_de_error": "Un error en este cálculo es fatal. Si duplicas la velocidad, la sustentación se cuadruplica. Confundir esto lleva a un control erróneo del avión."},
                    "electrica": {"uso": "Cálculo de atenuación de señal en decibelios (dB), que es una escala logarítmica (la inversa de la exponencial).", "consecuencia_de_error": "Un error de exponente en un cálculo de dB puede hacer que una señal sea mil veces más débil (o más fuerte) de lo esperado."}
                }
            },
            {
                "subtema_titulo": "4. Leyes de Exponentes (Potencia, Cero y Negativo)",
                "definicion": "Reglas adicionales de exponentes. Potencia de una potencia: (xᵃ)ᵇ = xᵃᵇ (los exponentes se multiplican). Exponente cero: cualquier base (excepto 0) elevada a la potencia cero es 1 (x⁰ = 1). Exponente negativo: x⁻ᵃ = 1 / xᵃ (se 'invierte' la base).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Simplificar (a³)⁴ * 5⁰\n1. Potencia de potencia: (a³)⁴ = a³*⁴ = a¹²\n2. Exponente cero: 5⁰ = 1\n3. Resultado: a¹² * 1 = a¹²",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Simplifica: ((y²)³) * y⁰ (usa ^ para exponente)",
                        "respuesta_correcta": "y^6",
                        "opciones": ["y^6", "y^5", "y^0", "y^1"]
                    },
                    "similares": [
                        {"pregunta": "Simplifica: (x⁴)² * x¹", "respuesta_correcta": "x^9", "opciones": ["x^9", "x^8", "x^7", "x^6"]},
                        {"pregunta": "Calcula el valor de (5x)⁰", "respuesta_correcta": "1", "opciones": ["1", "0", "5x", "5"]},
                        {"pregunta": "Simplifica: ((b⁵)²) / b⁷", "respuesta_correcta": "b^3", "opciones": ["b^3", "b^2", "b^17", "b^10"]},
                        {"pregunta": "Simplifica: (m³ * m²)⁰", "respuesta_correcta": "1", "opciones": ["1", "0", "m^5", "m^6"]},
                        {"pregunta": "Simplifica: (z¹⁰) / (z⁵)²", "respuesta_correcta": "1", "opciones": ["1", "z", "0", "z^20"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Un exponente cero (x⁰=1) se usa como 'caso base' en muchos algoritmos recursivos.", "consecuencia_de_error": "Si (x⁰) se evaluara como 0 en lugar de 1, muchos algoritmos de 'dividir y vencer' fallarían en su condición base."},
                    "quimica": {"uso": "Las 'leyes de velocidad' de 'orden cero' (concentración elevada a la 0) significan que la velocidad es constante e independiente de la concentración.", "consecuencia_de_error": "No entender el exponente cero impide modelar reacciones de orden cero, comunes en catálisis."},
                    "civil": {"uso": "En la fórmula de deflexión de vigas, la carga puntual (x⁰) se integra para dar la fuerza cortante (x¹).", "consecuencia_de_error": "Un error en la regla de potencias al integrar o derivar rompe la relación fundamental entre Carga, Cortante y Momento."},
                    "mecanica": {"uso": "Un exponente (x⁰) en una ecuación de movimiento implica un valor constante, como la gravedad (g), que no depende del tiempo.", "consecuencia_de_error": "Confundir un exponente 0 con un 1 cambiaría un valor constante por uno lineal."},
                    "mecatronica": {"uso": "El término 'Proporcional' (P) de un controlador PID es un término de 'orden cero' (multiplica el error, e⁰).", "consecuencia_de_error": "No entender los órdenes de los exponentes impide comprender cómo un controlador (P, I, D) afecta al sistema."},
                    "aeronautica": {"uso": "En aerodinámica, el 'arrastre parásito' se considera constante (exponente cero de la velocidad) a bajas velocidades.", "consecuencia_de_error": "Confundir el arrastre parásito (cte) con el inducido (v²) llevaría a un modelo de vuelo incorrecto."},
                    "electrica": {"uso": "Una fuente de voltaje 'DC' (Corriente Directa) es una función de tiempo elevada a la potencia cero (constante).", "consecuencia_de_error": "No entender esto hace imposible diferenciar entre el análisis de circuitos DC (algebraicos) y AC (diferenciales)."}
                }
            },
            {
                "subtema_titulo": "5. Multiplicación de Polinomios (Distributiva/FOIL)",
                "definicion": "Un 'polinomio' es una suma de términos (ej. x² + 3x). Para multiplicar polinomios, se aplica la 'Propiedad Distributiva': se multiplica CADA término del primer polinomio por CADA término del segundo. El método 'FOIL' (First, Outer, Inner, Last) es un atajo para multiplicar dos binomios.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Multiplicar (x + 3)(x - 2)\nUsando FOIL:\n1. First (Primeros): x * x = x²\n2. Outer (Externos): x * (-2) = -2x\n3. Inner (Internos): 3 * x = +3x\n4. Last (Últimos): 3 * (-2) = -6\n5. Combinar todo: x² - 2x + 3x - 6\n6. Simplificar (Términos Semejantes): x² + x - 6",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Multiplica: (2x + 1)(x - 5) (Escribe la expresión, ej: 3x^2+2x-1)",
                        "respuesta_correcta": "2x^2-9x-5",
                        "opciones": ["2x^2-9x-5", "2x^2-10x-5", "2x^2+9x-5", "2x^2-5"]
                    },
                    "similares": [
                        {"pregunta": "Multiplica: (3a - 2)(a + 4)", "respuesta_correcta": "3a^2+10a-8", "opciones": ["3a^2+10a-8", "3a^2+12a-8", "3a^2-10a-8", "3a^2-8"]},
                        {"pregunta": "Multiplica: (y + 5)(y - 3)", "respuesta_correcta": "y^2+2y-15", "opciones": ["y^2+2y-15", "y^2-2y-15", "y^2+8y-15", "y^2-15"]},
                        {"pregunta": "Multiplica usando distributiva: 4x * (x² + 2x - 1)", "respuesta_correcta": "4x^3+8x^2-4x", "opciones": ["4x^3+8x^2-4x", "4x^3+6x^2-4x", "4x^2+8x-4", "4x^3+2x-1"]},
                        {"pregunta": "Multiplica: (2m - 1)(m + 1)", "respuesta_correcta": "2m^2+m-1", "opciones": ["2m^2+m-1", "2m^2-m-1", "2m^2-1", "2m^2+3m-1"]},
                        {"pregunta": "Multiplica: (z - 4)(z + 4)", "respuesta_correcta": "z^2-16", "opciones": ["z^2-16", "z^2+16", "z^2-8z-16", "z^2-8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En 'Procesamiento de Señales Digitales' (DSP), la 'convolución' es una multiplicación de polinomios (señales) muy elegante.", "consecuencia_de_error": "No entender la multiplicación de polinomios impide diseñar filtros digitales (ej. los que limpian el ruido en audio)."},
                    "quimica": {"uso": "En termodinámica, para simplificar ecuaciones de estado (como Van der Waals) que involucran productos de términos (P + a/V²)(V - b).", "consecuencia_de_error": "Un error al desarrollar la ecuación impide despejar y resolver las propiedades del gas (P, V, T)."},
                    "civil": {"uso": "Cálculo de momentos en vigas donde la carga y la distancia son funciones (ej. M = F(x) * x).", "consecuencia_de_error": "Si la carga es un polinomio (ej. carga triangular), multiplicarla por la distancia (x) requiere esta habilidad."},
                    "mecanica": {"uso": "Análisis de sistemas dinámicos donde se multiplican términos de masa y aceleración (que pueden ser polinomios del tiempo).", "consecuencia_de_error": "Impide modelar sistemas con aceleración no constante."},
                    "mecatronica": {"uso": "Combinación de funciones de transferencia en sistemas de control (multiplicación en el dominio 's').", "consecuencia_de_error": "Si se tienen dos bloques en serie (ej. motor y controlador), la función total es el producto de sus polinomios. Un error aquí da un modelo incorrecto del sistema."},
                    "aeronautica": {"uso": "Simplificación de ecuaciones de estabilidad aerodinámica, que son polinomios de alto grado.", "consecuencia_de_error": "Una mala simplificación puede ocultar un término inestable en el modelo de vuelo."},
                    "electrica": {"uso": "Cálculo de la potencia (P=V*I) cuando tanto V como I son funciones del tiempo (ej. V(t) = t+1, I(t) = t-1).", "consecuencia_de_error": "Un error en la multiplicación daría una curva de potencia instantánea incorrecta."}
                }
            },
            {
                "subtema_titulo": "6. Productos Notables: Binomio al Cuadrado",
                "definicion": "Son atajos para la multiplicación de polinomios. El binomio al cuadrado es el más importante: (a + b)² = a² + 2ab + b² y (a - b)² = a² - 2ab + b². Es un error común pensar que (a+b)² = a² + b² (¡esto es incorrecto! El término '2ab' es crucial).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Desarrollar (x - 4)²\n1. Identificar 'a' y 'b': a=x, b=4. Usar la fórmula (a - b)².\n2. a² = (x)² = x²\n3. -2ab = -2(x)(4) = -8x\n4. +b² = +(4)² = 16\n5. Resultado: x² - 8x + 16",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Desarrolla el producto notable: (x + 5)² (Usa ^ para potencia, ej: x^2+10x+25)",
                        "respuesta_correcta": "x^2+10x+25",
                        "opciones": ["x^2+10x+25", "x^2+25", "x^2+5x+25", "x^2+10"]
                    },
                    "similares": [
                        {"pregunta": "Desarrolla: (a - 3)²", "respuesta_correcta": "a^2-6a+9", "opciones": ["a^2-6a+9", "a^2-9", "a^2+6a+9", "a^2-3a+9"]},
                        {"pregunta": "Desarrolla: (2y + 1)²", "respuesta_correcta": "4y^2+4y+1", "opciones": ["4y^2+4y+1", "2y^2+1", "4y^2+1", "4y^2+2y+1"]},
                        {"pregunta": "Desarrolla: (5z - 2)²", "respuesta_correcta": "25z^2-20z+4", "opciones": ["25z^2-20z+4", "25z^2-4", "25z^2-10z+4", "5z^2-20z+4"]},
                        {"pregunta": "Desarrolla: (x - 10)²", "respuesta_correcta": "x^2-20x+100", "opciones": ["x^2-20x+100", "x^2-100", "x^2-10x+100", "x^2+20x+100"]},
                        {"pregunta": "Desarrolla: (3m + 4)²", "respuesta_correcta": "9m^2+24m+16", "opciones": ["9m^2+24m+16", "9m^2+16", "9m^2+12m+16", "3m^2+24m+16"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Optimización de algoritmos que usan sumas cuadráticas.", "consecuencia_de_error": "No reconocer (x+1)² y calcular x*x + 2*x + 1 por separado es menos eficiente."},
                    "quimica": {"uso": "Resolución de ecuaciones de equilibrio químico (Kc) que involucran concentraciones al cuadrado.", "consecuencia_de_error": "Si la concentración de un producto es (C-x)², necesitas desarrollar este binomio para resolver la ecuación cuadrática resultante."},
                    "civil": {"uso": "Cálculo de momentos de inercia (que usan b*h²) y análisis de deformación.", "consecuencia_de_error": "Muchas fórmulas de ingeniería (como la de energía cinética) dependen de términos al cuadrado. Este es el atajo para manipularlos."},
                    "mecanica": {"uso": "En la fórmula de energía cinética K = ½mv². Si la velocidad es una suma (v = v₁ + v₂), K = ½m(v₁ + v₂)², lo que requiere desarrollar el binomio.", "consecuencia_de_error": "Un error aquí (olvidar el término 2ab) daría un cálculo de energía totalmente incorrecto."},
                    "mecatronica": {"uso": "Cálculo de la energía almacenada en un resorte (E = ½kx²). Si el desplazamiento 'x' es una función (ej. x = t+1), la energía es E = ½k(t+1)², que debe desarrollarse.", "consecuencia_de_error": "Permite modelar la energía en un sistema oscilatorio."},
                    "aeronautica": {"uso": "Ecuación de sustentación, donde la fuerza depende de la velocidad al cuadrado (L ∝ v²).", "consecuencia_de_error": "Si la velocidad es una suma (v_avión + v_viento), la sustentación depende de (v_avión + v_viento)², que debe desarrollarse."},
                    "electrica": {"uso": "Cálculo de potencia (P = I²R). Si la corriente es una suma de dos señales (I = I₁ + I₂), la potencia es P = (I₁ + I₂)²R.", "consecuencia_de_error": "Olvidar el término 2*I₁*I₂ (el término cruzado) es un error fundamental en el análisis de potencia de señales."}
                }
            },
            {
                "subtema_titulo": "7. Productos Notables: Diferencia de Cuadrados",
                "definicion": "Fórmula: (a + b)(a - b) = a² - b². Este producto notable es especial porque el término medio (-ab + ba) siempre se cancela. Se usa mucho más en 'factorización' (el proceso inverso).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Multiplicar (2x - 3)(2x + 3)\n1. Identificar 'a' y 'b': a=2x, b=3.\n2. Fórmula: a² - b²\n3. (2x)² - (3)²\n4. Resultado: 4x² - 9",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Multiplica: (y - 7)(y + 7) (Usa ^ para potencia)",
                        "respuesta_correcta": "y^2-49",
                        "opciones": ["y^2-49", "y^2+49", "y^2-14y+49", "y-49"]
                    },
                    "similares": [
                        {"pregunta": "Multiplica: (3x + 1)(3x - 1)", "respuesta_correcta": "9x^2-1", "opciones": ["9x^2-1", "9x^2+1", "3x^2-1", "9x^2-6x+1"]},
                        {"pregunta": "Multiplica: (a² - 2)(a² + 2)", "respuesta_correcta": "a^4-4", "opciones": ["a^4-4", "a^4+4", "a^4-2", "a^2-4"]},
                        {"pregunta": "Multiplica: (p + 10)(p - 10)", "respuesta_correcta": "p^2-100", "opciones": ["p^2-100", "p^2+100", "p^2-20p+100", "p-100"]},
                        {"pregunta": "Multiplica: (4z - 5)(4z + 5)", "respuesta_correcta": "16z^2-25", "opciones": ["16z^2-25", "16z^2+25", "4z^2-25", "16z^2-40z+25"]},
                        {"pregunta": "Multiplica: (x³ + y)(x³ - y)", "respuesta_correcta": "x^6-y^2", "opciones": ["x^6-y^2", "x^9-y^2", "x^6+y^2", "x^5-y^2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simplificación en cálculos de transformadas de Laplace y Z, donde aparecen términos (s+a)(s-a).", "consecuencia_de_error": "No reconocer este patrón hace la simplificación matemática mucho más lenta y propensa a errores."},
                    "quimica": {"uso": "Simplificación de constantes de equilibrio.", "consecuencia_de_error": "Facilita la manipulación de ecuaciones complejas."},
                    "civil": {"uso": "En el 'Círculo de Mohr' para análisis de esfuerzos, esta fórmula se usa para encontrar los esfuerzos principales.", "consecuencia_de_error": "Es una herramienta de simplificación clave para el análisis gráfico de esfuerzos."},
                    "mecanica": {"uso": "Simplificación de ecuaciones en análisis de vibraciones.", "consecuencia_de_error": "Permite encontrar las raíces de la ecuación característica de vibración más rápidamente."},
                    "mecatronica": {"uso": "Simplificación de funciones de transferencia en el dominio 's' (Laplace) para el análisis de estabilidad.", "consecuencia_de_error": "Permite identificar 'polos' y 'ceros' más fácilmente."},
                    "aeronautica": {"uso": "Simplificación de la ecuación de sustentación en régimen transónico (cerca de Mach 1).", "consecuencia_de_error": "Facilita el modelado matemático del vuelo a altas velocidades."},
                    "electrica": {"uso": "En análisis de fasores de AC, para multiplicar números complejos conjugados (ej. para calcular Potencia Aparente).", "consecuencia_de_error": "Un error aquí impide calcular la potencia total en un circuito de AC."}
                }
            },
            {
                "subtema_titulo": "8. Factorización: Factor Común (GCF)",
                "definicion": "La factorización es el proceso de 'desarmar' un polinomio en factores (lo opuesto a multiplicar). El primer paso es siempre buscar el 'Máximo Factor Común' (GCF): la variable y/o número que se repite en TODOS los términos.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Factorizar 4x³ - 8x² + 2x\n1. GCF numérico (el mayor número que divide a 4, -8 y 2): 2\n2. GCF variable (la menor potencia de 'x' que se repite): x¹\n3. GCF Total: 2x\n4. Dividir cada término entre el GCF: (4x³/2x) - (8x²/2x) + (2x/2x)\n5. Resultado: 2x(2x² - 4x + 1)",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Factoriza (encontrando el GCF): 6a²b - 9ab³ (Escribe la expresión, ej: 3ab(2a-3b^2))",
                        "respuesta_correcta": "3ab(2a-3b^2)",
                        "opciones": ["3ab(2a-3b^2)", "3(2a^2b-3ab^3)", "ab(6a-9b^2)", "3ab(2a+3b^2)"]
                    },
                    "similares": [
                        {"pregunta": "Factoriza: 5x + 15y", "respuesta_correcta": "5(x+3y)", "opciones": ["5(x+3y)", "5(x+15y)", "5x(1+3y)", "15(x+y)"]},
                        {"pregunta": "Factoriza: 10m⁴ - 5m³", "respuesta_correcta": "5m^3(2m-1)", "opciones": ["5m^3(2m-1)", "5m^3(2m)", "5m(2m^3-1)", "m^3(10m-5)"]},
                        {"pregunta": "Factoriza: 3ab² + 6a²b", "respuesta_correcta": "3ab(b+2a)", "opciones": ["3ab(b+2a)", "3ab(b+2)", "3(ab^2+2a^2b)", "ab(3b+6a)"]},
                        {"pregunta": "Factoriza: 4z³ - 2z", "respuesta_correcta": "2z(2z^2-1)", "opciones": ["2z(2z^2-1)", "2z(2z^2)", "2(2z^3-z)", "z(4z^2-2)"]},
                        {"pregunta": "Factoriza: 7p²q + 14p", "respuesta_correcta": "7p(pq+2)", "opciones": ["7p(pq+2)", "7p(pq+14)", "7(p^2q+2p)", "p(7pq+14)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En 'refactorización' de código. Si varias líneas de código repiten una acción (factor común), se 'factoriza' esa acción en una 'función'.", "consecuencia_de_error": "Un código sin factorizar (duplicado) es una pesadilla de mantener: si encuentras un bug, debes arreglarlo en 10 lugares diferentes."},
                    "quimica": {"uso": "Para simplificar ecuaciones de equilibrio. Si K_c = ( [A]*[B]² + [A]*[C] ), se factoriza [A] para analizar el efecto de A.", "consecuencia_de_error": "Impide ver el efecto directo que tiene un reactivo (el factor común) sobre el sistema."},
                    "civil": {"uso": "En análisis de vigas, si la carga es F₁=10kN y F₂=15kN, se factoriza (2*5 + 3*5) = 5*(2+3) para simplificar.", "consecuencia_de_error": "Es una técnica de simplificación que reduce la probabilidad de cometer errores de cálculo manual."},
                    "mecanica": {"uso": "En ecuaciones de movimiento, si M*a + M*g = F_ext, se factoriza la Masa (M) para despejar la aceleración: a = (F_ext / M) - g.", "consecuencia_de_error": "Es el paso algebraico clave para despejar la variable de interés."},
                    "mecatronica": {"uso": "En funciones de transferencia (control), factorizar el término 's' (s² + 2s = s(s+2)) permite identificar un 'integrador' (el 's' solo).", "consecuencia_de_error": "No factorizar impide identificar componentes clave del sistema (integradores, derivadores) que afectan la estabilidad."},
                    "aeronautica": {"uso": "Para simplificar las ecuaciones de sustentación. L = ½ρv² * C_L * A. Si todo es constante menos v, se factoriza (K * v²).", "consecuencia_de_error": "Permite 'aislar' el efecto de una sola variable (velocidad) sobre la sustentación."},
                    "electrica": {"uso": "Para simplificar ecuaciones de mallas. Si (I₁*R₁) + (I₁*R₂) = V, se factoriza I₁ para encontrar la corriente: I₁ * (R₁+R₂) = V.", "consecuencia_de_error": "Es el paso algebraico fundamental para resolver la 'resistencia total' en un circuito en serie."}
                }
            },
            {
                "subtema_titulo": "9. Factorización: Trinomios (x²+bx+c)",
                "definicion": "Se busca desarmar un trinomio en dos binomios: (x + p)(x + q). Se necesitan dos números (p y q) que multiplicados den 'c' y sumados den 'b'.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Factorizar x² + 5x + 6.\n1. Buscamos: ? * ? = 6 (el término 'c')\n2. Buscamos: ? + ? = 5 (el término 'b')\n3. Los números que cumplen ambas son 2 y 3. (2*3=6 y 2+3=5)\nResultado: (x + 2)(x + 3)",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Factoriza: a² - 7a + 10 (Escribe los factores, ej: (a-1)(a-2))",
                        "respuesta_correcta": "(a-2)(a-5)",
                        "opciones": ["(a-2)(a-5)", "(a+2)(a+5)", "(a-1)(a-10)", "(a+1)(a-10)"]
                    },
                    "similares": [
                        {"pregunta": "Factoriza: y² + 3y - 18", "respuesta_correcta": "(y+6)(y-3)", "opciones": ["(y+6)(y-3)", "(y-6)(y+3)", "(y+9)(y-2)", "(y+6)(y+3)"]},
                        {"pregunta": "Factoriza: z² - 4z - 21", "respuesta_correcta": "(z-7)(z+3)", "opciones": ["(z-7)(z+3)", "(z+7)(z-3)", "(z-7)(z-3)", "(z-21)(z+1)"]},
                        {"pregunta": "Factoriza: p² + 9p + 14", "respuesta_correcta": "(p+2)(p+7)", "opciones": ["(p+2)(p+7)", "(p-2)(p-7)", "(p+1)(p+14)", "(p+9)(p+14)"]},
                        {"pregunta": "Factoriza: x² - x - 12", "respuesta_correcta": "(x-4)(x+3)", "opciones": ["(x-4)(x+3)", "(x+4)(x-3)", "(x-6)(x+2)", "(x-4)(x-3)"]},
                        {"pregunta": "Factoriza: k² + 8k + 16", "respuesta_correcta": "(k+4)^2", "opciones": ["(k+4)^2", "(k+8)^2", "(k+4)(k-4)", "(k+2)(k+8)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Encontrar las 'raíces' de polinomios en algoritmos de optimización.", "consecuencia_of_error": "Permite encontrar los puntos donde la función (ej. el 'error' de una IA) es igual a cero."},
                    "quimica": {"uso": "Resolución de ecuaciones de equilibrio químico (cálculo de pH en ácidos débiles), que resultan en un trinomio.", "consecuencia_de_error": "No poder factorizar el trinomio impide encontrar la concentración de H⁺ (el pH)."},
                    "civil": {"uso": "Encontrar los puntos de 'momento flector cero' en una viga, que indican dónde la viga cambia de compresión a tensión.", "consecuencia_de_error": "Es vital para saber dónde colocar (o no) el acero de refuerzo en una viga de concreto."},
                    "mecanica": {"uso": "Resolver la 'ecuación característica' de un sistema masa-resorte-amortiguador. Las raíces indican si el sistema 'vibra', 'regresa lento' o está 'crítico'.", "consecuencia_de_error": "Un error en la factorización lleva a un diseño de suspensión de auto incorrecto (demasiado duro o demasiado blando)."},
                    "mecatronica": {"uso": "Encontrar los 'polos' de un sistema de control. La factorización de la ecuación característica (un trinomio) te dice si el robot es estable.", "consecuencia_de_error": "Un error de factorización puede hacerte creer que un dron es estable cuando en realidad es inestable y se estrellará."},
                    "aeronautica": {"uso": "Resolver ecuaciones de trayectoria parabólica (encontrar cuándo y dónde aterriza un objeto).", "consecuencia_de_error": "Impide predecir el punto de impacto de un objeto en caída."},
                    "electrica": {"uso": "Encontrar las 'raíces' (frecuencias naturales) de la ecuación de un circuito RLC. La factorización te dice si el circuito 'resonará'.", "consecuencia_de_error": "Un error de factorización impide diseñar un 'filtro' (como el sintonizador de radio), ya que no sabrás qué frecuencia deja pasar."}
                }
            },
            {
                "subtema_titulo": "10. Ecuaciones Lineales (Despejes)",
                "definicion": "Ecuaciones donde la variable tiene exponente 1 (ej. 3x + 5 = 20). Se resuelven 'despejando' la variable (dejándola sola) usando la regla de transposición (la operación opuesta pasa al otro lado: suma <-> resta, multiplicación <-> división).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Resolver (3x / 2) - 1 = 5\n1. Objetivo: Dejar sola la 'x'.\n2. Mover el '-1' (pasa como '+1'): 3x / 2 = 5 + 1  =>  3x / 2 = 6\n3. Mover el '/ 2' (pasa como '* 2'): 3x = 6 * 2  =>  3x = 12\n4. Mover el '* 3' (pasa como '/ 3'): x = 12 / 3\n5. Resultado: x = 4",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve para x: 3x + 15 = 45 (Escribe solo el número)",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "20", "30", "15"]
                    },
                    "similares": [
                        {"pregunta": "Resuelve para y: 2y - 8 = 10 (Solo el número)", "respuesta_correcta": "9", "opciones": ["9", "1", "18", "4"]},
                        {"pregunta": "Resuelve para z: 5 + 4z = 25 (Solo el número)", "respuesta_correcta": "5", "opciones": ["5", "4", "20", "6"]},
                        {"pregunta": "Resuelve para m: 7m - 1 = 20 (Solo el número)", "respuesta_correcta": "3", "opciones": ["3", "2.7", "21", "19"]},
                        {"pregunta": "Resuelve para p: 10 + 2p = 30 (Solo el número)", "respuesta_correcta": "10", "opciones": ["10", "20", "15", "5"]},
                        {"pregunta": "Resuelve para x: 6x + 2 = 32 (Solo el número)", "respuesta_correcta": "5", "opciones": ["5", "6", "30", "4"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Base de algoritmos simples y lógica de programación.", "consecuencia_de_error": "No poder despejar una variable en una ecuación de configuración (ej. `x = (Total - 10) / 2`) es un error de lógica fundamental que detiene el desarrollo."},
                    "quimica": {"uso": "Balances de masa simples. Si 'Entrada = Salida' (ej. 10 + X = 25), se despeja X para saber cuánto falta.", "consecuencia_de_error": "Un error en el balance de masa puede llevar a un diseño de proceso ineficiente o que no cumpla las especificaciones."},
                    "civil": {"uso": "Equilibrio estático (ΣF=0) para encontrar fuerzas de reacción desconocidas (ej. 50 + 30 - R = 0).", "consecuencia_de_error": "Un error al despejar una fuerza de reacción (R) puede llevar a diseñar un anclaje o soporte demasiado débil para las cargas reales."},
                    "mecanica": {"uso": "Análisis térmicos simples (Ley de Enfriamiento de Newton) o Ley de Hooke (F=kx) para encontrar la 'k'.", "consecuencia_de_error": "Un despeje incorrecto de 'k' (k=F/x) significa que se calculará mal la rigidez de un resorte, afectando todo el sistema."},
                    "mecatronica": {"uso": "Calibración de sensores (encontrar la recta y=mx+b). Se miden dos puntos (V, Temp) y se despeja 'm' y 'b'.", "consecuencia_de_error": "Un sensor mal calibrado (por un despeje incorrecto) dará mediciones falsas, y el robot no sabrá la temperatura real."},
                    "aeronautica": {"uso": "Cálculo de consumo de combustible a tasa constante. (Comb_Total = Tasa * Tiempo). Se despeja 'Tiempo' para saber la autonomía.", "consecuencia_de_error": "Un error de despeje en esta ecuación puede llevar a cargar menos combustible del necesario, con resultados catastróficos."},
                    "electrica": {"uso": "Ley de Ohm (V=IR) es la ecuación lineal más fundamental. Se usa para encontrar un voltaje, corriente o resistencia desconocida.", "consecuencia_de_error": "Un error al despejar la Ley de Ohm (ej. R=V*I en lugar de R=V/I) puede llevar a usar una resistencia incorrecta, quemando un LED o un microcontrolador."}
                }
            }
        ]
    },

    "GEOMETRIA": {
        "nombre_completo": "Geometría: El Fundamento del Espacio",
        "prerequisitos": ["ALGEBRA BASICA"],
        "quiz": [
            {
                "pregunta": "La suma de los ángulos internos de cualquier triángulo es:",
                "respuesta": "180",
                "opciones": ["180", "360", "90", "270"]
            },
            {
                "pregunta": "Un triángulo rectángulo tiene catetos que miden 6 y 8. ¿Cuánto mide la hipotenusa?",
                "respuesta": "10",
                "opciones": ["10", "14", "48", "2"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Ángulos y Triángulos (Suma de 180°)",
                "definicion": "Un ángulo mide la 'apertura' entre dos líneas. La propiedad fundamental de CUALQUIER triángulo plano es que la suma de sus tres ángulos internos siempre es 180 grados. Un 'triángulo rectángulo' tiene un ángulo de 90°, siendo la base para la trigonometría.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: En un triángulo, un ángulo mide 90° (el recto) y otro mide 30°. ¿Cuánto mide el tercer ángulo?\n1. Suma total debe ser 180°.\n2. Suma de ángulos conocidos: 90° + 30° = 120°.\n3. Ángulo faltante = 180° - 120° = 60°.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Dos ángulos de un triángulo miden 50° y 70°. ¿Cuánto mide el tercer ángulo (Escribe solo el número de grados)?",
                        "respuesta_correcta": "60",
                        "opciones": ["60", "120", "90", "180"]
                    },
                    "similares": [
                        {"pregunta": "En un triángulo rectángulo, uno de los ángulos agudos mide 40°. ¿Cuánto mide el otro ángulo agudo?", "respuesta_correcta": "50", "opciones": ["50", "40", "130", "90"]},
                        {"pregunta": "Un triángulo tiene ángulos A=25° y B=100°. ¿Cuánto mide el ángulo C?", "respuesta_correcta": "55", "opciones": ["55", "65", "155", "45"]},
                        {"pregunta": "Un triángulo isósceles tiene dos ángulos iguales de 50°. ¿Cuánto mide el tercer ángulo?", "respuesta_correcta": "80", "opciones": ["80", "100", "130", "50"]},
                        {"pregunta": "Un triángulo equilátero tiene sus 3 ángulos iguales. ¿Cuánto mide cada uno?", "respuesta_correcta": "60", "opciones": ["60", "90", "45", "180"]},
                        {"pregunta": "Dos ángulos de un triángulo miden 15° y 75°. ¿Cuánto mide el tercero?", "respuesta_correcta": "90", "opciones": ["90", "100", "80", "180"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En gráficos por computadora para calcular la 'normal' de una superficie (un vector perpendicular) usando los ángulos del triángulo que la forma.", "consecuencia_de_error": "Un error en el cálculo de ángulos puede hacer que un objeto 3D se ilumine incorrectamente, pareciendo 'roto' o 'inverso'."},
                    "quimica": {"uso": "Para entender la 'geometría molecular'. El ángulo entre los enlaces de los átomos (ej. 104.5° en el H₂O) determina la polaridad.", "consecuencia_de_error": "Interpretar mal los ángulos de enlace puede llevar a una predicción incorrecta de la polaridad o reactividad de una molécula."},
                    "civil": {"uso": "En topografía para medir terrenos usando la 'triangulación'. Si se miden dos ángulos de un terreno triangular, se puede conocer el tercero.", "consecuencia_de_error": "Un pequeño error en la medición de un ángulo en topografía puede magnificarse y resultar en un error de varios metros en la delimitación de un terreno."},
                    "mecanica": {"uso": "Para analizar la descomposición de fuerzas en vectores y en el diseño de piezas con ángulos específicos (ej. roscas de tornillos, engranajes cónicos).", "consecuencia_de_error": "Un análisis de fuerzas con ángulos erróneos puede subestimar las cargas reales sobre una pieza, causando una falla."},
                    "mecatronica": {"uso": "Para programar la cinemática de un brazo robótico, donde el ángulo de cada motor determina la posición final de la herramienta.", "consecuencia_de_error": "Un error en el cálculo del ángulo de un servomotor puede hacer que el robot choque consigo mismo o falle al tomar un objeto."},
                    "aeronautica": {"uso": "El 'ángulo de ataque' (AOA) es el ángulo entre el ala y el viento. Es el parámetro más crítico del vuelo.", "consecuencia_de_error": "Un AOA mal calculado o mal medido puede llevar a una 'pérdida' (stall), donde el ala deja de generar sustentación y el avión cae."},
                    "electrica": {"uso": "En corriente alterna (AC), para calcular el 'ángulo de fase' (el desfase) entre el voltaje y la corriente, lo que determina el factor de potencia.", "consecuencia_de_error": "Un ángulo de fase grande indica un sistema ineficiente, lo que puede causar multas de la compañía eléctrica y sobrecalentamiento de cables."}
                }
            },
            {
                "subtema_titulo": "2. Teorema de Pitágoras",
                "definicion": "En un triángulo rectángulo (uno con un ángulo de 90°), la suma del cuadrado de los catetos (los lados cortos 'a' y 'b') es igual al cuadrado de la hipotenusa (el lado largo 'c'): a² + b² = c².\n",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Los catetos de un triángulo rectángulo miden a=8 y b=15. ¿Cuánto mide la hipotenusa 'c'?\n1. Fórmula: a² + b² = c²\n2. Sustituir: 8² + 15² = c²\n3. Calcular potencias: 64 + 225 = c²\n4. Sumar: 289 = c²\n5. Despejar 'c' (raíz cuadrada): c = √289 = 17.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Una escalera de 5 metros está apoyada en una pared. Su base está a 3 metros de la pared. ¿A qué altura (en metros) llega en la pared?",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "2", "8", "16"]
                    },
                    "similares": [
                        {"pregunta": "Un triángulo rectángulo tiene un cateto de 6 y una hipotenusa de 10. ¿Cuánto mide el otro cateto?", "respuesta_correcta": "8", "opciones": ["8", "4", "16", "64"]},
                        {"pregunta": "Calcula la hipotenusa si los catetos miden 5 y 12.", "respuesta_correcta": "13", "opciones": ["13", "17", "7", "60"]},
                        {"pregunta": "Calcula la hipotenusa si los catetos miden 9 y 12.", "respuesta_correcta": "15", "opciones": ["15", "21", "3", "108"]},
                        {"pregunta": "Calcula la hipotenusa si los catetos miden 1 y 1.", "respuesta_correcta": "raiz(2)", "opciones": ["raiz(2)", "2", "1", "0.5"]},
                        {"pregunta": "Un poste de 12m se ancla con un cable de 13m. ¿A qué distancia de la base del poste está el ancla?", "respuesta_correcta": "5", "opciones": ["5", "25", "1", "156"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En videojuegos para calcular la distancia en línea recta (magnitud) entre dos puntos en 2D (jugador y enemigo).", "consecuencia_de_error": "Si el cálculo de distancia falla (ej. olvida la raíz cuadrada), la IA de un enemigo podría 'verte' a través de las paredes o calcular mal una ruta de ataque."},
                    "quimica": {"uso": "En cristalografía, para determinar las distancias interatómicas en una red cristalina 3D (usando Pitágoras en 3D: d² = x²+y²+z²).", "consecuencia_de_error": "Un error puede llevar a una identificación incorrecta de la estructura de un material."},
                    "civil": {"uso": "Para calcular la longitud de vigas diagonales, soportes inclinados o la longitud de una rampa.", "consecuencia_de_error": "Una viga diagonal mal calculada (ej. midiendo solo 'a' y 'b') simplemente no encajará en la estructura durante el ensamblaje, deteniendo la obra."},
                    "mecanica": {"uso": "Para determinar la 'magnitud' de un vector (velocidad, fuerza) a partir de sus componentes ortogonales (Fx, Fy). Mag = √(Fx² + Fy²).", "consecuencia_de_error": "Un cálculo erróneo de la magnitud de un vector puede llevar a un análisis dinámico incorrecto y fallas inesperadas."},
                    "mecatronica": {"uso": "Para calcular la posición de la punta de un robot SCARA, que se mueve en coordenadas polares (ángulo y extensión), convirtiéndolas a (x, y).", "consecuencia_de_error": "El robot no sabrá su posición cartesiana (x, y) exacta, haciéndolo inútil para tareas de ensamblaje de precisión."},
                    "aeronautica": {"uso": "Para calcular la 'velocidad verdadera' (True Airspeed) a partir de la velocidad horizontal y vertical medidas por los instrumentos.", "consecuencia_de_error": "Un error en el cálculo de la velocidad puede llevar al piloto a tomar decisiones incorrectas de navegación o de consumo de combustible."},
                    "electrica": {"uso": "Para calcular la 'Impedancia' total (Z) en un circuito AC, que es la hipotenusa de un triángulo formado por la Resistencia (R) y la Reactancia (X). Z² = R² + X².", "consecuencia_de_error": "Un cálculo erróneo de la impedancia (ej. sumar R+X) puede llevar a que un circuito consuma mucha más corriente de la esperada, quemando fusibles."}
                }
            },
            {
                "subtema_titulo": "3. Perímetros y Áreas (Figuras 2D)",
                "definicion": "El 'Perímetro' es la longitud total del contorno de una figura 2D (la suma de sus lados). El 'Área' es la medida de la superficie que encierra (cuántos 'cuadrados' caben dentro). Las fórmulas básicas (Rectángulo: L*A, Triángulo: b*h/2) son fundamentales.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Área de un trapecio con bases B=10m, b=6m y altura h=4m.\n1. Fórmula: A = ((Base Mayor + Base Menor) / 2) * Altura\n2. Sustituir: A = ((10 + 6) / 2) * 4\n3. Cálculo: A = (16 / 2) * 4 = 8 * 4 = 32\n4. Resultado: 32 (metros cuadrados).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el área de un círculo con diámetro de 10 (en términos de π, ej: '25pi').",
                        "respuesta_correcta": "25pi",
                        "opciones": ["25pi", "100pi", "10pi", "50pi"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el área de un triángulo de base 4 y altura 6. (A = b*h/2)", "respuesta_correcta": "12", "opciones": ["12", "24", "10", "6"]},
                        {"pregunta": "Calcula el perímetro de un rectángulo con lados 5 y 10.", "respuesta_correcta": "30", "opciones": ["30", "15", "50", "25"]},
                        {"pregunta": "Calcula el área de un cuadrado cuyo perímetro es 20.", "respuesta_correcta": "25", "opciones": ["25", "20", "100", "400"]},
                        {"pregunta": "Calcula el área de un círculo con radio 3 (en términos de π).", "respuesta_correcta": "9pi", "opciones": ["9pi", "6pi", "3pi", "18pi"]},
                        {"pregunta": "Un campo rectangular mide 50m de largo y 20m de ancho. ¿Cuál es su área?", "respuesta_correcta": "1000", "opciones": ["1000", "140", "70", "500"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En diseño de UI (Interfaz de Usuario), para calcular el espacio (área en píxeles) que ocupará un botón o una ventana en la pantalla.", "consecuencia_de_error": "Un mal cálculo del área puede resultar en una interfaz desordenada, con elementos sobrepuestos e inutilizable."},
                    "quimica": {"uso": "Para determinar el 'área superficial' de un catalizador, que es crucial para la velocidad de una reacción.", "consecuencia_de_error": "Subestimar el área superficial puede llevar a que una reacción industrial sea mucho más lenta de lo planeado, afectando la producción."},
                    "civil": {"uso": "Calcular los metros cuadrados (área) de un terreno, la cantidad de asfalto para una carretera o de pintura para una pared.", "consecuencia_de_error": "Un error en el cálculo de área es uno de los errores más costosos, llevando a comprar miles de dólares de más (o de menos) en material."},
                    "mecanica": {"uso": "Para calcular la superficie de una aleta de enfriamiento (para disipar calor) o el área de un pistón (que determina la fuerza del motor, F=P*A).", "consecuencia_de_error": "Un área de pistón mal calculada resultará en un motor que no entrega la fuerza esperada. Un área de disipación insuficiente causará sobrecalentamiento."},
                    "mecatronica": {"uso": "Para calcular el área que debe cubrir un sensor de visión para detectar piezas en una banda transportadora.", "consecuencia_de_error": "Un área de visión mal calculada puede hacer que el robot no 'vea' piezas que están en el borde de la banda."},
                    "aeronautica": {"uso": "El 'área del ala' (superficie alar) es un parámetro fundamental que determina cuánta sustentación genera un avión.", "consecuencia_de_error": "Un error en el cálculo del área del ala en la fase de diseño es impensable; resultaría en un avión que simplemente no puede volar."},
                    "electrica": {"uso": "Para calcular el 'área de la sección transversal' de un cable, que determina cuánta corriente (amperaje) puede transportar sin sobrecalentarse.", "consecuencia_de_error": "Un cable con un área insuficiente para la corriente se derretirá y causará un cortocircuito o un incendio."}
                }
            },
            {
                "subtema_titulo": "4. La Circunferencia (Radio, Diámetro y Pi)",
                "definicion": "Es el conjunto de puntos a una distancia fija (radio 'r') de un punto central. El 'Diámetro' (d) es la distancia de lado a lado (d=2r). 'Pi' (π ≈ 3.1416) es la razón constante entre la circunferencia y su diámetro. Su perímetro (longitud) es L = πd o L = 2πr. Su área es A = πr².\n",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Calcular el área de una pizza con un diámetro de 14 pulgadas.\n1. Diámetro (d) = 14. Necesitamos el radio (r).\n2. Radio (r) = d / 2 = 14 / 2 = 7 pulgadas.\n3. Fórmula del Área: A = πr²\n4. A = π * (7)² = 49π pulgadas cuadradas.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un círculo tiene una circunferencia (perímetro) de 30π. ¿Cuánto mide su radio? (Solo el número)",
                        "respuesta_correcta": "15",
                        "opciones": ["15", "30", "60", "10"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el área de un círculo con radio 1 (en términos de π).", "respuesta_correcta": "pi", "opciones": ["pi", "2pi", "1", "0.5pi"]},
                        {"pregunta": "Calcula el perímetro (circunferencia) de un círculo con radio 5 (en términos de π).", "respuesta_correcta": "10pi", "opciones": ["10pi", "25pi", "5pi", "20pi"]},
                        {"pregunta": "Calcula el área de un círculo con diámetro 2 (en términos de π).", "respuesta_correcta": "pi", "opciones": ["pi", "2pi", "4pi", "0.5pi"]},
                        {"pregunta": "Un círculo tiene un área de 81π. ¿Cuánto mide su radio?", "respuesta_correcta": "9", "opciones": ["9", "81", "18", "40.5"]},
                        {"pregunta": "Un círculo tiene un perímetro de 100π. ¿Cuánto mide su radio?", "respuesta_correcta": "50", "opciones": ["50", "100", "25", "200"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para definir zonas de efecto circulares en videojuegos (ej. el radio de una explosión o un hechizo de área).", "consecuencia_de_error": "Un radio de efecto mal calculado puede hacer que un ataque en un juego dañe a personajes que están visiblemente fuera del área."},
                    "quimica": {"uso": "Para modelar las órbitas de electrones en el modelo de Bohr o diseñar reactores de tanque agitado.", "consecuencia_de_error": "Un mal diseño de un reactor circular puede crear 'zonas muertas' donde la mezcla no es homogénea."},
                    "civil": {"uso": "Para el diseño de rotondas, arcos en puentes y túneles. También para calcular el área de una columna circular.", "consecuencia_de_error": "Una curva (arco) mal diseñada en una carretera puede hacer que los vehículos pierdan el control a cierta velocidad."},
                    "mecanica": {"uso": "Fundamental para el diseño de cualquier pieza que rote: engranajes, rodamientos, ejes, llantas. La 'velocidad angular' (rad/s) depende del radio.", "consecuencia_de_error": "Un engranaje con un diámetro incorrecto no encajará con los demás, rompiendo la transmisión."},
                    "mecatronica": {"uso": "Para diseñar el 'espacio de trabajo' de un robot tipo SCARA, que es fundamentalmente circular.", "consecuencia_de_error": "Un error en el cálculo de la circunferencia de alcance puede hacer que el robot no pueda alcanzar todos los puntos que necesita."},
                    "aeronautica": {"uso": "Para calcular la trayectoria de un 'viraje coordinado' de una aeronave, que describe un arco de circunferencia.", "consecuencia_de_error": "Un radio de viraje mal calculado puede hacer que el avión invada espacio aéreo restringido o entre en una condición insegura."},
                    "electrica": {"uso": "Para calcular el campo magnético alrededor de un conductor (Ley de Ampere), que se modela en círculos concéntricos.", "consecuencia_de_error": "Un mal cálculo del campo puede causar interferencia electromagnética (EMI) en dispositivos cercanos."}
                }
            },
            {
                "subtema_titulo": "5. Volúmenes (Figuras 3D)",
                "definicion": "Es la medida del espacio tridimensional que ocupa un objeto (cuántos 'cubos' caben dentro). Fórmulas clave: Cubo: L³, Prisma Rectangular: Largo*Ancho*Alto, Cilindro: (Área de la base) * Altura = πr²h. Esfera: (4/3)πr³.\n",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Volumen de un cilindro (un tanque) con radio r=3m y altura h=10m.\nV = π * r² * h\nV = π * (3)² * 10\nV = π * 9 * 10 = 90π m³ (metros cúbicos).\n\nInstrucción de Respuesta: Responde solo con el número o la expresión con 'pi'.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el volumen de una esfera con radio 3 (en términos de π, ej: '36pi').",
                        "respuesta_correcta": "36pi",
                        "opciones": ["36pi", "12pi", "27pi", "108pi"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el volumen de un cubo (dado) con lado de 4.", "respuesta_correcta": "64", "opciones": ["64", "16", "12", "32"]},
                        {"pregunta": "Calcula el volumen de un cilindro con radio 2 y altura 10 (en términos de π).", "respuesta_correcta": "40pi", "opciones": ["40pi", "20pi", "80pi", "400pi"]},
                        {"pregunta": "Un tanque rectangular mide 5m de largo, 2m de ancho y 3m de alto. ¿Cuál es su volumen?", "respuesta_correcta": "30", "opciones": ["30", "10", "60", "25"]},
                        {"pregunta": "Un cilindro tiene un área de base de 20 m² y una altura de 5 m. ¿Cuál es su volumen?", "respuesta_correcta": "100", "opciones": ["100", "4", "25", "40"]},
                        {"pregunta": "Un cilindro tiene un volumen de 100π y una altura de 10. ¿Cuánto mide su radio?", "respuesta_correcta": "10", "opciones": ["10", "100", "5", "20"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En renderizado 3D para la detección de colisiones volumétricas ('hitboxes').", "consecuencia_de_error": "Una mala detección de volúmenes puede hacer que en una simulación los objetos se atraviesen de forma no realista o colisionen con el aire."},
                    "quimica": {"uso": "Para determinar la capacidad (volumen) de un reactor químico o un tanque de almacenamiento.", "consecuencia_de_error": "Un error en el cálculo del volumen de un reactor puede llevar a llenarlo en exceso, causando un aumento peligroso de la presión."},
                    "civil": {"uso": "Para calcular la cantidad de concreto (metros cúbicos) para una zapata o la cantidad de tierra que se debe excavar.", "consecuencia_de_error": "Pedir menos concreto del necesario detiene la obra. Pedir de más significa un desperdicio enorme de dinero."},
                    "mecanica": {"uso": "Para calcular el peso de una pieza (Volumen * Densidad) y en mecánica de fluidos (caudal volumétrico: m³/s).", "consecuencia_de_error": "Un cálculo de volumen erróneo llevará a un cálculo de peso incorrecto, crítico en industrias como la aeroespacial o automotriz."},
                    "mecatronica": {"uso": "Para calcular el volumen del espacio de trabajo 3D de un brazo robótico.", "consecuencia_de_error": "Un diseño que subestime el volumen que ocupa el robot puede llevar a que colisione con maquinaria cercana."},
                    "aeronautica": {"uso": "Para calcular el volumen de los tanques de combustible o el volumen de la cabina de carga.", "consecuencia_de_error": "Un error en el volumen del tanque de combustible significa un error en el cálculo de la autonomía de vuelo (cuánto puede volar)."},
                    "electrica": {"uso": "Para calcular el volumen de aceite refrigerante necesario en un transformador de potencia.", "consecuencia_de_error": "Un volumen insuficiente de refrigerante causará que el transformador se sobrecaliente y falle."}
                }
            }
        ]
    },

    "TRIGONOMETRIA": {
        "nombre_completo": "Trigonometría",
        "prerequisitos": ["GEOMETRIA"],
        "quiz": [
            {
                "pregunta": "¿Valor del seno de 90 grados?",
                "respuesta": "1",
                "opciones": ["1", "0", "-1", "0.5"]
            },
            {
                "pregunta": "En un triángulo con lados a=3, b=5 y ángulo C=60°, ¿cuánto mide c²? (Ley de Cosenos)",
                "respuesta": "19",
                "opciones": ["19", "34", "49", "4"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Medición de Ángulos: Grados y Radianes",
                "definicion": "Los ángulos miden rotación. Los 'Grados' (°) dividen un círculo en 360 partes. Los 'Radianes' (rad) son la medida natural en matemáticas, basada en el radio. La equivalencia es: 180° = π radianes. Para convertir: Rad = Grados * (π/180).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Convertir 90° a radianes.\n1. Fórmula: Rad = 90 * (π / 180)\n2. Simplificar fracción: 90/180 = 1/2\n3. Resultado: π/2 radianes.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Convierte 270° a radianes. (Escribe en términos de pi, ej: 3pi/2)",
                        "respuesta_correcta": "3pi/2",
                        "opciones": ["3pi/2", "2pi/3", "4pi/3", "pi"]
                    },
                    "similares": [
                        {"pregunta": "Convierte 45° a radianes.", "respuesta_correcta": "pi/4", "opciones": ["pi/4", "pi/2", "pi/3", "pi/6"]},
                        {"pregunta": "Convierte 360° a radianes.", "respuesta_correcta": "2pi", "opciones": ["2pi", "pi", "3pi", "4pi"]},
                        {"pregunta": "Convierte 30° a radianes.", "respuesta_correcta": "pi/6", "opciones": ["pi/6", "pi/3", "pi/4", "pi/2"]},
                        {"pregunta": "Convierte 60° a radianes.", "respuesta_correcta": "pi/3", "opciones": ["pi/3", "pi/6", "2pi/3", "3pi/4"]},
                        {"pregunta": "¿Cuántos grados son π radianes?", "respuesta_correcta": "180", "opciones": ["180", "360", "90", "270"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Las librerías de matemáticas (math.sin, math.cos) en Python, C++ y Java SIEMPRE esperan radianes, no grados.", "consecuencia_de_error": "Pasar '90' (grados) a una función que espera radianes (donde 90 rad ≈ 5156°) romperá cualquier cálculo de física o gráficos."},
                    "quimica": {"uso": "En espectroscopía, la 'fase' de una onda se mide en radianes para analizar interferencias.", "consecuencia_de_error": "Confundir unidades de fase impide interpretar correctamente los patrones de difracción de rayos X."},
                    "civil": {"uso": "En diseño de carreteras, las curvas se definen por su 'grado de curvatura', que se relaciona directamente con el radio y el ángulo central.", "consecuencia_de_error": "Un error en la conversión de ángulos puede resultar en una curva de carretera demasiado cerrada y peligrosa."},
                    "mecanica": {"uso": "La 'velocidad angular' (ω) de un motor se mide en radianes/segundo para calcular la potencia (P = Torque * ω).", "consecuencia_de_error": "Usar RPM en lugar de rad/s en la fórmula de potencia dará un resultado errado por un factor de 60/2π (aprox 9.5)."},
                    "mecatronica": {"uso": "Los encoders de los motores envían pulsos que se convierten a posición angular. El control PID opera en radianes.", "consecuencia_de_error": "Un robot programado en grados cuando el controlador espera radianes girará 57 veces menos de lo esperado."},
                    "aeronautica": {"uso": "Cálculo de tasas de giro (turn rate) en navegación, medidas en grados por segundo o radianes por segundo.", "consecuencia_de_error": "Una confusión de unidades puede hacer que el piloto automático realice un viraje demasiado brusco o demasiado lento."},
                    "electrica": {"uso": "La frecuencia angular 'ω' en circuitos AC (ω = 2πf) está en radianes/s. Es la base para calcular impedancias.", "consecuencia_de_error": "Calcular la reactancia de un capacitor (1/ωC) usando Hz en vez de rad/s dará un valor incorrecto."}
                }
            },
            {
                "subtema_titulo": "2. Triángulos Rectángulos: Hipotenusa y Catetos",
                "definicion": "En un triángulo rectángulo (90°), los lados tienen nombres específicos según un ángulo de referencia (θ): la 'Hipotenusa' (siempre el lado más largo, opuesto a 90°), el 'Cateto Opuesto' (frente al ángulo) y el 'Cateto Adyacente' (toca al ángulo). Identificarlos es el paso 0 de la trigonometría.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Triángulo con lados 3, 4, 5. Si el ángulo θ está entre el lado 4 y el 5:\n1. Hipotenusa: 5 (el más largo).\n2. Adyacente: 4 (toca al ángulo θ).\n3. Opuesto: 3 (está al otro lado).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En un triángulo rectángulo, el lado que está frente al ángulo recto (90°) se llama... (una palabra)",
                        "respuesta_correcta": "hipotenusa",
                        "opciones": ["hipotenusa", "cateto", "adyacente", "opuesto"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En desarrollo de juegos 2D (sprites), para calcular hacia dónde 'mira' un personaje basándose en la posición del mouse (adyacente y opuesto).", "consecuencia_de_error": "Identificar mal los catetos hará que el personaje mire en la dirección incorrecta (ejes invertidos)."},
                    "quimica": {"uso": "Análisis de vectores de dipolo en moléculas. Se descompone el vector en componentes ortogonales (catetos).", "consecuencia_de_error": "Falla al predecir la polaridad neta de la molécula."},
                    "civil": {"uso": "Cálculo de pendientes en techos o rampas. La altura es el 'opuesto', la base horizontal es el 'adyacente'.", "consecuencia_de_error": "Confundir los catetos invierte el cálculo de la pendiente (rise/run), diseñando una rampa imposible de subir."},
                    "mecanica": {"uso": "Descomposición de fuerzas en un 'Plano Inclinado'. La gravedad se divide en componentes paralela (opuesto) y perpendicular (adyacente) al plano.", "consecuencia_de_error": "Confundir las componentes lleva a calcular mal la fricción y la aceleración del objeto que desliza."},
                    "mecatronica": {"uso": "Cinemática de un brazo robótico. Cada eslabón es la hipotenusa, y sus proyecciones (x, y) son los catetos.", "consecuencia_de_error": "El robot calculará mal su posición en el espacio."},
                    "aeronautica": {"uso": "Cálculo de la senda de planeo. La altura es el cateto opuesto, la distancia a la pista es el adyacente.", "consecuencia_de_error": "Un cálculo erróneo hace que el piloto crea que está más alto o bajo de lo que realmente está."},
                    "electrica": {"uso": "Triángulo de Potencias: Potencia Activa (Adyacente), Reactiva (Opuesto) y Aparente (Hipotenusa).", "consecuencia_de_error": "Confundir P (Activa) con Q (Reactiva) lleva a dimensionar mal los generadores y transformadores."}
                }
            },
            {
                "subtema_titulo": "3. Razones Trigonométricas Básicas (SOH CAH TOA)",
                "definicion": "Son las proporciones entre los lados de un triángulo rectángulo. SOH: Seno = Opuesto/Hipotenusa. CAH: Coseno = Adyacente/Hipotenusa. TOA: Tangente = Opuesto/Adyacente. ",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Triángulo con Opuesto=3, Adyacente=4, Hipotenusa=5.\n1. Sen(θ) = O/H = 3/5 = 0.6\n2. Cos(θ) = A/H = 4/5 = 0.8\n3. Tan(θ) = O/A = 3/4 = 0.75",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si Opuesto=5 y Hipotenusa=10, ¿cuánto vale el Seno? (Decimal)",
                        "respuesta_correcta": "0.5",
                        "opciones": ["0.5", "2", "0.2", "5"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Rotación de objetos 2D. x_nuevo = x*cos(θ) - y*sin(θ).", "consecuencia_de_error": "Confundir seno y coseno rota el objeto en la dirección contraria o lo deforma."},
                    "quimica": {"uso": "Difracción de rayos X (Ley de Bragg: nλ = 2d sin θ).", "consecuencia_de_error": "Usar la función incorrecta (ej. coseno) daría distancias atómicas erróneas."},
                    "civil": {"uso": "Proyección de fuerzas en vigas. Fx = F*cos(θ), Fy = F*sin(θ).", "consecuencia_de_error": "Calcular mal la componente vertical de una carga puede hacer que una columna se dimensione para menos peso del real."},
                    "mecanica": {"uso": "Cálculo de Torque (T = r * F * sin(θ)). El seno determina cuánto de la fuerza es perpendicular al brazo de palanca.", "consecuencia_de_error": "Sobresestimar el torque disponible en una máquina puede hacer que esta se detenga bajo carga."},
                    "mecatronica": {"uso": "Cinemática Directa. Posición X = L1*cos(θ1) + L2*cos(θ1+θ2).", "consecuencia_de_error": "Error fundamental en la posición del efector final del robot."},
                    "aeronautica": {"uso": "Factor de carga en un viraje: n = 1/cos(θ). A 60° de inclinación, el peso aparente se duplica (cos60 = 0.5).", "consecuencia_de_error": "Ignorar el factor 1/cos(θ) puede llevar a exceder el límite estructural de las alas en un viraje cerrado."},
                    "electrica": {"uso": "Factor de Potencia (FP = cos(θ)). Indica qué tan eficientemente se usa la energía.", "consecuencia_de_error": "Un FP bajo requiere cables más gruesos. Calcularlo mal lleva a instalaciones eléctricas peligrosas."}
                }
            },
            {
                "subtema_titulo": "4. Cálculo de Lados (Despejes)",
                "definicion": "Usar SOH-CAH-TOA para encontrar un lado desconocido cuando se tiene un ángulo y otro lado. Se trata de despejar la variable de la fórmula. Ej: Si sen(θ) = O/H, entonces O = H * sen(θ).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Una rampa tiene una hipotenusa de 10m y un ángulo de 30°. ¿Cuál es su altura (Opuesto)?\n1. Usamos Seno (relaciona O y H).\n2. sen(30°) = O / 10\n3. Despejar O: O = 10 * sen(30°)\n4. O = 10 * 0.5 = 5 metros.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un cable de 20m (hipotenusa) forma un ángulo de 60° con el suelo. ¿Cuál es la altura (opuesto)? (sen60≈0.866)",
                        "respuesta_correcta": "17.3",
                        "opciones": ["17.3", "10.0", "20.0", "34.6"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular la velocidad en X y Y de un proyectil dado su ángulo y velocidad total.", "consecuencia_de_error": "El proyectil no seguirá la trayectoria parabólica correcta en la simulación."},
                    "quimica": {"uso": "Calcular la altura de un cristal en un microscopio de fuerza atómica basado en el ángulo del láser.", "consecuencia_de_error": "Mediciones incorrectas de la topografía de la muestra."},
                    "civil": {"uso": "Calcular la altura de una torre midiendo la distancia a la base y el ángulo de visión.", "consecuencia_de_error": "Errores en levantamientos topográficos."},
                    "mecanica": {"uso": "Dimensionar un soporte inclinado. Si conoces la fuerza vertical requerida, calculas la fuerza total en la barra inclinada.", "consecuencia_de_error": "Subestimar la fuerza total en la barra puede causar pandeo o ruptura."},
                    "mecatronica": {"uso": "Calcular cuánto debe extenderse un actuador lineal para levantar un brazo a cierta altura.", "consecuencia_de_error": "El mecanismo no alcanzará la altura deseada o chocará con los topes mecánicos."},
                    "aeronautica": {"uso": "Navegación: Calcular cuánto se ha desviado un avión de su ruta (distancia lateral) basado en el ángulo de error.", "consecuencia_de_error": "El avión podría salirse de su aerovía asignada, creando riesgo de colisión."},
                    "electrica": {"uso": "Calcular la 'Potencia Reactiva' (Q) necesaria para corregir el factor de potencia de una fábrica.", "consecuencia_de_error": "Instalar un banco de capacitores del tamaño incorrecto, no logrando evitar las multas de la compañía eléctrica."}
                }
            },
            {
                "subtema_titulo": "5. Cálculo de Ángulos (Funciones Inversas)",
                "definicion": "Si conoces los lados, usas las funciones inversas (arcoseno, arcocoseno, arcotangente) para encontrar el ángulo. Ej: Si tan(θ) = x, entonces θ = arctan(x) (o tan⁻¹(x)).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un triángulo tiene opuesto=1 y adyacente=1. ¿Ángulo?\n1. Tan(θ) = 1/1 = 1.\n2. θ = arctan(1).\n3. Sabemos que tan(45°) = 1, así que θ = 45°.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si sen(x) = 0.5, ¿cuánto vale x en grados? (Ángulo agudo)",
                        "respuesta_correcta": "30",
                        "opciones": ["30", "60", "45", "90"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Función `atan2(y, x)`: Para que un personaje o torreta 'mire' hacia el jugador. Calcula el ángulo de rotación.", "consecuencia_de_error": "Los enemigos en el juego dispararán en la dirección equivocada."},
                    "quimica": {"uso": "Calcular el ángulo de refracción de la luz en una muestra (Ley de Snell: n1*sen1 = n2*sen2).", "consecuencia_de_error": "Error en la identificación de la sustancia por su índice de refracción."},
                    "civil": {"uso": "Calcular el ángulo de pendiente de un terreno a partir de las cotas de nivel (altura/distancia).", "consecuencia_de_error": "Diseñar una carretera con una pendiente demasiado pronunciada para los vehículos."},
                    "mecanica": {"uso": "Calcular el ángulo de lanzamiento óptimo de un proyectil o chorro de agua.", "consecuencia_de_error": "El chorro no alcanzará la distancia máxima o el objetivo deseado."},
                    "mecatronica": {"uso": "Cinemática Inversa: El robot conoce la posición (x, y) a la que debe ir, y debe calcular el ángulo de sus motores.", "consecuencia_de_error": "Si el cálculo del ángulo inverso falla, el robot no sabrá cómo configurar sus articulaciones."},
                    "aeronautica": {"uso": "Calcular el ángulo de corrección de deriva necesario para contrarrestar un viento cruzado.", "consecuencia_de_error": "El avión volará 'de lado' pero no avanzará hacia el destino correcto."},
                    "electrica": {"uso": "Calcular el ángulo de fase de una impedancia (θ = arctan(X/R)).", "consecuencia_de_error": "No saber el ángulo de fase impide diseñar circuitos que resuenen o filtren frecuencias correctamente."}
                }
            },
            {
                "subtema_titulo": "6. Razones Recíprocas (Csc, Sec, Cot)",
                "definicion": "Son las inversas multiplicativas de las básicas.\nCosecante (csc) = 1/sen (H/O).\nSecante (sec) = 1/cos (H/A).\nCotangente (cot) = 1/tan (A/O).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Si sen(θ) = 1/2, calcula csc(θ).\ncsc(θ) = 1 / (1/2) = 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si cos(x) = 0.5, ¿cuánto vale la secante (sec)? (Solo el número)",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "0.5", "1", "0.2"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simplificación de expresiones matemáticas en motores de renderizado.", "consecuencia_de_error": "Uso ineficiente de operaciones de división en shaders gráficos."},
                    "quimica": {"uso": "Análisis de estructuras cristalinas complejas.", "consecuencia_de_error": "Errores en cálculos cristalográficos avanzados."},
                    "civil": {"uso": "En fórmulas de pandeo de columnas (fórmula de la secante).", "consecuencia_de_error": "Subestimar la carga crítica de una columna que tiene una imperfección inicial."},
                    "mecanica": {"uso": "Análisis de mecanismos de levas y seguidores.", "consecuencia_de_error": "Perfil de leva incorrecto, causando desgaste o ruido."},
                    "mecatronica": {"uso": "Algoritmos de control numérico que evitan divisiones por cero (usando multiplicaciones por la recíproca).", "consecuencia_de_error": "Inestabilidad numérica en el microcontrolador."},
                    "aeronautica": {"uso": "Navegación en mapas (proyección Mercator usa log(sec + tan)).", "consecuencia_de_error": "Errores en la proyección de rutas en mapas planos."},
                    "electrica": {"uso": "Cálculos de admitancia (inverso de impedancia) en circuitos paralelo.", "consecuencia_de_error": "Dificultad para analizar circuitos en paralelo."}
                }
            },
            {
                "subtema_titulo": "7. El Círculo Unitario y Ángulos Notables",
                "definicion": "Un círculo de radio 1 centrado en el origen. Cualquier punto (x, y) en el círculo corresponde a (cos θ, sen θ). Permite definir trigonometría para ángulos mayores a 90° y negativos. Ángulos notables: 0, 30, 45, 60, 90.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Ángulo de 180° (π rad). El punto en el círculo es (-1, 0).\ncos(180°) = x = -1.\nsen(180°) = y = 0.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el valor de cos(180°)? (Usa el círculo unitario: punto a la izquierda)",
                        "respuesta_correcta": "-1",
                        "opciones": ["-1", "1", "0", "0.5"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Generación de movimiento circular y ondas en animaciones.", "consecuencia_de_error": "Movimientos que no son cíclicos o suaves."},
                    "quimica": {"uso": "Función de onda en orbitales atómicos.", "consecuencia_de_error": "Malentendidos en la forma y orientación de los orbitales electrónicos."},
                    "civil": {"uso": "Análisis de esfuerzos cíclicos (fatiga) en puentes.", "consecuencia_de_error": "Falla por fatiga no predicha."},
                    "mecanica": {"uso": "Análisis de posición de cigüeñales y mecanismos rotativos.", "consecuencia_de_error": "Sincronización incorrecta de válvulas en un motor."},
                    "mecatronica": {"uso": "Generación de señales sinusoidales para control de motores AC.", "consecuencia_de_error": "Motor que vibra o no gira suavemente."},
                    "aeronautica": {"uso": "Dinámica de vuelo y oscilaciones del avión.", "consecuencia_de_error": "Inestabilidad en el control de vuelo."},
                    "electrica": {"uso": "Generación de corriente alterna trifásica (fases a 0, 120, 240 grados).", "consecuencia_de_error": "Desbalance en sistemas de potencia trifásicos."}
                }
            },
            {
                "subtema_titulo": "8. Identidades Pitagóricas",
                "definicion": "Derivadas del Teorema de Pitágoras (x² + y² = 1) en el círculo unitario. La principal es: sen²(θ) + cos²(θ) = 1. Permite encontrar una función si conoces la otra.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Si sen(θ) = 0.6. ¿Cuánto vale cos(θ)? (en el primer cuadrante)\n(0.6)² + cos²(θ) = 1\n0.36 + cos²(θ) = 1\ncos²(θ) = 1 - 0.36 = 0.64\ncos(θ) = √0.64 = 0.8.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si sen²(x) + cos²(x) = 1, ¿a qué es igual 1 - cos²(x)?",
                        "respuesta_correcta": "sen^2(x)",
                        "opciones": ["sen^2(x)", "cos^2(x)", "tan^2(x)", "1"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Optimización gráfica: calcular cos a partir de sen evita llamar a la función `acos` (que es lenta).", "consecuencia_de_error": "Código menos eficiente en shaders gráficos."},
                    "quimica": {"uso": "Normalización de funciones de onda.", "consecuencia_de_error": "Probabilidades cuánticas mayores a 1 (imposible)."},
                    "civil": {"uso": "Simplificación de ecuaciones de esfuerzo en círculos de Mohr.", "consecuencia_de_error": "Cálculos de esfuerzo principal erróneos."},
                    "mecanica": {"uso": "Análisis de energía en péndulos y osciladores.", "consecuencia_de_error": "Balance de energía incorrecto."},
                    "mecatronica": {"uso": "Control vectorial de motores (Transformada de Park).", "consecuencia_de_error": "Control ineficiente del torque del motor."},
                    "aeronautica": {"uso": "Simplificación de ecuaciones de Euler para la rotación de la aeronave.", "consecuencia_de_error": "Errores en la simulación de la actitud del avión."},
                    "electrica": {"uso": "Cálculo de potencia reactiva Q = √(S² - P²).", "consecuencia_de_error": "Dimensionamiento incorrecto de bancos de capacitores."}
                }
            },
            {
                "subtema_titulo": "9. Ley de Senos",
                "definicion": "Para triángulos NO rectángulos (oblicuángulos). Relaciona cada lado con el seno de su ángulo opuesto: a/sen(A) = b/sen(B) = c/sen(C). Útil cuando conoces dos ángulos y un lado (AAS) o dos lados y un ángulo opuesto (SSA).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Triángulo con A=30°, B=45°, a=10. Hallar b.\nb / sen(45) = 10 / sen(30)\nb = 10 * (sen 45 / sen 30) = 10 * (0.707 / 0.5) = 14.14.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En un triángulo, a=10, A=30° (sen=0.5), B=90° (sen=1). ¿Cuánto vale el lado b? (b = 10 * 1 / 0.5)",
                        "respuesta_correcta": "20",
                        "opciones": ["20", "5", "15", "10"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Triangulación en GPS y sistemas de localización.", "consecuencia_de_error": "Ubicación del usuario errónea en el mapa."},
                    "quimica": {"uso": "Cálculo de ángulos de enlace en moléculas distorsionadas.", "consecuencia_de_error": "Modelo molecular inexacto."},
                    "civil": {"uso": "Levantamientos topográficos (redes de triangulación).", "consecuencia_de_error": "Mapas y límites de propiedad incorrectos."},
                    "mecanica": {"uso": "Análisis de mecanismos de 4 barras (triángulos variables).", "consecuencia_de_error": "Mecanismo que se traba o no alcanza la posición deseada."},
                    "mecatronica": {"uso": "Cinemática de robots paralelos (plataformas Stewart).", "consecuencia_de_error": "Movimiento impreciso de la plataforma."},
                    "aeronautica": {"uso": "Triángulo de velocidades (viento, rumbo, trayectoria).", "consecuencia_de_error": "Navegación incorrecta, el avión no llega al destino."},
                    "electrica": {"uso": "Análisis de sistemas trifásicos desbalanceados (diagramas fasoriales oblicuos).", "consecuencia_de_error": "Cálculo erróneo de corrientes de neutro."}
                }
            },
            {
                "subtema_titulo": "10. Ley de Cosenos",
                "definicion": "Generalización de Pitágoras para triángulos NO rectángulos. c² = a² + b² - 2ab*cos(C). Útil cuando conoces tres lados (LLL) o dos lados y el ángulo comprendido (SAS).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: a=3, b=4, C=90°. (Debe coincidir con Pitágoras)\nc² = 3² + 4² - 2(3)(4)cos(90).\nComo cos(90)=0, queda c² = 3² + 4², que es Pitágoras.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un triángulo tiene lados 3 y 4 con un ángulo de 60° (cos=0.5) entre ellos. Calcula c². (9 + 16 - 2*3*4*0.5)",
                        "respuesta_correcta": "13",
                        "opciones": ["13", "25", "37", "7"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular distancias entre puntos en mallas no cartesianas.", "consecuencia_de_error": "Distancias erróneas en grafos de navegación."},
                    "quimica": {"uso": "Cálculo de distancias interatómicas en moléculas.", "consecuencia_de_error": "Errores en la simulación de interacciones moleculares."},
                    "civil": {"uso": "Cálculo de la longitud de un túnel a través de una montaña (triangulación desde afuera).", "consecuencia_de_error": "El túnel tendría la longitud incorrecta o no se encontraría con el otro extremo."},
                    "mecanica": {"uso": "Análisis de fuerzas en estructuras articuladas.", "consecuencia_de_error": "Fallo en la predicción de cargas en los pernos."},
                    "mecatronica": {"uso": "Cinemática inversa de brazos robóticos de 2 eslabones (calcular ángulo de codo).", "consecuencia_de_error": "El robot no puede calcular cómo doblar el brazo para alcanzar un punto."},
                    "aeronautica": {"uso": "Cálculo de distancia entre dos puntos en la esfera terrestre (navegación de círculo máximo).", "consecuencia_de_error": "Cálculo incorrecto de la distancia de vuelo y combustible necesario."},
                    "electrica": {"uso": "Suma de dos voltajes AC con diferentes fases.", "consecuencia_de_error": "Voltaje resultante incorrecto, posible daño a equipos por sobrevoltaje."}
                }
            }
        ]
    },

    "GEOMETRIA ANALITICA": {
        "nombre_completo": "Geometría Analítica: El Puente al Cálculo",
        "prerequisitos": ["TRIGONOMETRIA"],
        "quiz": [
            {
                "pregunta": "Escribe la ecuación de la recta que pasa por (0, 0) con pendiente 1. (Formato: y=mx+b)",
                "respuesta": "y=x",
                "opciones": ["y=x", "y=x+1", "y=2x", "y=0"]
            },
            {
                "pregunta": "¿Cuál es la ecuación de un círculo con radio 1 y centro en el origen?",
                "respuesta": "x^2+y^2=1",
                "opciones": ["x^2+y^2=1", "x^2+y^2=2", "x+y=1", "x^2-y^2=1"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Distancia entre Dos Puntos y Punto Medio",
                "definicion": "La distancia entre dos puntos A(x₁, y₁) y B(x₂, y₂) en el plano cartesiano se calcula usando el Teorema de Pitágoras: d = √((x₂-x₁)² + (y₂-y₁)²). El Punto Medio es el promedio de las coordenadas: Pm = ((x₁+x₂)/2, (y₁+y₂)/2).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Distancia entre A(1, 2) y B(4, 6).\n1. Restar x: 4 - 1 = 3. Restar y: 6 - 2 = 4.\n2. Cuadrados: 3² = 9, 4² = 16.\n3. Suma: 9 + 16 = 25.\n4. Raíz: √25 = 5. La distancia es 5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la distancia entre los puntos (2, 3) y (5, 7). (Solo el número)",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "7", "25", "1"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En algoritmos de 'clustering' (IA), para medir qué tan similares son dos datos (distancia euclidiana).", "consecuencia_de_error": "El algoritmo agrupará datos incorrectos, fallando en clasificar usuarios o productos."},
                    "quimica": {"uso": "Para calcular la 'longitud de enlace' entre dos átomos en una simulación molecular 2D/3D.", "consecuencia_de_error": "Una longitud de enlace errónea predice una energía de enlace falsa."},
                    "civil": {"uso": "Para verificar las dimensiones en un levantamiento topográfico, calculando la distancia real entre dos mojones.", "consecuencia_de_error": "Errores en los límites de propiedad de un terreno."},
                    "mecanica": {"uso": "Para diseñar el eslabón de una máquina: la distancia entre los centros de los pernos.", "consecuencia_de_error": "La pieza no encajará en el ensamblaje."},
                    "mecatronica": {"uso": "Para calcular el 'error de posición' de un robot (distancia entre donde está y donde debería estar).", "consecuencia_de_error": "El robot creerá que ya llegó a su destino cuando aún no lo ha hecho."},
                    "aeronautica": {"uso": "Para calcular la distancia directa entre dos aeropuertos en un mapa plano (para distancias cortas).", "consecuencia_de_error": "Cálculo erróneo del combustible necesario para el tramo."},
                    "electrica": {"uso": "Para calcular la distancia entre dos cargas eléctricas y determinar la fuerza electrostática (Ley de Coulomb).", "consecuencia_de_error": "Cálculo incorrecto de la fuerza de atracción/repulsión."}
                }
            },
            {
                "subtema_titulo": "2. La Pendiente (Inclinación)",
                "definicion": "La pendiente 'm' mide la inclinación de una recta. Se define como 'subida sobre avance' (rise over run): m = (y₂ - y₁) / (x₂ - x₁). Una pendiente positiva sube, una negativa baja, una horizontal es 0 y una vertical es indefinida.",
                "diagrama": "GIFS/pendiente.gif", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Pendiente entre (1, 1) y (3, 5).\n1. Cambio en y: 5 - 1 = 4.\n2. Cambio en x: 3 - 1 = 2.\n3. Pendiente m = 4 / 2 = 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la pendiente de la recta que pasa por (0, 0) y (4, 2). (Fracción simplificada o decimal)",
                        "respuesta_correcta": "0.5",
                        "opciones": ["0.5", "2", "4", "0.2"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En Machine Learning (Regresión Lineal), la pendiente representa el 'peso' o importancia de una variable.", "consecuencia_de_error": "El modelo hará predicciones sesgadas o incorrectas."},
                    "quimica": {"uso": "En cinemática química, la pendiente de la gráfica concentración vs. tiempo es la 'velocidad de reacción'.", "consecuencia_de_error": "Medición incorrecta de qué tan rápido ocurre una reacción."},
                    "civil": {"uso": "Para calcular la pendiente de tuberías de desagüe (necesitan una pendiente mínima para fluir).", "consecuencia_de_error": "Una tubería con poca pendiente se atascará; una con mucha pendiente erosionará el tubo."},
                    "mecanica": {"uso": "La pendiente de la gráfica Esfuerzo vs. Deformación es el 'Módulo de Young' (rigidez del material).", "consecuencia_de_error": "Calcular mal la rigidez puede llevar a usar un material demasiado blando que se deformará."},
                    "mecatronica": {"uso": "La pendiente de la curva de calibración de un sensor (Voltaje vs. Magnitud).", "consecuencia_de_error": "Lecturas erróneas del sensor (ej. leer 50°C cuando son 100°C)."},
                    "aeronautica": {"uso": "La pendiente de la curva de 'Sustentación vs. Ángulo de Ataque'.", "consecuencia_de_error": "No saber cuánto aumenta la sustentación al levantar la nariz del avión."},
                    "electrica": {"uso": "La pendiente de la gráfica Voltaje vs. Corriente es la 'Resistencia' (R).", "consecuencia_de_error": "Medición incorrecta de la resistencia de un componente."}
                }
            },
            {
                "subtema_titulo": "3. Ecuación de la Recta (Punto-Pendiente y General)",
                "definicion": "La ecuación describe todos los puntos (x, y) que forman la línea. Forma Punto-Pendiente: y - y₁ = m(x - x₁). Forma Pendiente-Intersección: y = mx + b. Forma General: Ax + By + C = 0.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Recta con pendiente m=3 que pasa por el punto (1, 2).\n1. Usar y - y₁ = m(x - x₁): y - 2 = 3(x - 1).\n2. Desarrollar: y - 2 = 3x - 3.\n3. Despejar y: y = 3x - 1.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Escribe la ecuación de la recta con pendiente m=2 que pasa por el origen (0,0). (Formato: y=mx+b)",
                        "respuesta_correcta": "y=2x",
                        "opciones": ["y=2x", "y=0.5x", "y=x+2", "y=2x+2"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para interpolación lineal en animación (mover un objeto del punto A al B suavemente).", "consecuencia_de_error": "El objeto saltará o no seguirá la ruta deseada."},
                    "quimica": {"uso": "Ley de Beer-Lambert: La absorbancia es linealmente proporcional a la concentración (A = εlc). Es una recta y=mx.", "consecuencia_de_error": "Cálculo erróneo de la concentración de una muestra desconocida."},
                    "civil": {"uso": "Diseño de perfiles de carreteras (tramos rectos con pendientes constantes).", "consecuencia_de_error": "Carreteras incómodas o peligrosas para conducir."},
                    "mecanica": {"uso": "Ley de Hooke para resortes (F = kx). Es una ecuación de recta.", "consecuencia_de_error": "Selección incorrecta de resortes para una suspensión."},
                    "mecatronica": {"uso": "Linealización de sensores no lineales en tramos pequeños.", "consecuencia_de_error": "Pérdida de precisión en las lecturas del sensor."},
                    "aeronautica": {"uso": "Trayectoria de planeo (Glide Slope) para el aterrizaje.", "consecuencia_de_error": "El avión tocará tierra antes o después de la pista."},
                    "electrica": {"uso": "Curva de carga de una resistencia (V vs I).", "consecuencia_de_error": "Mal diseño de circuitos de polarización."}
                }
            },
            {
                "subtema_titulo": "4. Rectas Paralelas y Perpendiculares",
                "definicion": "Rectas Paralelas: Tienen la misma pendiente (m₁ = m₂). Nunca se tocan. Rectas Perpendiculares: Sus pendientes son recíprocas y de signo contrario (m₁ * m₂ = -1), formando un ángulo de 90°.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Recta y = 2x + 1.\nParalela: Debe tener m=2. Ej: y = 2x + 5.\nPerpendicular: Debe tener m = -1/2. Ej: y = -0.5x + 1.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si una recta tiene pendiente m=3, ¿cuál es la pendiente de una recta perpendicular?",
                        "respuesta_correcta": "-1/3",
                        "opciones": ["-1/3", "3", "-3", "1/3"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En gráficos 3D, para calcular vectores normales (perpendiculares) a las superficies para la iluminación.", "consecuencia_de_error": "Iluminación incorrecta, el objeto se ve plano."},
                    "quimica": {"uso": "Orientación de campos magnéticos y eléctricos en ondas electromagnéticas (son perpendiculares).", "consecuencia_de_error": "Malentendidos en espectroscopía."},
                    "civil": {"uso": "Diseño de estructuras rectangulares. Muros perpendiculares al suelo, vigas paralelas.", "consecuencia_de_error": "Edificios 'chuecos' o inestables."},
                    "mecanica": {"uso": "Diseño de mecanismos de guías lineales y ejes ortogonales.", "consecuencia_de_error": "La máquina se atasca por falta de alineación."},
                    "mecatronica": {"uso": "Sistema de coordenadas de un robot. Los ejes X, Y, Z deben ser mutuamente perpendiculares.", "consecuencia_de_error": "Errores de posicionamiento espacial del robot."},
                    "aeronautica": {"uso": "Alineación de las alas y estabilizadores.", "consecuencia_de_error": "Problemas de estabilidad y control del avión."},
                    "electrica": {"uso": "Campos electromagnéticos: Fuerza magnética es perpendicular a la velocidad y al campo B.", "consecuencia_de_error": "Mal diseño de motores eléctricos."}
                }
            },
            {
                "subtema_titulo": "5. Distancia de un Punto a una Recta",
                "definicion": "Es la distancia más corta (perpendicular) desde un punto P(x₁, y₁) a una recta Ax + By + C = 0. Fórmula: d = |Ax₁ + By₁ + C| / √(A² + B²).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Distancia de (2, 1) a la recta 3x - 4y + 0 = 0.\n1. Sustituir en valor absoluto: |3(2) - 4(1) + 0| = |6 - 4| = 2.\n2. Divisor: √(3² + (-4)²) = √(9 + 16) = 5.\n3. Distancia d = 2 / 5 = 0.4.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la distancia del punto (0, 0) a la recta 3x + 4y - 10 = 0. (d = |-10| / 5)",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "10", "5", "2.5"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Detección de colisiones: distancia mínima de un punto (jugador) a una pared (recta).", "consecuencia_de_error": "El jugador atraviesa las paredes."},
                    "quimica": {"uso": "Ajuste de curvas: minimizar la distancia de los puntos experimentales a la recta teórica (mínimos cuadrados).", "consecuencia_de_error": "Modelo de regresión inexacto."},
                    "civil": {"uso": "Distancia de seguridad de una construcción a una falla geológica o tubería de gas.", "consecuencia_de_error": "Riesgo de accidentes o violación de normativas."},
                    "mecanica": {"uso": "Tolerancias: distancia de un punto de la pieza a la superficie ideal.", "consecuencia_de_error": "Piezas fuera de especificación."},
                    "mecatronica": {"uso": "Navegación de robots: mantener una distancia constante a una pared (seguimiento de pared).", "consecuencia_de_error": "El robot choca o se aleja demasiado."},
                    "aeronautica": {"uso": "Desviación de ruta (Cross-track error): distancia del avión a la línea de ruta ideal.", "consecuencia_de_error": "Navegación imprecisa."},
                    "electrica": {"uso": "Distancia de seguridad entre líneas de alta tensión y el suelo u objetos.", "consecuencia_de_error": "Arcos eléctricos peligrosos."}
                }
            },
            {
                "subtema_titulo": "6. La Circunferencia (Ecuación Canónica)",
                "definicion": "Lugar geométrico de los puntos que equidistan de un centro (h, k). Ecuación canónica: (x - h)² + (y - k)² = r². Si el centro es el origen (0,0), es x² + y² = r².",
                "diagrama": "GIFS/seno_circulo_unitario.gif", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Círculo con centro (2, -1) y radio 3.\n1. h=2, k=-1, r=3.\n2. Sustituir: (x - 2)² + (y - (-1))² = 3².\n3. Ecuación: (x - 2)² + (y + 1)² = 9.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para la circunferencia (x - 3)² + (y - 4)² = 25, ¿cuál es el radio?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "25", "3", "4"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Radio de detección en juegos (ej. si el jugador entra en el círculo de visión del enemigo).", "consecuencia_de_error": "La IA no reacciona cuando debería."},
                    "quimica": {"uso": "Modelos atómicos simples (órbitas de Bohr).", "consecuencia_de_error": "Concepto erróneo de la estructura atómica."},
                    "civil": {"uso": "Diseño de glorietas, túneles y arcos.", "consecuencia_de_error": "Trazado vial inseguro."},
                    "mecanica": {"uso": "Diseño de engranajes, ejes y rodamientos.", "consecuencia_de_error": "Falla mecánica por dimensiones incorrectas."},
                    "mecatronica": {"uso": "Espacio de trabajo de un brazo robótico (alcance máximo).", "consecuencia_de_error": "El robot no alcanza los puntos necesarios."},
                    "aeronautica": {"uso": "Radio de acción de una aeronave.", "consecuencia_de_error": "Quedarse sin combustible antes de regresar."},
                    "electrica": {"uso": "Diagrama de Smith para líneas de transmisión (se basa en círculos).", "consecuencia_de_error": "Mal acople de impedancias, pérdida de señal."}
                }
            },
            {
                "subtema_titulo": "7. La Parábola (Foco y Directriz)",
                "definicion": "Lugar geométrico de los puntos que equidistan de un punto fijo (Foco) y una recta (Directriz). Ecuación vertical: (x-h)² = 4p(y-k). 'p' es la distancia del vértice al foco. ",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: x² = 8y. Vértice en (0,0).\n1. 4p = 8 -> p = 2.\n2. Es vertical positiva (abre arriba).\n3. Foco está en (0, p) -> (0, 2).\n4. Directriz es y = -p -> y = -2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la parábola x² = 12y, ¿cuánto vale 'p'? (4p=12)",
                        "respuesta_correcta": "3",
                         "opciones": ["3", "12", "4", "6"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Trayectorias de proyectiles en motores de física.", "consecuencia_de_error": "Movimiento irreal de objetos lanzados."},
                    "quimica": {"uso": "Espectrometría de masas (trayectoria de iones).", "consecuencia_de_error": "Mala identificación de compuestos."},
                    "civil": {"uso": "Diseño de cables en puentes colgantes y arcos parabólicos (distribuyen la carga uniformemente).", "consecuencia_de_error": "Estructura ineficiente o inestable."},
                    "mecanica": {"uso": "Diseño de faros y antenas (reflector parabólico).", "consecuencia_de_error": "La luz o señal no se concentra en un haz, perdiendo eficiencia."},
                    "mecatronica": {"uso": "Trayectorias de lanzamiento para robots.", "consecuencia_de_error": "Fallo al lanzar objetos al objetivo."},
                    "aeronautica": {"uso": "Vuelos de gravedad cero (trayectoria parabólica).", "consecuencia_de_error": "No se logra la microgravedad o se ponen fuerzas G peligrosas."},
                    "electrica": {"uso": "Antenas parabólicas de satélite.", "consecuencia_de_error": "Pérdida de señal de TV o internet."}
                }
            },
            {
                "subtema_titulo": "8. La Elipse (Ejes Mayor y Menor)",
                "definicion": "Lugar geométrico donde la suma de distancias a dos Focos es constante. Ecuación: (x-h)²/a² + (y-k)²/b² = 1. 'a' es el semieje mayor, 'b' es el semieje menor. ",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: x²/25 + y²/9 = 1.\n1. a²=25 -> a=5 (Eje mayor horizontal, longitud 10).\n2. b²=9 -> b=3 (Eje menor vertical, longitud 6).\n3. Centro en (0,0).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la elipse x²/100 + y²/36 = 1, ¿cuánto vale el semieje mayor 'a'?",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "100", "6", "36"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Colisiones con 'cajas' elípticas (más suaves que rectángulos).", "consecuencia_de_error": "Detección de colisiones imprecisa."},
                    "quimica": {"uso": "Orbitales electrónicos elípticos (modelo de Sommerfeld).", "consecuencia_de_error": "Modelo atómico incompleto."},
                    "civil": {"uso": "Arcos elípticos en puentes y acueductos (estética y distribución de carga).", "consecuencia_de_error": "Fallo estructural si no se calcula bien la distribución de carga."},
                    "mecanica": {"uso": "Engranajes elípticos (para velocidad variable).", "consecuencia_de_error": "Mecanismo trabado o con velocidad de salida incorrecta."},
                    "mecatronica": {"uso": "Trayectorias suaves de robots.", "consecuencia_de_error": "Movimiento robótico brusco."},
                    "aeronautica": {"uso": "Mecánica orbital (Leyes de Kepler). Las órbitas de satélites son elipses.", "consecuencia_de_error": "El satélite se pierde en el espacio o cae a la Tierra."},
                    "electrica": {"uso": "Polarización elíptica de ondas electromagnéticas.", "consecuencia_de_error": "Pérdida de señal en comunicaciones satelitales."}
                }
            },
            {
                "subtema_titulo": "9. La Hipérbola (Asíntotas)",
                "definicion": "Lugar geométrico donde la RESTA de distancias a dos focos es constante. Tiene dos ramas abiertas. Ecuación: (x-h)²/a² - (y-k)²/b² = 1. Tiene asíntotas (líneas a las que se acerca pero no toca).",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: x²/16 - y²/9 = 1.\n1. a=4, b=3.\n2. Abre horizontalmente (x es positivo).\n3. Asíntotas: y = ±(b/a)x -> y = ±(3/4)x.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la hipérbola x²/25 - y²/16 = 1, ¿cuál es el valor de 'a'?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "25", "4", "16"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Algoritmos de localización por diferencia de tiempo (TDOA).", "consecuencia_de_error": "Posicionamiento erróneo."},
                    "quimica": {"uso": "Cinética de adsorción (isotermas).", "consecuencia_de_error": "Mal diseño de filtros o catalizadores."},
                    "civil": {"uso": "Torres de enfriamiento (hiperboloides). Su forma optimiza el flujo de aire y la resistencia estructural.", "consecuencia_de_error": "Torre estructuralmente débil o ineficiente térmicamente."},
                    "mecanica": {"uso": "Engranajes hiperbólicos (hipoidales) para ejes que no se cruzan.", "consecuencia_de_error": "Ruido y desgaste en la transmisión."},
                    "mecatronica": {"uso": "Navegación robótica basada en balizas.", "consecuencia_de_error": "Robot perdido."},
                    "aeronautica": {"uso": "Sistemas de navegación de largo alcance (LORAN) usan intersección de hipérbolas.", "consecuencia_de_error": "Navegación marítima o aérea incorrecta."},
                    "electrica": {"uso": "Trayectorias de partículas cargadas repelidas por un núcleo (dispersión de Rutherford).", "consecuencia_de_error": "Errores en física de partículas."}
                }
            },
            {
                "subtema_titulo": "10. Coordenadas Polares (r, θ)",
                "definicion": "Alternativa al sistema cartesiano (x, y). Usa una distancia 'r' desde el origen y un ángulo 'θ'.\nx = r * cos(θ), y = r * sen(θ). r² = x² + y², tan(θ) = y/x.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Convertir el punto polar (4, 60°) a cartesiano.\nx = 4 * cos(60°) = 4 * 0.5 = 2.\ny = 4 * sen(60°) = 4 * 0.866 = 3.46.\nPunto: (2, 3.46).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Convierte el punto polar (10, 90°) a cartesiano (x, y). (cos90=0, sen90=1)",
                        "respuesta_correcta": "0,10",
                        "opciones": ["0,10", "10,0", "10,10", "0,0"]
                    }
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Joysticks analógicos entregan coordenadas polares (ángulo y magnitud de empuje).", "consecuencia_de_error": "Control del personaje errático."},
                    "quimica": {"uso": "Orbitales atómicos se describen mejor en coordenadas esféricas (extensión 3D de polares).", "consecuencia_de_error": "Ecuaciones de Schrödinger irresolubles."},
                    "civil": {"uso": "Levantamientos topográficos (distancia y azimut).", "consecuencia_de_error": "Mapas incorrectos."},
                    "mecanica": {"uso": "Análisis de levas y mecanismos rotativos.", "consecuencia_de_error": "Diseño de maquinaria defectuoso."},
                    "mecatronica": {"uso": "Robots SCARA y radares LIDAR operan nativamente en coordenadas polares.", "consecuencia_de_error": "El robot no puede interpretar su entorno."},
                    "aeronautica": {"uso": "Radares y navegación VOR (distancia y rumbo).", "consecuencia_de_error": "Errores de navegación aérea."},
                    "electrica": {"uso": "Análisis de fasores (magnitud y fase) es esencialmente coordenadas polares.", "consecuencia_de_error": "Imposible analizar circuitos de AC."}
                }
            }
        ]
    },

    "PRECALCULO": {
        "nombre_completo": "Precálculo: Fundamentos de la Variación",
        "prerequisitos": ["GEOMETRIA ANALITICA"],
        "quiz": [
            {
                "pregunta": "Si f(x) = 2x+1, ¿cuánto vale f(3)? (Solo el número)",
                "respuesta": "7",
                "opciones": ["7", "6", "8", "3"]
            },
            {
                "pregunta": "Resuelve para x: 2^x = 8 (Solo el número)",
                "respuesta": "3",
                "opciones": ["3", "4", "2", "8"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. ¿Qué es una Función? (Input/Output)",
                "definicion": "Una Función (f) es una regla que relaciona una entrada (x) con una ÚNICA salida (y). Se escribe y = f(x). Piensa en ella como una máquina: le metes materia prima (x) y saca un producto (f(x)). Si le metes lo mismo, siempre debe salir lo mismo.",
                "diagrama": "", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x² + 1. Calcula f(3).\n1. La 'máquina' toma la entrada (3), la eleva al cuadrado y le suma 1.\n2. f(3) = (3)² + 1 = 9 + 1\n3. Resultado: 10.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = 3x - 2, ¿cuánto vale f(5)? (Solo el número)",
                        "respuesta_correcta": "13",
                        "opciones": ["13", "15", "3", "17"]
                    },
                    "similares": [
                        {"pregunta": "Si g(t) = t² - t, calcula g(4). (16-4)", "respuesta_correcta": "12", "opciones": ["12", "16", "8", "20"]},
                        {"pregunta": "Si h(x) = 10/x, calcula h(2).", "respuesta_correcta": "5", "opciones": ["5", "2", "20", "10"]},
                        {"pregunta": "Si f(x) = x + 5, calcula f(-2).", "respuesta_correcta": "3", "opciones": ["3", "-3", "-7", "7"]},
                        {"pregunta": "Si p(x) = 2x, calcula p(0.5).", "respuesta_correcta": "1", "opciones": ["1", "0.5", "2", "4"]},
                        {"pregunta": "Si f(x) = 5 (función constante), calcula f(100).", "respuesta_correcta": "5", "opciones": ["5", "100", "500", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Es el concepto de 'subrutina' o 'método'. Recibe parámetros (x) y retorna un valor (y).", "consecuencia_de_error": "Una función de software que devuelve resultados diferentes para la misma entrada (sin ser aleatoria) tiene un 'bug' de estado o memoria."},
                    "quimica": {"uso": "La Ley de los Gases Ideales (P = nRT/V) es una función. La presión (P) es función de la temperatura (T) y volumen (V).", "consecuencia_de_error": "No entender la relación funcional impide controlar la presión en un tanque."},
                    "civil": {"uso": "El costo de una obra es función de los materiales: Costo(x) = Precio * x + ManoObra.", "consecuencia_de_error": "Presupuestar mal una obra por no definir bien la función de costos."},
                    "mecanica": {"uso": "La posición de un pistón es función del ángulo del cigüeñal: x(θ).", "consecuencia_de_error": "No poder sincronizar el encendido del motor con la posición del pistón."},
                    "mecatronica": {"uso": "La lectura de un sensor (Voltaje) es función de la variable física (Temperatura). V = f(T).", "consecuencia_de_error": "No poder calibrar un sensor para leer la temperatura real."},
                    "aeronautica": {"uso": "El empuje requerido es función del peso y la resistencia: T = f(W, D).", "consecuencia_de_error": "No calcular bien el empuje necesario para el despegue."},
                    "electrica": {"uso": "El voltaje en un capacitor es función del tiempo: V(t).", "consecuencia_de_error": "No predecir cuándo un circuito alcanzará su voltaje operativo."}
                }
            },
            {
                "subtema_titulo": "2. Dominio y Rango (Límites de Operación)",
                "definicion": "El 'Dominio' son todos los valores válidos que pueden entrar a la función (las 'x' permitidas). El 'Rango' son todos los valores posibles que pueden salir (las 'y' resultantes). Las restricciones más comunes son: no dividir por cero y no raíces pares de negativos.",
                "diagrama": "GIFS/dominio_rango.gif", # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = 1 / (x - 2).\n1. Restricción: El denominador no puede ser cero.\n2. x - 2 ≠ 0 -> x ≠ 2.\n3. Dominio: Todos los reales excepto el 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué valor de x NO está en el dominio de f(x) = 10 / (x - 5)?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "-5", "0", "10"]
                    },
                    "similares": [
                        {"pregunta": "Para f(x) = 1/x, ¿qué valor está prohibido?", "respuesta_correcta": "0", "opciones": ["0", "1", "-1", "infinity"]},
                        {"pregunta": "Para f(x) = √(x - 4), el dominio empieza en...", "respuesta_correcta": "4", "opciones": ["4", "-4", "0", "2"]},
                        {"pregunta": "Si el rango de f(x) = x² son los reales positivos, ¿puede f(x) valer -5? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "¿Qué valor hace que el denominador de 1/(x+3) sea cero?", "respuesta_correcta": "-3", "opciones": ["-3", "3", "0", "1"]},
                        {"pregunta": "El dominio de f(x) = x + 1 son... (todos/ninguno)", "respuesta_correcta": "todos", "opciones": ["todos", "ninguno", "positivos", "enteros"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Validación de datos. El 'dominio' de un campo de 'edad' es 0 a 120.", "consecuencia_de_error": "Permitir una edad negativa o letras en un campo numérico crashea la base de datos."},
                    "quimica": {"uso": "El dominio de la temperatura en agua líquida es 0°C a 100°C (a 1 atm).", "consecuencia_de_error": "Intentar aplicar ecuaciones de líquidos a vapor o hielo dará resultados absurdos."},
                    "civil": {"uso": "El rango elástico de una viga. Si la carga (x) excede el dominio elástico, la viga se deforma permanentemente.", "consecuencia_de_error": "Colapso estructural por exceder los límites de diseño."},
                    "mecanica": {"uso": "El rango de RPM seguras de un motor (zona roja).", "consecuencia_de_error": "Exceder el dominio de RPM causa que el motor explote o se desbiele."},
                    "mecatronica": {"uso": "El 'espacio de trabajo' de un robot es su dominio físico (hasta dónde llega su brazo).", "consecuencia_de_error": "Programar una coordenada fuera del dominio hará que el robot se bloquee o rompa sus motores intentando llegar."},
                    "aeronautica": {"uso": "La 'envolvente de vuelo' (Flight Envelope) es el dominio seguro de velocidad y altitud.", "consecuencia_de_error": "Volar fuera de la envolvente (muy lento o muy rápido) causa pérdida de control o daño estructural."},
                    "electrica": {"uso": "El voltaje máximo de entrada de un componente (ej. un capacitor de 16V).", "consecuencia_de_error": "Aplicar 20V a un capacitor con dominio de 0-16V hará que explote."}
                }
            },
            {
                "subtema_titulo": "3. Composición de Funciones (Sistemas en Serie)",
                "definicion": "Es aplicar una función dentro de otra: f(g(x)). La salida de 'g' se convierte en la entrada de 'f'. Es como conectar dos máquinas en una línea de producción.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x + 10, g(x) = 2x. Calcular f(g(3)).\n1. Primero la de adentro: g(3) = 2*3 = 6.\n2. Luego la de afuera con ese resultado: f(6) = 6 + 10 = 16.\nResultado: 16.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = x² y g(x) = x + 1, calcula f(g(2)). (Primero g(2)=3, luego f(3))",
                        "respuesta_correcta": "9",
                        "opciones": ["9", "5", "6", "8"]
                    },
                    "similares": [
                        {"pregunta": "Si f(x) = 2x y g(x) = 5x, calcula f(g(1)).", "respuesta_correcta": "10", "opciones": ["10", "7", "2", "5"]},
                        {"pregunta": "Si h(x) = x - 2 y p(x) = x², calcula p(h(5)). (5-2)^2", "respuesta_correcta": "9", "opciones": ["9", "23", "3", "25"]},
                        {"pregunta": "Si f(x) = x y g(x) = 10, calcula f(g(50)).", "respuesta_correcta": "10", "opciones": ["10", "50", "500", "60"]},
                        {"pregunta": "Si f(x) = x + 1, calcula f(f(1)). (1+1)+1", "respuesta_correcta": "3", "opciones": ["3", "2", "1", "4"]},
                        {"pregunta": "Si f(x) = √x y g(x) = 16, calcula f(g(x)).", "respuesta_correcta": "4", "opciones": ["4", "16", "256", "8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Pasar el resultado de una función como argumento a otra: `imprimir(calcular_total(precio))`.", "consecuencia_de_error": "Errores en el flujo de datos entre módulos del software."},
                    "quimica": {"uso": "Reacciones en cadena. El producto de la reacción 1 (g) es el reactivo de la reacción 2 (f).", "consecuencia_de_error": "No poder modelar procesos industriales de múltiples etapas."},
                    "civil": {"uso": "La carga en el techo (x) causa una deflexión (g), y esa deflexión causa un estrés en la columna (f).", "consecuencia_de_error": "Ignorar la cadena de efectos lleva a subestimar el estrés en los cimientos."},
                    "mecanica": {"uso": "Cajas de engranajes en serie. La velocidad de salida del engranaje 1 es la entrada del engranaje 2.", "consecuencia_de_error": "Cálculo incorrecto de la velocidad final de la máquina."},
                    "mecatronica": {"uso": "Cinemática directa: La posición de la muñeca depende del codo, que depende del hombro.", "consecuencia_de_error": "Error en la posición final del robot."},
                    "aeronautica": {"uso": "El movimiento del joystick (x) mueve un hidráulico (g), que mueve el alerón (f).", "consecuencia_de_error": "Diseño de controles de vuelo que no responden como se espera."},
                    "electrica": {"uso": "Amplificadores en cascada. La señal amplificada del etapa 1 entra a la etapa 2.", "consecuencia_de_error": "Saturación o distorsión de la señal de audio/radio."}
                }
            },
            {
                "subtema_titulo": "4. Función Inversa (Deshacer Operaciones)",
                "definicion": "La función inversa (f⁻¹) hace lo contrario que la original. Si f(x) te lleva de A a B, la inversa te lleva de B a A. Si y = f(x), entonces x = f⁻¹(y). Gráficamente, es un reflejo sobre la línea y=x.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Inversa de f(x) = 2x + 4.\n1. Escribir: y = 2x + 4\n2. Despejar x: y - 4 = 2x -> x = (y - 4) / 2\n3. Intercambiar variables: y = (x - 4) / 2\nInversa: f⁻¹(x) = x/2 - 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = x + 10, ¿cuál es su inversa f⁻¹(x)?",
                        "respuesta_correcta": "x-10",
                        "opciones": ["x-10", "x+10", "10x", "x/10"]
                    },
                    "similares": [
                        {"pregunta": "Si f(x) = 3x, ¿cuál es su inversa?", "respuesta_correcta": "x/3", "opciones": ["x/3", "3x", "x-3", "x+3"]},
                        {"pregunta": "Si f(x) = x - 5, ¿cuál es su inversa?", "respuesta_correcta": "x+5", "opciones": ["x+5", "x-5", "5x", "x/5"]},
                        {"pregunta": "Si f(x) = x/2, ¿cuál es su inversa?", "respuesta_correcta": "2x", "opciones": ["2x", "x/2", "x+2", "x-2"]},
                        {"pregunta": "Si f(x) = x³, ¿cuál es su inversa?", "respuesta_correcta": "x^(1/3)", "opciones": ["x^(1/3)", "x^2", "3x", "x/3"]},
                        {"pregunta": "Si una función convierte C° a F°, ¿qué hace su inversa?", "respuesta_correcta": "F a C", "opciones": ["F a C", "C a K", "K a F", "C a C"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Encriptación y desencriptación. La clave privada es la función inversa de la pública.", "consecuencia_de_error": "Pérdida de datos o brechas de seguridad."},
                    "quimica": {"uso": "Calcular la concentración inicial a partir del pH final.", "consecuencia_de_error": "Errores en el análisis químico inverso."},
                    "civil": {"uso": "Determinar la carga máxima permitida conociendo la deformación máxima del material.", "consecuencia_de_error": "No poder establecer límites de carga seguros."},
                    "mecanica": {"uso": "Ingeniería inversa: deducir las fuerzas originales a partir de la deformación de una pieza rota.", "consecuencia_de_error": "No encontrar la causa raíz de un accidente."},
                    "mecatronica": {"uso": "Cinemática Inversa: Calcular los ángulos de los motores necesarios para llegar a una coordenada (x,y).", "consecuencia_de_error": "El robot no se puede mover a un punto específico."},
                    "aeronautica": {"uso": "Calcular la altitud real a partir de la presión medida por el altímetro.", "consecuencia_de_error": "Lecturas de altitud falsas, riesgo de colisión con el terreno."},
                    "electrica": {"uso": "Conversión Analógico-Digital (ADC) y Digital-Analógico (DAC).", "consecuencia_de_error": "Sonido distorsionado o datos corruptos."}
                }
            },
            {
                "subtema_titulo": "5. Funciones Polinomiales (Raíces y Grado)",
                "definicion": "Son sumas de potencias de x (ej. 2x³ - 5x + 1). El 'Grado' es la potencia más alta y determina la forma básica. Las 'Raíces' son los valores de x donde f(x)=0 (cruces por el eje X).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x² - 9. Grado 2 (Parábola).\nRaíces: x² - 9 = 0 -> x² = 9 -> x = 3 y x = -3.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el grado del polinomio f(x) = 5x⁴ + 2x - 1? (Solo el número)",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "5", "1", "3"]
                    },
                    "similares": [
                        {"pregunta": "Las raíces de (x-2)(x-5) = 0 son 2 y...", "respuesta_correcta": "5", "opciones": ["5", "-5", "-2", "0"]},
                        {"pregunta": "Si el grado es 1 (mx+b), la gráfica es una...", "respuesta_correcta": "recta", "opciones": ["recta", "curva", "parabola", "punto"]},
                        {"pregunta": "¿Cuántos raíces tiene como máximo un polinomio de grado 3?", "respuesta_correcta": "3", "opciones": ["3", "2", "1", "4"]},
                        {"pregunta": "En f(x) = x³ - 8, una raíz es 2. ¿Cuánto es 2³ - 8?", "respuesta_correcta": "0", "opciones": ["0", "16", "4", "-4"]},
                        {"pregunta": "Si el coeficiente principal es positivo en una x², la parábola abre hacia...", "respuesta_correcta": "arriba", "opciones": ["arriba", "abajo", "izquierda", "derecha"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Códigos de corrección de errores (CRC) usan polinomios binarios.", "consecuencia_de_error": "Corrupción de datos en transmisiones de red."},
                    "quimica": {"uso": "Ajuste de curvas de calibración experimental.", "consecuencia_de_error": "Mediciones de laboratorio inexactas."},
                    "civil": {"uso": "La curva de deflexión de una viga es un polinomio de cuarto grado.", "consecuencia_de_error": "Cálculo incorrecto de la deformación de un puente."},
                    "mecanica": {"uso": "Diseño de levas (cam profiles) para movimientos suaves.", "consecuencia_de_error": "Vibración y desgaste excesivo en el motor."},
                    "mecatronica": {"uso": "Interpolación de trayectorias de robots (splines cúbicos).", "consecuencia_de_error": "Movimiento robótico brusco o impreciso."},
                    "aeronautica": {"uso": "El perfil alar (forma del ala) se describe con polinomios.", "consecuencia_de_error": "Mal rendimiento aerodinámico."},
                    "electrica": {"uso": "Funciones de transferencia de filtros analógicos.", "consecuencia_de_error": "El filtro no elimina el ruido deseado."}
                }
            },
            {
                "subtema_titulo": "6. Funciones Racionales (Polos y Asíntotas)",
                "definicion": "Son divisiones de polinomios: f(x) = P(x) / Q(x). Los 'Polos' son los valores que hacen cero al denominador (Q(x)=0), creando asíntotas verticales (la función explota a infinito). Son cruciales para la estabilidad.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = 1 / (x - 3).\nEl denominador es cero cuando x = 3.\nHay una Asíntota Vertical (Polo) en x = 3.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para f(x) = 5 / (x + 4), hay una asíntota vertical en x = ... (Solo el número)",
                        "respuesta_correcta": "-4",
                        "opciones": ["-4", "4", "5", "0"]
                    },
                    "similares": [
                        {"pregunta": "Para f(x) = 1/x, el polo está en x = ...", "respuesta_correcta": "0", "opciones": ["0", "1", "-1", "infinity"]},
                        {"pregunta": "¿Puede una función racional cruzar su asíntota vertical? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Si el denominador es (x-1)(x-2), hay polos en 1 y ...", "respuesta_correcta": "2", "opciones": ["2", "-2", "0", "-1"]},
                        {"pregunta": "En f(x) = x / (x - 5), el dominio son todos los reales excepto...", "respuesta_correcta": "5", "opciones": ["5", "-5", "0", "1"]},
                        {"pregunta": "Un polo en el lado derecho del plano complejo indica un sistema... (estable/inestable)", "respuesta_correcta": "inestable", "opciones": ["inestable", "estable", "neutro", "seguro"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de rendimiento: cuando la carga (x) se acerca a la capacidad máxima, el tiempo de respuesta (y) tiende a infinito (asíntota).", "consecuencia_de_error": "Colapso del servidor bajo carga."},
                    "quimica": {"uso": "Isotermas de adsorción (modelo de Langmuir).", "consecuencia_de_error": "Cálculo erróneo de la capacidad de un filtro."},
                    "civil": {"uso": "Fenómeno de resonancia en puentes: cuando la frecuencia de paso se acerca a la natural, la vibración tiende a infinito.", "consecuencia_de_error": "Colapso del puente (ej. Tacoma Narrows)."},
                    "mecanica": {"uso": "Resonancia mecánica en ejes giratorios.", "consecuencia_de_error": "Destrucción de la máquina."},
                    "mecatronica": {"uso": "Análisis de estabilidad de control (Lugar de las Raíces). Los polos determinan si el robot es estable.", "consecuencia_de_error": "El robot oscila sin control o se rompe."},
                    "aeronautica": {"uso": "Estabilidad dinámica de la aeronave.", "consecuencia_de_error": "Avión incontrolable."},
                    "electrica": {"uso": "Diseño de filtros y amplificadores. Los polos definen la frecuencia de corte y la resonancia.", "consecuencia_de_error": "El circuito oscila (aulla) en lugar de amplificar."}
                }
            },
            {
                "subtema_titulo": "7. Funciones Exponenciales (Crecimiento Rápido)",
                "definicion": "Funciones de la forma f(x) = aˣ (base constante, exponente variable). Modelan procesos donde el cambio es proporcional al tamaño actual (como bacterias o interés compuesto). Crecen más rápido que cualquier polinomio.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Crecimiento de bacterias. P(t) = 100 * 2ᵗ (se duplican cada hora).\nEn t=0: 100.\nEn t=1: 200.\nEn t=2: 400.\nEn t=3: 800.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = 2ˣ, ¿cuánto vale f(5)? (2*2*2*2*2)",
                        "respuesta_correcta": "32",
                        "opciones": ["32", "10", "25", "16"]
                    },
                    "similares": [
                        {"pregunta": "Si f(x) = 10ˣ, calcula f(2).", "respuesta_correcta": "100", "opciones": ["100", "20", "10", "200"]},
                        {"pregunta": "Cualquier base (positiva) a la potencia 0 es...", "respuesta_correcta": "1", "opciones": ["1", "0", "base", "indefinido"]},
                        {"pregunta": "En eˣ, la base 'e' vale aproximadamente...", "respuesta_correcta": "2.7", "opciones": ["2.7", "3.14", "1.6", "1.4"]},
                        {"pregunta": "Si una población se triplica cada hora, la base es...", "respuesta_correcta": "3", "opciones": ["3", "2", "1.5", "10"]},
                        {"pregunta": "3³ es igual a...", "respuesta_correcta": "27", "opciones": ["27", "9", "6", "33"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Complejidad exponencial O(2ⁿ) en algoritmos de fuerza bruta (ej. romper contraseñas).", "consecuencia_de_error": "El algoritmo nunca termina si los datos crecen un poco."},
                    "quimica": {"uso": "Cinética de reacción de primer orden (decaimiento exponencial).", "consecuencia_de_error": "Cálculo erróneo de la vida media de un reactivo."},
                    "civil": {"uso": "Amortiguamiento de vibraciones en edificios (la amplitud decae exponencialmente).", "consecuencia_de_error": "Subestimar el tiempo que un edificio vibrará tras un sismo."},
                    "mecanica": {"uso": "Ley de enfriamiento de Newton (la temperatura baja exponencialmente).", "consecuencia_de_error": "Tocar una pieza caliente antes de tiempo."},
                    "mecatronica": {"uso": "Carga de un capacitor en un circuito RC (base de temporizadores).", "consecuencia_de_error": "Tiempos de retardo incorrectos en el control."},
                    "aeronautica": {"uso": "Variación de la presión atmosférica con la altitud.", "consecuencia_de_error": "Calibración errónea de altímetros."},
                    "electrica": {"uso": "Respuesta transitoria de circuitos (encendido/apagado).", "consecuencia_de_error": "Picos de voltaje no previstos que queman componentes."}
                }
            },
            {
                "subtema_titulo": "8. Funciones Logarítmicas (Escalas)",
                "definicion": "Son la inversa de las exponenciales. y = logₐ(x) significa '¿a qué potencia debo elevar 'a' para obtener 'x'?'. Se usan para manejar rangos de números gigantescos (como la intensidad del sonido o terremotos).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: log₁₀(1000) = ?\nPregunta: ¿10 a la qué potencia da 1000?\n10³ = 1000.\nResultado: 3.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula log₂(8). (2 elevado a qué potencia da 8?)",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "4", "2", "8"]
                    },
                    "similares": [
                        {"pregunta": "Calcula log₁₀(100).", "respuesta_correcta": "2", "opciones": ["2", "10", "1", "100"]},
                        {"pregunta": "Calcula log₅(25).", "respuesta_correcta": "2", "opciones": ["2", "5", "1", "25"]},
                        {"pregunta": "Calcula el logaritmo natural ln(e).", "respuesta_correcta": "1", "opciones": ["1", "0", "e", "2.7"]},
                        {"pregunta": "log(1) es siempre...", "respuesta_correcta": "0", "opciones": ["0", "1", "undefined", "10"]},
                        {"pregunta": "Si 10ˣ = 10000, entonces x es...", "respuesta_correcta": "4", "opciones": ["4", "3", "5", "1000"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Búsqueda binaria (complejidad O(log n)). Es la forma más eficiente de buscar datos.", "consecuencia_de_error": "Usar búsqueda lineal en lugar de logarítmica hace que las bases de datos sean lentas."},
                    "quimica": {"uso": "Cálculo de pH (escala logarítmica negativa de la concentración de H+).", "consecuencia_de_error": "Un pequeño error en pH es un gran cambio en acidez."},
                    "civil": {"uso": "Escala de Richter (sismos). Un sismo grado 7 es 10 veces más fuerte que uno grado 6.", "consecuencia_de_error": "Subestimar la magnitud de un terremoto."},
                    "mecanica": {"uso": "Análisis de ruido y vibraciones (Decibelios).", "consecuencia_de_error": "Daño auditivo o estructural por subestimar la energía del sonido."},
                    "mecatronica": {"uso": "Sensores con respuesta logarítmica (ej. ojos humanos, sensores de luz).", "consecuencia_de_error": "Mala calibración de sensores de luminosidad."},
                    "aeronautica": {"uso": "Cálculo de la altitud de densidad.", "consecuencia_de_error": "Errores en el rendimiento de despegue."},
                    "electrica": {"uso": "Diagramas de Bode (respuesta en frecuencia). Usan escala logarítmica en ambos ejes.", "consecuencia_de_error": "Diseño incorrecto de filtros y amplificadores."}
                }
            },
            {
                "subtema_titulo": "9. Funciones Trigonométricas (Ondas y Ciclos)",
                "definicion": "Seno y Coseno modelan fenómenos periódicos (que se repiten), como el sonido, la luz y la corriente alterna. Propiedades clave: Amplitud (altura), Periodo (tiempo de un ciclo) y Frecuencia (ciclos por segundo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y = 5 * sen(x). La Amplitud es 5 (la onda sube hasta 5 y baja hasta -5).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para y = 10 cos(x), ¿cuál es la amplitud máxima?",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "1", "5", "20"]
                    },
                    "similares": [
                        {"pregunta": "El valor máximo de sen(x) es...", "respuesta_correcta": "1", "opciones": ["1", "0", "infinity", "-1"]},
                        {"pregunta": "El valor mínimo de cos(x) es...", "respuesta_correcta": "-1", "opciones": ["-1", "0", "1", "-10"]},
                        {"pregunta": "Una función que se repite se llama...", "respuesta_correcta": "periodica", "opciones": ["periodica", "lineal", "exponencial", "logaritmica"]},
                        {"pregunta": "Si la frecuencia es alta, el periodo es... (corto/largo)", "respuesta_correcta": "corto", "opciones": ["corto", "largo", "igual", "cero"]},
                        {"pregunta": "Para y = sen(x) + 2, la onda se desplaza hacia...", "respuesta_correcta": "arriba", "opciones": ["arriba", "abajo", "derecha", "izquierda"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Compresión de audio (MP3) y video (JPEG/MPEG) usando la Transformada Discreta del Coseno.", "consecuencia_de_error": "Archivos gigantes o de mala calidad."},
                    "quimica": {"uso": "Espectroscopía (análisis de ondas de luz emitidas por átomos).", "consecuencia_de_error": "Identificación incorrecta de sustancias."},
                    "civil": {"uso": "Análisis de sismos (ondas en el suelo) y mareas.", "consecuencia_de_error": "Edificios que no resisten la frecuencia de un sismo."},
                    "mecanica": {"uso": "Análisis de vibraciones en maquinaria rotativa.", "consecuencia_de_error": "Falla por fatiga debido a vibración excesiva."},
                    "mecatronica": {"uso": "Generación de señales PWM para control de motores.", "consecuencia_de_error": "Control de motor inestable."},
                    "aeronautica": {"uso": "Navegación por ondas de radio (VOR, GPS).", "consecuencia_de_error": "Errores de posición."},
                    "electrica": {"uso": "Corriente Alterna (AC). Todo el sistema eléctrico mundial es una onda senoidal.", "consecuencia_de_error": "Apagones y fallas de equipo."}
                }
            },
            {
                "subtema_titulo": "10. Transformación de Funciones (Desplazamientos)",
                "definicion": "Cómo cambiar la gráfica de una función sumando o multiplicando constantes. f(x) + c (sube), f(x+c) (izquierda), k*f(x) (estira verticalmente).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x². g(x) = (x-2)² + 3.\n1. (x-2): Desplaza la parábola 2 unidades a la derecha.\n2. +3: Desplaza la parábola 3 unidades hacia arriba.\nVértice nuevo: (2, 3).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si mueves f(x)=x² tres unidades hacia arriba, la nueva ecuación es: y = x² + ...",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "-3", "0", "9"]
                    },
                    "similares": [
                        {"pregunta": "Si mueves f(x) dos unidades a la derecha, escribes f(x - ...)", "respuesta_correcta": "2", "opciones": ["2", "-2", "0", "1"]},
                        {"pregunta": "Para invertir una función verticalmente (espejo), multiplicas por...", "respuesta_correcta": "-1", "opciones": ["-1", "1", "0", "2"]},
                        {"pregunta": "Si f(x) = |x|, la gráfica tiene forma de letra...", "respuesta_correcta": "v", "opciones": ["v", "u", "w", "l"]},
                        {"pregunta": "f(x-5) mueve la gráfica a la... (derecha/izquierda)", "respuesta_correcta": "derecha", "opciones": ["derecha", "izquierda", "arriba", "abajo"]},
                        {"pregunta": "2*f(x) hace la gráfica más... (alta/baja)", "respuesta_correcta": "alta", "opciones": ["alta", "baja", "ancha", "angosta"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de señales: amplificar (k*f), añadir 'offset' (f+c) o retrasar (f(t-c)).", "consecuencia_de_error": "Señales corruptas o fuera de rango."},
                    "quimica": {"uso": "Calibración de instrumentos: ajustar el cero (offset) y la ganancia (escala).", "consecuencia_de_error": "Mediciones sistemáticamente erróneas."},
                    "civil": {"uso": "Ajuste de curvas de diseño a la topografía real.", "consecuencia_de_error": "Carreteras que no se alinean con el terreno."},
                    "mecanica": {"uso": "Ajuste de controladores PID (sintonización de ganancias).", "consecuencia_de_error": "Control inestable."},
                    "mecatronica": {"uso": "Normalización de datos de sensores para que estén entre 0 y 1.", "consecuencia_de_error": "Algoritmos de IA que no convergen."},
                    "aeronautica": {"uso": "Trimado (ajuste fino) de las superficies de control.", "consecuencia_de_error": "El piloto debe pelear constantemente con los controles."},
                    "electrica": {"uso": "Acondicionamiento de señales (Amplificadores Operacionales).", "consecuencia_de_error": "La señal es demasiado débil para ser leída por el microcontrolador."}
                }
            }
        ]
    },

    "CALCULO DIFERENCIAL": {
        "nombre_completo": "Cálculo Diferencial: La Ciencia del Cambio",
        "prerequisitos": ["PRECALCULO"],
        "quiz": [
            {
                "pregunta": "¿Cuál es el límite de f(x)=x+2 cuando x tiende a 3?",
                "respuesta": "5",
                "opciones": ["5", "1", "6", "0"]
            },
            {
                "pregunta": "La derivada de una constante (ej. f(x)=5) es siempre...",
                "respuesta": "0",
                "opciones": ["0", "1", "x", "5"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. El Concepto de Límite",
                "definicion": "El 'Límite' describe el comportamiento de una función f(x) cuando 'x' se acerca infinitamente a un valor 'c', sin necesariamente llegar a tocarlo. Es la base para definir la continuidad y la derivada. Se escribe: lim(x→c) f(x) = L. ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Límite de f(x) = (x² - 1) / (x - 1) cuando x → 1.\n1. Sustitución directa: (1-1)/(1-1) = 0/0 (Indeterminado).\n2. Factorizar: (x-1)(x+1) / (x-1).\n3. Cancelar: Nos queda (x+1).\n4. Evaluar límite: 1 + 1 = 2.\nResultado: 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el límite de f(x) = x + 5 cuando x tiende a 3. (Solo el número)",
                        "respuesta_correcta": "8",
                        "opciones": ["8", "2", "15", "3"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el límite de f(x) = 2x cuando x tiende a 4.", "respuesta_correcta": "8", "opciones": ["8", "6", "2", "4"]},
                        {"pregunta": "Límite de f(x) = (x² - 9)/(x - 3) cuando x tiende a 3. (Pista: Factoriza)", "respuesta_correcta": "6", "opciones": ["6", "0", "indefinido", "9"]},
                        {"pregunta": "Si el límite por la izquierda es 5 y por la derecha es 5, el límite es...", "respuesta_correcta": "5", "opciones": ["5", "0", "indefinido", "10"]},
                        {"pregunta": "Si el límite por la izquierda es 2 y por la derecha es 4, el límite...", "respuesta_correcta": "no existe", "opciones": ["no existe", "es 3", "es 2", "es 4"]},
                        {"pregunta": "Límite de una constante f(x)=10 cuando x tiende a 1000.", "respuesta_correcta": "10", "opciones": ["10", "0", "1000", "infinito"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de complejidad asintótica (Big O). Se evalúa el límite del tiempo de ejecución cuando los datos (n) tienden a infinito.", "consecuencia_de_error": "No prever que un algoritmo colapsará el servidor cuando aumenten los usuarios."},
                    "quimica": {"uso": "Definición de 'velocidad de reacción instantánea': el límite del cambio de concentración cuando el tiempo tiende a cero.", "consecuencia_de_error": "Medición imprecisa de la cinética de una reacción rápida."},
                    "civil": {"uso": "Análisis de carga crítica en columnas. Se evalúa el límite de la estabilidad antes del pandeo.", "consecuencia_de_error": "Falla estructural súbita."},
                    "mecanica": {"uso": "Definición de 'velocidad instantánea'. Sin límites, solo tendríamos velocidad promedio.", "consecuencia_de_error": "Imposible diseñar velocímetros o sistemas de frenado ABS."},
                    "mecatronica": {"uso": "Análisis de estabilidad de control: ver si el error del sistema tiende a cero cuando el tiempo tiende a infinito (lim t→∞ e(t) = 0).", "consecuencia_de_error": "Un robot que nunca se estabiliza y oscila eternamente."},
                    "aeronautica": {"uso": "Análisis de flujo compresible cerca de la velocidad del sonido (Mach 1), donde las ecuaciones presentan singularidades (límites infinitos).", "consecuencia_de_error": "Ondas de choque inesperadas que destruyen el ala."},
                    "electrica": {"uso": "Respuesta en estado estacionario: el límite del voltaje/corriente cuando t → ∞.", "consecuencia_de_error": "Diseñar un circuito pensando que se estabilizará en 5V cuando en realidad oscila."}
                }
            },
            {
                "subtema_titulo": "2. Continuidad",
                "definicion": "Una función es 'continua' si no tiene saltos, huecos o asíntotas. Matemáticamente: el límite cuando x→c existe y es igual al valor de la función f(c). Es decir, puedes dibujar la gráfica sin despegar el lápiz.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = 1/x.\n¿Es continua en x=0? No.\n1. f(0) no está definida (división por cero).\n2. El límite cuando x→0 no existe (va a infinito).\nHay una 'discontinuidad de salto infinito'.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La función f(x) = 1/(x-2) tiene una discontinuidad en x = ... (Solo el número)",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "-2", "0", "1"]
                    },
                    "similares": [
                        {"pregunta": "¿La función f(x) = x² es continua en todos los reales? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "Una función con un 'agujero' en la gráfica es...", "respuesta_correcta": "discontinua", "opciones": ["discontinua", "continua", "derivable", "constante"]},
                        {"pregunta": "Si lim x->a f(x) ≠ f(a), la función es discontinua.", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La función f(x) = |x| (valor absoluto) es continua en x=0? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "¿En qué valor tiene discontinuidad f(x) = (x+1)/(x+5)?", "respuesta_correcta": "-5", "opciones": ["-5", "5", "1", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En renderizado de gráficos, las superficies deben ser continuas para que la luz se refleje bien (sin costuras visibles).", "consecuencia_de_error": "Grietas visibles en los modelos 3D o artefactos de iluminación."},
                    "quimica": {"uso": "Las propiedades termodinámicas (como la Entropía) deben ser continuas. Un salto indica un 'cambio de fase' (ej. líquido a gas).", "consecuencia_de_error": "No detectar un punto de ebullición o congelación en el diseño de una tubería."},
                    "civil": {"uso": "La curva de deflexión de una viga debe ser continua. Un 'salto' significaría que la viga está rota.", "consecuencia_de_error": "Modelo matemático que permite vigas rotas como soluciones válidas."},
                    "mecanica": {"uso": "Perfiles de levas y engranajes. La superficie debe ser continua y suave para evitar golpes.", "consecuencia_de_error": "Desgaste prematuro, ruido excesivo y vibración."},
                    "mecatronica": {"uso": "Trayectorias de robots. El movimiento debe ser continuo (sin teletransportación) y suave.", "consecuencia_de_error": "Movimientos bruscos que dañan los motores o tiran la carga."},
                    "aeronautica": {"uso": "Continuidad del flujo de aire sobre el ala. Si el flujo se separa (discontinuidad), el avión entra en pérdida.", "consecuencia_de_error": "Pérdida súbita de sustentación."},
                    "electrica": {"uso": "La corriente en un inductor y el voltaje en un capacitor deben ser funciones continuas (no pueden cambiar instantáneamente).", "consecuencia_de_error": "Picos de voltaje infinitos teóricos que queman componentes en la realidad."}
                }
            },
            {
                "subtema_titulo": "3. La Derivada (Definición Geométrica)",
                "definicion": "La derivada f'(x) es la pendiente de la 'recta tangente' a la curva en un punto. Mide qué tan inclinada está la función. Si la pendiente es positiva, la función crece; si es negativa, decrece; si es cero, es un punto plano (posible máximo o mínimo). ",
                "diagrama": "GIFS/derivada.gif",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x². En x=3.\nLa derivada es f'(x) = 2x.\nLa pendiente en x=3 es 2(3) = 6.\nSignifica que por cada 1 unidad que avanzas en x, la función sube 6 unidades en ese instante.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = 5x + 2 (una recta), ¿cuál es su derivada (pendiente) constante?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "2", "5x", "7"]
                    },
                    "similares": [
                        {"pregunta": "La derivada de una línea horizontal (f(x)=3) es...", "respuesta_correcta": "0", "opciones": ["0", "1", "x", "3"]},
                        {"pregunta": "Si la derivada es negativa, la función está...", "respuesta_correcta": "decreciendo", "opciones": ["decreciendo", "creciendo", "constante", "cero"]},
                        {"pregunta": "La derivada representa la pendiente de la recta...", "respuesta_correcta": "tangente", "opciones": ["tangente", "secante", "normal", "paralela"]},
                        {"pregunta": "Si f(x) = x, su derivada es...", "respuesta_correcta": "1", "opciones": ["1", "x", "0", "2"]},
                        {"pregunta": "En un pico máximo de una montaña rusa, la pendiente (derivada) es...", "respuesta_correcta": "0", "opciones": ["0", "positiva", "negativa", "infinita"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En IA (Redes Neuronales), el 'gradiente' es un vector de derivadas que indica la 'pendiente' del error.", "consecuencia_de_error": "La red neuronal no puede aprender porque no sabe en qué dirección 'bajar' para reducir el error."},
                    "quimica": {"uso": "La derivada de la concentración respecto al tiempo es la 'Velocidad de Reacción'.", "consecuencia_de_error": "No saber qué tan rápido ocurre una reacción exotérmica puede causar una explosión."},
                    "civil": {"uso": "La derivada de la posición (topografía) es la pendiente del terreno.", "consecuencia_de_error": "Diseñar una carretera con una pendiente imposible de subir para los camiones."},
                    "mecanica": {"uso": "La derivada de la posición es la Velocidad. La derivada de la velocidad es la Aceleración.", "consecuencia_de_error": "Imposible analizar fuerzas (F=ma) si no puedes calcular la aceleración desde la posición."},
                    "mecatronica": {"uso": "Para medir la velocidad de un motor usando solo un sensor de posición (encoder). El software deriva la posición.", "consecuencia_de_error": "Lecturas de velocidad ruidosas o retrasadas, causando inestabilidad en el control."},
                    "aeronautica": {"uso": "La derivada del perfil del ala (su curvatura) determina la distribución de presión.", "consecuencia_de_error": "Diseño de ala ineficiente con mucho arrastre."},
                    "electrica": {"uso": "La derivada del flujo magnético respecto al tiempo es el Voltaje inducido (Ley de Faraday: V = -dΦ/dt).", "consecuencia_de_error": "No entender cómo funcionan los generadores, transformadores ni motores."}
                }
            },
            {
                "subtema_titulo": "4. Regla de la Potencia",
                "definicion": "Es el atajo para derivar funciones tipo xⁿ. La regla es: baja el exponente y réstale uno. d/dx (xⁿ) = n*xⁿ⁻¹. La derivada de una constante sola es 0.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Derivar f(x) = x³ + 5x² - 10.\n1. x³ -> 3x²\n2. 5x² -> 5 * (2x¹) = 10x\n3. -10 -> 0 (es constante)\nResultado: f'(x) = 3x² + 10x.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la derivada de f(x) = x⁴. (Usa ^ para potencia)",
                        "respuesta_correcta": "4x^3",
                        "opciones": ["4x^3", "x^3", "3x^4", "4x"]
                    },
                    "similares": [
                        {"pregunta": "Calcula la derivada de f(x) = x⁶.", "respuesta_correcta": "6x^5", "opciones": ["6x^5", "x^5", "5x^6", "6x"]},
                        {"pregunta": "Calcula la derivada de f(x) = 3x².", "respuesta_correcta": "6x", "opciones": ["6x", "3x", "9x^2", "6x^2"]},
                        {"pregunta": "Calcula la derivada de f(x) = 100 (constante).", "respuesta_correcta": "0", "opciones": ["0", "100", "1", "x"]},
                        {"pregunta": "Calcula la derivada de f(x) = x⁻² (-2*x^-3).", "respuesta_correcta": "-2x^-3", "opciones": ["-2x^-3", "-2x^-1", "x^-3", "-x^-2"]},
                        {"pregunta": "Calcula la derivada de f(x) = 5x + 2.", "respuesta_correcta": "5", "opciones": ["5", "2", "5x", "7"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de sensibilidad en algoritmos numéricos.", "consecuencia_de_error": "Errores de redondeo que se amplifican incontrolablemente."},
                    "quimica": {"uso": "Ecuaciones de estado viriales (series de potencias para gases reales).", "consecuencia_de_error": "Cálculos de presión incorrectos a altas densidades."},
                    "civil": {"uso": "Cálculo de la fuerza cortante (V) derivando la ecuación de momento (M), que suele ser un polinomio.", "consecuencia_de_error": "Diseño de vigas que fallan por corte."},
                    "mecanica": {"uso": "Energía Cinética (K = ½mv²). La derivada respecto a la velocidad es el Momento (mv).", "consecuencia_de_error": "Errores en cálculos de impulso y choque."},
                    "mecatronica": {"uso": "Linealización de sensores cuya respuesta es polinómica.", "consecuencia_de_error": "Mediciones inexactas en los extremos del rango del sensor."},
                    "aeronautica": {"uso": "Relación entre potencia requerida y velocidad (la potencia varía con v³).", "consecuencia_de_error": "Subestimar drásticamente la potencia necesaria para volar más rápido."},
                    "electrica": {"uso": "Potencia P = I²R. La tasa de cambio de la potencia respecto a la corriente es 2IR.", "consecuencia_de_error": "Análisis de sensibilidad térmica de circuitos."}
                }
            },
            {
                "subtema_titulo": "5. Regla del Producto",
                "definicion": "Para derivar dos funciones que se multiplican: f(x) * g(x). No es solo multiplicar derivadas. La fórmula es: (f * g)' = f'g + fg' (La derivada del primero por el segundo, más el primero por la derivada del segundo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y = x² * sen(x)\nf = x², g = sen(x)\nf' = 2x, g' = cos(x)\nResultado: 2x*sen(x) + x²*cos(x).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = x * x, usando la regla del producto (1*x + x*1), ¿qué obtienes?",
                        "respuesta_correcta": "2x",
                        "opciones": ["2x", "x^2", "1", "2"]
                    },
                    "similares": [
                        {"pregunta": "Derivada de x * eˣ. (f=x, g=eˣ).", "respuesta_correcta": "e^x+xe^x", "opciones": ["e^x+xe^x", "xe^x", "e^x", "2xe^x"]},
                        {"pregunta": "Derivada de 5x * x². (5*x² + 5x*2x) = 15x². (Verifícalo derivando 5x³).", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "En la regla f'g + fg', f es la... función.", "respuesta_correcta": "primera", "opciones": ["primera", "segunda", "última", "constante"]},
                        {"pregunta": "Derivada de x * ln(x). (1*ln(x) + x*(1/x))", "respuesta_correcta": "ln(x)+1", "opciones": ["ln(x)+1", "ln(x)", "1/x", "x"]},
                        {"pregunta": "¿La derivada de (f*g) es f' * g'?", "respuesta_correcta": "no", "opciones": ["no", "si"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de probabilidades conjuntas variables en el tiempo d(P(A)*P(B))/dt.", "consecuencia_de_error": "Modelos probabilísticos dinámicos erróneos."},
                    "quimica": {"uso": "Ley de los Gases Ideales derivada respecto al tiempo (PV = nRT), donde P y V cambian simultáneamente.", "consecuencia_de_error": "Errores en el control de reactores a presión variable."},
                    "civil": {"uso": "Carga variable en una viga de longitud variable (ej. puente levadizo o grúa telescópica).", "consecuencia_de_error": "Falla estructural durante el movimiento."},
                    "mecanica": {"uso": "Potencia = Torque * Velocidad Angular. Si ambos cambian, se necesita la regla del producto para hallar la tasa de cambio de potencia.", "consecuencia_de_error": "Mal diseño de sistemas de transmisión de potencia variable."},
                    "mecatronica": {"uso": "Control de robots con masa variable (ej. un robot que vacía una botella mientras la mueve).", "consecuencia_de_error": "El robot pierde precisión a medida que cambia la masa."},
                    "aeronautica": {"uso": "Empuje = Flujo Masico * Velocidad de Salida. Ambos cambian con la altura.", "consecuencia_de_error": "Cálculo erróneo del rendimiento del motor en ascenso."},
                    "electrica": {"uso": "Potencia P = V(t) * I(t) en corriente alterna. La derivada instantánea requiere la regla del producto.", "consecuencia_de_error": "Análisis incorrecto de la potencia instantánea y el factor de potencia."}
                }
            },
            {
                "subtema_titulo": "6. Regla del Cociente",
                "definicion": "Para derivar una división: f(x) / g(x). Fórmula: (f'g - fg') / g². (Derivada del de arriba por el de abajo, MENOS el de arriba por derivada del de abajo, todo sobre el de abajo al cuadrado).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Derivar tan(x) = sen(x) / cos(x).\nf=sen, g=cos. f'=cos, g'=-sen.\n(cos*cos - sen*(-sen)) / cos²\n(cos² + sen²) / cos² = 1 / cos² = sec²(x).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Derivada de 1/x usando regla del cociente. (0*x - 1*1)/x²",
                        "respuesta_correcta": "-1/x^2",
                        "opciones": ["-1/x^2", "1/x", "ln(x)", "-1/x"]
                    },
                    "similares": [
                        {"pregunta": "En la fórmula (f'g - fg')/g², ¿qué función es 'g'?", "respuesta_correcta": "abajo", "opciones": ["abajo", "arriba", "izquierda", "derecha"]},
                        {"pregunta": "Derivada de x / (x+1).", "respuesta_correcta": "1/(x+1)^2", "opciones": ["1/(x+1)^2", "-1/(x+1)^2", "1", "2x"]},
                        {"pregunta": "Si f(x) = 5/x², ¿cuál es su derivada? (-10/x^3)", "respuesta_correcta": "-10/x^3", "opciones": ["-10/x^3", "10/x", "5/x", "-5/x^3"]},
                        {"pregunta": "¿El orden importa en la resta del numerador (f'g - fg')?", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "Derivada de eˣ / x. (x*eˣ - eˣ)/x²", "respuesta_correcta": "(xe^x-e^x)/x^2", "opciones": ["(xe^x-e^x)/x^2", "e^x/x^2", "e^x", "(e^x-xe^x)/x^2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de eficiencia: Operaciones por segundo (Ops/sec). Derivar para encontrar el pico de eficiencia.", "consecuencia_de_error": "Mala gestión de recursos del servidor."},
                    "quimica": {"uso": "Concentración = Moles / Volumen. Si el volumen cambia (dilución), la tasa de cambio de concentración requiere esta regla.", "consecuencia_de_error": "Errores en el control de concentración en reactores de volumen variable."},
                    "civil": {"uso": "Esfuerzo = Fuerza / Área. Si el área cambia (ej. corrosión) y la fuerza cambia, se necesita la regla del cociente.", "consecuencia_de_error": "No predecir la falla de materiales que se degradan."},
                    "mecanica": {"uso": "Presión = Fuerza / Área. Tasa de cambio de presión en un pistón.", "consecuencia_de_error": "Diseño incorrecto de sistemas hidráulicos."},
                    "mecatronica": {"uso": "Relación de transmisión variable (CVT). Derivar la relación de velocidades.", "consecuencia_de_error": "Control inestable de la transmisión."},
                    "aeronautica": {"uso": "Relación Sustentación/Arrastre (L/D). Encontrar la velocidad que maximiza este cociente (máximo alcance).", "consecuencia_de_error": "Planificación de vuelo ineficiente, mayor consumo de combustible."},
                    "electrica": {"uso": "Resistencia = Voltaje / Corriente. Análisis de resistencias dinámicas.", "consecuencia_de_error": "Modelado incorrecto de componentes no lineales como diodos."}
                }
            },
            {
                "subtema_titulo": "7. Regla de la Cadena (Funciones Compuestas)",
                "definicion": "La regla más importante. Sirve para derivar funciones dentro de funciones: f(g(x)). Regla: Deriva la función de afuera (evaluada en la de adentro) y multiplica por la derivada de la de adentro. dy/dx = dy/du * du/dx.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y = (3x + 1)²\n1. Afuera: u², derivada 2u.\n2. Adentro: u = 3x+1, derivada 3.\n3. Multiplicar: 2(3x+1) * 3 = 6(3x+1).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Deriva sen(2x). (Derivada de sen(u) es cos(u), derivada de 2x es 2)",
                        "respuesta_correcta": "2cos(2x)",
                        "opciones": ["2cos(2x)", "cos(2x)", "2sen(2x)", "-cos(2x)"]
                    },
                    "similares": [
                        {"pregunta": "Deriva (x² + 1)⁵. (5(x²+1)⁴ * 2x)", "respuesta_correcta": "10x(x^2+1)^4", "opciones": ["10x(x^2+1)^4", "5(x^2+1)^4", "10x", "5x(x^2+1)"]},
                        {"pregunta": "Deriva e^(3x). (e^u * u')", "respuesta_correcta": "3e^(3x)", "opciones": ["3e^(3x)", "e^(3x)", "e^(3x)/3", "3xe^(3x)"]},
                        {"pregunta": "Deriva cos(x²). (-sen(x²) * 2x)", "respuesta_correcta": "-2xsen(x^2)", "opciones": ["-2xsen(x^2)", "sen(x^2)", "2xcos(x^2)", "-2x"]},
                        {"pregunta": "Deriva √ (2x). (1/(2√2x) * 2)", "respuesta_correcta": "1/sqrt(2x)", "opciones": ["1/sqrt(2x)", "1/2sqrt(x)", "sqrt(2)", "1"]},
                        {"pregunta": "Deriva ln(5x). (1/(5x) * 5)", "respuesta_correcta": "1/x", "opciones": ["1/x", "1/5x", "5/x", "5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Backpropagation en Redes Neuronales. Es literalmente la aplicación repetida de la regla de la cadena para calcular gradientes.", "consecuencia_de_error": "La IA no funciona. Punto."},
                    "quimica": {"uso": "Cinética compleja: La velocidad depende de la Concentración, que depende del Tiempo. v = f(C(t)).", "consecuencia_de_error": "Modelos cinéticos inservibles."},
                    "civil": {"uso": "Efectos térmicos: El estrés depende de la expansión, que depende de la temperatura, que depende del tiempo. σ(ε(T(t))).", "consecuencia_de_error": "No prever fallas por ciclos térmicos (día/noche)."},
                    "mecanica": {"uso": "Transmisión de movimiento a través de mecanismos enlazados. Velocidad final = v1 * v2 * v3...", "consecuencia_de_error": "Cálculo erróneo de velocidades en maquinaria compleja."},
                    "mecatronica": {"uso": "Sistemas de control en cascada. El control de posición depende del control de velocidad, que depende del control de corriente.", "consecuencia_de_error": "Inestabilidad del lazo de control."},
                    "aeronautica": {"uso": "Atmósfera estándar: La presión depende de la altitud, que depende del tiempo. P(h(t)).", "consecuencia_de_error": "Lecturas incorrectas de instrumentos durante ascenso/descenso."},
                    "electrica": {"uso": "Circuitos dependientes del tiempo. Voltaje depende de la carga, carga depende de la corriente, corriente depende del tiempo.", "consecuencia_de_error": "Análisis incorrecto de circuitos transitorios."}
                }
            },
            {
                "subtema_titulo": "8. Derivación Implícita",
                "definicion": "Se usa cuando 'y' no está despejada (ej. x² + y² = 25). Derivas término a término, y cada vez que derivas 'y', multiplicas por 'y''. Luego despejas 'y''.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: x² + y² = 25\n1. Derivar x²: 2x\n2. Derivar y²: 2y * y'\n3. Derivar 25: 0\n4. Ecuación: 2x + 2yy' = 0 -> 2yy' = -2x -> y' = -x/y.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la ecuación x + y = 10, deriva implícitamente para hallar y'. (1 + y' = 0)",
                        "respuesta_correcta": "-1",
                        "opciones": ["-1", "1", "0", "10"]
                    },
                    "similares": [
                        {"pregunta": "Deriva y² = x. (2y*y' = 1). Despeja y'.", "respuesta_correcta": "1/(2y)", "opciones": ["1/(2y)", "2y", "1/y", "1"]},
                        {"pregunta": "Deriva xy = 1. (Regla producto: 1*y + x*y' = 0). Despeja y'.", "respuesta_correcta": "-y/x", "opciones": ["-y/x", "y/x", "1/x", "-x/y"]},
                        {"pregunta": "En un círculo x²+y²=r², la pendiente y' es... (-x/y)", "respuesta_correcta": "-x/y", "opciones": ["-x/y", "x/y", "-y/x", "y/x"]},
                        {"pregunta": "Si y³ = x, ¿cuánto vale y'?", "respuesta_correcta": "1/(3y^2)", "opciones": ["1/(3y^2)", "3y^2", "1/3", "y^2"]},
                        {"pregunta": "¿La derivada implícita se usa cuando no puedes despejar 'y'?", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Gráficos por computadora: Trazado de curvas de nivel y superficies implícitas (metaballs).", "consecuencia_de_error": "Renderizado incorrecto de superficies orgánicas."},
                    "quimica": {"uso": "Termodinámica: Relaciones de Maxwell, donde las variables están entrelazadas (P, V, T, S).", "consecuencia_de_error": "Imposible derivar propiedades termodinámicas complejas."},
                    "civil": {"uso": "Análisis de estabilidad de taludes donde la superficie de falla tiene una forma compleja no explícita.", "consecuencia_de_error": "Cálculo erróneo del factor de seguridad del talud."},
                    "mecanica": {"uso": "Cinemática de mecanismos cerrados (ej. mecanismo de 4 barras). La posición de un eslabón depende implícitamente del otro.", "consecuencia_de_error": "No poder calcular velocidades en mecanismos articulados."},
                    "mecatronica": {"uso": "Restricciones de movimiento en robots paralelos.", "consecuencia_de_error": "Planificación de trayectoria que viola las restricciones mecánicas."},
                    "aeronautica": {"uso": "Diseño de perfiles alares definidos por ecuaciones implícitas.", "consecuencia_de_error": "Geometría del ala incorrecta."},
                    "electrica": {"uso": "Curvas características de componentes no lineales (diodos, transistores) dadas como I=f(V, I).", "consecuencia_de_error": "Punto de operación (bias) del circuito incorrecto."}
                }
            },
            {
                "subtema_titulo": "9. Derivadas de Orden Superior",
                "definicion": "Derivar la derivada. La primera derivada (f') es velocidad/pendiente. La segunda derivada (f'') es aceleración/concavidad. La tercera (f''') es el 'jerk' (tirón).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: f(x) = x³\nf'(x) = 3x²\nf''(x) = 6x\nf'''(x) = 6\nf''''(x) = 0.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x) = x⁴, ¿cuál es la segunda derivada f''(x)?",
                        "respuesta_correcta": "12x^2",
                        "opciones": ["12x^2", "4x^3", "12x", "24x"]
                    },
                    "similares": [
                        {"pregunta": "Si f(x) = sen(x), ¿cuál es la segunda derivada? (sen -> cos -> -sen)", "respuesta_correcta": "-sen(x)", "opciones": ["-sen(x)", "cos(x)", "sen(x)", "-cos(x)"]},
                        {"pregunta": "La segunda derivada de la posición es la...", "respuesta_correcta": "aceleracion", "opciones": ["aceleracion", "velocidad", "jerk", "fuerza"]},
                        {"pregunta": "Si f''(x) es positiva, la curva es cóncava hacia...", "respuesta_correcta": "arriba", "opciones": ["arriba", "abajo", "izquierda", "derecha"]},
                        {"pregunta": "Calcula la tercera derivada de f(x) = 5x² + x.", "respuesta_correcta": "0", "opciones": ["0", "10", "5", "1"]},
                        {"pregunta": "Si f(x) = eˣ, ¿cuál es su derivada número 100?", "respuesta_correcta": "e^x", "opciones": ["e^x", "100e^x", "xe^x", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de imágenes: La segunda derivada (Laplaciano) se usa para detectar bordes.", "consecuencia_de_error": "Algoritmos de visión artificial que no detectan objetos."},
                    "quimica": {"uso": "Ecuación de Schrödinger (depende de la segunda derivada de la función de onda).", "consecuencia_de_error": "Imposible resolver la estructura atómica."},
                    "civil": {"uso": "La ecuación de la viga relaciona la carga con la cuarta derivada de la deflexión (EI y'''' = q).", "consecuencia_de_error": "Fundamento absoluto del diseño de vigas. Sin esto, no hay rascacielos."},
                    "mecanica": {"uso": "Segunda Ley de Newton (F = m * x''). Dinámica.", "consecuencia_de_error": "Sin segunda derivada, no hay física dinámica."},
                    "mecatronica": {"uso": "Control de movimiento: Minimizar el 'Jerk' (tercera derivada) para que el robot no vibre.", "consecuencia_de_error": "Movimientos bruscos que desgastan los engranajes."},
                    "aeronautica": {"uso": "Radio de curvatura de una trayectoria (depende de y''). Importante para fuerzas G.", "consecuencia_de_error": "Maniobras que exceden la resistencia estructural o humana."},
                    "electrica": {"uso": "Ecuación de onda de señales electromagnéticas (segundas derivadas en espacio y tiempo).", "consecuencia_de_error": "No entender la propagación de señales."}
                }
            },
            {
                "subtema_titulo": "10. Optimización (Máximos y Mínimos)",
                "definicion": "El uso más práctico de la derivada. En un punto máximo o mínimo (cima o valle), la pendiente es plana (cero). Pasos: 1. Derivar f'(x). 2. Igualar a cero y resolver (Puntos Críticos). 3. Verificar si es máx o mín.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Minimizar f(x) = x² - 4x + 5.\n1. Derivar: f'(x) = 2x - 4.\n2. Igualar a cero: 2x - 4 = 0 -> 2x = 4 -> x = 2.\n3. Mínimo en x=2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Encuentra el valor de x que minimiza la función f(x) = x² - 10x. (Deriva e iguala a 0)",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "10", "0", "-5"]
                    },
                    "similares": [
                        {"pregunta": "Encuentra el máximo de f(x) = -x² + 4x. (Deriva: -2x+4=0)", "respuesta_correcta": "2", "opciones": ["2", "-2", "4", "0"]},
                        {"pregunta": "Para optimizar, igualamos la derivada a...", "respuesta_correcta": "0", "opciones": ["0", "1", "x", "infinito"]},
                        {"pregunta": "Si f'(c) = 0, 'c' se llama punto...", "respuesta_correcta": "critico", "opciones": ["critico", "inflexion", "asintota", "polo"]},
                        {"pregunta": "Un granjero quiere cercar el área máxima rectangular. ¿Qué forma debe tener?", "respuesta_correcta": "cuadrado", "opciones": ["cuadrado", "circulo", "largo", "triangulo"]},
                        {"pregunta": "Derivada de la ganancia = Ingreso marginal - Costo marginal. Para máxima ganancia, deben ser...", "respuesta_correcta": "iguales", "opciones": ["iguales", "diferentes", "cero", "maximo"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Entrenamiento de IA: Minimizar la 'función de pérdida' (error) ajustando los pesos.", "consecuencia_de_error": "La IA nunca aprende o se queda en un mínimo local malo."},
                    "quimica": {"uso": "Minimizar la Energía Libre de Gibbs para encontrar el estado de equilibrio.", "consecuencia_de_error": "Predicciones de reacciones incorrectas."},
                    "civil": {"uso": "Diseño de costo mínimo: Encontrar las dimensiones de una viga que soporten la carga con el menor material posible.", "consecuencia_de_error": "Estructuras innecesariamente caras y pesadas."},
                    "mecanica": {"uso": "Optimización de forma para reducir concentración de esfuerzos o arrastre aerodinámico.", "consecuencia_de_error": "Piezas que pesan más de lo necesario o consumen más energía."},
                    "mecatronica": {"uso": "Optimización de trayectoria: Mover el brazo del punto A al B en el menor tiempo o con la menor energía.", "consecuencia_de_error": "Robots lentos e ineficientes."},
                    "aeronautica": {"uso": "Encontrar la velocidad de crucero para máxima autonomía (máxima distancia por litro de combustible).", "consecuencia_de_error": "Rutas de vuelo ineficientes, aerolíneas perdiendo dinero."},
                    "electrica": {"uso": "Transferencia de máxima potencia: La resistencia de carga debe ser igual a la resistencia de la fuente.", "consecuencia_de_error": "Desperdicio de energía y señal débil en antenas."}
                }
            }
        ]
    },


    "VECTORES Y GEOMETRIA": {
        "nombre_completo": "Vectores y Geometría Plana",
        "prerequisitos": ["PRECALCULO"],
        "quiz": [
            {
                "pregunta": "Calcula la magnitud del vector v=(3, 4). (Solo el número)",
                "respuesta": "5",
                "opciones": ["5", "7", "25", "1"]
            },
            {
                "pregunta": "Calcula el producto punto de (1, 0) y (0, 1).",
                "respuesta": "0",
                "opciones": ["0", "1", "2", "-1"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Vectores en el Plano (Componentes)",
                "definicion": "Un vector en 2D es una cantidad con magnitud y dirección. Se representa como una flecha que va del origen (0,0) a un punto (x, y). Las coordenadas 'x' y 'y' se llaman componentes rectangulares.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Vector v que va de (0,0) a (3, 4).\nComponente x = 3.\nComponente y = 4.\nSe escribe v = (3, 4) o v = 3i + 4j.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Escribe las componentes del vector que va de (0,0) a (5, -2). (Formato: (x, y))",
                        "respuesta_correcta": "(5, -2)",
                        "opciones": ["(5, -2)", "(-5, 2)", "(5, 2)", "(2, 5)"]
                    },
                    "similares": [
                        {"pregunta": "Escribe las componentes del vector de (0,0) a (-1, 1).", "respuesta_correcta": "(-1, 1)", "opciones": ["(-1, 1)", "(1, -1)", "(-1, -1)", "(1, 1)"]},
                        {"pregunta": "Si v = 2i + 5j, escríbelo como par ordenado.", "respuesta_correcta": "(2, 5)", "opciones": ["(2, 5)", "(5, 2)", "(2, -5)", "(-2, 5)"]},
                        {"pregunta": "El vector cero es...", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "(1, 1)", "0", "undefined"]},
                        {"pregunta": "Un vector en el eje Y positivo tiene componente x igual a...", "respuesta_correcta": "0", "opciones": ["0", "1", "y", "-1"]},
                        {"pregunta": "Escribe el vector posición del punto (-3, 0).", "respuesta_correcta": "(-3, 0)", "opciones": ["(-3, 0)", "(0, -3)", "(3, 0)", "(0, 3)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Almacenar la posición (x, y) de un píxel o sprite en la pantalla.", "consecuencia_de_error": "El objeto se dibuja en el lugar incorrecto."},
                    "quimica": {"uso": "Representar la velocidad de una partícula en una simulación 2D de un gas.", "consecuencia_de_error": "Cálculo erróneo de la energía cinética."},
                    "civil": {"uso": "Representar fuerzas en el plano de un muro o una viga.", "consecuencia_de_error": "Error en el diagrama de cuerpo libre."},
                    "mecanica": {"uso": "Describir el desplazamiento de una pieza en un mecanismo plano.", "consecuencia_de_error": "La máquina se atasca o choca."},
                    "mecatronica": {"uso": "Coordenadas de navegación para un robot de limpieza (Roomba).", "consecuencia_de_error": "El robot no cubre toda el área o choca."},
                    "aeronautica": {"uso": "Representar el viento como un vector de velocidad horizontal.", "consecuencia_de_error": "Navegación imprecisa."},
                    "electrica": {"uso": "Representar fasores de voltaje y corriente en el plano complejo (2D).", "consecuencia_de_error": "Análisis de circuitos de CA incorrecto."}
                }
            },
            {
                "subtema_titulo": "2. Magnitud (Norma) de un Vector",
                "definicion": "La magnitud es la 'longitud' de la flecha. Se calcula usando el Teorema de Pitágoras: |v| = √(x² + y²). Siempre es un número positivo.",
                "diagrama": "GIFS/magnitud_vector.gif",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Calcular la magnitud de v = (-3, 4).\n1. Cuadrados: (-3)² = 9, 4² = 16.\n2. Suma: 9 + 16 = 25.\n3. Raíz: √25 = 5.\n|v| = 5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la magnitud del vector v = (6, 8). (Solo el número)",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "14", "100", "2"]
                    },
                    "similares": [
                        {"pregunta": "Magnitud de v = (1, 1). (Escribe 'raiz(2)' o 'sqrt(2)')", "respuesta_correcta": "raiz(2)", "opciones": ["raiz(2)", "1", "2", "0.5"]},
                        {"pregunta": "Magnitud de v = (5, 12).", "respuesta_correcta": "13", "opciones": ["13", "17", "60", "7"]},
                        {"pregunta": "Magnitud de v = (0, -7).", "respuesta_correcta": "7", "opciones": ["7", "-7", "0", "49"]},
                        {"pregunta": "Magnitud de v = (-3, 0).", "respuesta_correcta": "3", "opciones": ["3", "-3", "0", "9"]},
                        {"pregunta": "Si la magnitud es 1, el vector se llama...", "respuesta_correcta": "unitario", "opciones": ["unitario", "nulo", "normal", "base"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular la velocidad (rapidez) de un jugador a partir de su vector de movimiento.", "consecuencia_de_error": "El jugador se mueve a velocidades inconsistentes."},
                    "quimica": {"uso": "Calcular la velocidad molecular promedio en un gas 2D.", "consecuencia_de_error": "Cálculo de temperatura incorrecto."},
                    "civil": {"uso": "Calcular la fuerza total (tensión) en un cable de un puente.", "consecuencia_de_error": "El cable se rompe si la magnitud excede su resistencia."},
                    "mecanica": {"uso": "Calcular la fuerza resultante sobre un perno.", "consecuencia_de_error": "Falla por corte en el perno."},
                    "mecatronica": {"uso": "Calcular la distancia al objetivo para saber cuándo frenar.", "consecuencia_de_error": "El robot choca con el objetivo."},
                    "aeronautica": {"uso": "Calcular la velocidad total del aire (True Airspeed).", "consecuencia_de_error": "Lecturas de velocidad falsas."},
                    "electrica": {"uso": "Calcular el voltaje pico a partir de componentes en cuadratura.", "consecuencia_de_error": "Sobrecarga de componentes."}
                }
            },
            {
                "subtema_titulo": "3. Dirección (Ángulo) de un Vector",
                "definicion": "La dirección es el ángulo 'θ' que forma el vector con el eje X positivo. Se calcula con la tangente inversa: θ = arctan(y/x). Hay que tener cuidado con el cuadrante.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Dirección de v = (1, 1).\n1. y=1, x=1.\n2. tan(θ) = 1/1 = 1.\n3. θ = arctan(1) = 45°.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el ángulo (en grados) del vector v = (0, 5)? (Eje Y positivo)",
                        "respuesta_correcta": "90",
                        "opciones": ["90", "0", "180", "45"]
                    },
                    "similares": [
                        {"pregunta": "Ángulo del vector v = (5, 0).", "respuesta_correcta": "0", "opciones": ["0", "90", "180", "360"]},
                        {"pregunta": "Ángulo del vector v = (-5, 0) (Eje X negativo).", "respuesta_correcta": "180", "opciones": ["180", "0", "-90", "90"]},
                        {"pregunta": "Si x=1, y=1.732 (raiz de 3), el ángulo es... (60/30)", "respuesta_correcta": "60", "opciones": ["60", "30", "45", "90"]},
                        {"pregunta": "El ángulo se mide en sentido...", "respuesta_correcta": "antihorario", "opciones": ["antihorario", "horario", "radial", "lineal"]},
                        {"pregunta": "¿Qué función trigonométrica inversa usas con y/x?", "respuesta_correcta": "arco tangente", "opciones": ["arco tangente", "arco seno", "arco coseno", "tangente"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Orientar un sprite o modelo 3D para que mire en la dirección del movimiento.", "consecuencia_de_error": "El personaje camina de lado o de espaldas."},
                    "quimica": {"uso": "Determinar la orientación de una molécula polar en un campo.", "consecuencia_de_error": "Error en simulaciones de electroforesis."},
                    "civil": {"uso": "Definir la dirección de una fuerza (ej. viento) sobre una estructura.", "consecuencia_de_error": "Refuerzos colocados en el ángulo incorrecto."},
                    "mecanica": {"uso": "Calcular el ángulo de aplicación de una fuerza en una palanca.", "consecuencia_de_error": "Pérdida de eficiencia mecánica (torque)."},
                    "mecatronica": {"uso": "Navegación: calcular el rumbo (heading) del robot.", "consecuencia_de_error": "El robot se pierde."},
                    "aeronautica": {"uso": "Calcular el rumbo magnético para llegar a un destino.", "consecuencia_de_error": "El avión vuela en la dirección equivocada."},
                    "electrica": {"uso": "Calcular el ángulo de fase de la impedancia.", "consecuencia_de_error": "Factor de potencia bajo."}
                }
            },
            {
                "subtema_titulo": "4. Suma y Resta de Vectores (Analítica)",
                "definicion": "Para sumar vectores, se suman sus componentes: (x₁, y₁) + (x₂, y₂) = (x₁+x₂, y₁+y₂). La resta es sumar el negativo: v - w = v + (-w). Gráficamente es poner uno tras otro (punta a cola).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Sumar v = (2, 5) y w = (1, -3).\nSuma = (2+1, 5+(-3)) = (3, 2).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Suma los vectores a=(10, 2) y b=(-4, 3). (Formato: (x,y))",
                        "respuesta_correcta": "(6, 5)",
                        "opciones": ["(6, 5)", "(14, 5)", "(6, -1)", "(14, -1)"]
                    },
                    "similares": [
                        {"pregunta": "Resta a=(5, 5) - b=(2, 2).", "respuesta_correcta": "(3, 3)", "opciones": ["(3, 3)", "(7, 7)", "(2, 2)", "(-3, -3)"]},
                        {"pregunta": "Suma v=(1, 0) + w=(0, 1).", "respuesta_correcta": "(1, 1)", "opciones": ["(1, 1)", "(1, 0)", "(0, 1)", "(0, 0)"]},
                        {"pregunta": "Si sumas un vector con su opuesto (-v), obtienes...", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "2v", "-v", "1"]},
                        {"pregunta": "Suma (2, -2) + (-2, 2).", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "(4, -4)", "(-4, 4)", "(2, 2)"]},
                        {"pregunta": "Resta (10, 10) - (5, 15).", "respuesta_correcta": "(5, -5)", "opciones": ["(5, -5)", "(15, 25)", "(5, 5)", "(-5, 5)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular la nueva posición: Pos_final = Pos_inicial + Velocidad.", "consecuencia_de_error": "Teletransportación o movimiento errático."},
                    "quimica": {"uso": "Superposición de movimientos moleculares.", "consecuencia_de_error": "Cálculo de difusión incorrecto."},
                    "civil": {"uso": "Suma de fuerzas en un nodo (Estática). La suma debe ser cero.", "consecuencia_de_error": "Colapso estructural por desequilibrio."},
                    "mecanica": {"uso": "Suma de velocidades relativas (v_barco + v_rio).", "consecuencia_de_error": "No llegar al destino deseado al cruzar un río."},
                    "mecatronica": {"uso": "Suma de errores de posición para el control integral.", "consecuencia_de_error": "Control inestable."},
                    "aeronautica": {"uso": "Corrección de deriva: Rumbo + Viento = Trayectoria.", "consecuencia_de_error": "Navegación fuera de curso."},
                    "electrica": {"uso": "Suma de corrientes en un nodo (Kirchhoff).", "consecuencia_de_error": "Análisis de circuito incorrecto."}
                }
            },
            {
                "subtema_titulo": "5. Multiplicación por un Escalar",
                "definicion": "Multiplicar un vector 'v' por un número 'k' (escalar). Cambia la magnitud pero no la dirección (si k es positivo). Si k es negativo, invierte la dirección. kv = (kx, ky).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: v = (2, -3). Calcular 3v.\n3v = (3*2, 3*-3) = (6, -9).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si v = (1, 4), ¿cuál es el vector 5v?",
                        "respuesta_correcta": "(5, 20)",
                        "opciones": ["(5, 20)", "(6, 9)", "(1, 20)", "(5, 4)"]
                    },
                    "similares": [
                        {"pregunta": "Si v = (2, 2), calcula -1v.", "respuesta_correcta": "(-2, -2)", "opciones": ["(-2, -2)", "(2, 2)", "(-1, -1)", "(0, 0)"]},
                        {"pregunta": "Si v = (10, 0), calcula 0.5v.", "respuesta_correcta": "(5, 0)", "opciones": ["(5, 0)", "(20, 0)", "(5, 5)", "(10, 0.5)"]},
                        {"pregunta": "Si v = (0, 0), calcula 100v.", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "(100, 100)", "(100, 0)", "100"]},
                        {"pregunta": "Multiplicar por -2, ¿cambia la dirección? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "Multiplicar por 2, ¿duplica la magnitud? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Escalar un modelo 3D (hacerlo más grande o más chico).", "consecuencia_de_error": "Objetos de tamaño incorrecto en la pantalla."},
                    "quimica": {"uso": "Escalar vectores de velocidad al aumentar la temperatura.", "consecuencia_de_error": "Simulación térmica incorrecta."},
                    "civil": {"uso": "Aplicar un 'factor de seguridad' a las cargas (ej. diseñar para 1.5 veces la carga real).", "consecuencia_de_error": "Estructura insegura."},
                    "mecanica": {"uso": "Aumentar la fuerza aplicada en una palanca.", "consecuencia_de_error": "Falla mecánica."},
                    "mecatronica": {"uso": "Aumentar la velocidad de un motor proporcionalmente al error (Control P).", "consecuencia_de_error": "Respuesta lenta o sobreimpulso."},
                    "aeronautica": {"uso": "Aumentar el empuje del motor (vector fuerza).", "consecuencia_de_error": "Aceleración insuficiente."},
                    "electrica": {"uso": "Amplificación de una señal (voltaje).", "consecuencia_de_error": "Señal saturada o débil."}
                }
            },
            {
                "subtema_titulo": "6. Vectores Unitarios (i, j)",
                "definicion": "Vectores de magnitud 1 que apuntan en los ejes principales. i = (1, 0) es la dirección X. j = (0, 1) es la dirección Y. Cualquier vector se puede escribir como v = xi + yj.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: v = (3, 5) se escribe como v = 3i + 5j.\nPara normalizar un vector (hacerlo unitario), divides por su magnitud: u = v / |v|.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Normaliza el vector v=(3, 4). Su magnitud es 5. ¿Cuál es el vector unitario?",
                        "respuesta_correcta": "(0.6, 0.8)",
                        "opciones": ["(0.6, 0.8)", "(3, 4)", "(0.3, 0.4)", "(1, 1)"]
                    },
                    "similares": [
                        {"pregunta": "Escribe (5, 2) usando i y j.", "respuesta_correcta": "5i+2j", "opciones": ["5i+2j", "2i+5j", "5i-2j", "7ij"]},
                        {"pregunta": "Normaliza v=(10, 0).", "respuesta_correcta": "(1, 0)", "opciones": ["(1, 0)", "(10, 0)", "(0.1, 0)", "(0, 1)"]},
                        {"pregunta": "Normaliza v=(0, -5).", "respuesta_correcta": "(0, -1)", "opciones": ["(0, -1)", "(0, -5)", "(-1, 0)", "(0, 1)"]},
                        {"pregunta": "¿Cuál es la magnitud de 'i'?", "respuesta_correcta": "1", "opciones": ["1", "0", "i", "x"]},
                        {"pregunta": "El vector 'j' apunta hacia...", "respuesta_correcta": "arriba", "opciones": ["arriba", "derecha", "abajo", "izquierda"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Dirección de movimiento en juegos. Se usa el vector unitario para mover al personaje a velocidad constante sin importar la dirección.", "consecuencia_de_error": "Moverse en diagonal sería más rápido que en línea recta (bug clásico)."},
                    "quimica": {"uso": "Definir la orientación de enlaces.", "consecuencia_de_error": "Geometría molecular errónea."},
                    "civil": {"uso": "Definir la dirección de las cargas (ej. gravedad es -j).", "consecuencia_de_error": "Signos de fuerza incorrectos."},
                    "mecanica": {"uso": "Definir ejes de coordenadas locales de una pieza.", "consecuencia_de_error": "Errores de ensamblaje."},
                    "mecatronica": {"uso": "Vector de dirección hacia el objetivo.", "consecuencia_de_error": "El robot no va directo al punto."},
                    "aeronautica": {"uso": "Vectores de ejes del avión (nariz, ala).", "consecuencia_de_error": "Instrumentos de horizonte artificial fallidos."},
                    "electrica": {"uso": "Definir la dirección del campo eléctrico.", "consecuencia_de_error": "Cálculo de fuerza eléctrica errado."}
                }
            },
            {
                "subtema_titulo": "7. Producto Punto (Escalar)",
                "definicion": "Multiplicación de dos vectores que resulta en un número. v · w = x₁x₂ + y₁y₂. Si es 0, son perpendiculares. Si es positivo, apuntan en dirección similar.",
                "diagrama": "GIFS/producto_punto.gif",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: v = (2, 3) y w = (4, -1).\nv · w = (2*4) + (3*-1) = 8 - 3 = 5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el producto punto de v=(1, 5) y w=(2, 2). (2+10)",
                        "respuesta_correcta": "12",
                        "opciones": ["12", "10", "7", "2"]
                    },
                    "similares": [
                        {"pregunta": "Producto punto de (3, 0) y (0, 5).", "respuesta_correcta": "0", "opciones": ["0", "15", "3", "5"]},
                        {"pregunta": "Producto punto de (1, 1) y (-1, -1).", "respuesta_correcta": "-2", "opciones": ["-2", "0", "2", "1"]},
                        {"pregunta": "Producto punto de (2, 2) y (1, 0).", "respuesta_correcta": "2", "opciones": ["2", "0", "4", "1"]},
                        {"pregunta": "Si el producto punto es 0, el ángulo es...", "respuesta_correcta": "90", "opciones": ["90", "0", "180", "45"]},
                        {"pregunta": "Producto punto de i · i.", "respuesta_correcta": "1", "opciones": ["1", "0", "i", "2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de iluminación. Luz · Normal = Brillo.", "consecuencia_de_error": "Objetos negros o mal iluminados."},
                    "quimica": {"uso": "Cálculo de energía de enlace.", "consecuencia_de_error": "Estabilidad molecular incorrecta."},
                    "civil": {"uso": "Proyección de fuerzas.", "consecuencia_de_error": "Componentes de carga erróneos."},
                    "mecanica": {"uso": "Cálculo de Trabajo (W = F · d).", "consecuencia_de_error": "Balance energético fallido."},
                    "mecatronica": {"uso": "Detectar si el robot está alineado con la meta.", "consecuencia_de_error": "Movimiento ineficiente."},
                    "aeronautica": {"uso": "Viento de frente vs cruzado.", "consecuencia_de_error": "Cálculo de despegue inseguro."},
                    "electrica": {"uso": "Potencia activa (P = V · I).", "consecuencia_de_error": "Medición de consumo eléctrico errónea."}
                }
            },
            {
                "subtema_titulo": "8. Ángulo entre dos Vectores",
                "definicion": "Se usa el producto punto para hallar el ángulo θ: cos(θ) = (v · w) / (|v| |w|).",
                "diagrama": "",  # 🖼️ INICIALIZADOv
                "ejemplo_resuelto": "Ejemplo: v=(1,0), w=(1,1).\n1. v·w = 1.\n2. |v|=1, |w|=√2.\n3. cos(θ) = 1/√2 = 0.707.\n4. θ = 45°.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si dos vectores son perpendiculares, su producto punto es...",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "1", "-1", "infinito"]
                    },
                    "similares": [
                        {"pregunta": "Si dos vectores son paralelos (mismo sentido), el ángulo es...", "respuesta_correcta": "0", "opciones": ["0", "90", "180", "45"]},
                        {"pregunta": "Si v·w es negativo, el ángulo es... (agudo/obtuso)", "respuesta_correcta": "obtuso", "opciones": ["obtuso", "agudo"]},
                        {"pregunta": "Calcula cos(θ) si v·w=10 y |v||w|=20.", "respuesta_correcta": "0.5", "opciones": ["0.5", "2", "200", "10"]},
                        {"pregunta": "¿Qué función inversa usas para hallar el ángulo? (acos/asin)", "respuesta_correcta": "acos", "opciones": ["acos", "asin", "atan", "tan"]},
                        {"pregunta": "El ángulo entre i y j es...", "respuesta_correcta": "90", "opciones": ["90", "0", "45", "180"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Campo de visión (Field of View) de IA.", "consecuencia_de_error": "Enemigos que no te ven."},
                    "quimica": {"uso": "Ángulos de enlace.", "consecuencia_de_error": "Geometría molecular errónea."},
                    "civil": {"uso": "Ángulos entre vigas.", "consecuencia_de_error": "Uniones soldadas con ángulo incorrecto."},
                    "mecanica": {"uso": "Ángulos de transmisión de fuerza.", "consecuencia_de_error": "Eficiencia mecánica baja."},
                    "mecatronica": {"uso": "Orientación de sensores.", "consecuencia_de_error": "Lecturas sesgadas."},
                    "aeronautica": {"uso": "Ángulo de deriva.", "consecuencia_de_error": "Navegación incorrecta."},
                    "electrica": {"uso": "Fase entre V e I.", "consecuencia_de_error": "Factor de potencia bajo."}
                }
            },
            {
                "subtema_titulo": "9. Proyección Ortogonal",
                "definicion": "Es la 'sombra' de un vector sobre otro. Útil para descomponer fuerzas en componentes 'útiles' (paralelas al movimiento) y 'inútiles' (perpendiculares). Proy(v) = ((v·w)/|w|²) * w.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Proyectar v=(3,4) sobre el eje X (w=(1,0)).\nSombra = 3. Vector = (3, 0).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Proyecta v=(10, 20) sobre el eje X (1,0). (Solo la componente X)",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "20", "30", "0"]
                    },
                    "similares": [
                        {"pregunta": "Proyecta v=(5, 8) sobre el eje Y (0,1). (Solo componente Y)", "respuesta_correcta": "8", "opciones": ["8", "5", "13", "0"]},
                        {"pregunta": "Si v es perpendicular a w, la proyección es...", "respuesta_correcta": "0", "opciones": ["0", "v", "w", "1"]},
                        {"pregunta": "La proyección es un...", "respuesta_correcta": "vector", "opciones": ["vector", "escalar"]},
                        {"pregunta": "La componente escalar es v·w dividido por la magnitud de...", "respuesta_correcta": "w", "opciones": ["w", "v"]},
                        {"pregunta": "Proyección de (2,2) sobre (1,0).", "respuesta_correcta": "(2, 0)", "opciones": ["(2, 0)", "(0, 2)", "(2, 2)", "(1, 0)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Deslizamiento sobre paredes en juegos.", "consecuencia_de_error": "Personaje atorado en la pared."},
                    "quimica": {"uso": "Componentes dipolares.", "consecuencia_de_error": "Análisis de polaridad incorrecto."},
                    "civil": {"uso": "Componente normal y tangencial de una fuerza.", "consecuencia_de_error": "Fallo por deslizamiento."},
                    "mecanica": {"uso": "Torque efectivo.", "consecuencia_de_error": "Menor fuerza de giro."},
                    "mecatronica": {"uso": "Control de fuerza normal.", "consecuencia_de_error": "Robot daña la superficie."},
                    "aeronautica": {"uso": "Componente de viento cruzado.", "consecuencia_de_error": "Aterrizaje peligroso."},
                    "electrica": {"uso": "Potencia activa vs reactiva.", "consecuencia_de_error": "Ineficiencia energética."}
                }
            },
            {
                "subtema_titulo": "10. Aplicación: Velocidad Relativa (2D)",
                "definicion": "La velocidad depende del observador. V_relativa = V_objeto - V_observador. Se restan los vectores de velocidad.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Auto A va al Norte a 20 m/s (0, 20). Auto B va al Este a 20 m/s (20, 0).\nVelocidad de A vista desde B = Va - Vb = (0, 20) - (20, 0) = (-20, 20).\nParece que A se mueve al Noroeste.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Tren A va a 10 m/s (derecha). Tú corres en el tren a 2 m/s (derecha). ¿Tu velocidad respecto al suelo?",
                        "respuesta_correcta": "12",
                        "opciones": ["12", "8", "10", "20"]
                    },
                    "similares": [
                        {"pregunta": "Si corres hacia atrás a 2 m/s en el mismo tren, tu velocidad suelo es...", "respuesta_correcta": "8", "opciones": ["8", "12", "-2", "-8"]},
                        {"pregunta": "Auto A (10,0), Auto B (10,0). Velocidad relativa de A vista por B.", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "(20, 0)", "(10, 0)", "(-10, 0)"]},
                        {"pregunta": "Avión (0, 100), Viento (20, 0). Velocidad sobre tierra. (Suma)", "respuesta_correcta": "(20, 100)", "opciones": ["(20, 100)", "(-20, 100)", "(0, 100)", "(120, 0)"]},
                        {"pregunta": "Si dos autos chocan de frente a 50 km/h cada uno, la velocidad relativa de impacto es...", "respuesta_correcta": "100", "opciones": ["100", "0", "50", "25"]},
                        {"pregunta": "Para calcular velocidad relativa, los vectores se...", "respuesta_correcta": "restan", "opciones": ["restan", "suman", "multiplican", "dividen"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cámara siguiendo al jugador.", "consecuencia_de_error": "Cámara temblorosa o perdida."},
                    "quimica": {"uso": "Colisiones moleculares.", "consecuencia_de_error": "Cálculo de energía de reacción erróneo."},
                    "civil": {"uso": "Flujo de agua relativo a una compuerta móvil.", "consecuencia_de_error": "Cálculo de caudal incorrecto."},
                    "mecanica": {"uso": "Velocidad de deslizamiento en engranajes.", "consecuencia_de_error": "Desgaste y fricción."},
                    "mecatronica": {"uso": "Evastión de obstáculos móviles.", "consecuencia_de_error": "Colisión del robot."},
                    "aeronautica": {"uso": "Velocidad Aire vs Velocidad Tierra.", "consecuencia_de_error": "Navegación fallida."},
                    "electrica": {"uso": "Velocidad relativa del campo magnético en un motor de inducción (deslizamiento).", "consecuencia_de_error": "Cálculo de torque y eficiencia del motor."}
                }
            }
        ]
    },

    "CALCULO INTEGRAL": {
        "nombre_completo": "Cálculo Integral: La Ciencia de la Acumulación",
        "prerequisitos": ["CALCULO DIFERENCIAL"],
        "quiz": [
            {
                "pregunta": "¿Cuál es la antiderivada de f(x) = 2x?",
                "respuesta": "x^2+C",
                "opciones": ["x^2+C", "2x^2", "2", "x+C"]
            },
            {
                "pregunta": "El Teorema Fundamental dice que la integral de a a b es F(b) - ...",
                "respuesta": "F(a)",
                "opciones": ["F(a)", "F(b)", "f(a)", "0"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. La Antiderivada (Integral Indefinida)",
                "definicion": "La integración es la operación inversa a la derivación. Si la derivada te da la 'velocidad' de cambio, la integral te devuelve la 'cantidad' original. Buscamos una función F(x) tal que F'(x) = f(x). Siempre se añade una '+C' (Constante de Integración) porque la derivada de una constante es cero.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Encontrar la antiderivada de f(x) = 2x.\nPregunta: ¿Qué función, al derivarla, da 2x?\nRespuesta: x², porque la derivada de x² es 2x.\nSolución General: ∫ 2x dx = x² + C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la integral indefinida: ∫ 5 dx. (Recuerda la +C)",
                        "respuesta_correcta": "5x+C",
                        "opciones": ["5x+C", "5", "x+C", "0"]
                    },
                    "similares": [
                        {"pregunta": "Calcula ∫ 3x² dx.", "respuesta_correcta": "x^3+C", "opciones": ["x^3+C", "6x", "3x^3", "x^2"]},
                        {"pregunta": "Calcula ∫ 10x dx.", "respuesta_correcta": "5x^2+C", "opciones": ["5x^2+C", "10x^2", "5x", "10"]},
                        {"pregunta": "Calcula ∫ 4 dx.", "respuesta_correcta": "4x+C", "opciones": ["4x+C", "4", "x^4", "0"]},
                        {"pregunta": "Calcula ∫ 0 dx.", "respuesta_correcta": "C", "opciones": ["C", "0", "x", "1"]},
                        {"pregunta": "Si la derivada es v(t) = 9.8, ¿cuál es la integral (velocidad)?", "respuesta_correcta": "9.8t+C", "opciones": ["9.8t+C", "9.8", "4.9t^2", "t"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Recuperar datos originales a partir de datos de cambios (deltas) comprimidos.", "consecuencia_de_error": "Archivo corrupto al descomprimir."},
                    "quimica": {"uso": "Integrar la 'velocidad de reacción' para saber la 'concentración' en un tiempo t.", "consecuencia_de_error": "No saber cuánto producto se ha creado en el reactor."},
                    "civil": {"uso": "Obtener la ecuación de la 'pendiente' de una viga integrando la ecuación de 'curvatura'.", "consecuencia_de_error": "Cálculo erróneo de la deformación de la estructura."},
                    "mecanica": {"uso": "Obtener la 'velocidad' integrando la 'aceleración' de un sensor.", "consecuencia_de_error": "Datos de navegación inercial falsos."},
                    "mecatronica": {"uso": "El término 'I' (Integral) en un control PID acumula el error pasado para corregir el rumbo.", "consecuencia_de_error": "El robot nunca llega exactamente al objetivo (error de estado estacionario)."},
                    "aeronautica": {"uso": "Calcular la altitud integrando la velocidad vertical (rate of climb).", "consecuencia_de_error": "Lectura de altitud incorrecta si falla el barómetro."},
                    "electrica": {"uso": "Calcular el voltaje en un capacitor integrando la corriente: V = (1/C)∫i dt.", "consecuencia_de_error": "Diseño de circuito de temporización fallido."}
                }
            },
            {
                "subtema_titulo": "2. Regla de la Potencia para Integrales",
                "definicion": "Es la inversa de la regla de derivación. Para integrar xⁿ, sumas 1 al exponente y divides por el nuevo exponente. Fórmula: ∫ xⁿ dx = (xⁿ⁺¹) / (n+1) + C (para n ≠ -1).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ∫ x³ dx\n1. Sumar 1 al exponente: 3 + 1 = 4.\n2. Dividir por el nuevo exponente: / 4.\n3. Resultado: (x⁴ / 4) + C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula ∫ x⁵ dx. (Usa ^ para potencia)",
                        "respuesta_correcta": "x^6/6+C",
                        "opciones": ["x^6/6+C", "5x^4", "x^5/5", "x^6"]
                    },
                    "similares": [
                        {"pregunta": "Calcula ∫ x² dx.", "respuesta_correcta": "x^3/3+C", "opciones": ["x^3/3+C", "2x", "x^2/2", "x^3"]},
                        {"pregunta": "Calcula ∫ x dx. (x es x¹)", "respuesta_correcta": "x^2/2+C", "opciones": ["x^2/2+C", "1", "x^2", "2x"]},
                        {"pregunta": "Calcula ∫ x⁴ dx.", "respuesta_correcta": "x^5/5+C", "opciones": ["x^5/5+C", "4x^3", "x^5", "x^4/4"]},
                        {"pregunta": "Calcula ∫ x⁹ dx.", "respuesta_correcta": "x^10/10+C", "opciones": ["x^10/10+C", "9x^8", "x^9", "x^10"]},
                        {"pregunta": "Calcula ∫ x⁻³ dx. (-3+1 = -2)", "respuesta_correcta": "x^-2/-2+C", "opciones": ["x^-2/-2+C", "-3x^-4", "x^-4/-4", "x^-2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de uso total de memoria integrando una función de crecimiento polinomial.", "consecuencia_de_error": "Desbordamiento de memoria (Out of Memory)."},
                    "quimica": {"uso": "Cálculo de trabajo de expansión de un gas (W = ∫ P dV) en procesos politrópicos.", "consecuencia_de_error": "Balance de energía incorrecto en un motor."},
                    "civil": {"uso": "Cálculo del momento de inercia de secciones rectangulares (∫ y² dA).", "consecuencia_de_error": "Viga subdimensionada que se rompe."},
                    "mecanica": {"uso": "Cálculo de la posición de un objeto con aceleración variable (polinomio).", "consecuencia_de_error": "Predicción de trayectoria fallida."},
                    "mecatronica": {"uso": "Linealización de sensores con respuesta polinómica inversa.", "consecuencia_de_error": "Lecturas de sensor no lineales."},
                    "aeronautica": {"uso": "Cálculo del perfil aerodinámico del ala.", "consecuencia_de_error": "Ala con forma incorrecta y mala sustentación."},
                    "electrica": {"uso": "Energía almacenada en un campo (integral del cuadrado del campo).", "consecuencia_de_error": "Cálculo de pérdidas por calor erróneo."}
                }
            },
            {
                "subtema_titulo": "3. Integral Definida y Área Bajo la Curva",
                "definicion": "La Integral Definida ∫[a, b] f(x) dx calcula el 'área neta' encerrada entre la función y el eje X, desde x=a hasta x=b. Es la suma de infinitos rectángulos infinitesimales (Sumas de Riemann).",
                "diagrama": "GIFS/integral.gif",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Área bajo y = 2x desde x=0 hasta x=4.\nGeométricamente es un triángulo de base 4 y altura 8 (2*4).\nÁrea = (4*8)/2 = 16 unidades cuadradas.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el área bajo f(x)=3 desde x=0 hasta x=5. (Rectángulo de base 5, altura 3)",
                        "respuesta_correcta": "15",
                        "opciones": ["15", "5", "3", "8"]
                    },
                    "similares": [
                        {"pregunta": "Área bajo f(x)=x de 0 a 4. (Triángulo base 4, altura 4)", "respuesta_correcta": "8", "opciones": ["8", "16", "4", "12"]},
                        {"pregunta": "Área bajo f(x)=5 de 0 a 2.", "respuesta_correcta": "10", "opciones": ["10", "5", "2", "7"]},
                        {"pregunta": "La integral definida representa el...", "respuesta_correcta": "area bajo la curva", "opciones": ["area bajo la curva", "pendiente", "volumen", "limite"]},
                        {"pregunta": "Integral de 0 a 10 de f(x)=0.", "respuesta_correcta": "0", "opciones": ["0", "10", "1", "infinito"]},
                        {"pregunta": "Si el área arriba del eje X es 5 y abajo es 2, la integral neta es...", "respuesta_correcta": "3", "opciones": ["3", "7", "5", "-2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Integrar la tasa de transferencia (MB/s) en el tiempo para saber el total de datos descargados.", "consecuencia_de_error": "Barra de progreso de descarga incorrecta."},
                    "quimica": {"uso": "Área bajo la curva en cromatografía: determina la cantidad total de una sustancia.", "consecuencia_de_error": "Medición de pureza o concentración errónea."},
                    "civil": {"uso": "Diagramas de fuerza cortante y momento flector. El área del diagrama de carga es el cortante.", "consecuencia_de_error": "Diseño estructural fallido."},
                    "mecanica": {"uso": "El Trabajo es el área bajo la curva de Fuerza vs Distancia.", "consecuencia_de_error": "Cálculo de consumo de energía erróneo."},
                    "mecatronica": {"uso": "Distancia total recorrida por un robot (área bajo la gráfica velocidad-tiempo).", "consecuencia_de_error": "El robot se detiene antes o después de la meta."},
                    "aeronautica": {"uso": "Cálculo de la sustentación total integrando la distribución de presión sobre el ala.", "consecuencia_de_error": "El avión no despega."},
                    "electrica": {"uso": "Energía consumida (kWh) es el área bajo la curva de Potencia vs Tiempo.", "consecuencia_de_error": "Facturación eléctrica incorrecta."}
                }
            },
            {
                "subtema_titulo": "4. Teorema Fundamental del Cálculo (TFC)",
                "definicion": "Conecta la derivada con la integral. Dice que para evaluar una integral definida ∫[a,b] f(x) dx, solo necesitas encontrar la antiderivada F(x) y restar: F(b) - F(a).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ∫[1, 3] 2x dx.\n1. Antiderivada F(x) = x².\n2. Evaluar en b=3: 3² = 9.\n3. Evaluar en a=1: 1² = 1.\n4. Restar: 9 - 1 = 8.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula ∫[0, 2] 3x² dx. (Antiderivada x³. Evalúa 2³ - 0³)",
                        "respuesta_correcta": "8",
                        "opciones": ["8", "6", "12", "4"]
                    },
                    "similares": [
                        {"pregunta": "Calcula ∫[0, 3] 2x dx.", "respuesta_correcta": "9", "opciones": ["9", "6", "3", "18"]},
                        {"pregunta": "Calcula ∫[1, 2] 1 dx.", "respuesta_correcta": "1", "opciones": ["1", "2", "0", "3"]},
                        {"pregunta": "Calcula ∫[0, 1] 4x³ dx.", "respuesta_correcta": "1", "opciones": ["1", "4", "0", "2"]},
                        {"pregunta": "Si F(5)=10 y F(2)=4, ¿cuánto vale la integral de 2 a 5?", "respuesta_correcta": "6", "opciones": ["6", "14", "4", "2"]},
                        {"pregunta": "Calcula ∫[0, π] sen(x) dx. (Antiderivada -cos(x))", "respuesta_correcta": "2", "opciones": ["2", "0", "1", "-2"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Optimización de cálculos acumulativos en bases de datos.", "consecuencia_de_error": "Consultas SQL lentas e ineficientes."},
                    "quimica": {"uso": "Calcular el cambio total de Entalpía integrando la capacidad calorífica.", "consecuencia_de_error": "Errores en el diseño de intercambiadores de calor."},
                    "civil": {"uso": "Calcular la deformación total sumando los cambios infinitesimales a lo largo de la viga.", "consecuencia_de_error": "Edificio que se deforma más allá de los límites de servicio."},
                    "mecanica": {"uso": "Teorema Trabajo-Energía: El trabajo total es el cambio en energía cinética (Kb - Ka).", "consecuencia_de_error": "No poder predecir la velocidad final de un sistema."},
                    "mecatronica": {"uso": "Control predictivo: estimar la posición futura integrando la velocidad actual.", "consecuencia_de_error": "Colisión del robot por mala predicción."},
                    "aeronautica": {"uso": "Calcular el cambio total de peso del avión por consumo de combustible.", "consecuencia_de_error": "Planificación de vuelo peligrosa."},
                    "electrica": {"uso": "Calcular el voltaje total acumulado en un capacitor durante un tiempo t.", "consecuencia_de_error": "Diseño de circuitos de tiempo (timers) defectuoso."}
                }
            },
            {
                "subtema_titulo": "5. Integración por Sustitución (Cambio de Variable)",
                "definicion": "Es la 'Regla de la Cadena' en reversa. Se usa cuando tienes una función compuesta y su derivada está presente. Se sustituye una parte difícil por 'u'.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ∫ 2x(x² + 1)⁵ dx.\n1. Elegir u = x² + 1.\n2. Derivar u: du = 2x dx.\n3. Sustituir: ∫ u⁵ du.\n4. Integrar: u⁶/6.\n5. Regresar a x: (x² + 1)⁶ / 6 + C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para ∫ cos(3x) * 3 dx, si u=3x, ¿qué es du? (Escribe la expresión con dx)",
                        "respuesta_correcta": "3dx",
                        "opciones": ["3dx", "dx", "3x dx", "cos(3x)"]
                    },
                    "similares": [
                        {"pregunta": "En ∫ (x+1)⁵ dx, si u=x+1, ¿cuánto es du?", "respuesta_correcta": "dx", "opciones": ["dx", "x dx", "5dx", "1"]},
                        {"pregunta": "En ∫ 2x * e^(x²) dx, ¿cuál es la mejor 'u'?", "respuesta_correcta": "x^2", "opciones": ["x^2", "e^x", "2x", "e"]},
                        {"pregunta": "Integra ∫ eᵘ du.", "respuesta_correcta": "e^u+C", "opciones": ["e^u+C", "u*e^u", "e^u/u", "ln(u)"]},
                        {"pregunta": "Integra ∫ u² du.", "respuesta_correcta": "u^3/3+C", "opciones": ["u^3/3+C", "2u", "u^2", "u^3"]},
                        {"pregunta": "La sustitución 'u' simplifica la integral. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simplificación de algoritmos complejos mediante transformación de variables.", "consecuencia_de_error": "Código ineficiente y difícil de mantener."},
                    "quimica": {"uso": "Resolver leyes de velocidad de reacciones complejas.", "consecuencia_de_error": "Modelos cinéticos que no ajustan a la realidad."},
                    "civil": {"uso": "Integración de funciones de carga no uniformes (ej. presión de agua).", "consecuencia_de_error": "Cálculo de fuerzas hidrostáticas incorrecto."},
                    "mecanica": {"uso": "Resolver ecuaciones de movimiento con resistencia del aire variable.", "consecuencia_de_error": "Simulación de trayectoria imprecisa."},
                    "mecatronica": {"uso": "Análisis de sistemas no lineales.", "consecuencia_de_error": "Control deficiente en robots avanzados."},
                    "aeronautica": {"uso": "Cálculos de flujo de fluidos compresibles.", "consecuencia_de_error": "Diseño de toberas supersónicas ineficiente."},
                    "electrica": {"uso": "Análisis de señales moduladas (AM/FM).", "consecuencia_de_error": "Mala recepción de señal."}
                }
            },
            {
                "subtema_titulo": "6. Integración por Partes",
                "definicion": "Es la 'Regla del Producto' en reversa. Se usa para integrar productos de funciones de distinto tipo (ej. x * eˣ). Fórmula: ∫ u dv = uv - ∫ v du.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ∫ x cos(x) dx.\n1. u = x (se simplifica al derivar), dv = cos(x) dx (fácil de integrar).\n2. du = dx, v = sen(x).\n3. Fórmula: x*sen(x) - ∫ sen(x) dx.\n4. Resultado: x*sen(x) + cos(x) + C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la fórmula ∫ u dv = uv - ∫ v du, ¿qué parte debes saber integrar fácilmente?",
                        "respuesta_correcta": "dv",
                        "opciones": ["dv", "u", "du", "uv"]
                    },
                    "similares": [
                        {"pregunta": "Para ∫ x * eˣ dx, ¿qué eliges como 'u'?", "respuesta_correcta": "x", "opciones": ["x", "e^x", "dx", "ninguna"]},
                        {"pregunta": "Para ∫ ln(x) dx, ¿qué eliges como 'u'?", "respuesta_correcta": "ln(x)", "opciones": ["ln(x)", "x", "1", "dx"]},
                        {"pregunta": "¿La integración por partes viene de la regla del...?", "respuesta_correcta": "producto", "opciones": ["producto", "cociente", "cadena", "suma"]},
                        {"pregunta": "Si u=x, ¿cuánto vale du?", "respuesta_correcta": "dx", "opciones": ["dx", "x", "0", "1"]},
                        {"pregunta": "Si dv=eˣ dx, ¿cuánto vale v?", "respuesta_correcta": "e^x", "opciones": ["e^x", "x*e^x", "e^x/x", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Base de la Transformada de Fourier (análisis de señales digitales).", "consecuencia_de_error": "Falla en algoritmos de compresión de audio/video."},
                    "quimica": {"uso": "Mecánica Cuántica: valores esperados de posición y momento.", "consecuencia_de_error": "Cálculos cuánticos erróneos."},
                    "civil": {"uso": "Análisis de vigas con cargas triangulares.", "consecuencia_de_error": "Deflexión mal calculada."},
                    "mecanica": {"uso": "Centro de presión en superficies sumergidas.", "consecuencia_de_error": "Falla en compuertas de presas."},
                    "mecatronica": {"uso": "Respuesta en frecuencia de sistemas de control.", "consecuencia_de_error": "Diseño de filtros inestable."},
                    "aeronautica": {"uso": "Teoría de capa límite (fricción del aire).", "consecuencia_de_error": "Cálculo de arrastre incorrecto."},
                    "electrica": {"uso": "Cálculo de potencia RMS y energía en señales complejas.", "consecuencia_de_error": "Errores en medición de calidad de energía."}
                }
            },
            {
                "subtema_titulo": "7. Integrales Trigonométricas Básicas",
                "definicion": "Integrar funciones seno, coseno, tangente, etc. Son esenciales para todo lo que oscila o rota. Recuerda: ∫ cos(x) = sen(x), ∫ sen(x) = -cos(x).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ∫ (cos(x) + 2) dx\n1. Integral de cos(x) es sen(x).\n2. Integral de 2 es 2x.\nResultado: sen(x) + 2x + C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es la integral de -sen(x)?",
                        "respuesta_correcta": "cos(x)+C",
                        "opciones": ["cos(x)+C", "-cos(x)+C", "sen(x)", "-sen(x)"]
                    },
                    "similares": [
                        {"pregunta": "Integral de cos(x).", "respuesta_correcta": "sen(x)+C", "opciones": ["sen(x)+C", "-sen(x)", "cos(x)", "-cos(x)"]},
                        {"pregunta": "Integral de sec²(x). (Derivada de tan es sec²)", "respuesta_correcta": "tan(x)+C", "opciones": ["tan(x)+C", "sec(x)", "cos(x)", "sen(x)"]},
                        {"pregunta": "Integral de sen(2x). (Usa sustitución, divide por 2)", "respuesta_correcta": "-cos(2x)/2+C", "opciones": ["-cos(2x)/2+C", "cos(2x)", "-cos(2x)", "sen(2x)/2"]},
                        {"pregunta": "Integral de 0.", "respuesta_correcta": "C", "opciones": ["C", "0", "1", "x"]},
                        {"pregunta": "¿La integral de tan(x) es ln|sec(x)|?", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Generación de audio (sintetizadores) y gráficos (ondas).", "consecuencia_de_error": "Sonidos o animaciones distorsionadas."},
                    "quimica": {"uso": "Espectroscopía y análisis de ondas.", "consecuencia_de_error": "Mala interpretación de datos."},
                    "civil": {"uso": "Análisis de sismos (ondas) en estructuras.", "consecuencia_de_error": "Edificios vulnerables a terremotos."},
                    "mecanica": {"uso": "Vibraciones mecánicas (resortes, péndulos).", "consecuencia_de_error": "Falla por resonancia."},
                    "mecatronica": {"uso": "Control de motores AC (ondas sinusoidales).", "consecuencia_de_error": "Movimiento ineficiente del motor."},
                    "aeronautica": {"uso": "Corrientes alternas en sistemas de potencia del avión.", "consecuencia_de_error": "Falla eléctrica."},
                    "electrica": {"uso": "Cálculo de voltaje promedio y RMS en AC.", "consecuencia_de_error": "Mal diseño de fuentes de poder."}
                }
            },
            {
                "subtema_titulo": "8. Área entre Dos Curvas",
                "definicion": "Para hallar el área encerrada entre dos funciones f(x) (arriba) y g(x) (abajo), se integra la resta: ∫ [f(x) - g(x)] dx.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Área entre y=x y y=x² de 0 a 1.\n1. Arriba está y=x (en el intervalo 0-1). Abajo y=x².\n2. Resta: x - x².\n3. Integrar: (x²/2) - (x³/3) evaluado en 1.\n4. (1/2 - 1/3) = 1/6.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el área entre y=5 y y=0 de x=0 a x=2. (Rectángulo)",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "5", "2", "7"]
                    },
                    "similares": [
                        {"pregunta": "Área entre y=2x y el eje x de 0 a 2. (Triángulo)", "respuesta_correcta": "4", "opciones": ["4", "2", "8", "1"]},
                        {"pregunta": "Si f(x) > g(x), la integral es ∫(f - g).", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Área entre y=x y y=0 de 0 a 5.", "respuesta_correcta": "12.5", "opciones": ["12.5", "25", "10", "5"]},
                        {"pregunta": "Para hallar los límites de integración, debes encontrar los puntos de...", "respuesta_correcta": "interseccion", "opciones": ["interseccion", "tangencia", "inflexion", "corte"]},
                        {"pregunta": "El área siempre debe ser un número...", "respuesta_correcta": "positivo", "opciones": ["positivo", "negativo", "imaginario", "cero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de la diferencia de rendimiento entre dos algoritmos.", "consecuencia_de_error": "Mala elección de tecnología."},
                    "quimica": {"uso": "Comparación de perfiles de reacción.", "consecuencia_de_error": "Optimización de proceso fallida."},
                    "civil": {"uso": "Cálculo de áreas de corte y relleno en carreteras.", "consecuencia_de_error": "Errores en presupuesto de tierra."},
                    "mecanica": {"uso": "Trabajo neto en un ciclo termodinámico (área dentro del ciclo PV).", "consecuencia_de_error": "Cálculo de eficiencia del motor erróneo."},
                    "mecatronica": {"uso": "Error acumulado entre trayectoria deseada y real.", "consecuencia_de_error": "Mala calibración del robot."},
                    "aeronautica": {"uso": "Diferencia de presión entre intradós y extradós (sustentación).", "consecuencia_de_error": "Cálculo de sustentación incorrecto."},
                    "electrica": {"uso": "Energía disipada vs almacenada (histéresis).", "consecuencia_de_error": "Sobrecalentamiento de núcleos magnéticos."}
                }
            },
            {
                "subtema_titulo": "9. Sólidos de Revolución",
                "definicion": "Calcula el área de la 'piel' o superficie exterior de un sólido formado al girar una curva f(x). Fórmula: A = ∫ 2π * f(x) * √(1 + (f'(x))²) dx. Es como sumar cintas infinitas alrededor del eje.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Cilindro (girar y=3 de 0 a 2 alrededor de X).\n1. f(x)=3, f'(x)=0.\n2. Integral: ∫ 2π(3) √(1+0) dx = ∫ 6π dx.\n3. Evaluado de 0 a 2: 6π(2) - 0 = 12π.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el área superficial de girar y=2 (cilindro radio 2) de 0 a 5 alrededor del eje X. (2π*2*5)",
                        "respuesta_correcta": "20pi",
                        "opciones": ["20pi", "10pi", "40pi", "25pi"]
                    },
                    "similares": [
                        {"pregunta": "Al girar una línea recta y=mx se forma un...", "respuesta_correcta": "cono", "opciones": ["cono", "cilindro", "esfera", "toro"]},
                        {"pregunta": "La fórmula del área superficial incluye la longitud de... (arco/cuerda)", "respuesta_correcta": "arco", "opciones": ["arco", "cuerda", "radio", "altura"]},
                        {"pregunta": "Si giras un semicírculo sobre su diámetro obtienes el área de una...", "respuesta_correcta": "esfera", "opciones": ["esfera", "circulo", "disco", "anillo"]},
                        {"pregunta": "El término 2πy representa la ... de la cinta. (circunferencia/radio)", "respuesta_correcta": "circunferencia", "opciones": ["circunferencia", "radio", "area", "grosor"]},
                        {"pregunta": "Esta integral calcula el área de la superficie... (lateral/total)", "respuesta_correcta": "lateral", "opciones": ["lateral", "total", "base", "interna"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Renderizado de mallas 3D. Calcular texturas para objetos de revolución.", "consecuencia_de_error": "Texturas estiradas o deformes."},
                    "quimica": {"uso": "Área de contacto en tuberías para catálisis o transferencia de calor.", "consecuencia_de_error": "Diseño de intercambiadores de calor ineficiente."},
                    "civil": {"uso": "Cálculo de material para pintar tanques o cúpulas.", "consecuencia_de_error": "Presupuesto de pintura incorrecto."},
                    "mecanica": {"uso": "Área de superficie para disipación de calor en aletas de enfriamiento.", "consecuencia_de_error": "Motor que se sobrecalienta."},
                    "mecatronica": {"uso": "Diseño de carcasas protectoras para robots cilíndricos.", "consecuencia_de_error": "Material insuficiente para cubrir el robot."},
                    "aeronautica": {"uso": "Área mojada (wetted area) del fuselaje para calcular la fricción del aire.", "consecuencia_de_error": "Estimación de arrastre (drag) incorrecta."},
                    "electrica": {"uso": "Efecto piel (Skin effect). La corriente viaja por la superficie del conductor.", "consecuencia_de_error": "Cables de alta frecuencia con resistencia mayor a la esperada."}
                }
            },
            {
                "subtema_titulo": "10. Aplicación: Valor Promedio de una Función",
                "definicion": "El promedio continuo de una función f(x) en [a, b]. Fórmula: (1 / (b-a)) * ∫[a,b] f(x) dx. Es como 'aplanar' el área bajo la curva en un rectángulo.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Temperatura T(t) = 2t en un día de 0 a 10 horas.\nPromedio = (1/10) ∫ 2t dt = (1/10) [t²] de 0 a 10.\n= (1/10) * 100 = 10 grados promedio.",
                "ejercicio": {
                    "principal": {"pregunta": "Calcula el valor promedio de f(x)=4 de 0 a 5.", "respuesta_correcta": "4"},
                    "similares": [
                        {"pregunta": "Valor promedio de f(x)=2x de 0 a 2. (Integral=4, longitud=2)", "respuesta_correcta": "2"},
                        {"pregunta": "El voltaje promedio de una onda senoidal pura es...", "respuesta_correcta": "0"},
                        {"pregunta": "Para calcular el promedio, divides la integral entre la...", "respuesta_correcta": "longitud"},
                        {"pregunta": "Promedio de f(x)=10 de 2 a 4.", "respuesta_correcta": "10"},
                        {"pregunta": "Valor promedio de la velocidad es la velocidad media. (verdadero/falso)", "respuesta_correcta": "verdadero"}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Carga promedio de CPU.", "consecuencia_de_error": "Mal dimensionamiento de servidores."},
                    "quimica": {"uso": "Concentración promedio en un reactor.", "consecuencia_de_error": "Control de calidad deficiente."},
                    "civil": {"uso": "Carga promedio sobre un puente con tráfico variable.", "consecuencia_de_error": "Subestimar la fatiga del material."},
                    "mecanica": {"uso": "Potencia promedio de un motor en un ciclo.", "consecuencia_de_error": "Consumo de combustible mal calculado."},
                    "mecatronica": {"uso": "Corriente promedio en un motor PWM.", "consecuencia_de_error": "Sobrecalentamiento del motor."},
                    "aeronautica": {"uso": "Velocidad promedio de vuelo.", "consecuencia_de_error": "Error en tiempo de llegada."},
                    "electrica": {"uso": "Valor DC de una señal. Es fundamental en rectificadores.", "consecuencia_de_error": "Diseño de fuente de poder fallido."}
                }
            }
        ]
    },

    "ALGEBRA LINEAL": {
        "nombre_completo": "Álgebra Lineal: El Motor de la Ingeniería Moderna",
        "prerequisitos": ["VECTORES Y GEOMETRIA"],
        "quiz": [
            {
                "pregunta": "¿El determinante de la matriz identidad [[1, 0], [0, 1]] es?",
                "respuesta": "1",
                "opciones": ["1", "0", "2", "-1"]
            },
            {
                "pregunta": "Si Ax = b, y A tiene inversa, entonces x = ...",
                "respuesta": "A^-1*b",
                "opciones": ["A^-1*b", "b/A", "A*b", "b*A^-1"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Matrices: Definición y Dimensiones",
                "definicion": "Una Matriz es un arreglo rectangular de números ordenados en 'filas' (m) y 'columnas' (n). Su dimensión es m x n. Es la estructura de datos fundamental para almacenar información en ingeniería. Un vector es simplemente una matriz de una sola columna (n=1).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Matriz A = [[1, 2, 3], [4, 5, 6]].\n1. Cuenta las filas (horizontales): 2.\n2. Cuenta las columnas (verticales): 3.\n3. Dimensión: 2x3.\n4. Elemento a₂₃ (fila 2, columna 3) es el 6.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Dada la matriz M = [[1, 5], [2, 6], [3, 7]], ¿cuál es su dimensión? (filas x columnas, ej: 3x2)",
                        "respuesta_correcta": "3x2",
                        "opciones": ["3x2", "2x3", "6", "3x3"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuál es el elemento a₁₂ (fila 1, col 2) de M = [[10, 20], [30, 40]]?", "respuesta_correcta": "20", "opciones": ["20", "10", "30", "40"]},
                        {"pregunta": "Una matriz de 1 fila y 5 columnas se llama vector...", "respuesta_correcta": "fila", "opciones": ["fila", "columna", "nulo", "cuadrado"]},
                        {"pregunta": "Si A tiene 3 filas y 3 columnas, es una matriz...", "respuesta_correcta": "cuadrada", "opciones": ["cuadrada", "rectangular", "identidad", "nula"]},
                        {"pregunta": "La dimensión de un vector v = (x, y, z) escrito como columna es...", "respuesta_correcta": "3x1", "opciones": ["3x1", "1x3", "3x3", "1x1"]},
                        {"pregunta": "¿Cuántos elementos totales tiene una matriz de 4x5?", "respuesta_correcta": "20", "opciones": ["20", "9", "16", "25"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Almacenamiento de imágenes. Una imagen en escala de grises es una matriz donde cada elemento (pixel) es un número del 0 al 255.", "consecuencia_de_error": "Confundir filas con columnas rota la imagen 90 grados o corrompe el archivo al leerlo."},
                    "quimica": {"uso": "Matriz de coeficientes estequiométricos para balancear múltiples reacciones simultáneas.", "consecuencia_de_error": "Definir mal las dimensiones impide resolver el sistema de ecuaciones de balance de masa."},
                    "civil": {"uso": "Matriz de conectividad. Define qué vigas están conectadas a qué nodos en una estructura.", "consecuencia_de_error": "Un error aquí significa simular una estructura donde las vigas están flotando o desconectadas, invalidando el análisis."},
                    "mecanica": {"uso": "Tensor de Inercia. Una matriz 3x3 que describe cómo se distribuye la masa de un objeto 3D.", "consecuencia_de_error": "Usar las dimensiones incorrectas hace imposible calcular la dinámica rotacional (cómo gira el objeto)."},
                    "mecatronica": {"uso": "Matriz Jacobiana. Relaciona las velocidades de las articulaciones con la velocidad de la mano del robot.", "consecuencia_de_error": "Un error de dimensión en la Jacobiana hace que el código de control del robot falle (crash) inmediatamente."},
                    "aeronautica": {"uso": "Matrices de estado. Guardan todas las variables de vuelo (posición, velocidad, ángulos) en un solo bloque para el piloto automático.", "consecuencia_de_error": "Si el piloto automático lee la 'velocidad' en la casilla de la 'altitud', el avión se estrellará."},
                    "electrica": {"uso": "Matriz de Admitancia (Ybus) en sistemas de potencia. Modela toda la red eléctrica de una ciudad.", "consecuencia_de_error": "Dimensionar mal esta matriz impide simular el flujo de potencia y prevenir apagones."}
                }
            },
            {
                "subtema_titulo": "2. Suma y Resta de Matrices",
                "definicion": "Solo se pueden sumar o restar matrices de la **misma dimensión**. La operación se hace elemento a elemento: C₁₁ = A₁₁ + B₁₁. Es una operación lineal fundamental.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Sumar A=[[1, 2], [3, 4]] y B=[[10, 10], [10, 10]].\nC = [[1+10, 2+10], [3+10, 4+10]]\nResultado: [[11, 12], [13, 14]].",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Suma [[1, 5], [2, -1]] + [[0, 2], [3, 4]].",
                        "respuesta_correcta": "[[1,7],[5,3]]",
                        "opciones": ["[[1,7],[5,3]]", "[[1,3],[5,7]]", "[[0,0],[0,0]]", "[[1,5],[2,4]]"]
                    },
                    "similares": [
                        {"pregunta": "Resta [[10, 10]] - [[2, 3]].", "respuesta_correcta": "[[8,7]]", "opciones": ["[[8,7]]", "[[12,13]]", "[[-8,-7]]", "[[20,30]]"]},
                        {"pregunta": "Suma [[1], [2]] + [[3], [4]]. (Vector columna)", "respuesta_correcta": "[[4],[6]]", "opciones": ["[[4],[6]]", "[[3],[8]]", "[[2],[2]]", "[[1],[4]]"]},
                        {"pregunta": "¿Se puede sumar una matriz 2x2 con una 2x3? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Si A + B = C, entonces B + A = C. ¿Esta propiedad es...?", "respuesta_correcta": "conmutativa", "opciones": ["conmutativa", "asociativa", "distributiva", "identidad"]},
                        {"pregunta": "Calcula [[5, 0], [0, 5]] - [[5, 0], [0, 5]].", "respuesta_correcta": "[[0,0],[0,0]]", "opciones": ["[[0,0],[0,0]]", "[[10,0],[0,10]]", "[[5,5],[5,5]]", "[[1,1],[1,1]]"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de imágenes: Sumar dos imágenes para hacer una superposición o restar el 'fondo' para detectar movimiento.", "consecuencia_de_error": "Si las imágenes no tienen la misma dimensión, la operación falla o genera ruido visual."},
                    "quimica": {"uso": "Suma de espectros. Si tienes una mezcla, el espectro total es la suma de los espectros de los componentes individuales.", "consecuencia_de_error": "No poder identificar los componentes de una mezcla compleja."},
                    "civil": {"uso": "Superposición de cargas. Se calcula la matriz de fuerzas por 'peso propio' y se suma a la matriz de fuerzas por 'viento'.", "consecuencia_de_error": "Ignorar la suma de efectos puede llevar a subestimar la carga total sobre una columna."},
                    "mecanica": {"uso": "Suma de campos de desplazamiento en análisis de vibraciones (superposición modal).", "consecuencia_de_error": "Predicción incorrecta de la deformación total de la pieza."},
                    "mecatronica": {"uso": "Suma de vectores de error en control. Error_Total = Error_Posición + Error_Velocidad (ponderados).", "consecuencia_de_error": "Un control inestable que no corrige bien el movimiento."},
                    "aeronautica": {"uso": "Suma de matrices de perturbación. Se suma el efecto del viento al estado nominal del avión.", "consecuencia_de_error": "El simulador de vuelo no reflejará las condiciones reales de turbulencia."},
                    "electrica": {"uso": "Suma de corrientes en un nodo (Matricial). I_total = I_fuente + I_carga.", "consecuencia_de_error": "Violación de la Ley de Kirchhoff y análisis de circuito fallido."}
                }
            },
            {
                "subtema_titulo": "3. Multiplicación de Matrices (El Corazón del Álgebra Lineal)",
                "definicion": "La operación más importante. Multiplicar A (mxn) por B (nxp) da una matriz C (mxp). La regla es: 'Fila por Columna'. Cada elemento Cᵢⱼ es el producto punto de la Fila 'i' de A por la Columna 'j' de B.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: [[1, 2]] (1x2) multiplicado por [[3], [4]] (2x1).\n1. Fila 1 de A: (1, 2). Columna 1 de B: (3, 4).\n2. Producto punto: (1*3) + (2*4) = 3 + 8 = 11.\n3. Resultado: [[11]] (una matriz 1x1).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Multiplica A=[[1, 0], [0, 1]] por B=[[5], [6]]. (Identidad por vector)",
                        "respuesta_correcta": "[[5],[6]]",
                        "opciones": ["[[5],[6]]", "[[1],[0]]", "[[6],[5]]", "[[5, 6]]"]
                    },
                    "similares": [
                        {"pregunta": "Calcula [[2, 0], [0, 2]] * [[3], [4]]. (Escalado)", "respuesta_correcta": "[[6],[8]]", "opciones": ["[[6],[8]]", "[[3],[4]]", "[[2],[2]]", "[[5],[6]]"]},
                        {"pregunta": "Multiplica [[1, 2], [3, 4]] * [[1, 0], [0, 1]]. (Por identidad)", "respuesta_correcta": "[[1,2],[3,4]]", "opciones": ["[[1,2],[3,4]]", "[[0,0],[0,0]]", "[[1,0],[0,1]]", "[[3,4],[1,2]]"]},
                        {"pregunta": "Para multiplicar A*B, el número de columnas de A debe ser igual al número de ... de B.", "respuesta_correcta": "filas", "opciones": ["filas", "columnas", "diagonales", "elementos"]},
                        {"pregunta": "Si A es 3x2 y B es 2x4, ¿de qué dimensión es el resultado?", "respuesta_correcta": "3x4", "opciones": ["3x4", "2x2", "3x2", "2x4"]},
                        {"pregunta": "Calcula [[0, 1], [1, 0]] * [[2], [3]]. (Intercambia filas)", "respuesta_correcta": "[[3],[2]]", "opciones": ["[[3],[2]]", "[[2],[3]]", "[[0],[0]]", "[[1],[1]]"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Gráficos 3D. Rotar, escalar y mover un personaje es simplemente multiplicar su matriz de vértices por una 'Matriz de Transformación'.", "consecuencia_de_error": "Si el orden de multiplicación es incorrecto (A*B vs B*A), el personaje girará alrededor del punto equivocado y saldrá volando."},
                    "quimica": {"uso": "Operadores en Mecánica Cuántica. Aplicar un operador a una función de onda es una multiplicación matriz-vector.", "consecuencia_de_error": "Resultados cuánticos físicamente imposibles."},
                    "civil": {"uso": "F = K * d. (Fuerza = Matriz de Rigidez * Desplazamiento). Es la ecuación fundamental del análisis estructural.", "consecuencia_de_error": "Si la multiplicación está mal, se calculan fuerzas internas falsas y el edificio se diseña mal."},
                    "mecanica": {"uso": "Dinámica multicuerpo. Calcular las velocidades de todos los eslabones de una máquina a la vez.", "consecuencia_de_error": "Simulación cinemática que no respeta las uniones mecánicas."},
                    "mecatronica": {"uso": "Cinemática Directa: Multiplicar las matrices de cada articulación (A1 * A2 * A3) para saber dónde está la mano del robot.", "consecuencia_de_error": "El robot golpea una pared porque calculó mal su posición final."},
                    "aeronautica": {"uso": "Rotación de coordenadas. Convertir la velocidad del viento (ejes tierra) a ejes del avión usando una matriz de rotación.", "consecuencia_de_error": "El avión corrige el viento en la dirección equivocada."},
                    "electrica": {"uso": "V = Z * I. (Vector Voltaje = Matriz de Impedancia * Vector Corriente). Análisis de redes complejas.", "consecuencia_de_error": "Cálculo erróneo de caídas de voltaje en la red."}
                }
            },
            {
                "subtema_titulo": "4. Determinantes (2x2 y 3x3)",
                "definicion": "El determinante (det(A) o |A|) es un número único asociado a una matriz cuadrada. Mide cómo la matriz 'escala' el área (en 2D) o volumen (en 3D). Si el Det=0, la matriz 'aplasta' el espacio y NO tiene inversa (es singular).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Det de A = [[3, 1], [4, 2]].\nFórmula 2x2: (a*d) - (b*c).\nDet = (3*2) - (1*4) = 6 - 4 = 2.\n(Como no es 0, el sistema tiene solución única).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el determinante de [[5, 2], [3, 1]]. (5*1 - 2*3)",
                        "respuesta_correcta": "-1",
                        "opciones": ["-1", "1", "11", "0"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el determinante de [[1, 0], [0, 1]].", "respuesta_correcta": "1", "opciones": ["1", "0", "2", "-1"]},
                        {"pregunta": "Calcula el determinante de [[2, 2], [2, 2]]. (Linealmente dependiente)", "respuesta_correcta": "0", "opciones": ["0", "4", "8", "-4"]},
                        {"pregunta": "Si el determinante es 0, la matriz se llama...", "respuesta_correcta": "singular", "opciones": ["singular", "invertible", "identidad", "diagonal"]},
                        {"pregunta": "Calcula el determinante de [[10, 0], [0, 5]].", "respuesta_correcta": "50", "opciones": ["50", "15", "5", "0"]},
                        {"pregunta": "En una matriz 3x3, si una fila es ceros, el determinante es...", "respuesta_correcta": "0", "opciones": ["0", "1", "infinito", "desconocido"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Para verificar si un sistema de ecuaciones tiene solución única antes de gastar recursos en resolverlo.", "consecuencia_de_error": "El programa entra en un bucle infinito o crashea por 'división por cero' al intentar invertir una matriz singular."},
                    "quimica": {"uso": "El Jacobiano (un determinante) se usa para cambiar variables en integrales múltiples termodinámicas.", "consecuencia_de_error": "Cálculo de energía libre incorrecto."},
                    "civil": {"uso": "Verificar la estabilidad de una estructura. Si el determinante de la Matriz de Rigidez es 0, la estructura es inestable (un mecanismo).", "consecuencia_de_error": "Diseñar un puente que se derrumba por su propio peso porque no es estático."},
                    "mecanica": {"uso": "Producto Cruz: El vector resultante se calcula formalmente como el determinante de una matriz con i,j,k.", "consecuencia_de_error": "Cálculo de torque incorrecto."},
                    "mecatronica": {"uso": "Singularidades del robot. Si el determinante del Jacobiano es 0, el robot pierde un grado de libertad (se 'traba').", "consecuencia_de_error": "El robot se bloquea mecánicamente o sus motores se aceleran al infinito tratando de moverse en una dirección imposible."},
                    "aeronautica": {"uso": "Estabilidad dinámica. Los signos de los determinantes en las ecuaciones de movimiento indican si el avión es estable o inestable.", "consecuencia_de_error": "Diseñar un avión que entra en barrena incontrolable."},
                    "electrica": {"uso": "Resolución de circuitos por Regla de Cramer (usa determinantes).", "consecuencia_de_error": "Método ineficiente para sistemas grandes, pero útil teóricamente para entender la solubilidad del circuito."}
                }
            },
            {
                "subtema_titulo": "5. Matriz Inversa (A⁻¹)",
                "definicion": "La inversa A⁻¹ es la matriz que 'deshace' lo que hizo A. A * A⁻¹ = I (Identidad). Es análogo a dividir (multiplicar por 1/x). Solo existe si el determinante no es cero. Se usa para despejar la 'x' en Ax=b -> x = A⁻¹b.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Si A multiplica un vector por 2, su inversa A⁻¹ lo divide por 2 (multiplica por 0.5).\nSi A=[[2,0],[0,2]], entonces A⁻¹=[[0.5,0],[0,0.5]].\nComprobación: 2 * 0.5 = 1.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si A = [[4, 0], [0, 1]], ¿cuál es su inversa? (Inverso de la diagonal)",
                        "respuesta_correcta": "[[0.25,0],[0,1]]",
                        "opciones": ["[[0.25,0],[0,1]]", "[[4,0],[0,1]]", "[[-4,0],[0,-1]]", "[[1,0],[0,4]]"]
                    },
                    "similares": [
                        {"pregunta": "La inversa de la matriz identidad I es...", "respuesta_correcta": "I", "opciones": ["I", "-I", "0", "A"]},
                        {"pregunta": "Si A * B = I, entonces B es la ... de A.", "respuesta_correcta": "inversa", "opciones": ["inversa", "transpuesta", "adjunta", "copia"]},
                        {"pregunta": "Para que exista la inversa, la matriz debe ser... (cuadrada/rectangular)", "respuesta_correcta": "cuadrada", "opciones": ["cuadrada", "rectangular", "triangular", "nula"]},
                        {"pregunta": "Si el determinante es 0, la inversa... (existe/no existe)", "respuesta_correcta": "no existe", "opciones": ["no existe", "existe", "es cero", "es identidad"]},
                        {"pregunta": "La inversa de una matriz de rotación es la rotación en sentido...", "respuesta_correcta": "contrario", "opciones": ["contrario", "igual", "doble", "nulo"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Desencriptación. Si la matriz A encripta el mensaje, la matriz A⁻¹ lo desencripta.", "consecuencia_de_error": "Pérdida de datos; el mensaje original no se puede recuperar."},
                    "quimica": {"uso": "Desacoplar espectros mezclados. Si tienes una mezcla de señales, la inversa te dice cuánto hay de cada componente puro.", "consecuencia_de_error": "Análisis químico incorrecto."},
                    "civil": {"uso": "Resolver el sistema [K]{d}={F}. El desplazamiento {d} = [K]⁻¹ * {F}. Permite saber cuánto se deforma el edificio ante una fuerza.", "consecuencia_de_error": "Cálculo de deformación erróneo. El edificio podría moverse más de lo permitido por seguridad."},
                    "mecanica": {"uso": "Recuperar las fuerzas originales a partir de las lecturas de deformación de un sensor (strain gauge).", "consecuencia_de_error": "Medición de fuerza incorrecta."},
                    "mecatronica": {"uso": "Cinemática de Velocidad Inversa. Calcular la velocidad de los motores necesaria para que la mano se mueva a cierta velocidad (v = J * w -> w = J⁻¹ * v).", "consecuencia_de_error": "El robot se mueve a la velocidad incorrecta o en la dirección incorrecta."},
                    "aeronautica": {"uso": "Sistemas de navegación inercial. Invertir la matriz de rotación para saber la posición global a partir de los sensores locales.", "consecuencia_de_error": "El avión pierde su ubicación en el mapa."},
                    "electrica": {"uso": "Desacoplar sistemas MIMO (Multiple Input Multiple Output) en control avanzado.", "consecuencia_de_error": "Interferencia entre señales de control."}
                }
            },
            {
                "subtema_titulo": "6. Sistemas de Ecuaciones Lineales (Ax = b)",
                "definicion": "Representar un sistema de ecuaciones como una matriz. 'A' es la matriz de coeficientes, 'x' el vector de incógnitas, 'b' el vector de resultados. Resolver el sistema es encontrar el vector 'x'.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Sistema:\n2x + y = 5\nx - y = 1\nMatriz A = [[2, 1], [1, -1]]. Vector b = [[5], [1]].\nEcuación Matricial: [[2, 1], [1, -1]] * [[x], [y]] = [[5], [1]].",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Escribe el vector b para el sistema: 3x=9, 2y=4.",
                        "respuesta_correcta": "[[9],[4]]",
                        "opciones": ["[[9],[4]]", "[[3],[2]]", "[[9, 4]]", "[[0],[0]]"]
                    },
                    "similares": [
                        {"pregunta": "Escribe la matriz A para: 1x + 2y = 5, 3x + 4y = 6.", "respuesta_correcta": "[[1,2],[3,4]]", "opciones": ["[[1,2],[3,4]]", "[[1,3],[2,4]]", "[[5],[6]]", "[[0,0],[0,0]]"]},
                        {"pregunta": "En Ax=b, ¿qué representa x?", "respuesta_correcta": "vector de incognitas", "opciones": ["vector de incognitas", "vector de resultados", "matriz identidad", "determinante"]},
                        {"pregunta": "Si tienes 3 ecuaciones con 3 incógnitas, A es de tamaño...", "respuesta_correcta": "3x3", "opciones": ["3x3", "3x1", "1x3", "9x9"]},
                        {"pregunta": "Un sistema homogéneo es cuando b es igual a...", "respuesta_correcta": "0", "opciones": ["0", "1", "x", "A"]},
                        {"pregunta": "Resolver Ax=b es encontrar el punto de ... de las rectas/planos.", "respuesta_correcta": "interseccion", "opciones": ["interseccion", "origen", "tangencia", "paralelismo"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Resolución de circuitos lógicos y optimización de redes.", "consecuencia_de_error": "Diseño de red ineficiente."},
                    "quimica": {"uso": "Balanceo de ecuaciones químicas. Cada elemento es una ecuación lineal.", "consecuencia_de_error": "Ecuación química imposible o no balanceada."},
                    "civil": {"uso": "Método de los Elementos Finitos (FEM). Un edificio se modela como un sistema gigante de Ax=b donde x son los desplazamientos.", "consecuencia_de_error": "Es la base de todo el software moderno de ingeniería civil. Un error aquí es impensable."},
                    "mecanica": {"uso": "Análisis de equilibrio estático de cuerpos rígidos complejos.", "consecuencia_de_error": "Falla de soportes."},
                    "mecatronica": {"uso": "Sensor Fusion: Combinar datos de múltiples sensores para obtener una mejor estimación (filtro de Kalman, basado en Ax=b).", "consecuencia_de_error": "Datos de sensores ruidosos e inexactos."},
                    "aeronautica": {"uso": "Distribución de flujo en una red de tuberías de combustible.", "consecuencia_de_error": "Falta de combustible en un motor."},
                    "electrica": {"uso": "Análisis de Mallas y Nodos. Encontrar todos los voltajes y corrientes de un circuito resolviendo la matriz.", "consecuencia_de_error": "No poder analizar circuitos con más de 2 componentes."}
                }
            },
            {
                "subtema_titulo": "7. Eliminación de Gauss-Jordan",
                "definicion": "El algoritmo sistemático para resolver sistemas Ax=b. Se usan operaciones de fila (sumar filas, multiplicar por escalares) para convertir la matriz A en la matriz Identidad (I). Al final, el vector 'b' se convierte en la solución 'x'.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Matriz Aumentada [[1, 1 | 3], [1, -1 | 1]] (Sistema x+y=3, x-y=1)\n1. Fila2 = Fila2 - Fila1 -> [[1, 1 | 3], [0, -2 | -2]]\n2. Fila2 = Fila2 / -2 -> [[1, 1 | 3], [0, 1 | 1]] (y=1)\n3. Fila1 = Fila1 - Fila2 -> [[1, 0 | 2], [0, 1 | 1]]\nResultado: x=2, y=1.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la matriz [[1, 0 | 5], [0, 1 | 2]], ¿cuánto vale x?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "1", "0", "2"]
                    },
                    "similares": [
                        {"pregunta": "En la misma matriz, ¿cuánto vale y?", "respuesta_correcta": "2", "opciones": ["2", "5", "1", "0"]},
                        {"pregunta": "El objetivo de Gauss-Jordan es obtener la matriz...", "respuesta_correcta": "identidad", "opciones": ["identidad", "diagonal", "nula", "transpuesta"]},
                        {"pregunta": "¿Puedes multiplicar una fila por cero en Gauss-Jordan? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "¿Puedes intercambiar dos filas? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "Si obtienes una fila de ceros igual a un número (0 0 | 5), el sistema no tiene...", "respuesta_correcta": "solucion", "opciones": ["solucion", "incognitas", "matriz", "filas"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Es el algoritmo que usan las computadoras (librerías como LAPACK) para resolver sistemas lineales.", "consecuencia_de_error": "Implementación ineficiente o numéricamente inestable del solver."},
                    "quimica": {"uso": "Cálculo de mezclas complejas.", "consecuencia_de_error": "Receta química incorrecta."},
                    "civil": {"uso": "El solver interno de SAP2000/Revit usa variaciones optimizadas de Gauss para resolver las estructuras.", "consecuencia_de_error": "Resultados de simulación incorrectos."},
                    "mecanica": {"uso": "Resolución de fuerzas en armaduras estáticamente determinadas.", "consecuencia_de_error": "Cálculo de fuerza incorrecto."},
                    "mecatronica": {"uso": "Inversión de matrices en tiempo real para control de robots.", "consecuencia_de_error": "Retardo en el control si el algoritmo es lento."},
                    "aeronautica": {"uso": "Balance de carga y centrado del avión.", "consecuencia_de_error": "Avión desbalanceado."},
                    "electrica": {"uso": "Resolución de sistemas de ecuaciones de circuitos grandes.", "consecuencia_de_error": "Análisis de circuito fallido."}
                }
            },
            {
                "subtema_titulo": "8. Espacios Vectoriales y Base",
                "definicion": "Un Espacio Vectorial es un conjunto de vectores que se pueden sumar y escalar. Una 'Base' es el conjunto mínimo de vectores necesarios para generar todo el espacio (ej. i, j, k generan todo el espacio 3D). La 'Dimensión' es el número de vectores en la base.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: R² (el plano 2D). Base estándar: {(1,0), (0,1)}.\nCualquier vector (a,b) se puede escribir como a*(1,0) + b*(0,1).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuántos vectores se necesitan para formar una base en R³ (espacio 3D)?",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "2", "1", "Infinite"]
                    },
                    "similares": [
                        {"pregunta": "¿Son (1,0) y (2,0) una base de R²? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "La base estándar de R² son los vectores i y...", "respuesta_correcta": "j", "opciones": ["j", "k", "0", "v"]},
                        {"pregunta": "Si una base tiene 2 vectores, la dimensión del espacio es...", "respuesta_correcta": "2", "opciones": ["2", "3", "1", "4"]},
                        {"pregunta": "¿El vector (0,0) puede ser parte de una base? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "La 'independencia lineal' es requisito para una base.", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Compresión de imágenes (JPEG). Se cambia de la base de 'pixeles' a una base de 'frecuencias' (cosenos), donde es más fácil comprimir.", "consecuencia_de_error": "Archivos de imagen enormes o de muy mala calidad."},
                    "quimica": {"uso": "Orbitales Moleculares: Se construyen como una combinación lineal de orbitales atómicos (que sirven como base).", "consecuencia_de_error": "Teoría de enlace químico incorrecta."},
                    "civil": {"uso": "Análisis Modal. Las vibraciones de un edificio se descomponen en una 'base' de modos naturales de vibración.", "consecuencia_de_error": "No identificar el modo de vibración que causará resonancia con un sismo."},
                    "mecanica": {"uso": "Grados de libertad de un mecanismo. El número de vectores base necesarios para describir su movimiento.", "consecuencia_de_error": "Diseñar un mecanismo que se traba (sobrerestringido) o se mueve sin control (subrestringido)."},
                    "mecatronica": {"uso": "Espacio de estados. Representar el estado de un sistema complejo como un vector en un espacio n-dimensional.", "consecuencia_de_error": "Imposibilidad de aplicar control moderno (State-Space Control)."},
                    "aeronautica": {"uso": "Modos de estabilidad de la aeronave (Fugoide, Corto Periodo). Son la base del movimiento dinámico.", "consecuencia_de_error": "Diseño de avión inestable."},
                    "electrica": {"uso": "Análisis de señales. Cualquier señal se puede representar como suma de senos y cosenos (Serie de Fourier, una base de funciones).", "consecuencia_de_error": "Imposible diseñar sistemas de telecomunicaciones (WiFi, 5G)."}
                }
            },
            {
                "subtema_titulo": "9. Eigenvalores y Eigenvectores (Valores Propios)",
                "definicion": "Son la 'huella digital' de una matriz cuadrada. Un 'Eigenvector' (v) es un vector que NO cambia de dirección cuando es transformado por la matriz A. Solo se estira o encoge. El factor de estiramiento es el 'Eigenvalor' (λ). Ecuación: Av = λv.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Matriz A = [[3, 0], [0, 5]].\nSi v = (1, 0), Av = (3, 0) = 3*v. (La dirección no cambió, se estiró por 3).\nEntonces, 3 es un eigenvalor y (1, 0) es su eigenvector.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si A es una matriz diagonal [[4, 0], [0, 2]], ¿cuál es el eigenvalor asociado al primer eje?",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "2", "0", "8"]
                    },
                    "similares": [
                        {"pregunta": "En Av = λv, ¿qué símbolo representa el eigenvalor?", "respuesta_correcta": "lambda", "opciones": ["lambda", "v", "A", "x"]},
                        {"pregunta": "Si λ = 1, la matriz... el vector.", "respuesta_correcta": "mantiene", "opciones": ["mantiene", "duplica", "anula", "invierte"]},
                        {"pregunta": "Si λ = 0, la matriz... el vector.", "respuesta_correcta": "anula", "opciones": ["anula", "mantiene", "duplica", "invierte"]},
                        {"pregunta": "Los eigenvalores determinan la ... del sistema.", "respuesta_correcta": "estabilidad", "opciones": ["estabilidad", "masa", "carga", "velocidad"]},
                        {"pregunta": "¿Los eigenvectores cambian de dirección al multiplicarse por A? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Google PageRank. El eigenvector principal de la 'matriz de internet' dice qué páginas son las más importantes.", "consecuencia_de_error": "Motores de búsqueda irrelevantes."},
                    "quimica": {"uso": "Mecánica Cuántica. La Ecuación de Schrödinger es una ecuación de eigenvalores/eigenvectores. Los eigenvalores son los niveles de energía permitidos.", "consecuencia_de_error": "Imposible entender el átomo o diseñar nuevos materiales."},
                    "civil": {"uso": "Pandeo de columnas. El eigenvalor más pequeño de la matriz de rigidez es la carga crítica de pandeo.", "consecuencia_de_error": "Colapso súbito de columnas bajo peso."},
                    "mecanica": {"uso": "Frecuencias Naturales. Los eigenvalores de un sistema mecánico son las frecuencias a las que vibrará naturalmente (resonancia).", "consecuencia_de_error": "Si una máquina opera a su frecuencia natural (un eigenvalor), se destruirá."},
                    "mecatronica": {"uso": "Estabilidad de Control. Si todos los eigenvalores (polos) tienen parte real negativa, el robot es estable.", "consecuencia_de_error": "Robot inestable que oscila o se sale de control."},
                    "aeronautica": {"uso": "Análisis de 'Flutter' (Flameo). Vibraciones autoexcitadas en las alas que dependen de los eigenvalores complejos del sistema.", "consecuencia_de_error": "Desintegración del ala en vuelo."},
                    "electrica": {"uso": "Modos de propagación en guías de onda.", "consecuencia_de_error": "Pérdida de señal en cables o fibra óptica."}
                }
            },
            {
                "subtema_titulo": "10. Transformaciones Lineales (Geometría)",
                "definicion": "Ver las matrices como 'funciones' que mueven el espacio. Una matriz puede rotar, escalar, reflejar o inclinar (shear) un vector. Multiplicar por una matriz es transformar el espacio.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Matriz de Escala S = [[2, 0], [0, 2]].\nSi v = (1, 1), Sv = (2, 2). Duplicó el tamaño del vector sin cambiar su dirección.\nEjemplo: Matriz de Rotación 90° R = [[0, -1], [1, 0]]. Rv = (-1, 1).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si aplicas la matriz identidad I a un vector v, el resultado es...",
                        "respuesta_correcta": "v",
                        "opciones": ["v", "0", "-v", "2v"]
                    },
                    "similares": [
                        {"pregunta": "Una matriz que agranda un objeto se llama matriz de...", "respuesta_correcta": "escala", "opciones": ["escala", "rotacion", "traslacion", "proyeccion"]},
                        {"pregunta": "Una matriz que gira un objeto se llama matriz de...", "respuesta_correcta": "rotacion", "opciones": ["rotacion", "escala", "identidad", "nula"]},
                        {"pregunta": "Para aplicar dos transformaciones A y B, se multiplican las matrices: C = A*B.", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La transformación lineal mapea el origen (0,0) al...", "respuesta_correcta": "0,0", "opciones": ["0,0", "1,1", "infinito", "cualquiera"]},
                        {"pregunta": "Si el determinante es negativo, la transformación invierte la orientación (espejo).", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Toda la computación gráfica (videojuegos, películas CGI). Mover, rotar y escalar objetos 3D son multiplicaciones de matrices.", "consecuencia_de_error": "Gráficos distorsionados o objetos en posiciones incorrectas."},
                    "quimica": {"uso": "Operaciones de simetría en moléculas (rotaciones, reflexiones) para clasificarlas en grupos puntuales.", "consecuencia_de_error": "Error en la predicción de espectros (IR/Raman)."},
                    "civil": {"uso": "Transformación de coordenadas locales (de la viga) a coordenadas globales (del edificio).", "consecuencia_de_error": "Ensamblaje incorrecto de la matriz de rigidez global, resultados de simulación erróneos."},
                    "mecanica": {"uso": "Análisis de deformación (Strain). Cómo un cuadrado se deforma en un rombo bajo carga.", "consecuencia_de_error": "Cálculo incorrecto de la plasticidad o falla del material."},
                    "mecatronica": {"uso": "Visión por computadora. Transformar la imagen de la cámara (perspectiva) a coordenadas del mundo real.", "consecuencia_de_error": "El robot ve un objeto en una posición pero intenta agarrarlo en otra."},
                    "aeronautica": {"uso": "Transformación entre ejes de viento, ejes de estabilidad y ejes de cuerpo para ecuaciones de vuelo.", "consecuencia_de_error": "Errores en la simulación de la dinámica de vuelo."},
                    "electrica": {"uso": "Transformada de Clarke y Park. Convierte corrientes trifásicas (abc) en un sistema rotatorio (dq0) para controlar motores.", "consecuencia_de_error": "Control vectorial de motores imposible. Motores menos eficientes."}
                }
            }
        ]
    },

    "CALCULO VECTORIAL": {
        "nombre_completo": "Cálculo Vectorial: Movimiento y Campos",
        "prerequisitos": ["CALCULO INTEGRAL", "VECTORES Y GEOMETRIA"],
        "quiz": [
            {
                "pregunta": "Si r(t) = (t, t²), ¿cuál es el vector velocidad r'(t)?",
                "respuesta": "(1, 2t)",
                "opciones": ["(1, 2t)", "(t, 2t)", "(0, 2t)", "(1, t)"]
            },
            {
                "pregunta": "El gradiente de f(x,y) es un vector perpendicular a las curvas de...",
                "respuesta": "nivel",
                "opciones": ["nivel", "fuerza", "tiempo", "campo"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Funciones Vectoriales Planas (Trayectorias)",
                "definicion": "Una función vectorial en 2D, r(t) = (x(t), y(t)), describe la posición de una partícula en el plano en función del tiempo 't'. En lugar de una gráfica estática y=f(x), esto es una película del movimiento. ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: r(t) = (2t, t²). (Una parábola).\nSi t=0, pos = (0, 0).\nSi t=1, pos = (2, 1).\nSi t=2, pos = (4, 4).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si r(t) = (t + 1, 3t), ¿cuál es la posición en t=2? (Formato: (x, y))",
                        "respuesta_correcta": "(3, 6)",
                        "opciones": ["(3, 6)", "(2, 6)", "(3, 3)", "(1, 6)"]
                    },
                    "similares": [
                        {"pregunta": "Si r(t) = (t², t), ¿dónde está en t=3?", "respuesta_correcta": "(9, 3)", "opciones": ["(9, 3)", "(3, 9)", "(6, 3)", "(9, 9)"]},
                        {"pregunta": "Si r(t) = (cos t, sen t), en t=0, la posición es...", "respuesta_correcta": "(1, 0)", "opciones": ["(1, 0)", "(0, 1)", "(0, 0)", "(-1, 0)"]},
                        {"pregunta": "Para r(t) = (2t, 5), ¿la coordenada 'y' cambia? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Si x(t)=t y y(t)=t, la trayectoria es una...", "respuesta_correcta": "recta", "opciones": ["recta", "parabola", "circulo", "elipse"]},
                        {"pregunta": "En t=0, r(t)=(5t, 10t) está en el...", "respuesta_correcta": "origen", "opciones": ["origen", "final", "eje x", "eje y"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Animación de sprites 2D. r(t) define dónde dibujar al personaje en cada frame.", "consecuencia_de_error": "El personaje se teletransporta o se mueve a saltos."},
                    "quimica": {"uso": "Difusión en placas de Petri. Modelar la posición de un frente de reacción en 2D.", "consecuencia_de_error": "Medición incorrecta de la velocidad de difusión."},
                    "civil": {"uso": "Diseño de curvas de carreteras (alineamiento horizontal). r(t) es el eje de la vía.", "consecuencia_de_error": "Curvas demasiado cerradas que causan accidentes."},
                    "mecanica": {"uso": "Trayectoria de una herramienta de corte en un torno o fresadora CNC 2D.", "consecuencia_de_error": "La máquina corta la pieza con la forma equivocada."},
                    "mecatronica": {"uso": "Planificación de ruta para robots móviles (ej. aspiradoras) en el piso (plano 2D).", "consecuencia_de_error": "El robot choca o no cubre toda el área."},
                    "aeronautica": {"uso": "Patrones de espera en el tráfico aéreo (vistos desde arriba, en radar 2D).", "consecuencia_de_error": "Colisión entre aeronaves por no seguir la ruta precisa."},
                    "electrica": {"uso": "Trayectoria de un electrón en un campo magnético perpendicular (círculo en 2D).", "consecuencia_de_error": "Fallo en el diseño de tubos de vacío o sensores Hall."}
                }
            },
            {
                "subtema_titulo": "2. Derivada Vectorial (Velocidad Instantánea)",
                "definicion": "La derivada r'(t) es el vector velocidad v(t). Se obtiene derivando cada componente: v(t) = (x'(t), y'(t)). Este vector siempre es 'tangente' a la trayectoria y apunta hacia donde se mueve el objeto.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: r(t) = (t², 3t).\nDerivamos x: d(t²)/dt = 2t.\nDerivamos y: d(3t)/dt = 3.\nVector Velocidad v(t) = (2t, 3).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si r(t) = (5t, t³), calcula el vector velocidad v(t). (Formato: (5, 3t^2))",
                        "respuesta_correcta": "(5, 3t^2)",
                        "opciones": ["(5, 3t^2)", "(5t, 3t^2)", "(0, 3t)", "(5, 3t)"]
                    },
                    "similares": [
                        {"pregunta": "Si r(t) = (cos t, sen t), calcula v(t).", "respuesta_correcta": "(-sen t, cos t)", "opciones": ["(-sen t, cos t)", "(sen t, cos t)", "(cos t, -sen t)", "(-cos t, sen t)"]},
                        {"pregunta": "Deriva r(t) = (4, 2t).", "respuesta_correcta": "(0, 2)", "opciones": ["(0, 2)", "(4, 2)", "(0, 2t)", "(4, 0)"]},
                        {"pregunta": "Si la posición es (t, t), la velocidad es...", "respuesta_correcta": "(1, 1)", "opciones": ["(1, 1)", "(t, t)", "(0, 0)", "(1, 0)"]},
                        {"pregunta": "El vector velocidad es ... a la trayectoria.", "respuesta_correcta": "tangente", "opciones": ["tangente", "perpendicular", "paralelo", "secante"]},
                        {"pregunta": "Si v(t) = (0,0), el objeto está...", "respuesta_correcta": "quieto", "opciones": ["quieto", "moviendose", "acelerando", "girando"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Motores de física 2D (como Box2D). La velocidad determina el rebote y la fricción.", "consecuencia_de_error": "Objetos que atraviesan paredes o no rebotan."},
                    "quimica": {"uso": "Velocidad de migración de iones en electroforesis de gel (2D).", "consecuencia_de_error": "Separación incorrecta de ADN o proteínas."},
                    "civil": {"uso": "Velocidad de flujo de agua en un canal abierto (visto en planta).", "consecuencia_de_error": "Erosión del canal o desbordamiento."},
                    "mecanica": {"uso": "Análisis de mecanismos planos (bielas, manivelas). Velocidad lineal de un punto.", "consecuencia_de_error": "Vibración excesiva o ruptura por fatiga."},
                    "mecatronica": {"uso": "Odometría: calcular la velocidad del robot basada en los encoders de las ruedas.", "consecuencia_de_error": "El robot pierde la noción de dónde está."},
                    "aeronautica": {"uso": "Vector de velocidad del viento vs Vector de rumbo (triángulo de velocidades en mapa 2D).", "consecuencia_de_error": "Navegación errónea, deriva no corregida."},
                    "electrica": {"uso": "Velocidad de fase de una onda en una guía de ondas rectangular.", "consecuencia_de_error": "Pérdida de señal o interferencia."}
                }
            },
            {
                "subtema_titulo": "3. Rapidez y Longitud de Arco",
                "definicion": "La 'rapidez' es la magnitud del vector velocidad: |v(t)| = √((x')² + (y')²). La 'longitud de arco' (distancia recorrida) es la integral de la rapidez en el tiempo: L = ∫ |v(t)| dt.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: r(t) = (3t, 4t) de t=0 a t=2. (Movimiento rectilíneo).\n1. v(t) = (3, 4).\n2. Rapidez |v| = √(3² + 4²) = 5.\n3. Longitud = ∫(de 0 a 2) 5 dt = 5(2) - 5(0) = 10.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si v(t) = (6, 8), ¿cuál es la rapidez constante? (Raíz de 6^2+8^2)",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "14", "100", "2"]
                    },
                    "similares": [
                        {"pregunta": "Si rapidez es 5 m/s, ¿cuánto recorre en 4s?", "respuesta_correcta": "20", "opciones": ["20", "25", "9", "1"]},
                        {"pregunta": "Calcula la rapidez si v = (1, 1).", "respuesta_correcta": "raiz(2)", "opciones": ["raiz(2)", "1", "2", "0.5"]},
                        {"pregunta": "La integral de la rapidez nos da la...", "respuesta_correcta": "distancia", "opciones": ["distancia", "aceleracion", "velocidad", "posicion"]},
                        {"pregunta": "Si v(t) = (t, 0), la rapidez es...", "respuesta_correcta": "t", "opciones": ["t", "0", "1", "t^2"]},
                        {"pregunta": "La longitud de un círculo de radio 1 (t=0 a 2pi) es...", "respuesta_correcta": "2pi", "opciones": ["2pi", "pi", "1", "4pi"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular la distancia total recorrida por un jugador para estadísticas o logros.", "consecuencia_de_error": "Datos de juego incorrectos."},
                    "quimica": {"uso": "Longitud del camino recorrido por una partícula en movimiento browniano 2D.", "consecuencia_de_error": "Errores en modelos de difusión."},
                    "civil": {"uso": "Longitud exacta de un cable o tubería curva en un plano.", "consecuencia_de_error": "Pedir menos material del necesario (cables cortos)."},
                    "mecanica": {"uso": "Longitud de una correa o cadena en un sistema de poleas.", "consecuencia_de_error": "La correa no encaja o queda floja."},
                    "mecatronica": {"uso": "Consumo de batería: depende de la distancia total recorrida por el robot.", "consecuencia_de_error": "El robot se queda sin batería antes de volver a la base."},
                    "aeronautica": {"uso": "Distancia de vuelo real considerando las curvas de la ruta.", "consecuencia_de_error": "Cálculo de combustible insuficiente."},
                    "electrica": {"uso": "Longitud de pista en un circuito impreso (PCB) para calcular resistencia y retardo.", "consecuencia_de_error": "Señales desincronizadas en alta frecuencia."}
                }
            },
            {
                "subtema_titulo": "4. Aceleración y Vectores T y N",
                "definicion": "La aceleración a(t) es la derivada de la velocidad. Se descompone en dos componentes: 'Tangencial' (cambia la rapidez, acelerar/frenar) y 'Normal' (cambia la dirección, girar). a = a_T * T + a_N * N.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Auto en curva circular constante.\nRapidez constante -> Aceleración Tangencial = 0.\nGiro constante -> Aceleración Normal existe (centrípeta), apunta al centro.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un auto va a rapidez constante en un círculo, ¿su aceleración tangencial es...? (Solo el número)",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "constante", "variable", "negativa"]
                    },
                    "similares": [
                        {"pregunta": "La aceleración normal siempre apunta hacia el... de la curva.", "respuesta_correcta": "centro", "opciones": ["centro", "fuera", "tangente", "atras"]},
                        {"pregunta": "Si a(t) = (0, -9.8) y v(t) = (10, 0), el objeto está... (cayendo/girando/ambos)", "respuesta_correcta": "ambos", "opciones": ["ambos", "cayendo", "girando", "quieto"]},
                        {"pregunta": "La aceleración es la derivada de la...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "posicion", "rapidez", "tiempo"]},
                        {"pregunta": "Si frenas en línea recta, tu aceleración normal es...", "respuesta_correcta": "0", "opciones": ["0", "negativa", "positiva", "infinita"]},
                        {"pregunta": "Vector unitario tangente apunta en dirección del...", "respuesta_correcta": "movimiento", "opciones": ["movimiento", "centro", "normal", "origen"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de derrapes en juegos de carreras. Si la fuerza Normal necesaria > fricción, el auto derrapa.", "consecuencia_de_error": "Física de conducción irreal."},
                    "quimica": {"uso": "Separación en centrífugas. La aceleración normal separa partículas por densidad.", "consecuencia_de_error": "Mezcla no separada correctamente."},
                    "civil": {"uso": "Diseño de curvas en carreteras/trenes. La fuerza normal (centrífuga) no debe volcar el vehículo.", "consecuencia_de_error": "Vehículos volcándose en curvas cerradas."},
                    "mecanica": {"uso": "Fuerzas en rodamientos. La aceleración normal crea cargas radiales en los ejes.", "consecuencia_de_error": "Rodamientos destruidos por carga excesiva."},
                    "mecatronica": {"uso": "Sensores inerciales (IMU) miden estas aceleraciones para saber la orientación.", "consecuencia_de_error": "El robot pierde el equilibrio y cae."},
                    "aeronautica": {"uso": "Fuerzas G en un viraje. Son puramente aceleración normal.", "consecuencia_de_error": "Piloto desmayado o alas rotas por exceso de Gs."},
                    "electrica": {"uso": "Fuerza sobre una carga en movimiento circular en un campo magnético.", "consecuencia_de_error": "Fallo en el confinamiento de plasma o haces de electrones."}
                }
            },
            {
                "subtema_titulo": "5. Campos Vectoriales 2D (Mapas de Flechas)",
                "definicion": "Un campo vectorial asigna un vector a cada punto del plano. F(x,y) = (P(x,y), Q(x,y)). Modela cosas como viento, corrientes de agua o fuerzas invisibles (gravedad, magnetismo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Campo de velocidades de un remolino: F(x,y) = (-y, x).\nEn (1,0), el vector es (0,1) -> Arriba.\nEn (0,1), el vector es (-1,0) -> Izquierda.\n¡Los vectores giran alrededor del origen!",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En el campo constante F(x,y) = (0, -9.8), ¿hacia dónde apuntan todas las flechas?",
                        "respuesta_correcta": "abajo",
                        "opciones": ["abajo", "arriba", "izquierda", "derecha"]
                    },
                    "similares": [
                        {"pregunta": "En F(x,y) = (x, y), los vectores apuntan...", "respuesta_correcta": "hacia afuera", "opciones": ["hacia afuera", "hacia el origen", "en circulo", "hacia arriba"]},
                        {"pregunta": "Un campo que representa la velocidad de un fluido se llama campo de...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "fuerza", "escalar", "presion"]},
                        {"pregunta": "Si F(x,y) = (1, 0), el flujo va a la...", "respuesta_correcta": "derecha", "opciones": ["derecha", "izquierda", "arriba", "abajo"]},
                        {"pregunta": "El campo gravitatorio apunta siempre hacia el centro de la masa.", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Un mapa de viento es un ejemplo de campo...", "respuesta_correcta": "vectorial", "opciones": ["vectorial", "escalar", "nulo", "constante"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de fluidos o viento en juegos. El campo vectorial 'empuja' a los jugadores.", "consecuencia_de_error": "El viento empuja en la dirección incorrecta."},
                    "quimica": {"uso": "Campos de gradiente de concentración (difusión). Las moléculas se mueven según el campo.", "consecuencia_de_error": "Predicción errónea del flujo de sustancias."},
                    "civil": {"uso": "Mapa de flujo de aguas subterráneas o viento alrededor de un edificio.", "consecuencia_de_error": "Cimentaciones inundadas o ventanas rotas por presión de viento."},
                    "mecanica": {"uso": "Campo de velocidades dentro de una tubería o alrededor de un perfil aerodinámico.", "consecuencia_de_error": "Turbulencia inesperada y pérdida de energía."},
                    "mecatronica": {"uso": "Campos de potencial artificial. El robot ve la meta como un 'atractor' y los obstáculos como 'repulsores' en un campo vectorial.", "consecuencia_de_error": "El robot choca con obstáculos."},
                    "aeronautica": {"uso": "Patrones de flujo de aire sobre el ala (laminar vs turbulento).", "consecuencia_de_error": "Diseño de ala ineficiente."},
                    "electrica": {"uso": "Campo Eléctrico (E) y Magnético (B). Son campos vectoriales fundamentales.", "consecuencia_de_error": "Mal diseño de motores, transformadores y antenas."}
                }
            },
            {
                "subtema_titulo": "6. Derivadas Parciales (Introducción 2D)",
                "definicion": "Si tenemos una función de altura z = f(x,y) sobre el plano. La derivada parcial ∂f/∂x es la pendiente si te mueves solo en X. ∂f/∂y es la pendiente si te mueves solo en Y. Es como medir la inclinación de una montaña de Este a Oeste vs Norte a Sur.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Terreno z = x² + y².\n1. Pendiente en X (∂z/∂x): 2x (tratamos y como constante).\n2. Pendiente en Y (∂z/∂y): 2y (tratamos x como constante).\nEn el punto (1,1), la pendiente en X es 2, en Y es 2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x,y) = 3x + 5y, ¿cuál es la derivada parcial ∂f/∂x? (La pendiente en x)",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "5", "3x", "0"]
                    },
                    "similares": [
                        {"pregunta": "Si f(x,y) = 3x + 5y, ¿cuál es ∂f/∂y?", "respuesta_correcta": "5", "opciones": ["5", "3", "5y", "0"]},
                        {"pregunta": "Si f(x,y) = x*y, calcula ∂f/∂x. (La y es constante)", "respuesta_correcta": "y", "opciones": ["y", "x", "1", "0"]},
                        {"pregunta": "Si z = 10 (plano), sus derivadas parciales son...", "respuesta_correcta": "0", "opciones": ["0", "1", "10", "infinito"]},
                        {"pregunta": "∂f/∂x mide el cambio en la dirección...", "respuesta_correcta": "horizontal", "opciones": ["horizontal", "vertical", "diagonal", "total"]},
                        {"pregunta": "Si f(x,y) = x² + y, calcula ∂f/∂y.", "respuesta_correcta": "1", "opciones": ["1", "0", "2x", "y"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Generación de terrenos. Calcular la pendiente para saber si el jugador puede caminar o se resbala.", "consecuencia_de_error": "Jugadores subiendo paredes verticales."},
                    "quimica": {"uso": "Tasas de reacción que dependen de dos concentraciones. ∂Velocidad/∂[A].", "consecuencia_de_error": "Control de reacción inestable."},
                    "civil": {"uso": "Pendiente del terreno en mapas topográficos para drenaje de agua.", "consecuencia_de_error": "Agua estancada o inundaciones."},
                    "mecanica": {"uso": "Esfuerzos en placas. Cómo cambia la tensión en dirección x vs y.", "consecuencia_de_error": "Fractura de material por tensión no detectada."},
                    "mecatronica": {"uso": "Detección de bordes en imágenes (cambio brusco de color = derivada alta).", "consecuencia_de_error": "El robot no ve el borde de la mesa y se cae."},
                    "aeronautica": {"uso": "Cambio de presión sobre el ala en dirección de la cuerda vs envergadura.", "consecuencia_de_error": "Pérdida de sustentación en las puntas del ala."},
                    "electrica": {"uso": "Gradiente de potencial eléctrico.", "consecuencia_de_error": "Ruptura dieléctrica (chispazo)."}
                }
            },
            {
                "subtema_titulo": "7. El Gradiente (Vector de Máxima Pendiente)",
                "definicion": "El vector Gradiente (∇f) combina las derivadas parciales: ∇f = (∂f/∂x, ∂f/∂y). Este vector apunta SIEMPRE hacia donde la función crece más rápido (cuesta arriba más empinada). Su magnitud es la pendiente máxima.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Colina z = 10 - x² - y².\n∇f = (-2x, -2y).\nEn el punto (1, 1), el gradiente es (-2, -2).\nSignifica que para subir más rápido, debes caminar hacia el origen (hacia el pico).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si f(x,y) = 2x + 4y, ¿cuál es el vector gradiente ∇f?",
                        "respuesta_correcta": "(2, 4)",
                        "opciones": ["(2, 4)", "(2x, 4y)", "(4, 2)", "6"]
                    },
                    "similares": [
                        {"pregunta": "El gradiente siempre es ... a las curvas de nivel.", "respuesta_correcta": "perpendicular", "opciones": ["perpendicular", "paralelo", "tangente", "secante"]},
                        {"pregunta": "Si estás en la cima de una montaña, el gradiente vale...", "respuesta_correcta": "0", "opciones": ["0", "infinito", "maximo", "1"]},
                        {"pregunta": "Si f(x,y) = x², el gradiente es (2x, ...)", "respuesta_correcta": "0", "opciones": ["0", "1", "2y", "y"]},
                        {"pregunta": "El gradiente apunta en dirección de máximo...", "respuesta_correcta": "ascenso", "opciones": ["ascenso", "descenso", "constante", "giro"]},
                        {"pregunta": "Si ∇f = (3, 4), la pendiente máxima es... (magnitud)", "respuesta_correcta": "5", "opciones": ["5", "7", "12", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Algoritmo 'Gradient Descent' en IA. Se calcula el gradiente del 'error' para saber cómo ajustar los pesos y reducir el error.", "consecuencia_de_error": "La IA no aprende nada."},
                    "quimica": {"uso": "Difusión. Las partículas se mueven en la dirección opuesta al gradiente de concentración (de más a menos).", "consecuencia_de_error": "Error en modelos de difusión y mezcla."},
                    "civil": {"uso": "Flujo de agua subterránea. El agua fluye en la dirección opuesta al gradiente de presión.", "consecuencia_de_error": "Contaminación de acuíferos no prevista."},
                    "mecanica": {"uso": "Transferencia de calor. El calor fluye en dirección opuesta al gradiente de temperatura.", "consecuencia_de_error": "Sobrecalentamiento de componentes."},
                    "mecatronica": {"uso": "Navegación por potencial. El robot sigue el gradiente negativo para llegar a la meta (mínimo potencial).", "consecuencia_de_error": "El robot se queda atorado en un mínimo local."},
                    "aeronautica": {"uso": "Optimización de formas aerodinámicas usando métodos de gradiente.", "consecuencia_de_error": "Diseños subóptimos con mayor consumo de combustible."},
                    "electrica": {"uso": "Campo Eléctrico E = -∇V (El campo es el negativo del gradiente de voltaje).", "consecuencia_de_error": "Cálculo de fuerzas eléctricas incorrecto."}
                }
            },
            {
                "subtema_titulo": "8. Divergencia en 2D (Fuentes y Sumideros)",
                "definicion": "Operación sobre un campo vectorial. Mide si el campo 'nace' (fuente) o 'muere' (sumidero) en un punto. Div F = ∂P/∂x + ∂Q/∂y. Si es positiva, el fluido se expande. Si es negativa, se comprime.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Campo F = (x, y) (Explosión radial).\n∂x/∂x = 1. ∂y/∂y = 1.\nDiv F = 1 + 1 = 2. (Positivo: es una fuente, todo sale).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la divergencia de F = (2x, 3y). (2+3)",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "6xy", "(2, 3)", "0"]
                    },
                    "similares": [
                        {"pregunta": "Divergencia de F = (y, -x) (Rotación pura). (0+0)", "respuesta_correcta": "0", "opciones": ["0", "1", "-1", "2y"]},
                        {"pregunta": "Si la divergencia es positiva, el punto es una...", "respuesta_correcta": "fuente", "opciones": ["fuente", "sumidero", "vortice", "nada"]},
                        {"pregunta": "Si la divergencia es negativa, el punto es un...", "respuesta_correcta": "sumidero", "opciones": ["sumidero", "fuente", "vortice", "nada"]},
                        {"pregunta": "Un fluido incompresible (como agua) tiene divergencia igual a...", "respuesta_correcta": "0", "opciones": ["0", "1", "infinita", "constante"]},
                        {"pregunta": "Divergencia de F = (5, 5) (Campo constante).", "respuesta_correcta": "0", "opciones": ["0", "10", "5", "25"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de fluidos (juegos o cine). Se fuerza div=0 para que el agua no desaparezca ni se cree sola.", "consecuencia_de_error": "El agua pierde volumen y desaparece visualmente."},
                    "quimica": {"uso": "Balance de masa en reactores. Divergencia mide la acumulación neta de material.", "consecuencia_de_error": "Violación de la ley de conservación de la masa."},
                    "civil": {"uso": "Flujo de tráfico o agua. Detectar dónde se acumulan los coches (congestión) o el agua.", "consecuencia_de_error": "Diseño de carreteras con embotellamientos crónicos."},
                    "mecanica": {"uso": "Flujo de aire en motores. Detectar zonas de compresión y expansión.", "consecuencia_de_error": "Pérdida de eficiencia en compresores."},
                    "mecatronica": {"uso": "Sensores de flujo óptico.", "consecuencia_de_error": "Medición de movimiento incorrecta."},
                    "aeronautica": {"uso": "Flujo compresible a alta velocidad. La divergencia no es cero (el aire se comprime).", "consecuencia_de_error": "Ondas de choque mal calculadas."},
                    "electrica": {"uso": "Ley de Gauss: La divergencia del campo eléctrico es proporcional a la carga. Div E = ρ/ε.", "consecuencia_de_error": "No poder relacionar la carga eléctrica con el campo que genera."}
                }
            },
            {
                "subtema_titulo": "9. Rotacional en 2D (Vorticidad)",
                "definicion": "Mide la tendencia de un campo a 'girar' alrededor de un punto. En 2D es un escalar: Rot F = ∂Q/∂x - ∂P/∂y. Si no es cero, un objeto pequeño puesto ahí giraría.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: F = (-y, x) (Remolino).\nP=-y, Q=x.\n∂Q/∂x = 1. ∂P/∂y = -1.\nRot = 1 - (-1) = 2. (Hay rotación fuerte).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el rotacional 2D de F = (y, 0). (0 - 1)",
                        "respuesta_correcta": "-1",
                        "opciones": ["-1", "1", "0", "y"]
                    },
                    "similares": [
                        {"pregunta": "Rotacional de F = (x, y) (Explosión radial). (0 - 0)", "respuesta_correcta": "0", "opciones": ["0", "1", "2", "-1"]},
                        {"pregunta": "Si el rotacional es 0, el campo es...", "respuesta_correcta": "irrotacional", "opciones": ["irrotacional", "rotacional", "divergente", "solenoidal"]},
                        {"pregunta": "El rotacional mide el...", "respuesta_correcta": "giro", "opciones": ["giro", "flujo", "volumen", "area"]},
                        {"pregunta": "Rotacional de un campo constante F=(1, 2).", "respuesta_correcta": "0", "opciones": ["0", "1", "3", "2"]},
                        {"pregunta": "En un remolino, el rotacional es... (cero/diferente de cero)", "respuesta_correcta": "diferente de cero", "opciones": ["diferente de cero", "cero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de tornados, humo y turbulencia en videojuegos.", "consecuencia_de_error": "Efectos visuales planos y poco realistas."},
                    "quimica": {"uso": "Mezclado en reactores. Se necesita alta vorticidad (rotacional) para mezclar bien.", "consecuencia_de_error": "Mezcla pobre, reacción incompleta."},
                    "civil": {"uso": "Vorticidad en pilares de puentes en ríos. Los vórtices pueden socavar los cimientos.", "consecuencia_de_error": "Colapso del puente por erosión."},
                    "mecanica": {"uso": "Diseño de turbinas y bombas. El rotacional impulsa el fluido.", "consecuencia_de_error": "Bomba que no mueve el agua."},
                    "mecatronica": {"uso": "Control de drones cuadricópteros (basado en vórtices de aire).", "consecuencia_de_error": "Inestabilidad en vuelo."},
                    "aeronautica": {"uso": "Vórtices de punta de ala. Generan resistencia y peligro para otros aviones.", "consecuencia_de_error": "Accidentes por estela turbulenta."},
                    "electrica": {"uso": "Campos magnéticos. Rot B = corriente. Un campo magnético 'rota' alrededor del cable.", "consecuencia_de_error": "No entender la inducción ni los transformadores."}
                }
            },
            {
                "subtema_titulo": "10. Integrales de Línea (Trabajo en 2D)",
                "definicion": "Suma el efecto de un campo vectorial a lo largo de una trayectoria curva. Trabajo W = ∫ F · dr. Es la suma de los productos punto en cada paso del camino.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Moverse del (0,0) al (1,0) con Fuerza F=(x, 0).\nTrayectoria y=0, dy=0. dr=(dx, 0).\nF·dr = x dx.\nIntegral ∫ x dx de 0 a 1 = 1/2.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si F=(1, 2) es constante y te mueves del (0,0) al (2,0), el trabajo es... (F·d = 1*2 + 2*0)",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "0", "3", "6"]
                    },
                    "similares": [
                        {"pregunta": "Si te mueves perpendicular a la fuerza, el trabajo es...", "respuesta_correcta": "0", "opciones": ["0", "maximo", "negativo", "infinito"]},
                        {"pregunta": "Si la trayectoria es cerrada y el campo conservativo, el trabajo es...", "respuesta_correcta": "0", "opciones": ["0", "doble", "pi", "area"]},
                        {"pregunta": "La integral de línea calcula el...", "respuesta_correcta": "trabajo", "opciones": ["trabajo", "flujo", "area", "volumen"]},
                        {"pregunta": "Si F=(0, 5) y te mueves en horizontal (eje X), el trabajo es...", "respuesta_correcta": "0", "opciones": ["0", "5", "10", "undefined"]},
                        {"pregunta": "Trabajo de moverte 1m en contra de una fuerza de 10N.", "respuesta_correcta": "-10", "opciones": ["-10", "10", "0", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular energía gastada por un personaje al recorrer un camino complejo.", "consecuencia_de_error": "Barra de energía del juego inconsistente."},
                    "quimica": {"uso": "Trabajo termodinámico en un ciclo PV.", "consecuencia_de_error": "Cálculo de eficiencia de motor erróneo."},
                    "civil": {"uso": "Trabajo realizado al mover tierra en una ruta curva de construcción.", "consecuencia_de_error": "Costos de maquinaria mal calculados."},
                    "mecanica": {"uso": "Cálculo exacto de trabajo en mecanismos de trayectoria curva.", "consecuencia_de_error": "Diseño de motores con potencia insuficiente."},
                    "mecatronica": {"uso": "Energía consumida por un brazo robótico en una trayectoria.", "consecuencia_de_error": "Batería del robot dura menos de lo planeado."},
                    "aeronautica": {"uso": "Trabajo contra el arrastre en una ruta de vuelo real.", "consecuencia_de_error": "Falta de combustible."},
                    "electrica": {"uso": "Voltaje (Diferencia de potencial). Es la integral de línea del campo eléctrico.", "consecuencia_de_error": "Concepto erróneo de voltaje."}
                }
            }
        ]
    },


    "ECUACIONES DIFERENCIALES": {
        "nombre_completo": "Ecuaciones Diferenciales: El Lenguaje del Cambio",
        "prerequisitos": ["CALCULO VECTORIAL", "ALGEBRA LINEAL"],
        "quiz": [
            {
                "pregunta": "¿Cuál es el orden de la ecuación y'' + 2y' = 0? (Solo el número)",
                "respuesta": "2",
                "opciones": ["2", "1", "3", "0"]
            },
            {
                "pregunta": "La Transformada de Laplace convierte una EDO en una ecuación...",
                "respuesta": "algebraica",
                "opciones": ["algebraica", "diferencial", "integral", "compleja"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Definición y Clasificación (Orden y Linealidad)",
                "definicion": "Una Ecuación Diferencial Ordinaria (EDO) relaciona una función desconocida y(t) con sus derivadas y', y'', etc. El 'Orden' es la derivada más alta (ej. y'' es orden 2). La 'Linealidad' significa que 'y' y sus derivadas no están elevadas a potencias ni dentro de funciones (como sen(y)).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y'' + 3y' + 2y = cos(x)\n1. Derivada más alta: y''. Orden = 2.\n2. Términos de y: Todos tienen potencia 1 (y, y', y'').\n3. Conclusión: EDO de Segundo Orden, Lineal.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el orden de la ecuación y''' - 5y = 0? (Solo el número)",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "1", "5", "0"]
                    },
                    "similares": [
                        {"pregunta": "La ecuación y' = y² es... (lineal/no lineal)", "respuesta_correcta": "no lineal", "opciones": ["no lineal", "lineal"]},
                        {"pregunta": "¿Cuál es el orden de d²y/dx² + y = 0?", "respuesta_correcta": "2", "opciones": ["2", "1", "0", "4"]},
                        {"pregunta": "En la ecuación F = m*a (donde a = x''), ¿el orden es?", "respuesta_correcta": "2", "opciones": ["2", "1", "3", "0"]},
                        {"pregunta": "Si la ecuación tiene y*y', ¿es lineal? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "La ecuación y' + x²y = 0 es... (lineal/no lineal)", "respuesta_correcta": "lineal", "opciones": ["lineal", "no lineal"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Clasificar la complejidad de un modelo de simulación. Las EDOs lineales se resuelven rápido; las no lineales requieren métodos numéricos costosos.", "consecuencia_de_error": "Intentar resolver una ecuación no lineal con métodos lineales dará resultados totalmente falsos."},
                    "quimica": {"uso": "Las leyes de velocidad (cinética) son EDOs. Orden 1: A -> B. Orden 2: 2A -> B.", "consecuencia_de_error": "Clasificar mal el orden de reacción lleva a errores graves en el diseño del tamaño del reactor."},
                    "civil": {"uso": "La ecuación de la viga es de 4to orden (Lineal).", "consecuencia_de_error": "Usar una ecuación de orden menor impediría calcular la deflexión correcta."},
                    "mecanica": {"uso": "Las ecuaciones de movimiento (Newton) son de 2do orden. Si hay fricción del aire (v²), se vuelven no lineales.", "consecuencia_de_error": "Ignorar la no linealidad a altas velocidades predice trayectorias imposibles."},
                    "mecatronica": {"uso": "La mayoría de la teoría de control moderna se basa en sistemas Lineales (LTI).", "consecuencia_de_error": "Aplicar control lineal a un robot muy no lineal lo hará inestable."},
                    "aeronautica": {"uso": "Las ecuaciones de Navier-Stokes (flujo de aire) son EDOs/EDPs no lineales de 2do orden.", "consecuencia_de_error": "La no linealidad es lo que crea turbulencia. Ignorarla es fatal."},
                    "electrica": {"uso": "Circuitos RLC son lineales de 2do orden. Diodos y transistores introducen no linealidad.", "consecuencia_de_error": "Un análisis lineal en un circuito con transistores no predecirá la distorsión de la señal."}
                }
            },
            {
                "subtema_titulo": "2. EDOs de Primer Orden: Variables Separables",
                "definicion": "El método más simple. Si puedes escribir la ecuación como g(y)dy = f(x)dx, entonces integras ambos lados por separado para encontrar la solución.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: dy/dx = x/y\n1. Separar: y dy = x dx\n2. Integrar: ∫ y dy = ∫ x dx\n3. y²/2 = x²/2 + C\n4. Solución: y² - x² = C (Hipérbolas).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve la EDO dy/dx = y. (Separa dy/y = dx e integra). Solución: y = ... (Usa C como constante)",
                        "respuesta_correcta": "Ce^x",
                        "opciones": ["Ce^x", "x^2/2", "e^y", "Cx"]
                    },
                    "similares": [
                        {"pregunta": "Resuelve dy/dx = x. (y = ...)", "respuesta_correcta": "x^2/2+C", "opciones": ["x^2/2+C", "x+C", "x^2", "1"]},
                        {"pregunta": "Resuelve dy/dx = 1/y. (y dy = dx)", "respuesta_correcta": "y^2/2=x+C", "opciones": ["y^2/2=x+C", "y=x+C", "y=ln(x)", "y^2=x"]},
                        {"pregunta": "Si dy/dt = k*y (crecimiento exponencial), la solución es y = A*e^(...)", "respuesta_correcta": "kt", "opciones": ["kt", "k", "t", "-kt"]},
                        {"pregunta": "¿La ecuación y' = x + y es separable? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Resuelve dy/dx = 0. (y = ...)", "respuesta_correcta": "C", "opciones": ["C", "0", "x", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Modelado de crecimiento de usuarios o propagación de virus en redes (Modelo SIR simplificado).", "consecuencia_de_error": "Subestimar la carga del servidor durante un crecimiento viral."},
                    "quimica": {"uso": "Cinética de primer orden (decaimiento radiactivo o descomposición). d[A]/dt = -k[A].", "consecuencia_de_error": "Error en la datación por radiocarbono o en la fecha de caducidad de un fármaco."},
                    "civil": {"uso": "Consolidación de suelos (drenaje de agua) en el tiempo.", "consecuencia_de_error": "El edificio se hunde más de lo previsto con los años."},
                    "mecanica": {"uso": "Velocidad de un objeto con resistencia del aire lineal (v' = -kv).", "consecuencia_de_error": "Cálculo incorrecto de la velocidad terminal de un paracaidista."},
                    "mecatronica": {"uso": "Descarga de una batería. El voltaje cae proporcionalmente a la carga restante.", "consecuencia_de_error": "El indicador de batería muestra 50% cuando está a punto de morir."},
                    "aeronautica": {"uso": "Vaciado de tanques de combustible por gravedad (Ley de Torricelli).", "consecuencia_de_error": "El motor se apaga por falta de flujo de combustible."},
                    "electrica": {"uso": "Carga de un capacitor (Circuito RC). I = dq/dt.", "consecuencia_de_error": "El temporizador del circuito no funciona al tiempo correcto."}
                }
            },
            {
                "subtema_titulo": "3. EDOs de Primer Orden: Lineales (Factor Integrante)",
                "definicion": "Para ecuaciones de la forma y' + P(x)y = Q(x). Se usa un 'Factor Integrante' I(x) = e^(∫ P(x) dx). Al multiplicar toda la ecuación por I(x), el lado izquierdo se convierte en la derivada de un producto.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y' + y = e^x.\n1. P(x)=1. Factor I(x) = e^(∫ 1 dx) = e^x.\n2. Multiplicar: e^x*y' + e^x*y = e^x*e^x = e^(2x).\n3. Lado izq es (y*e^x)'. Integrar: y*e^x = ∫ e^(2x) dx = 0.5*e^(2x) + C.\n4. Despejar y: y = 0.5*e^x + C*e^(-x).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para y' + 2y = x, ¿cuál es el factor integrante I(x)? (e elevado a la integral de 2)",
                        "respuesta_correcta": "e^(2x)",
                        "opciones": ["e^(2x)", "e^x", "2x", "x^2"]
                    },
                    "similares": [
                        {"pregunta": "Para y' + 5y = 0, ¿cuál es el factor integrante?", "respuesta_correcta": "e^(5x)", "opciones": ["e^(5x)", "5x", "e^5", "5"]},
                        {"pregunta": "Para y' + (1/x)y = 3, ¿cuál es el factor integrante? (e^ln(x) = x)", "respuesta_correcta": "x", "opciones": ["x", "ln(x)", "1/x", "e^x"]},
                        {"pregunta": "Este método sirve para ecuaciones de la forma y' + Py = ...", "respuesta_correcta": "Q", "opciones": ["Q", "y", "0", "x"]},
                        {"pregunta": "Si P(x) = -2, el factor es e^(-2x).", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "El objetivo es convertir el lado izquierdo en la derivada de un...", "respuesta_correcta": "producto", "opciones": ["producto", "cociente", "suma", "exponente"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Modelar la temperatura de un CPU (calentamiento constante Q, enfriamiento proporcional P).", "consecuencia_de_error": "El ventilador no se enciende a tiempo y el procesador se quema."},
                    "quimica": {"uso": "Reactores de mezcla completa con entrada y salida de fluido (dilución continua).", "consecuencia_de_error": "La concentración del producto químico fluctúa peligrosamente."},
                    "civil": {"uso": "Acumulación de contaminantes en un lago con un río que entra y otro que sale.", "consecuencia_de_error": "Predicción ecológica fallida."},
                    "mecanica": {"uso": "Frenado de un vehículo con frenos y resistencia del aire.", "consecuencia_de_error": "Distancia de frenado mal calculada."},
                    "mecatronica": {"uso": "Respuesta de un motor a un cambio de voltaje (escalón).", "consecuencia_de_error": "El robot reacciona lento o con 'lag'."},
                    "aeronautica": {"uso": "Dinámica de la velocidad de un avión al cambiar la potencia del motor.", "consecuencia_de_error": "El piloto automático no logra mantener la velocidad constante."},
                    "electrica": {"uso": "Circuitos RL (Resistor-Inductor) conectados a una fuente de voltaje variable.", "consecuencia_de_error": "Picos de corriente que destruyen el circuito al encenderlo."}
                }
            },
            {
                "subtema_titulo": "4. Aplicaciones 1er Orden: Ley de Enfriamiento y Crecimiento",
                "definicion": "Modelos reales. Crecimiento Poblacional: P' = kP (exponencial). Ley de Enfriamiento de Newton: T' = -k(T - T_ambiente) (la velocidad de enfriamiento depende de la diferencia de temperatura).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un café a 90°C en un cuarto a 20°C.\nEDO: T' = -k(T - 20).\nSolución: T(t) = 20 + (90-20)e^(-kt) = 20 + 70e^(-kt).\nLa temperatura decae exponencialmente hacia 20°C.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si una población crece al 5% anual, la EDO es P' = 0.05P. La solución es P(t) = P_inicial * e^(...)",
                        "respuesta_correcta": "0.05t",
                        "opciones": ["0.05t", "0.5t", "5t", "0.005t"]
                    },
                    "similares": [
                        {"pregunta": "En el enfriamiento, si T_ambiente = 25, la temperatura final (t->infinito) será...", "respuesta_correcta": "25", "opciones": ["25", "0", "100", "infinita"]},
                        {"pregunta": "Si k es negativo en P' = kP, la población...", "respuesta_correcta": "decrece", "opciones": ["decrece", "crece", "se mantiene", "oscila"]},
                        {"pregunta": "La vida media radiactiva se modela con una EDO de... orden.", "respuesta_correcta": "1er", "opciones": ["1er", "2do", "3er", "0"]},
                        {"pregunta": "Si T' = -k(T - 30), ¿cuál es la temperatura ambiente?", "respuesta_correcta": "30", "opciones": ["30", "0", "k", "T"]},
                        {"pregunta": "El modelo de interés compuesto continuo usa la función...", "respuesta_correcta": "exponencial", "opciones": ["exponencial", "lineal", "senoidal", "logaritmica"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Predicción de tráfico en servidores (crecimiento viral).", "consecuencia_de_error": "Servidores caídos por no escalar a tiempo."},
                    "quimica": {"uso": "Cinética química básica.", "consecuencia_de_error": "Tiempos de proceso industrial incorrectos."},
                    "civil": {"uso": "Curado del concreto (el calor se disipa según la ley de enfriamiento).", "consecuencia_de_error": "Concreto agrietado por estrés térmico."},
                    "mecanica": {"uso": "Tratamiento térmico de metales (templado). El perfil de enfriamiento define la dureza.", "consecuencia_de_error": "Piezas de metal demasiado blandas o quebradizas."},
                    "mecatronica": {"uso": "Calentamiento de motores eléctricos bajo carga.", "consecuencia_de_error": "Motores quemados por no predecir la temperatura final."},
                    "aeronautica": {"uso": "Enfriamiento de la turbina después del apagado.", "consecuencia_de_error": "Daño al motor por 'choque térmico' si se apaga mal."},
                    "electrica": {"uso": "Descarga de un capacitor (flash de cámara, desfibrilador).", "consecuencia_de_error": "El desfibrilador no entrega la descarga a tiempo."}
                }
            },
            {
                "subtema_titulo": "5. EDOs de 2do Orden Homogéneas (Masa-Resorte)",
                "definicion": "Ecuaciones tipo ay'' + by' + cy = 0. Modelan oscilaciones libres. Se usa la 'Ecuación Característica': ar² + br + c = 0. Las raíces 'r' determinan si el sistema oscila (raíces complejas) o no (reales).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y'' + 4y = 0. (Oscilador armónico).\nEcuación: r² + 4 = 0 -> r² = -4 -> r = ±2i.\nSolución: y(t) = C1 cos(2t) + C2 sen(2t). (Oscila indefinidamente).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para y'' - 9y = 0, la ecuación característica es r² - 9 = 0. Las raíces son 3 y ...",
                        "respuesta_correcta": "-3",
                        "opciones": ["-3", "9", "0", "1"]
                    },
                    "similares": [
                        {"pregunta": "Si las raíces son reales y negativas, el sistema... (oscila/decae)", "respuesta_correcta": "decae", "opciones": ["decae", "oscila", "crece", "explota"]},
                        {"pregunta": "Si las raíces son imaginarias puras (±ki), el sistema... (oscila/explota)", "respuesta_correcta": "oscila", "opciones": ["oscila", "decae", "se detiene", "rompe"]},
                        {"pregunta": "Para un sistema masa-resorte m*a + k*x = 0, la ecuación es mx'' + kx = ...", "respuesta_correcta": "0", "opciones": ["0", "1", "F", "mg"]},
                        {"pregunta": "En y'' + 2y' + y = 0, la raíz es -1 (doble). La solución tiene la forma C1*e^-t + C2*t*...", "respuesta_correcta": "e^-t", "opciones": ["e^-t", "t", "1", "e^t"]},
                        {"pregunta": "Este tipo de EDO modela sistemas con... derivadas.", "respuesta_correcta": "dos", "opciones": ["dos", "una", "tres", "cero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Animaciones de 'rebote' (spring physics) en interfaces de usuario (iOS/Android).", "consecuencia_de_error": "Animaciones rígidas o que nunca se detienen."},
                    "quimica": {"uso": "Vibración de enlaces moleculares (modelo oscilador armónico).", "consecuencia_de_error": "Espectros IR mal interpretados."},
                    "civil": {"uso": "Frecuencia natural de un edificio. Si el sismo iguala esta frecuencia, el edificio colapsa.", "consecuencia_de_error": "Resonancia destructiva (ej. Puente Tacoma Narrows)."},
                    "mecanica": {"uso": "Sistemas de suspensión de autos (masa-resorte-amortiguador).", "consecuencia_de_error": "Auto inestable o muy incómodo (bota demasiado)."},
                    "mecatronica": {"uso": "Control PD (Proporcional-Derivativo) de posición. Se modela como un resorte virtual.", "consecuencia_de_error": "El brazo del robot vibra al intentar detenerse."},
                    "aeronautica": {"uso": "Estabilidad estática longitudinal. El avión debe regresar a nivelarse como un resorte.", "consecuencia_de_error": "Avión inestable que requiere corrección constante del piloto."},
                    "electrica": {"uso": "Circuitos RLC sin fuente. La energía oscila entre el campo eléctrico (C) y magnético (L).", "consecuencia_de_error": "Oscilaciones parásitas que generan ruido en la señal."}
                }
            },
            {
                "subtema_titulo": "6. EDOs de 2do Orden No Homogéneas (Fuerzas Externas)",
                "definicion": "Ecuaciones tipo ay'' + by' + cy = g(t), donde g(t) es una fuerza externa. La solución es la suma de la 'Homogénea' (transitoria) + la 'Particular' (estado estable, forzado). Método de Coeficientes Indeterminados: adivinar la forma de Yp basada en g(t).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: y'' - y = e^x.\n1. Homogénea: y_h = C1e^x + C2e^-x.\n2. Particular (g=e^x): Como e^x ya está en la homogénea, probamos Yp = Axe^x.\n3. Derivar, sustituir y hallar A.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si la fuerza externa es g(t) = 5 (constante), propones una solución particular Yp = A (constante).",
                        "respuesta_correcta": "verdadero",
                        "opciones": ["verdadero", "falso"]
                    },
                    "similares": [
                        {"pregunta": "Si g(t) = cos(t), propones Yp = A cos(t) + B ...", "respuesta_correcta": "sen(t)", "opciones": ["sen(t)", "cos(t)", "tan(t)", "t"]},
                        {"pregunta": "Si g(t) = t² (polinomio grado 2), propones Yp = At² + Bt + ...", "respuesta_correcta": "C", "opciones": ["C", "0", "1", "D"]},
                        {"pregunta": "La solución total es y = y_homogenea + ...", "respuesta_correcta": "y_particular", "opciones": ["y_particular", "y_general", "y_final", "0"]},
                        {"pregunta": "Este tipo de ecuación modela vibraciones...", "respuesta_correcta": "forzadas", "opciones": ["forzadas", "libres", "amortiguadas", "caoticas"]},
                        {"pregunta": "Si la frecuencia de g(t) iguala la natural, ocurre...", "respuesta_correcta": "resonancia", "opciones": ["resonancia", "estabilidad", "silencio", "friccion"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Respuesta de un servidor a una carga de usuarios variable g(t).", "consecuencia_de_error": "Servidor lento o caído bajo carga específica."},
                    "quimica": {"uso": "Reactor con alimentación variable de reactivos.", "consecuencia_de_error": "Calidad del producto inconsistente."},
                    "civil": {"uso": "Edificio sometido a la fuerza de un terremoto g(t) o viento racheado.", "consecuencia_de_error": "Falla estructural si la fuerza externa causa resonancia."},
                    "mecanica": {"uso": "Motor desbalanceado que genera una fuerza vibratoria senoidal g(t) sobre la base.", "consecuencia_de_error": "Fatiga de los soportes y ruido excesivo."},
                    "mecatronica": {"uso": "Respuesta de un servo a un comando de posición cambiante.", "consecuencia_de_error": "Error de seguimiento (el robot no sigue la ruta exacta)."},
                    "aeronautica": {"uso": "Respuesta del ala a una ráfaga de viento (turbulencia).", "consecuencia_de_error": "Cargas estructurales imprevistas en el ala."},
                    "electrica": {"uso": "Circuito RLC conectado a la red eléctrica (AC). g(t) es el voltaje senoidal.", "consecuencia_de_error": "Imposible diseñar cualquier aparato que se conecte a un enchufe."}
                }
            },
            {
                "subtema_titulo": "7. Transformada de Laplace (Del Tiempo a la Frecuencia)",
                "definicion": "Una herramienta poderosa que convierte EDOs (difíciles, dominio 't') en Ecuaciones Algebraicas (fáciles, dominio 's'). L{f(t)} = F(s). La derivada se convierte en multiplicación: L{y'} = sY(s) - y(0).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Transformar y' + y = 0.\n1. L{y'} = sY - y(0).\n2. L{y} = Y.\n3. Ecuación algebraica: sY - y(0) + Y = 0 -> Y(s+1) = y(0).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La Transformada de Laplace de la derivada y'' se convierte en s multiplicado por s, o sea...",
                        "respuesta_correcta": "s^2",
                        "opciones": ["s^2", "s", "1/s", "s^3"]
                    },
                    "similares": [
                        {"pregunta": "La transformada convierte el dominio del tiempo (t) al dominio de...", "respuesta_correcta": "s", "opciones": ["s", "f", "x", "w"]},
                        {"pregunta": "L{1} (una constante) es...", "respuesta_correcta": "1/s", "opciones": ["1/s", "s", "1", "0"]},
                        {"pregunta": "L{e^at} es 1 / (s - ...)", "respuesta_correcta": "a", "opciones": ["a", "1", "s", "0"]},
                        {"pregunta": "Laplace convierte ecuaciones diferenciales en ecuaciones...", "respuesta_correcta": "algebraicas", "opciones": ["algebraicas", "integrales", "complejas", "nulas"]},
                        {"pregunta": "Es la herramienta principal para la teoría de...", "respuesta_correcta": "control", "opciones": ["control", "juegos", "probabilidad", "numeros"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de desempeño de sistemas en el dominio de la frecuencia.", "consecuencia_de_error": "Diseño de sistemas inestables."},
                    "quimica": {"uso": "Control de procesos químicos (temperatura, flujo) usando controladores PID.", "consecuencia_de_error": "Proceso inestable que oscila."},
                    "civil": {"uso": "Análisis dinámico de estructuras bajo cargas sísmicas (espectro de respuesta).", "consecuencia_de_error": "Diseño sísmico inadecuado."},
                    "mecanica": {"uso": "Análisis de vibraciones y diseño de amortiguadores.", "consecuencia_de_error": "Máquinas ruidosas o que se rompen."},
                    "mecatronica": {"uso": "Diseño de Controladores (PID). Se diseñan en el dominio 's' (Lugar de las Raíces).", "consecuencia_de_error": "El robot es inestable o lento."},
                    "aeronautica": {"uso": "Diseño de pilotos automáticos y sistemas de estabilidad (Fly-by-wire).", "consecuencia_de_error": "Avión inestable por software."},
                    "electrica": {"uso": "Análisis de circuitos en el dominio de la frecuencia (Impedancia sL, 1/sC).", "consecuencia_de_error": "Diseño de filtros y telecomunicaciones imposible."}
                }
            },
            {
                "subtema_titulo": "8. Transformada Inversa y Solución",
                "definicion": "Una vez resuelta la ecuación algebraica Y(s), usamos la Transformada Inversa L⁻¹ para volver al dominio del tiempo y(t). Se usan 'Fracciones Parciales' para simplificar Y(s) a formas conocidas.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Y(s) = 1 / (s - 3).\nSabemos que L{e^at} = 1/(s-a).\nAquí a=3.\nEntonces la inversa es y(t) = e^(3t).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La inversa de 1/s es la función constante...",
                        "respuesta_correcta": "1",
                        "opciones": ["1", "t", "e^t", "0"]
                    },
                    "similares": [
                        {"pregunta": "La inversa de 1/(s-2) es e elevado a la...", "respuesta_correcta": "2t", "opciones": ["2t", "-2t", "t", "s"]},
                        {"pregunta": "La inversa de 1/s² es...", "respuesta_correcta": "t", "opciones": ["t", "1", "t^2", "s"]},
                        {"pregunta": "Para invertir fracciones complejas, usamos fracciones...", "respuesta_correcta": "parciales", "opciones": ["parciales", "totales", "mixtas", "impropias"]},
                        {"pregunta": "La solución final debe estar en función de...", "respuesta_correcta": "t", "opciones": ["t", "s", "x", "y"]},
                        {"pregunta": "Si Y(s) = 1/(s+5), el exponente es...", "respuesta_correcta": "-5t", "opciones": ["-5t", "5t", "t", "5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de señales: pasar del espectro de frecuencia al audio real.", "consecuencia_de_error": "Audio corrupto."},
                    "quimica": {"uso": "Predecir la concentración en el tiempo de un sistema controlado.", "consecuencia_de_error": "No saber cuándo detener la reacción."},
                    "civil": {"uso": "Obtener la gráfica de desplazamiento vs tiempo de un edificio en un sismo.", "consecuencia_de_error": "Desconocer el desplazamiento máximo."},
                    "mecanica": {"uso": "Obtener la posición de un mecanismo en el tiempo.", "consecuencia_de_error": "Interferencia entre piezas móviles."},
                    "mecatronica": {"uso": "Simular la respuesta temporal de un robot a un comando.", "consecuencia_de_error": "No cumplir con los tiempos de ciclo requeridos."},
                    "aeronautica": {"uso": "Simular la respuesta del avión a una turbulencia.", "consecuencia_de_error": "Evaluación incorrecta del confort y seguridad."},
                    "electrica": {"uso": "Obtener la señal de voltaje real de salida de un filtro.", "consecuencia_de_error": "Señal distorsionada."}
                }
            },
            {
                "subtema_titulo": "9. Sistemas de Ecuaciones Diferenciales",
                "definicion": "Cuando tienes múltiples variables que dependen unas de otras (ej. depredador-presa, o circuitos acoplados). Se escriben como vectores: X' = AX. Se resuelven usando Eigenvalores y Eigenvectores de la matriz A.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: x' = y, y' = x. Matriz A=[[0,1],[1,0]].\nEigenvalores: λ=1, λ=-1.\nSolución general: Combinación de e^t y e^-t.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un sistema de 2 ecuaciones diferenciales de primer orden equivale a una ecuación de ... orden.",
                        "respuesta_correcta": "segundo",
                        "opciones": ["segundo", "primero", "tercero", "cero"]
                    },
                    "similares": [
                        {"pregunta": "En X' = AX, ¿qué es A?", "respuesta_correcta": "una matriz", "opciones": ["una matriz", "un vector", "un numero", "una funcion"]},
                        {"pregunta": "Si los eigenvalores son negativos, el sistema es...", "respuesta_correcta": "estable", "opciones": ["estable", "inestable", "caotico", "nulo"]},
                        {"pregunta": "Este método se usa para sistemas...", "respuesta_correcta": "acoplados", "opciones": ["acoplados", "independientes", "simples", "lineales"]},
                        {"pregunta": "En el modelo depredador-presa, si aumentan los lobos, los conejos...", "respuesta_correcta": "disminuyen", "opciones": ["disminuyen", "aumentan", "igual", "nada"]},
                        {"pregunta": "X' representa la ... del estado X.", "respuesta_correcta": "derivada", "opciones": ["derivada", "integral", "suma", "matriz"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Modelar propagación de virus (S.I.R.: Susceptibles, Infectados, Recuperados). Son 3 EDOs acopladas.", "consecuencia_de_error": "Malas políticas de salud pública."},
                    "quimica": {"uso": "Reacciones competitivas o consecutivas (A->B->C).", "consecuencia_de_error": "Mezcla final de productos incorrecta."},
                    "civil": {"uso": "Edificios de varios pisos. Cada piso es una masa acoplada a las otras.", "consecuencia_de_error": "Análisis sísmico incorrecto de rascacielos."},
                    "mecanica": {"uso": "Suspensiones de vehículos (llanta acoplada al chasis).", "consecuencia_de_error": "Auto inestable en baches."},
                    "mecatronica": {"uso": "Robots de múltiples articulaciones. El movimiento de un brazo afecta al otro (fuerzas de Coriolis).", "consecuencia_de_error": "Control descoordinado del robot."},
                    "aeronautica": {"uso": "Dinámica de vuelo 6-DOF (6 Grados de Libertad). Todas las rotaciones y traslaciones están acopladas.", "consecuencia_de_error": "Simulador de vuelo irreal."},
                    "electrica": {"uso": "Redes eléctricas complejas (mallas interconectadas).", "consecuencia_de_error": "Fallo en la distribución de energía."}
                }
            },
            {
                "subtema_titulo": "10. Aplicación: Circuitos RLC y Masa-Resorte",
                "definicion": "Analogía electromecánica. Un circuito RLC (Resistencia, Inductor, Capacitor) se comporta EXACTAMENTE igual que un sistema Masa-Resorte-Amortiguador. La inductancia (L) es como la masa (m), la resistencia (R) como la fricción (b), y la capacitancia (1/C) como la rigidez del resorte (k). ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Mecánico: mx'' + bx' + kx = F(t)\nEléctrico: Lq'' + Rq' + (1/C)q = V(t)\nAmbos son sistemas de 2do orden. Si b (o R) es bajo, el sistema oscila.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En la analogía, la Inductancia (L) equivale a la...",
                        "respuesta_correcta": "masa",
                        "opciones": ["masa", "friccion", "resorte", "velocidad"]
                    },
                    "similares": [
                        {"pregunta": "La Resistencia (R) equivale a la...", "respuesta_correcta": "friccion", "opciones": ["friccion", "masa", "resorte", "fuerza"]},
                        {"pregunta": "El Capacitor (1/C) equivale al...", "respuesta_correcta": "resorte", "opciones": ["resorte", "masa", "friccion", "velocidad"]},
                        {"pregunta": "El voltaje V(t) equivale a la...", "respuesta_correcta": "fuerza", "opciones": ["fuerza", "velocidad", "posicion", "masa"]},
                        {"pregunta": "La corriente (I=q') equivale a la...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "fuerza", "posicion", "aceleracion"]},
                        {"pregunta": "Un circuito sin resistencia (R=0) oscilaría por...", "respuesta_correcta": "siempre", "opciones": ["siempre", "nunca", "poco", "nada"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de sistemas físicos usando circuitos analógicos (computadoras analógicas antiguas).", "consecuencia_de_error": "Pérdida de la intuición física del sistema."},
                    "quimica": {"uso": "No aplica directamente, pero la analogía ayuda a entender sistemas oscilatorios.", "consecuencia_de_error": "N/A"},
                    "civil": {"uso": "Amortiguadores de masa sintonizada (TMD) en edificios para reducir oscilaciones (análogo a filtros notch).", "consecuencia_de_error": "Edificio inconfortable o inseguro."},
                    "mecanica": {"uso": "Diseño de suspensión activa usando teoría de control eléctrico.", "consecuencia_de_error": "Suspensión ineficiente."},
                    "mecatronica": {"uso": "Modelado unificado de sistemas electromecánicos (motores + carga mecánica) en una sola ecuación.", "consecuencia_de_error": "Ignorar el efecto de la carga mecánica sobre el circuito eléctrico del motor."},
                    "aeronautica": {"uso": "Sistemas de control fly-by-wire que amortiguan las oscilaciones naturales del avión.", "consecuencia_de_error": "Avión difícil de controlar."},
                    "electrica": {"uso": "Diseño de filtros RLC para radio y audio.", "consecuencia_de_error": "El radio no sintoniza la estación correcta."}
                }
            }
        ]
    },

    "FIS-01": {
        "nombre_completo": "Vectores y Magnitudes (Física)",
        "prerequisitos": ["TRIGONOMETRIA"],
        "quiz": [
            {
                "pregunta": "¿La temperatura es una magnitud escalar o vectorial?",
                "respuesta": "escalar",
                "opciones": ["escalar", "vectorial", "nula", "variable"]
            },
            {
                "pregunta": "¿La fuerza es una magnitud escalar o vectorial?",
                "respuesta": "vectorial",
                "opciones": ["vectorial", "escalar", "estatica", "adimensional"]
            }
        ],
        "refuerzo": [
            # --- TEMA 1 ORIGINAL (TEXTO EXACTO) ---
            {
                "subtema_titulo": "1. Magnitudes Escalares y Vectoriales",
                "definicion": "Un 'Escalar' es una cantidad definida solo por un número y unidad (ej. Masa, Temperatura, Tiempo). Un 'Vector' es una cantidad definida por 'magnitud' Y 'dirección' (ej. Fuerza, Velocidad, Desplazamiento).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: '5 kg' es un escalar. '10 N hacia el Este' es un vector. '20 m/s' es un escalar (se llama rapidez), pero '20 m/s hacia el Norte' es un vector (se llama velocidad).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La aceleración (como la de la gravedad, 'g') es una magnitud...",
                        "respuesta_correcta": "vectorial",
                        "opciones": ["vectorial", "escalar", "constante", "fija"]
                    },
                    "similares": [
                        {"pregunta": "La 'masa' de un objeto es...", "respuesta_correcta": "escalar", "opciones": ["escalar", "vectorial", "peso", "fuerza"]},
                        {"pregunta": "El 'peso' (fuerza de gravedad) es...", "respuesta_correcta": "vectorial", "opciones": ["vectorial", "escalar", "masa", "constante"]},
                        {"pregunta": "El 'tiempo' transcurrido es...", "respuesta_correcta": "escalar", "opciones": ["escalar", "vectorial", "relativo", "negativo"]},
                        {"pregunta": "La 'velocidad' (con dirección) es...", "respuesta_correcta": "vectorial", "opciones": ["vectorial", "escalar", "rapidez", "lenta"]},
                        {"pregunta": "El 'volumen' de un tanque es...", "respuesta_correcta": "escalar", "opciones": ["escalar", "vectorial", "cubico", "denso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En motores de física de videojuegos, la 'masa' de un objeto es un escalar, pero su 'velocidad' y 'fuerza' son vectores.", "consecuencia_de_error": "Confundir un escalar con un vector en la programación de un juego haría que los objetos se muevan de forma errática o no respondan a las fuerzas correctamente."},
                    "quimica": {"uso": "La 'concentración' o 'temperatura' de una solución son escalares. El 'momento dipolar' de una molécula es un vector.", "consecuencia_de_error": "No se necesita una dirección para medir la temperatura, pero sí para entender la polaridad de una molécula."},
                    "civil": {"uso": "La 'carga' (peso) sobre una viga es un vector (apunta hacia abajo). El 'área' de la viga es un escalar.", "consecuencia_de_error": "Un error al tratar el peso como un escalar impediría analizar cómo se distribuyen las fuerzas en la estructura."},
                    "mecanica": {"uso": "El 'Torque' (momento) es un vector, la 'Masa' es un escalar. La 'Potencia' es un escalar.", "consecuencia_de_error": "No entender que el torque es un vector (con dirección) impide analizar cómo una fuerza causa una rotación."},
                    "mecatronica": {"uso": "La 'posición' de un robot es un vector (x, y, z). La 'velocidad' de su motor (RPM) suele tratarse como un escalar, pero la 'velocidad' de la mano es un vector.", "consecuencia_de_error": "Un robot que solo conoce su rapidez (escalar) pero no su dirección (vector) es inútil para tareas de precisión."},
                    "aeronautica": {"uso": "La 'altitud' es un escalar. El 'viento' es un vector (magnitud y dirección).", "consecuencia_de_error": "Un piloto que solo considera la magnitud del viento (escalar) pero no su dirección (vector) calculará mal su ruta y consumo de combustible."},
                    "electrica": {"uso": "La 'Resistencia' (Ohms) es un escalar. El 'Campo Eléctrico' es un vector.", "consecuencia_de_error": "Tratar al campo eléctrico como un escalar haría imposible predecir la dirección de la fuerza sobre un electrón."}
                }
            },

            # --- TEMA 2 ORIGINAL (TEXTO EXACTO) ---
            {
                "subtema_titulo": "2. Descomposición de Vectores (Trigonometría)",
                "definicion": "Dividir un vector en sus 'componentes' rectangulares (ejes X e Y) usando SOH-CAH-TOA. Es la operación más importante de la estática.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Descomponer una Fuerza F=100N con un ángulo de 30° respecto a la horizontal.\nFx = F * cos(30°) = 100 * 0.866 = 86.6 N\nFy = F * sen(30°) = 100 * 0.5 = 50 N",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un vector Velocidad V=20m/s apunta a 45°. ¿Cuál es su componente Vx? (cos(45°)≈0.707)",
                        "respuesta_correcta": "14.14",
                        "opciones": ["14.14", "20", "10", "0.707"]
                    },
                    "similares": [
                        {"pregunta": "Fuerza F=100N a 60°. ¿Cuánto vale Fx? (cos60=0.5)", "respuesta_correcta": "50", "opciones": ["50", "86.6", "100", "25"]},
                        {"pregunta": "Fuerza F=100N a 30°. ¿Cuánto vale Fy? (sen30=0.5)", "respuesta_correcta": "50", "opciones": ["50", "86.6", "25", "100"]},
                        {"pregunta": "Si Vx=3 y Vy=4, ¿cuál es la magnitud? (Pitágoras)", "respuesta_correcta": "5", "opciones": ["5", "7", "25", "1"]},
                        {"pregunta": "Vector V=10 a 90° (Vertical). ¿Cuánto vale Vx?", "respuesta_correcta": "0", "opciones": ["0", "10", "1", "5"]},
                        {"pregunta": "Vector V=10 a 0° (Horizontal). ¿Cuánto vale Vy?", "respuesta_correcta": "0", "opciones": ["0", "10", "1", "5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En videojuegos, para calcular cuánto de la 'velocidad' de un personaje se aplica al movimiento horizontal (Vx) y cuánto al salto (Vy).", "consecuencia_de_error": "Un error en la descomposición haría que el personaje salte muy alto pero no avance, o viceversa."},
                    "quimica": {"uso": "Para analizar las fuerzas de un 'vector de dipolo' de una molécula en un campo eléctrico externo.", "consecuencia_de_error": "Permite predecir cómo rotará una molécula polar en un campo."},
                    "civil": {"uso": "Es la base del 'Método de Nodos' en armaduras. Cada fuerza en una viga diagonal se descompone en Fx y Fy para lograr el equilibrio (ΣFx=0, ΣFy=0).", "consecuencia_de_error": "Un error en la descomposición de una sola fuerza en un puente resultará en un cálculo erróneo de TODAS las demás fuerzas, llevando a un colapso."},
                    "mecanica": {"uso": "En 'Estática', para analizar cualquier fuerza que no sea puramente horizontal o vertical (ej. un cable que sostiene un peso).", "consecuencia_de_error": "Imposible calcular la 'tensión' en un cable o la 'compresión' en un soporte sin descomponer las fuerzas."},
                    "mecatronica": {"uso": "Es la base de la 'cinemática inversa'. Se conoce la velocidad vectorial (Vx, Vy) de la mano y se usa trigonometría para 'componer' los ángulos de motor.", "consecuencia_de_error": "Es la matemática central que permite a un robot moverse suavemente a un punto (x, y)."},
                    "aeronautica": {"uso": "Para descomponer la fuerza de 'Sustentación' (Lift) durante un viraje. Parte de la sustentación (L*cos(θ)) combate el peso y otra parte (L*sen(θ)) es la que da vuelta al avión.", "consecuencia_de_error": "Un piloto que no entiende esto, no entiende cómo dar vuelta. Perdería altitud en cada viraje."},
                    "electrica": {"uso": "Para descomponer el 'fasor' de Potencia Aparente (S) en Potencia Activa (P = S*cos(θ)) y Potencia Reactiva (Q = S*sen(θ)).", "consecuencia_de_error": "Un error aquí lleva a instalar cables incorrectos, pagar multas por bajo factor de potencia y desperdiciar energía."}
                }
            },

            # --- TEMA 3 ORIGINAL (TEXTO EXACTO) ---
            {
                "subtema_titulo": "3. Suma de Vectores (Método Analítico)",
                "definicion": "No se pueden sumar magnitudes (5N + 10N no siempre es 15N). Para sumar V₁ + V₂, primero se descomponen ambos, luego se suman las componentes por separado (Rx = V₁x + V₂x, Ry = V₁y + V₂y) y al final se recompone el vector resultante.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: F₁=(10, 20) y F₂=(5, -10).\nFuerza Resultante (R) = ?\nRx = 10 + 5 = 15\nRy = 20 + (-10) = 10\nR = (15, 10)",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Suma los vectores V₁=(3, 8) y V₂=(2, 2). El vector resultante es...",
                        "respuesta_correcta": "(5, 10)",
                        "opciones": ["(5, 10)", "(1, 6)", "(6, 16)", "(5, 6)"]
                    },
                    "similares": [
                        {"pregunta": "Resta V1=(5,5) menos V2=(1,4).", "respuesta_correcta": "(4, 1)", "opciones": ["(4, 1)", "(6, 9)", "(4, 9)", "(6, 1)"]},
                        {"pregunta": "Suma (1, 0) + (0, 1).", "respuesta_correcta": "(1, 1)", "opciones": ["(1, 1)", "(1, 0)", "(0, 1)", "(0, 0)"]},
                        {"pregunta": "Si la suma de fuerzas es (0, 0), el objeto está en...", "respuesta_correcta": "equilibrio", "opciones": ["equilibrio", "movimiento", "caida", "vuelo"]},
                        {"pregunta": "Suma (3, 3) + (-3, -3).", "respuesta_correcta": "(0, 0)", "opciones": ["(0, 0)", "(6, 6)", "(0, 6)", "(3, 3)"]},
                        {"pregunta": "Calcula 2*V si V=(3, -1).", "respuesta_correcta": "(6, -2)", "opciones": ["(6, -2)", "(5, 1)", "(3, -2)", "(6, -1)"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En un motor de física, para calcular la 'fuerza neta' sobre un objeto (F_gravedad + F_viento + F_jugador) y saber hacia dónde se moverá.", "consecuencia_de_error": "Un error en la suma de vectores hará que el objeto se mueva en una dirección ilógica."},
                    "quimica": {"uso": "Para encontrar el 'momento dipolar neto' de una molécula sumando los vectores de dipolo de cada enlace.", "consecuencia_de_error": "Permite predecir si una molécula será polar (ej. H₂O) o no polar (ej. CO₂), lo cual define todas sus propiedades."},
                    "civil": {"uso": "Para encontrar la 'fuerza resultante' en un nodo de un puente. El nodo está en equilibrio si la suma de todas las fuerzas (vectores) es (0, 0).", "consecuencia_de_error": "Es la comprobación fundamental de la estática. Si la suma no es cero, el cálculo está mal y el diseño no es seguro."},
                    "mecanica": {"uso": "Para encontrar el centro de masa de un objeto compuesto, sumando los vectores de posición de cada parte (ponderados por su masa).", "consecuencia_de_error": "Un centro de masa mal calculado causará vibraciones inesperadas en un objeto que rota."},
                    "mecatronica": {"uso": "Para calcular la posición final de la mano de un robot, sumando el vector del 'brazo' + el vector del 'antebrazo'.", "consecuencia_de_error": "Es la base de la 'cinemática directa'. Un error en la suma y el robot no sabe dónde está su mano."},
                    "aeronautica": {"uso": "Para calcular la 'velocidad sobre tierra' (Ground Speed), que es la suma vectorial de la 'velocidad del avión' + la 'velocidad del viento'.", "consecuencia_de_error": "Es el cálculo más importante en navegación. Un error aquí y el piloto no sabrá a dónde se dirige realmente."},
                    "electrica": {"uso": "Para encontrar el voltaje o corriente total en un nodo de AC (Leyes de Kirchhoff para fasores).", "consecuencia_de_error": "No se pueden sumar voltajes de AC (120V + 120V) directamente; debe ser una suma vectorial (fasorial), de lo contrario, los cálculos de la red eléctrica estarían mal."}
                }
            },

            # --- TEMAS EXTRA (AMPLIACIÓN SOLICITADA) ---
            {
                "subtema_titulo": "4. Vectores Unitarios (i, j, k)",
                "definicion": "Son vectores de magnitud 1 que solo indican dirección. 'i' apunta en X, 'j' en Y, 'k' en Z. Permiten escribir vectores como suma de partes: F = 30i + 40j.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Convertir el vector (3, 4) a notación unitaria.\nRespuesta: 3i + 4j.\nMagnitud = √(3² + 4²) = 5.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Normaliza el vector v=(3, 4). Su magnitud es 5. ¿Cuál es el vector unitario?",
                        "respuesta_correcta": "(0.6, 0.8)",
                        "opciones": ["(0.6, 0.8)", "(3, 4)", "(0.3, 0.4)", "(1, 1)"]
                    },
                    "similares": [
                        {"pregunta": "Escribe (5, 2) usando i y j.", "respuesta_correcta": "5i+2j", "opciones": ["5i+2j", "2i+5j", "5i-2j", "7ij"]},
                        {"pregunta": "Normaliza v=(10, 0).", "respuesta_correcta": "(1, 0)", "opciones": ["(1, 0)", "(10, 0)", "(0.1, 0)", "(0, 1)"]},
                        {"pregunta": "Normaliza v=(0, -5).", "respuesta_correcta": "(0, -1)", "opciones": ["(0, -1)", "(0, -5)", "(-1, 0)", "(0, 1)"]},
                        {"pregunta": "¿Cuál es la magnitud de 'i'?", "respuesta_correcta": "1", "opciones": ["1", "0", "i", "x"]},
                        {"pregunta": "El vector 'j' apunta hacia...", "respuesta_correcta": "arriba", "opciones": ["arriba", "derecha", "abajo", "izquierda"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Dirección de movimiento en juegos.", "consecuencia_de_error": "Personaje moviéndose a velocidad incorrecta en diagonales."},
                    "quimica": {"uso": "Orientación de espines electrónicos.", "consecuencia_de_error": "Errores en modelos cuánticos."},
                    "civil": {"uso": "Definición de dirección de fuerzas 3D.", "consecuencia_de_error": "Análisis matricial incorrecto."},
                    "mecanica": {"uso": "Ejes de rotación locales.", "consecuencia_de_error": "Errores de ensamblaje."},
                    "mecatronica": {"uso": "Vector de orientación del efector final.", "consecuencia_de_error": "Robot con la mano torcida."},
                    "aeronautica": {"uso": "Sistemas de navegación inercial (Norte, Este, Abajo).", "consecuencia_de_error": "Desviación de rumbo."},
                    "electrica": {"uso": "Análisis de campos electromagnéticos.", "consecuencia_de_error": "Diseño de antenas fallido."}
                }
            },
            {
                "subtema_titulo": "5. Producto Punto (Trabajo Físico)",
                "definicion": "Multiplicación de dos vectores que da un ESCALAR. A · B = |A||B|cos(θ). En física, representa cuánto de un vector actúa en la dirección del otro. Aplicación clave: Trabajo = Fuerza · Distancia.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Empujas una caja con 10N hacia el Este, y se mueve 5m al Este. Ángulo = 0°.\nTrabajo = 10 * 5 * cos(0°) = 50 Joules.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula el producto punto de dos vectores perpendiculares (ángulo 90°).",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "1", "-1", "infinito"]
                    },
                    "similares": [
                        {"pregunta": "Calcula el producto punto de A=(2,0) y B=(3,0).", "respuesta_correcta": "6", "opciones": ["6", "0", "5", "1"]},
                        {"pregunta": "Si F=10N y d=2m en la misma dirección, ¿cuánto es el trabajo?", "respuesta_correcta": "20", "opciones": ["20", "0", "5", "12"]},
                        {"pregunta": "A · B es un resultado...", "respuesta_correcta": "escalar", "opciones": ["escalar", "vectorial", "nulo", "matriz"]},
                        {"pregunta": "El producto punto se usa para calcular el ángulo entre vectores.", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si A=(1, 2) y B=(3, 4), A·B = 1*3 + 2*4 = ...", "respuesta_correcta": "11", "opciones": ["11", "10", "7", "14"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de iluminación (Lambert).", "consecuencia_de_error": "Objetos negros o mal iluminados."},
                    "quimica": {"uso": "Energía de interacción dipolo-dipolo.", "consecuencia_de_error": "Simulaciones moleculares erróneas."},
                    "civil": {"uso": "Proyección de fuerzas.", "consecuencia_de_error": "Subestimar cargas de viento."},
                    "mecanica": {"uso": "Cálculo de potencia mecánica.", "consecuencia_de_error": "Selección incorrecta de motor."},
                    "mecatronica": {"uso": "Detección de orientación al objetivo.", "consecuencia_de_error": "Robot oscilando."},
                    "aeronautica": {"uso": "Cálculo de arrastre parásito.", "consecuencia_de_error": "Estimación de eficiencia errónea."},
                    "electrica": {"uso": "Potencia Activa (Watts).", "consecuencia_de_error": "Facturación eléctrica incorrecta."}
                }
            },
            {
                "subtema_titulo": "6. Producto Cruz (Torque y Rotación)",
                "definicion": "Multiplicación de dos vectores que da un VECTOR perpendicular. |A x B| = |A||B|sen(θ). En física, representa rotación o 'Torque' (Momento). T = r x F.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Llave de tuercas. Radio r=0.2m (eje X), Fuerza F=100N (eje Y).\nTorque = 0.2 * 100 * sen(90°) = 20 Nm (en dirección Z, saliendo del plano).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El producto cruz de dos vectores paralelos (ángulo 0°) es...",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "1", "-1", "maximo"]
                    },
                    "similares": [
                        {"pregunta": "El resultado de A x B es un...", "respuesta_correcta": "vector", "opciones": ["vector", "escalar", "numero", "angulo"]},
                        {"pregunta": "Dirección del torque si r es X y F es Y (Regla mano derecha).", "respuesta_correcta": "z", "opciones": ["z", "x", "y", "-x"]},
                        {"pregunta": "Calcula magnitud de Torque: r=2m, F=10N, ángulo=90°.", "respuesta_correcta": "20", "opciones": ["20", "0", "10", "5"]},
                        {"pregunta": "¿Qué operación física usa producto cruz: Trabajo o Torque?", "respuesta_correcta": "torque", "opciones": ["torque", "trabajo", "potencia", "energia"]},
                        {"pregunta": "i x j = ...", "respuesta_correcta": "k", "opciones": ["k", "-k", "0", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de normales en triángulos.", "consecuencia_de_error": "Texturas invertidas."},
                    "quimica": {"uso": "Momento magnético en RMN.", "consecuencia_de_error": "Interpretación de espectros errónea."},
                    "civil": {"uso": "Momentos de flexión en vigas 3D.", "consecuencia_de_error": "Falla por torsión."},
                    "mecanica": {"uso": "Dinámica rotacional (Torque).", "consecuencia_de_error": "Diseño de maquinaria fallido."},
                    "mecatronica": {"uso": "Motores eléctricos (Ley de Lorentz).", "consecuencia_de_error": "Motor sin fuerza."},
                    "aeronautica": {"uso": "Estabilidad (cabeceo, alabeo, guiñada).", "consecuencia_de_error": "Avión inestable."},
                    "electrica": {"uso": "Fuerza de Lorentz.", "consecuencia_de_error": "Falla en diseño de generadores."}
                }
            }
        ]
    },

    "FIS-02": {
        "nombre_completo": "Cinemática: El Estudio del Movimiento",
        "prerequisitos": ["FIS-01"],
        "quiz": [
            {
                "pregunta": "En un MRUA, ¿qué magnitud permanece constante?",
                "respuesta": "aceleracion",
                "opciones": ["aceleracion", "velocidad", "posicion", "tiempo"]
            },
            {
                "pregunta": "Si lanzas una pelota hacia arriba, ¿cuál es su velocidad en el punto más alto?",
                "respuesta": "0",
                "opciones": ["0", "9.8", "maxima", "infinita"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Distancia vs. Desplazamiento",
                "definicion": "La 'Distancia' (d) es un escalar: cuánto camino recorriste en total (el odómetro del auto). El 'Desplazamiento' (Δx) es un vector: la línea recta desde el inicio hasta el final (posición final - inicial).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Corres 100m al Este y regresas 20m al Oeste.\nDistancia: 100 + 20 = 120 m.\nDesplazamiento: 100 - 20 = 80 m al Este.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Caminas 10m al Norte, 10m al Sur. ¿Cuál es tu desplazamiento total?",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "20", "10", "100"]
                    },
                    "similares": [
                        {"pregunta": "Caminas 5m, regresas 5m. ¿Cuál es la distancia recorrida?", "respuesta_correcta": "10", "opciones": ["10", "0", "5", "25"]},
                        {"pregunta": "Das una vuelta completa a una pista de 400m. ¿Desplazamiento?", "respuesta_correcta": "0", "opciones": ["0", "400", "800", "1"]},
                        {"pregunta": "Posición inicial x=2, final x=10. Desplazamiento:", "respuesta_correcta": "8", "opciones": ["8", "12", "20", "2"]},
                        {"pregunta": "Posición inicial x=5, final x=-5. Desplazamiento:", "respuesta_correcta": "-10", "opciones": ["-10", "10", "0", "25"]},
                        {"pregunta": "Vas de A a B (10km) y vuelves a A. Distancia total:", "respuesta_correcta": "20", "opciones": ["20", "0", "10", "100"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "En GPS o Google Maps. La 'ruta' calcula distancia (tiempo de viaje), pero la 'dirección' al destino es el desplazamiento.", "consecuencia_de_error": "Calcular el costo de combustible basado en desplazamiento en línea recta en lugar de distancia de carretera."},
                    "quimica": {"uso": "Difusión de gases. Una partícula recorre una gran distancia chocando, pero su desplazamiento neto es pequeño.", "consecuencia_de_error": "Mal cálculo del tiempo que tarda un olor o gas en cruzar una habitación."},
                    "civil": {"uso": "Movimiento de tierras. Importa el desplazamiento de la tierra (volumen x distancia de acarreo) para costos.", "consecuencia_de_error": "Presupuesto de obra incorrecto al no considerar la ruta real de los camiones."},
                    "mecanica": {"uso": "Mecanismo biela-manivela. El pistón sube y baja (mucha distancia), pero al final del ciclo su desplazamiento es cero.", "consecuencia_de_error": "Confundir el desgaste (distancia) con la posición neta."},
                    "mecatronica": {"uso": "Encoders de robots. Miden distancia recorrida (pulsos), pero el controlador necesita saber la posición absoluta (desplazamiento).", "consecuencia_de_error": "El robot pierde su 'home' y choca con los límites mecánicos."},
                    "aeronautica": {"uso": "Navegación. La distancia afecta el combustible; el desplazamiento es la ruta directa al aeropuerto.", "consecuencia_de_error": "Quedarse sin combustible por planear ruta directa pero tener que dar rodeos."},
                    "electrica": {"uso": "Corriente Alterna. Los electrones oscilan (mucha distancia), pero su desplazamiento neto (velocidad de deriva) es lentísimo.", "consecuencia_de_error": "Concepto fundamental para entender que la energía viaja rápido, no los electrones."}
                }
            },
            {
                "subtema_titulo": "2. Rapidez vs. Velocidad",
                "definicion": "La 'Rapidez' es escalar (distancia/tiempo). La 'Velocidad' es vectorial (desplazamiento/tiempo). En física, 'Velocidad' siempre implica dirección.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Recorres 100m en 10s en círculo y vuelves al inicio.\nRapidez = 100m/10s = 10 m/s.\nVelocidad = 0m/10s = 0 m/s (porque desplazamiento es 0).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un auto viaja a 60 km/h hacia el Norte. ¿60 km/h es su rapidez o velocidad?",
                        "respuesta_correcta": "rapidez",
                        "opciones": ["rapidez", "velocidad", "aceleracion", "tiempo"]
                    },
                    "similares": [
                        {"pregunta": "'60 km/h al Norte' es su...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "rapidez", "posicion", "fuerza"]},
                        {"pregunta": "Si v = -15 m/s, el signo indica...", "respuesta_correcta": "direccion", "opciones": ["direccion", "magnitud", "tiempo", "nada"]},
                        {"pregunta": "La velocidad media en un viaje de ida y vuelta siempre es...", "respuesta_correcta": "0", "opciones": ["0", "maxima", "constante", "doble"]},
                        {"pregunta": "Distancia 100m, tiempo 5s. Rapidez media:", "respuesta_correcta": "20", "opciones": ["20", "500", "0.05", "10"]},
                        {"pregunta": "Un velocímetro de auto mide... (rapidez/velocidad)", "respuesta_correcta": "rapidez", "opciones": ["rapidez", "velocidad", "aceleracion", "posicion"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Física de videojuegos. La rapidez determina la animación (correr), la velocidad determina la nueva posición (x, y).", "consecuencia_de_error": "El personaje corre en el lugar sin avanzar."},
                    "quimica": {"uso": "Teoría Cinética de Gases. La temperatura depende de la rapidez cuadrática media, no de la velocidad vectorial (que promedia cero).", "consecuencia_de_error": "Error conceptual al ligar temperatura con dirección de flujo."},
                    "civil": {"uso": "Diseño de carreteras. La rapidez de diseño define peraltes y radios de curva.", "consecuencia_de_error": "Autos saliéndose de la curva por exceso de fuerza centrífuga."},
                    "mecanica": {"uso": "Balanceo de rotores. Importa la velocidad tangencial (vector) para calcular fuerzas centrífugas.", "consecuencia_de_error": "Vibraciones destructivas en turbinas."},
                    "mecatronica": {"uso": "Control PID. El término derivativo actúa sobre la velocidad (cambio de error), que tiene signo (dirección).", "consecuencia_de_error": "El robot no sabe si frenar o acelerar."},
                    "aeronautica": {"uso": "Velocidad Aire (Airspeed) vs Velocidad Tierra (Ground Speed). El viento afecta la velocidad vectorial.", "consecuencia_de_error": "Errores críticos en tiempos de llegada y navegación."},
                    "electrica": {"uso": "Velocidad de propagación de señal en un cable (rapidez) vs velocidad de deriva de electrones.", "consecuencia_de_error": "Problemas de latencia en redes de alta frecuencia."}
                }
            },
            {
                "subtema_titulo": "3. Movimiento Rectilíneo Uniforme (MRU)",
                "definicion": "Movimiento en línea recta con Velocidad Constante. La aceleración es cero. Ecuación única: Posición final = Posición inicial + Velocidad * Tiempo (x = x₀ + vt).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un tren está en el km 10 (x₀) y viaja a 80 km/h (v). ¿Dónde está en 2 horas (t)?\nx = 10 + (80 * 2) = 10 + 160 = 170 km.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si viajas a 50 m/s constantes por 10s, ¿cuántos metros avanzas?",
                        "respuesta_correcta": "500",
                        "opciones": ["500", "5", "50", "0.2"]
                    },
                    "similares": [
                        {"pregunta": "En MRU, la aceleración vale...", "respuesta_correcta": "0", "opciones": ["0", "constante", "variable", "infinita"]},
                        {"pregunta": "Recorres 120km en 2h. Velocidad constante:", "respuesta_correcta": "60", "opciones": ["60", "240", "30", "120"]},
                        {"pregunta": "x = 5 + 3t. ¿Cuál es la velocidad?", "respuesta_correcta": "3", "opciones": ["3", "5", "8", "0"]},
                        {"pregunta": "x = 5 + 3t. ¿Cuál es la posición inicial?", "respuesta_correcta": "5", "opciones": ["5", "3", "8", "0"]},
                        {"pregunta": "¿Cuánto tardas en recorrer 100m a 5m/s?", "respuesta_correcta": "20", "opciones": ["20", "500", "0.05", "5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Movimiento de proyectiles simples (balas sin gravedad) o plataformas móviles en juegos.", "consecuencia_de_error": "Objetos que aceleran inesperadamente o se teletransportan."},
                    "quimica": {"uso": "Cromatografía. Los componentes se mueven a velocidad constante a lo largo del papel/columna.", "consecuencia_de_error": "Mala identificación de sustancias por tiempos de retención erróneos."},
                    "civil": {"uso": "Cintas transportadoras de material o flujo de agua en canales de pendiente constante.", "consecuencia_de_error": "Desbordamiento de material o cuellos de botella."},
                    "mecanica": {"uso": "Mecanizado en torno CNC. La herramienta debe moverse a velocidad de avance constante para un acabado liso.", "consecuencia_de_error": "Piezas con superficie rugosa o herramientas rotas."},
                    "mecatronica": {"uso": "Sincronización de bandas transportadoras en líneas de producción.", "consecuencia_de_error": "Productos que chocan o se caen de la línea."},
                    "aeronautica": {"uso": "Vuelo de crucero. El piloto automático busca mantener MRU para máxima eficiencia.", "consecuencia_de_error": "Mayor consumo de combustible y fatiga de pasajeros."},
                    "electrica": {"uso": "Transmisión de datos en fibra óptica. La luz viaja a velocidad constante 'c/n'.", "consecuencia_de_error": "Errores de sincronización en telecomunicaciones."}
                }
            },
            {
                "subtema_titulo": "4. Aceleración (El Cambio de Velocidad)",
                "definicion": "La aceleración (a) mide qué tan rápido cambia la velocidad. a = (Vf - Vi) / t. Puede ser cambio de magnitud (frenar/acelerar) o de dirección (girar).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un auto pasa de 0 a 20 m/s en 4 segundos.\na = (20 - 0) / 4 = 5 m/s². (Cada segundo, su velocidad aumenta en 5 m/s).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un auto frena de 30 m/s a 10 m/s en 2s. Calcula la aceleración (será negativa).",
                        "respuesta_correcta": "-10",
                        "opciones": ["-10", "10", "20", "-20"]
                    },
                    "similares": [
                        {"pregunta": "Si la velocidad es constante, la aceleración es...", "respuesta_correcta": "0", "opciones": ["0", "1", "infinita", "constante"]},
                        {"pregunta": "Unidad de aceleración en el SI.", "respuesta_correcta": "m/s^2", "opciones": ["m/s^2", "m/s", "km/h", "N"]},
                        {"pregunta": "Aceleras de 0 a 10 en 5s. a = ?", "respuesta_correcta": "2", "opciones": ["2", "0.5", "50", "5"]},
                        {"pregunta": "Si a = -2 m/s² y v = 10 m/s (positiva), el objeto está... (acelerando/frenando)", "respuesta_correcta": "frenando", "opciones": ["frenando", "acelerando", "quieto", "girando"]},
                        {"pregunta": "Cambio de velocidad de 50 a 60 en 1s. a = ?", "respuesta_correcta": "10", "opciones": ["10", "50", "60", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de vehículos. La aceleración define el 'pique' o la potencia del motor en el juego.", "consecuencia_de_error": "Autos que se sienten 'lentos' o incontrolables."},
                    "quimica": {"uso": "Centrífugas. La aceleración centrípeta (a = v²/r) separa las mezclas por densidad.", "consecuencia_de_error": "La sangre o mezcla no se separa correctamente."},
                    "civil": {"uso": "Diseño de curvas en carreteras. Se limita la aceleración lateral para evitar derrapes.", "consecuencia_de_error": "Carreteras peligrosas donde los autos se vuelcan."},
                    "mecanica": {"uso": "Fuerzas inerciales (F=ma). Piezas sometidas a alta aceleración (pistones) necesitan ser muy ligeras y fuertes.", "consecuencia_de_error": "Rotura de bielas o pistones a altas RPM."},
                    "mecatronica": {"uso": "Acelerómetros (sensores IMU) en drones para estabilización.", "consecuencia_de_error": "El dron no puede mantenerse nivelado y se estrella."},
                    "aeronautica": {"uso": "Fuerzas G. Una aceleración de 9.8 m/s² es 1G. Los pilotos soportan hasta 9G en combate.", "consecuencia_de_error": "Pérdida de conciencia del piloto (G-LOC)."},
                    "electrica": {"uso": "Aceleración de cargas en campos eléctricos. Base de los tubos de rayos X.", "consecuencia_de_error": "Radiación generada de frecuencia incorrecta (imagen borrosa)."}
                }
            },
            {
                "subtema_titulo": "5. Ecuaciones del MRUA (Las 4 Fantásticas)",
                "definicion": "Cuando la aceleración es constante. 1) Vf = Vi + at. 2) d = ((Vi+Vf)/2)*t. 3) d = Vi*t + 0.5*a*t². 4) Vf² = Vi² + 2ad. Permiten resolver cualquier problema sabiendo 3 variables.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un avión aterriza a 60 m/s (Vi) y frena con a=-2 m/s². ¿Cuánto recorre hasta detenerse (Vf=0)?\nUsar eq 4: 0² = 60² + 2(-2)d -> 0 = 3600 - 4d -> 4d = 3600 -> d = 900 metros.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Partes del reposo (Vi=0) con a=4 m/s². ¿Distancia en 3s? (d = 0.5*a*t²)",
                        "respuesta_correcta": "18",
                        "opciones": ["18", "6", "12", "36"]
                    },
                    "similares": [
                        {"pregunta": "Vi=10, a=2, t=5. ¿Vf?", "respuesta_correcta": "20", "opciones": ["20", "50", "10", "25"]},
                        {"pregunta": "Vi=0, Vf=20, t=10. ¿Distancia? (d = (Vf/2)*t)", "respuesta_correcta": "100", "opciones": ["100", "200", "50", "10"]},
                        {"pregunta": "Frenas de 20 a 0 en una distancia de 40m. ¿Aceleración? (Vf²=Vi²+2ad -> -400 = 80a)", "respuesta_correcta": "-5", "opciones": ["-5", "5", "-10", "10"]},
                        {"pregunta": "Vi=5, t=2, a=3. d = 5*2 + 0.5*3*4 = 10 + 6. d=?", "respuesta_correcta": "16", "opciones": ["16", "10", "22", "8"]},
                        {"pregunta": "Si a=0, la ecuación d = Vi*t + 0.5*a*t² se convierte en la ecuación de...", "respuesta_correcta": "MRU", "opciones": ["MRU", "MRUA", "Caida Libre", "Tiro Parabolico"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Animaciones 'ease-out' (frenado suave) en interfaces de usuario.", "consecuencia_de_error": "Animaciones robóticas o que terminan de golpe."},
                    "quimica": {"uso": "Espectrometría de masas. Calcular la distancia que recorre un ion acelerado antes de golpear el detector.", "consecuencia_de_error": "Mala calibración de la masa molecular detectada."},
                    "civil": {"uso": "Longitud de carriles de incorporación en autopistas. Deben permitir acelerar de 0 a 100 km/h.", "consecuencia_de_error": "Accidentes por autos entrando lento a la vía rápida."},
                    "mecanica": {"uso": "Diseño de frenos. Calcular distancia de frenado para dimensionar discos y pastillas.", "consecuencia_de_error": "Frenos insuficientes para la masa y velocidad del vehículo."},
                    "mecatronica": {"uso": "Planificación de trayectorias de robots (Rampas de velocidad trapezoidales).", "consecuencia_de_error": "Movimientos vibratorios o que exceden los límites del motor."},
                    "aeronautica": {"uso": "Cálculo de longitud de pista necesaria para despegue y aterrizaje (V1, Vr, V2).", "consecuencia_de_error": "Avión saliéndose de la pista."},
                    "electrica": {"uso": "Cañón de electrones (CRT). Distancia necesaria para acelerar el electrón al voltaje deseado.", "consecuencia_de_error": "Fallo en el enfoque del haz de electrones."}
                }
            },
            {
                "subtema_titulo": "6. Caída Libre (Gravedad)",
                "definicion": "Un caso especial de MRUA donde la aceleración es la gravedad (g ≈ 9.81 m/s²), siempre hacia ABAJO. Se suele ignorar la resistencia del aire en problemas básicos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Dejas caer una piedra (Vi=0) desde un puente. Tarda 3s en caer. Altura del puente?\nd = Vi*t + 0.5*g*t² -> d = 0 + 0.5 * 9.8 * 3² = 4.9 * 9 = 44.1 metros.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Dejas caer un objeto (g=10 m/s²). ¿Cuál es su velocidad a los 2 segundos?",
                        "respuesta_correcta": "20",
                        "opciones": ["20", "10", "5", "0"]
                    },
                    "similares": [
                        {"pregunta": "En caída libre, la velocidad inicial al 'dejar caer' es...", "respuesta_correcta": "0", "opciones": ["0", "9.8", "infinita", "variable"]},
                        {"pregunta": "Distancia caída en 1s (g=9.8).", "respuesta_correcta": "4.9", "opciones": ["4.9", "9.8", "19.6", "1"]},
                        {"pregunta": "¿La gravedad afecta a los objetos pesados más que a los ligeros (sin aire)? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Valor aproximado de g en la Tierra.", "respuesta_correcta": "9.8", "opciones": ["9.8", "1.6", "3.7", "24"]},
                        {"pregunta": "Si lanzas hacia abajo con Vi=10, ¿Vf a 1s? (g=10)", "respuesta_correcta": "20", "opciones": ["20", "10", "0", "30"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Física de saltos en plataformas. Configurar 'g' afecta qué tan alto y rápido se siente el salto.", "consecuencia_de_error": "Juego con gravedad 'lunar' o 'pesada' no intencional."},
                    "quimica": {"uso": "Torres de lavado de gases. Las gotas de líquido caen por gravedad mientras el gas sube.", "consecuencia_de_error": "Diseño ineficiente de la torre, mala absorción."},
                    "civil": {"uso": "Pilotaje. Se deja caer un martillo pesado para clavar pilotes. La altura define la energía de impacto.", "consecuencia_de_error": "Pilote no clavado a la profundidad o capacidad de carga correcta."},
                    "mecanica": {"uso": "Pruebas de impacto (Drop test) para certificar cascos o embalajes.", "consecuencia_de_error": "Producto que se rompe al caerse de la mesa."},
                    "mecatronica": {"uso": "Estimación de la orientación (inclinación) usando la gravedad como vector de referencia en un acelerómetro.", "consecuencia_de_error": "El robot no sabe dónde está 'abajo' y se cae."},
                    "aeronautica": {"uso": "Maniobras de gravedad cero (Vuelo parabólico). El avión cae con a=g.", "consecuencia_de_error": "Pasajeros golpeándose contra el techo o suelo."},
                    "electrica": {"uso": "Interruptores de mercurio (antiguos) o sensores de inclinación basados en gravedad.", "consecuencia_de_error": "Fallo en la activación de sistemas de seguridad."}
                }
            },
            {
                "subtema_titulo": "7. Tiro Vertical (Subida y Bajada)",
                "definicion": "Lanzar algo hacia arriba. Sube desacelerando (a = -g) hasta detenerse (V=0 en altura máxima) y luego cae acelerando. El tiempo de subida es igual al de bajada (si llega al mismo nivel).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Lanzas pelota a 30 m/s hacia arriba (g=10). ¿Tiempo para altura máxima?\nVf = Vi - gt -> 0 = 30 - 10t -> 10t = 30 -> t = 3 segundos.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Lanzas algo a 20 m/s hacia arriba (g=10). ¿Cuánto tarda en llegar al punto más alto?",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "1", "4", "0.5"]
                    },
                    "similares": [
                        {"pregunta": "En la altura máxima, la velocidad es...", "respuesta_correcta": "0", "opciones": ["0", "maxima", "9.8", "negativa"]},
                        {"pregunta": "En la altura máxima, la aceleración es... (0, g, -g)", "respuesta_correcta": "g", "opciones": ["g", "0", "-g", "variable"]},
                        {"pregunta": "Si tarda 3s en subir, ¿cuánto tarda en bajar al mismo punto?", "respuesta_correcta": "3", "opciones": ["3", "6", "1.5", "0"]},
                        {"pregunta": "Si lanzas a 30 m/s, ¿con qué velocidad regresa a tu mano? (desprecia aire)", "respuesta_correcta": "30", "opciones": ["30", "0", "15", "60"]},
                        {"pregunta": "Altura máxima si Vi=10, g=10. (Vf²=Vi²-2gh -> 0=100-20h)", "respuesta_correcta": "5", "opciones": ["5", "10", "20", "2.5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular la altura de salto de un personaje. H = Vi² / 2g.", "consecuencia_de_error": "Personaje salta demasiado alto y se sale del mapa."},
                    "quimica": {"uso": "Diseño de fuentes o reactores de lecho fluidizado donde las partículas son empujadas hacia arriba por un gas.", "consecuencia_de_error": "El material sale volando del reactor o se asienta en el fondo."},
                    "civil": {"uso": "Bombas de concreto o agua. Calcular la presión necesaria para subir el fluido a cierta altura vertical.", "consecuencia_de_error": "La bomba no tiene fuerza para llevar el agua al tinaco."},
                    "mecanica": {"uso": "Válvulas de motor. El resorte debe empujar la válvula hacia abajo más rápido de lo que la inercia la lanza hacia arriba.", "consecuencia_de_error": "'Flotación de válvulas' a altas RPM, destruyendo el motor."},
                    "mecatronica": {"uso": "Drones. Para mantener altura, el empuje debe igualar al peso. Para subir, empuje > peso.", "consecuencia_de_error": "Dron oscilando en altura sin control."},
                    "aeronautica": {"uso": "Velocidad de ascenso (Rate of Climb). Crítico para librar obstáculos tras el despegue.", "consecuencia_de_error": "Choque contra terreno elevado."},
                    "electrica": {"uso": "Pararrayos. Ionización ascendente (leader) que conecta con la descarga descendente.", "consecuencia_de_error": "Fallo en la protección contra rayos."}
                }
            },
            {
                "subtema_titulo": "8. Gráficas de Movimiento: Posición vs. Tiempo (x-t)",
                "definicion": "Muestran dónde está el objeto en cada momento. La PENDIENTE (inclinación) de la línea es la VELOCIDAD. Pendiente constante = MRU. Curva = MRUA (Aceleración).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Una línea recta que sube significa velocidad constante positiva. Una línea horizontal significa que el objeto está quieto (Velocidad=0).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En una gráfica x-t, una línea horizontal indica que la velocidad es...",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "constante", "infinita", "negativa"]
                    },
                    "similares": [
                        {"pregunta": "La pendiente de la gráfica x-t representa la...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "aceleracion", "distancia", "tiempo"]},
                        {"pregunta": "Una pendiente negativa en x-t significa que el objeto...", "respuesta_correcta": "retrocede", "opciones": ["retrocede", "avanza", "frena", "acelera"]},
                        {"pregunta": "Una línea curva (parábola) en x-t indica que hay...", "respuesta_correcta": "aceleracion", "opciones": ["aceleracion", "velocidad constante", "reposo", "friccion"]},
                        {"pregunta": "Si la gráfica x-t es una recta inclinada hacia arriba, el movimiento es... (MRU/MRUA)", "respuesta_correcta": "MRU", "opciones": ["MRU", "MRUA", "Caida Libre", "Tiro Parabolico"]},
                        {"pregunta": "Mayor pendiente significa mayor...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "tiempo", "distancia", "fuerza"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Animación. Las curvas de animación (Bezier) son gráficas x-t. Ajustar la pendiente ajusta la velocidad.", "consecuencia_de_error": "Animaciones rígidas y poco naturales."},
                    "quimica": {"uso": "Cinética química. Gráfica de concentración vs tiempo. La pendiente es la velocidad de reacción.", "consecuencia_de_error": "Mala interpretación de la rapidez de la reacción."},
                    "civil": {"uso": "Cronogramas de obra (Diagramas Espacio-Tiempo). Pendiente = velocidad de avance de la construcción.", "consecuencia_de_error": "Retrasos en el proyecto por mala planificación."},
                    "mecanica": {"uso": "Perfil de levas. La forma física de la leva es literalmente una gráfica x-t polar que empuja una varilla.", "consecuencia_de_error": "Válvulas que abren a destiempo o golpean."},
                    "mecatronica": {"uso": "Análisis de trayectorias grabadas por un robot para suavizar movimientos.", "consecuencia_de_error": "Movimientos bruscos que dañan la carga."},
                    "aeronautica": {"uso": "Análisis de datos de caja negra (FDR) post-vuelo.", "consecuencia_de_error": "Imposibilidad de determinar la causa de un accidente."},
                    "electrica": {"uso": "Osciloscopio. Muestra Voltaje (analogo a posición) vs Tiempo. La pendiente es el 'Slew Rate'.", "consecuencia_de_error": "Distorsión de señal si el amplificador es lento."}
                }
            },
            {
                "subtema_titulo": "9. Gráficas de Movimiento: Velocidad vs. Tiempo (v-t)",
                "definicion": "La PENDIENTE es la ACELERACIÓN. El ÁREA bajo la curva es el DESPLAZAMIENTO (distancia recorrida). Es la gráfica más útil en ingeniería.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un triángulo de base 4s y altura 10 m/s.\nÁrea = (4 * 10) / 2 = 20 metros recorridos.\nPendiente = 10 / 4 = 2.5 m/s² de aceleración.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En una gráfica v-t, el área bajo la curva representa la...",
                        "respuesta_correcta": "distancia",
                        "opciones": ["distancia", "velocidad", "aceleracion", "tiempo"]
                    },
                    "similares": [
                        {"pregunta": "La pendiente de la gráfica v-t representa la...", "respuesta_correcta": "aceleracion", "opciones": ["aceleracion", "velocidad", "posicion", "fuerza"]},
                        {"pregunta": "Una línea horizontal en v-t (v=constante) significa aceleración...", "respuesta_correcta": "0", "opciones": ["0", "constante", "variable", "infinita"]},
                        {"pregunta": "Si la línea baja (pendiente negativa), el objeto está...", "respuesta_correcta": "frenando", "opciones": ["frenando", "acelerando", "girando", "cayendo"]},
                        {"pregunta": "Si la velocidad cruza el eje horizontal (pasa de + a -), el objeto...", "respuesta_correcta": "regresa", "opciones": ["regresa", "frena", "acelera", "se detiene"]},
                        {"pregunta": "Un rectángulo en v-t (base 5, altura 10) tiene área...", "respuesta_correcta": "50", "opciones": ["50", "15", "2", "5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Integración numérica. Calcular posición sumando el área de la velocidad en cada frame.", "consecuencia_de_error": "Acumulación de error que hace que el objeto se deslice."},
                    "quimica": {"uso": "Caudal vs Tiempo. El área bajo la curva es el Volumen total transferido.", "consecuencia_de_error": "Llenado excesivo o insuficiente de tanques."},
                    "civil": {"uso": "Hidrología. Hidrograma (Caudal vs Tiempo). El área es el volumen total de la tormenta.", "consecuencia_de_error": "Diseño insuficiente de drenajes pluviales."},
                    "mecanica": {"uso": "Ciclos de conducción (Drive cycles) para pruebas de emisiones y consumo.", "consecuencia_de_error": "El vehículo no cumple las normas ambientales."},
                    "mecatronica": {"uso": "Control de motores. Se envía un perfil de velocidad (trapezoide) y el driver calcula la posición integrando el área.", "consecuencia_de_error": "El robot se pasa de largo del objetivo."},
                    "aeronautica": {"uso": "Despegue. Integrar la curva de velocidad para asegurar que se alcanza V_takeoff antes del final de la pista.", "consecuencia_de_error": "Aborto de despegue tardío o accidente."},
                    "electrica": {"uso": "Energía. Potencia vs Tiempo. El área son los kWh consumidos.", "consecuencia_de_error": "Facturación errónea o baterías descargadas antes de tiempo."}
                }
            },
            {
                "subtema_titulo": "10. Tiro Parabólico",
                "definicion": "Movimiento curvo bajo gravedad. La clave: SEPARAR en dos movimientos independientes.\nEje X: MRU (Velocidad constante, ax=0).\nEje Y: MRUA (Caída libre, ay=-g).\nEl tiempo 't' es el mismo para ambos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Lanzas horizontalmente una pelota a 10 m/s desde 20m de altura.\n1. Tiempo de caída (Eje Y): d = 0.5gt² -> 20 = 5t² -> t²=4 -> t=2s.\n2. Distancia horizontal (Eje X): d = vt -> d = 10 * 2 = 20 metros.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En el punto más alto de un tiro parabólico, ¿la velocidad VERTICAL es?",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "maxima", "constante", "negativa"]
                    },
                    "similares": [
                        {"pregunta": "En tiro parabólico, la velocidad HORIZONTAL es... (constante/variable)", "respuesta_correcta": "constante", "opciones": ["constante", "variable", "cero", "acelerada"]},
                        {"pregunta": "El ángulo para el máximo alcance horizontal es...", "respuesta_correcta": "45", "opciones": ["45", "90", "30", "60"]},
                        {"pregunta": "¿Qué fuerza actúa sobre el proyectil en el aire? (solo una)", "respuesta_correcta": "gravedad", "opciones": ["gravedad", "impulso", "friccion", "magnetismo"]},
                        {"pregunta": "Si lanzas una bala y dejas caer otra al mismo tiempo, ¿cuál toca suelo primero?", "respuesta_correcta": "iguales", "opciones": ["iguales", "la bala", "la caida", "depende"]},
                        {"pregunta": "La trayectoria forma una figura geométrica llamada...", "respuesta_correcta": "parabola", "opciones": ["parabola", "circulo", "elipse", "recta"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Angry Birds, Worms. Calcular la trayectoria de proyectiles para la jugabilidad.", "consecuencia_de_error": "El juego se siente roto si la parábola no es realista."},
                    "quimica": {"uso": "Diseño de rociadores (spray). Las gotas siguen trayectorias parabólicas para cubrir un área.", "consecuencia_de_error": "Cobertura desigual de pintura o pesticida."},
                    "civil": {"uso": "Chorros de agua en fuentes decorativas o vertederos de presas.", "consecuencia_de_error": "El agua cae fuera de la pileta o erosiona el suelo equivocado."},
                    "mecanica": {"uso": "Balística. Diseño de armas o lanzadores de pelotas. Ajustar ángulo y fuerza.", "consecuencia_de_error": "Proyectil no alcanza el blanco."},
                    "mecatronica": {"uso": "Robots de recolección agrícola que lanzan la fruta al contenedor.", "consecuencia_de_error": "Fruta golpeada o perdida."},
                    "aeronautica": {"uso": "Lanzamiento de cargas humanitarias o paracaidistas desde el aire.", "consecuencia_de_error": "La carga cae en zona enemiga o inaccesible."},
                    "electrica": {"uso": "Desviación de electrones en un campo eléctrico (osciloscopio CRT). Siguen una trayectoria parabólica.", "consecuencia_de_error": "La imagen no se dibuja en la pantalla correctamente."}
                }
            }
        ]
    },

    "FIS-03": {
        "nombre_completo": "Dinámica: Fuerzas y Leyes de Newton",
        "prerequisitos": ["FIS-02"],
        "quiz": [
            {
                "pregunta": "Si la fuerza neta es cero, ¿la aceleración es?",
                "respuesta": "0",
                "opciones": ["0", "constante", "maxima", "negativa"]
            },
            {
                "pregunta": "La fuerza que se opone al deslizamiento entre superficies se llama...",
                "respuesta": "friccion",
                "opciones": ["friccion", "normal", "peso", "tension"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Masa vs. Peso",
                "definicion": "Error clásico: La 'Masa' (m) es cantidad de materia (escalar, kg) y no cambia. El 'Peso' (W) es la fuerza de gravedad sobre esa masa (vector, N). W = m * g. En la Luna, tu masa es la misma, pero tu peso cambia.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Una roca de 10kg. (g=9.8 m/s²)\nMasa = 10 kg (Aquí y en China).\nPeso = 10 kg * 9.8 m/s² = 98 Newtons (Hacia el centro de la Tierra).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un astronauta de 80kg está en el espacio (g=0). ¿Cuál es su peso en Newtons?",
                        "respuesta_correcta": "0",
                        "opciones": ["0", "80", "800", "8"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuál es su masa en el espacio? (en kg)", "respuesta_correcta": "80", "opciones": ["80", "0", "8", "800"]},
                        {"pregunta": "Si g=10, ¿cuál es el peso de una caja de 5kg?", "respuesta_correcta": "50", "opciones": ["50", "5", "0.5", "500"]},
                        {"pregunta": "El peso se mide en... (kg/N)", "respuesta_correcta": "N", "opciones": ["N", "kg", "lb", "m/s"]},
                        {"pregunta": "La masa se mide en... (kg/N)", "respuesta_correcta": "kg", "opciones": ["kg", "N", "g", "m"]},
                        {"pregunta": "Si pesas 700N (g=10), ¿tu masa es?", "respuesta_correcta": "70", "opciones": ["70", "700", "7", "7000"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Motores de física. Configurar `mass = 1` y `gravity = 9.8`. Si confundes masa con peso, la simulación explota.", "consecuencia_de_error": "Objetos que caen demasiado rápido o flotan extrañamente."},
                    "quimica": {"uso": "Balanza analítica. Calibrada para medir la fuerza (peso) pero mostrar masa (kg).", "consecuencia_de_error": "Errores de pesaje si la balanza no está nivelada o calibrada para la gravedad local."},
                    "civil": {"uso": "Cálculo de 'Cargas Muertas'. El peso propio de la estructura (W) que debe soportar los cimientos.", "consecuencia_de_error": "Colapso estructural por subestimar el peso del concreto."},
                    "mecanica": {"uso": "Diseño de elevadores. El motor debe vencer el Peso, no la Masa.", "consecuencia_de_error": "El elevador no se mueve o el cable se rompe."},
                    "mecatronica": {"uso": "Selección de motores. El torque necesario depende del peso del brazo robótico.", "consecuencia_de_error": "Motores que se queman por sobrecarga."},
                    "aeronautica": {"uso": "Balance de peso y centrado. El peso total (W) debe ser contrarrestado por la sustentación (L).", "consecuencia_de_error": "El avión no despega o es inestable."},
                    "electrica": {"uso": "Fuerza eléctrica vs Gravitacional. En partículas (electrones), el peso es despreciable comparado con la fuerza eléctrica.", "consecuencia_de_error": "Considerar la gravedad en el diseño de circuitos (innecesario)."}
                }
            },
            {
                "subtema_titulo": "2. Primera Ley (Inercia)",
                "definicion": "Un objeto se resiste a cambiar su movimiento. Si ΣF = 0 (Fuerza Neta cero), el objeto se queda quieto (v=0) O se mueve en línea recta a velocidad constante (MRU). No se necesita fuerza para mantener el movimiento, solo para cambiarlo.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un disco de hockey deslizándose sobre hielo infinito (sin fricción). Aunque nadie lo empuje, seguirá moviéndose eternamente a velocidad constante por inercia.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un cohete apaga sus motores en el espacio profundo, ¿se detiene inmediatamente? (si/no)",
                        "respuesta_correcta": "no",
                        "opciones": ["no", "si"]
                    },
                    "similares": [
                        {"pregunta": "La medida de la inercia de un cuerpo es su...", "respuesta_correcta": "masa", "opciones": ["masa", "peso", "volumen", "velocidad"]},
                        {"pregunta": "Un auto viaja a velocidad constante. ¿La fuerza neta sobre él es?", "respuesta_correcta": "0", "opciones": ["0", "maxima", "negativa", "constante"]},
                        {"pregunta": "Si frenas de golpe, tu cuerpo se va hacia... (adelante/atras)", "respuesta_correcta": "adelante", "opciones": ["adelante", "atras", "arriba", "abajo"]},
                        {"pregunta": "¿Se necesita fuerza continua para mantener un objeto en movimiento en el vacío?", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Estado de movimiento con aceleración cero: Reposo o...", "respuesta_correcta": "velocidad constante", "opciones": ["velocidad constante", "aceleracion", "caida libre", "frenado"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de naves espaciales (tipo Asteroids). La nave sigue deslizándose aunque sueltes la tecla.", "consecuencia_de_error": "Juego poco realista donde las cosas se frenan solas sin fricción."},
                    "quimica": {"uso": "Centrifugación. Las partículas más densas tienen más inercia y 'siguen derecho' hacia el fondo del tubo.", "consecuencia_de_error": "No entender la separación de mezclas."},
                    "civil": {"uso": "Sismorresistencia. La base del edificio se mueve con el sismo, pero la parte de arriba quiere quedarse quieta (inercia), causando corte.", "consecuencia_de_error": "El edificio se rompe por la base."},
                    "mecanica": {"uso": "Volantes de inercia (Flywheel). Almacenan energía cinética para mantener el motor girando suavemente.", "consecuencia_de_error": "Motor que vibra o se apaga entre explosiones."},
                    "mecatronica": {"uso": "Aceleración de arranque. El motor necesita más fuerza para 'arrancar' (vencer inercia) que para mantener la velocidad.", "consecuencia_de_error": "El robot arranca lento o con tirones."},
                    "aeronautica": {"uso": "Turbulencia. El avión quiere seguir recto, el aire lo empuja. La inercia del avión amortigua los golpes.", "consecuencia_de_error": "Diseño estructural insuficiente para cargas inerciales."},
                    "electrica": {"uso": "Inductores. Son la 'inercia' de la corriente. Un inductor se opone al cambio de corriente (como la masa al cambio de velocidad).", "consecuencia_de_error": "Picos de voltaje destructivos al apagar un interruptor."}
                }
            },
            {
                "subtema_titulo": "3. Segunda Ley (La Ecuación Maestra ΣF=ma)",
                "definicion": "La aceleración es proporcional a la Fuerza Neta e inversamente proporcional a la masa. ΣF = m * a. IMPORTANTE: ΣF es la suma vectorial de TODAS las fuerzas (F_motor - F_fricción - F_peso... etc).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Empujas (100N) una caja de 20kg. La fricción te resta 40N.\n1. Fuerza Neta ΣF = 100 - 40 = 60 N.\n2. a = ΣF / m = 60 / 20 = 3 m/s².",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Fuerza neta de 50N sobre masa de 10kg. ¿Aceleración?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "500", "0.2", "10"]
                    },
                    "similares": [
                        {"pregunta": "Si aplicas la misma fuerza a doble masa, la aceleración se reduce a la...", "respuesta_correcta": "mitad", "opciones": ["mitad", "doble", "cuarta parte", "misma"]},
                        {"pregunta": "Para acelerar 2kg a 10 m/s², ¿qué fuerza necesitas?", "respuesta_correcta": "20", "opciones": ["20", "5", "0.2", "12"]},
                        {"pregunta": "Un objeto de 5kg cae (Fuerza = Peso = 50N). La resistencia del aire es 10N. ΣF = ?", "respuesta_correcta": "40", "opciones": ["40", "50", "60", "10"]},
                        {"pregunta": "Si ΣF = 0, entonces a = ...", "respuesta_correcta": "0", "opciones": ["0", "1", "constante", "g"]},
                        {"pregunta": "Unidad de Fuerza (kg * m/s²).", "respuesta_correcta": "newton", "opciones": ["newton", "joule", "watt", "pascal"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Núcleo de cualquier motor físico (PhysX, Havok). `position += velocity * dt`, `velocity += (force/mass) * dt`.", "consecuencia_de_error": "El juego no tiene física, es solo animación."},
                    "quimica": {"uso": "Dinámica Molecular. Calcular cómo se mueven los átomos bajo fuerzas electrostáticas (F=ma).", "consecuencia_de_error": "Simulaciones moleculares erróneas."},
                    "civil": {"uso": "Análisis dinámico. F_sismo = Masa_edificio * Aceleración_suelo.", "consecuencia_de_error": "Subestimar las fuerzas sísmicas."},
                    "mecanica": {"uso": "Dimensionamiento de motores. Fuerza necesaria para acelerar un vehículo de 0 a 100 en X segundos.", "consecuencia_de_error": "Auto con motor insuficiente."},
                    "mecatronica": {"uso": "Control de torque. El microcontrolador calcula la fuerza necesaria para mover el brazo a la velocidad deseada.", "consecuencia_de_error": "Error de posición o sobrecorriente."},
                    "aeronautica": {"uso": "Despegue. Empuje - Arrastre = Masa * Aceleración.", "consecuencia_de_error": "Pista insuficiente para despegar."},
                    "electrica": {"uso": "Analogía en circuitos (Leyes de Kirchhoff). La suma de fuerzas (voltajes) impulsa la carga.", "consecuencia_de_error": "Mal análisis de mallas."}
                }
            },
            {
                "subtema_titulo": "4. Tercera Ley (Acción y Reacción)",
                "definicion": "Si A empuja a B, B empuja a A con la misma fuerza pero en sentido opuesto. Las fuerzas SIEMPRE vienen en pares. Nota: Nunca se cancelan porque actúan sobre objetos DIFERENTES.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Disparar un cañón.\nAcción: El cañón empuja la bala hacia adelante.\nReacción: La bala empuja el cañón hacia atrás (retroceso).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si golpeas una pared con 50N, ¿con cuánta fuerza te golpea la pared?",
                        "respuesta_correcta": "50",
                        "opciones": ["50", "0", "100", "25"]
                    },
                    "similares": [
                        {"pregunta": "La fuerza de reacción al peso de un libro (Tierra atrae Libro) es...", "respuesta_correcta": "libro atrae tierra", "opciones": ["libro atrae tierra", "mesa empuja libro", "libro empuja mesa", "nada"]},
                        {"pregunta": "Un mosquito choca con un camión. ¿Quién siente más fuerza?", "respuesta_correcta": "iguales", "opciones": ["iguales", "camion", "mosquito", "depende"]},
                        {"pregunta": "¿Quién siente más aceleración (por tener menos masa)?", "respuesta_correcta": "mosquito", "opciones": ["mosquito", "camion", "iguales", "nadie"]},
                        {"pregunta": "Los cohetes funcionan en el vacío gracias a la... (1ra/2da/3ra ley)", "respuesta_correcta": "3ra", "opciones": ["3ra", "1ra", "2da", "4ta"]},
                        {"pregunta": "La fuerza Normal es una reacción a la fuerza de contacto. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Colisiones. Si el Jugador choca con el Enemigo, ambos deben recibir fuerzas de rebote opuestas.", "consecuencia_de_error": "Objetos que se atraviesan o no rebotan correctamente."},
                    "quimica": {"uso": "Presión de un gas. Las moléculas golpean la pared (acción) y la pared las rebota (reacción). La suma es la presión.", "consecuencia_de_error": "No entender el origen molecular de la presión."},
                    "civil": {"uso": "Cimentación. El edificio empuja al suelo (Acción), el suelo empuja al edificio (Reacción/Normal).", "consecuencia_de_error": "Hundimiento si el suelo no puede generar suficiente reacción."},
                    "mecanica": {"uso": "Engranajes. Diente A empuja a Diente B, B empuja a A. Esa fuerza separa los ejes.", "consecuencia_de_error": "Ejes que se doblan o rodamientos que fallan."},
                    "mecatronica": {"uso": "Retroceso en actuadores. Si un robot empuja fuerte, su base puede volcarse hacia atrás.", "consecuencia_de_error": "Robot inestable que se cae al operar."},
                    "aeronautica": {"uso": "Propulsión Jet y Hélices. Empujan el aire atrás, el aire empuja el avión adelante.", "consecuencia_de_error": "Imposible diseñar sistemas de propulsión."},
                    "electrica": {"uso": "Fuerzas entre cables. Dos cables con corriente se repelen mutuamente con igual fuerza.", "consecuencia_de_error": "Cables que se rompen o chicotean en un cortocircuito."}
                }
            },
            {
                "subtema_titulo": "5. Diagrama de Cuerpo Libre (DCL)",
                "definicion": "La herramienta MÁS importante. Es un dibujo que aísla el objeto y muestra TODAS las fuerzas externas como vectores (flechas) que salen de él. Sin DCL, no se puede plantear ΣF=ma.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Bloque deslizando en una mesa con fricción.\nFlechas: 1. Peso (abajo). 2. Normal (arriba). 3. Fricción (atrás).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En un plano inclinado, la Normal es perpendicular a...",
                        "respuesta_correcta": "la superficie",
                        "opciones": ["la superficie", "el suelo", "la gravedad", "el peso"]
                    },
                    "similares": [
                        {"pregunta": "El peso siempre apunta hacia...", "respuesta_correcta": "abajo", "opciones": ["abajo", "arriba", "la superficie", "el movimiento"]},
                        {"pregunta": "La fricción cinética siempre se opone al...", "respuesta_correcta": "movimiento", "opciones": ["movimiento", "peso", "suelo", "aire"]},
                        {"pregunta": "La tensión siempre 'jala' del objeto. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Un DCL incluye fuerzas internas del objeto. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "¿Cuántas fuerzas actúan sobre un objeto en caída libre (sin aire)?", "respuesta_correcta": "1", "opciones": ["1", "2", "0", "3"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Debugging de física. Visualizar los vectores de fuerza sobre el personaje para ver por qué se comporta raro.", "consecuencia_de_error": "No poder arreglar bugs de movimiento."},
                    "quimica": {"uso": "Análisis de fuerzas sobre una partícula cargada en un campo eléctrico y magnético.", "consecuencia_de_error": "Error en la predicción de trayectoria."},
                    "civil": {"uso": "Paso 1 de cualquier cálculo estructural. DCL de cada nodo de la armadura.", "consecuencia_de_error": "Cálculo estructural totalmente erróneo."},
                    "mecanica": {"uso": "Análisis de fatiga. Determinar qué fuerzas actúan realmente sobre un perno.", "consecuencia_de_error": "Falla de la pieza por no considerar una fuerza."},
                    "mecatronica": {"uso": "DCL de cada eslabón del robot para calcular torques.", "consecuencia_de_error": "Motores subdimensionados."},
                    "aeronautica": {"uso": "El DCL del avión (L, W, T, D) define las ecuaciones de vuelo.", "consecuencia_de_error": "Modelo de vuelo incorrecto."},
                    "electrica": {"uso": "Análisis de fuerzas electrostáticas sobre una carga.", "consecuencia_de_error": "Mal diseño de aisladores."}
                }
            },
            {
                "subtema_titulo": "6. Fuerzas de Fricción (Estática vs. Cinética)",
                "definicion": "Fricción Estática (fs): Fuerza variable que impide que se inicie el movimiento (fs ≤ μs*N). Fricción Cinética (fk): Fuerza constante que frena el deslizamiento (fk = μk*N). μs > μk (es más difícil arrancar que mantener).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Mover un mueble. Empujas suave y no se mueve (fricción estática iguala tu fuerza). Empujas fuerte, vence la estática y empieza a moverse. Ahora actúa la fricción cinética (más débil).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si empujas con 10N y el objeto NO se mueve, la fricción estática es...",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "0", "mayor a 10", "5"]
                    },
                    "similares": [
                        {"pregunta": "La fórmula de fricción cinética es fk = ... * Normal.", "respuesta_correcta": "uk", "opciones": ["uk", "us", "g", "m"]},
                        {"pregunta": "¿Cuál coeficiente es usualmente mayor? (estatico/cinetico)", "respuesta_correcta": "estatico", "opciones": ["estatico", "cinetico"]},
                        {"pregunta": "La fuerza de fricción depende del área de contacto. (falso en modelo simple)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "La fricción depende de la fuerza Normal. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si μk=0.5 y N=100N, ¿cuánto vale la fricción cinética?", "respuesta_correcta": "50", "opciones": ["50", "100", "200", "25"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Física de conducción en juegos. Diferencia entre 'agarre' (estática) y 'derrape' (cinética).", "consecuencia_de_error": "Autos que se sienten como si estuvieran en hielo o rieles."},
                    "quimica": {"uso": "Flujo de polvos y granulados. El ángulo de reposo depende de la fricción interna.", "consecuencia_de_error": "Silos que se atascan o derrumbes de material."},
                    "civil": {"uso": "Muros de contención. La fricción del suelo evita que el muro se deslice.", "consecuencia_de_error": "Muro que se desliza y colapsa."},
                    "mecanica": {"uso": "Embragues y frenos. Dependen 100% de la fricción. El ABS evita pasar de estática a cinética (bloqueo).", "consecuencia_de_error": "Frenos que no frenan o embragues que patinan."},
                    "mecatronica": {"uso": "Grippers (pinzas). Deben aplicar suficiente fuerza Normal para que la Fricción sostenga el objeto.", "consecuencia_de_error": "El robot tira los objetos al moverlos."},
                    "aeronautica": {"uso": "Frenado en pista y agarre de neumáticos en lluvia (aquaplaning pierde fricción).", "consecuencia_de_error": "Salida de pista al aterrizar."},
                    "electrica": {"uso": "Conectores. La fricción mantiene el enchufe conectado.", "consecuencia_de_error": "Cables que se desconectan solos."}
                }
            },
            {
                "subtema_titulo": "7. Tensión y Poleas",
                "definicion": "La 'Tensión' (T) es la fuerza transmitida por un cable o cuerda. Es la misma a lo largo de toda la cuerda (si es ideal). Las poleas cambian la dirección de la fuerza y pueden dar ventaja mecánica.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Máquina de Atwood (dos masas m1 y m2 colgadas de una polea). Tensión es la misma para ambas. T - m1g = m1a y m2g - T = m2a.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si cuelgas 10kg de una cuerda quieta (g=10), ¿cuál es la tensión?",
                        "respuesta_correcta": "100",
                        "opciones": ["100", "10", "0", "50"]
                    },
                    "similares": [
                        {"pregunta": "La tensión 'empuja' o 'jala'?", "respuesta_correcta": "jala", "opciones": ["jala", "empuja"]},
                        {"pregunta": "Una polea fija ideal cambia la magnitud de la fuerza. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "En una cuerda ideal sin masa, la tensión es uniforme. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Dos equipos tiran de una cuerda con 100N cada uno. ¿Tensión?", "respuesta_correcta": "100", "opciones": ["100", "200", "0", "50"]},
                        {"pregunta": "Grúa levanta carga acelerando. ¿Tensión > Peso? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de cuerdas, puentes colgantes o telas en videojuegos (sistemas masa-resorte).", "consecuencia_de_error": "Cuerdas que se comportan como resortes elásticos irreales."},
                    "quimica": {"uso": "Tensión superficial. Análogo a una membrana tensa en la superficie de un líquido.", "consecuencia_de_error": "Errores en capilaridad y formación de gotas."},
                    "civil": {"uso": "Puentes atirantados y colgantes. Todo el peso lo soportan los cables a tensión.", "consecuencia_de_error": "Rotura de cables y colapso del puente."},
                    "mecanica": {"uso": "Bandas y correas de transmisión. La diferencia de tensión mueve las poleas.", "consecuencia_de_error": "Bandas que patinan y no transmiten potencia."},
                    "mecatronica": {"uso": "Robots accionados por cables (tendones), como manos robóticas dexterosas.", "consecuencia_de_error": "Control impreciso de los dedos."},
                    "aeronautica": {"uso": "Cables de control de vuelo en aviones pequeños (timones).", "consecuencia_de_error": "Pérdida de control si el cable se destensa."},
                    "electrica": {"uso": "Tendido de cables de alta tensión. La tensión mecánica (T) debe equilibrarse para que no se rompan.", "consecuencia_de_error": "Cables caídos por viento o hielo."}
                }
            },
            {
                "subtema_titulo": "8. Planos Inclinados",
                "definicion": "Problema clásico. Se rota el sistema de coordenadas para que el eje X sea paralelo a la rampa. El Peso (mg) se descompone: Px = mg*sen(θ) (te jala hacia abajo) y Py = mg*cos(θ) (te pega a la rampa).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Bloque en rampa de 30°. Fuerza que lo hace bajar (sin fricción) = mg * sen(30°) = 0.5 * Peso. Normal = mg * cos(30°).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En una rampa, la componente del peso que causa el movimiento es mg por... (seno/coseno)",
                        "respuesta_correcta": "seno",
                        "opciones": ["seno", "coseno", "tangente", "ninguna"]
                    },
                    "similares": [
                        {"pregunta": "La Normal en un plano inclinado es igual al Peso total. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Si el ángulo es 0 (plano), el sen(0) es 0, ¿fuerza de bajada?", "respuesta_correcta": "0", "opciones": ["0", "peso", "1", "infinita"]},
                        {"pregunta": "Si el ángulo es 90 (caída), el sen(90) es 1, ¿fuerza de bajada?", "respuesta_correcta": "peso", "opciones": ["peso", "0", "1", "mitad"]},
                        {"pregunta": "Bloque de 10kg en rampa 30° (sen30=0.5, g=10). Fuerza bajada:", "respuesta_correcta": "50", "opciones": ["50", "100", "86", "25"]},
                        {"pregunta": "¿Qué fuerza combate a Px si el bloque está quieto?", "respuesta_correcta": "friccion", "opciones": ["friccion", "normal", "peso", "tension"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Detectar si un personaje puede caminar por una pendiente o se resbala.", "consecuencia_de_error": "Personajes subiendo montañas verticales caminando."},
                    "quimica": {"uso": "Diseño de tolvas y canaletas para el flujo de sólidos a granel.", "consecuencia_de_error": "Material que no fluye y atasca la producción."},
                    "civil": {"uso": "Estabilidad de taludes (tierra). Evitar derrumbes en carreteras de montaña.", "consecuencia_de_error": "Deslaves catastróficos."},
                    "mecanica": {"uso": "Tornillos. Un tornillo es básicamente un plano inclinado enrollado. Px es la fuerza que lo aprieta.", "consecuencia_de_error": "Tornillos que se aflojan solos por vibración."},
                    "mecatronica": {"uso": "Robots móviles subiendo rampas. Calcular si el motor tiene torque suficiente para vencer mg*sen(θ).", "consecuencia_de_error": "El robot se detiene a mitad de la rampa."},
                    "aeronautica": {"uso": "Análisis de fuerzas en ascenso/descenso. El peso tiene componente en el eje de empuje.", "consecuencia_de_error": "Cálculo erróneo de rendimiento en ascenso."},
                    "electrica": {"uso": "Bandejas portacables en inclinación. Asegurar los cables.", "consecuencia_de_error": "Cables que se deslizan y desconectan."}
                }
            },
            {
                "subtema_titulo": "9. Fuerza Centrípeta (Dinámica Circular)",
                "definicion": "Para girar, necesitas una fuerza que apunte AL CENTRO: la Fuerza Centrípeta (Fc). Fc = m * ac = m * (v²/r). NO es una fuerza nueva, es el rol que juega la tensión, fricción o gravedad.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Auto dando vuelta. La fricción de las llantas actúa como Fc. Si Fricción < m*v²/r, el auto derrapa (se sale por la tangente por inercia).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si duplicas la velocidad en una curva, la fuerza necesaria se multiplica por...",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "2", "8", "1"]
                    },
                    "similares": [
                        {"pregunta": "La fuerza centrípeta apunta hacia el... del círculo.", "respuesta_correcta": "centro", "opciones": ["centro", "fuera", "tangente", "atras"]},
                        {"pregunta": "La 'fuerza centrífuga' es una fuerza real en un marco inercial. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Un satélite orbita gracias a la fuerza de...", "respuesta_correcta": "gravedad", "opciones": ["gravedad", "magnetismo", "electrica", "friccion"]},
                        {"pregunta": "Si se rompe la cuerda al girar una piedra, sale volando hacia... (fuera/tangente)", "respuesta_correcta": "tangente", "opciones": ["tangente", "fuera", "centro", "atras"]},
                        {"pregunta": "Fc depende de la masa, radio y...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "tiempo", "altura", "temperatura"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Física de vehículos de carreras. Calcular agarre en curvas.", "consecuencia_de_error": "Juego de carreras injugable o irreal."},
                    "quimica": {"uso": "Ultracentrifugadoras. Generan miles de 'g' para separar ADN o proteínas.", "consecuencia_de_error": "Rotura del rotor si no está balanceado."},
                    "civil": {"uso": "Peralte en carreteras (inclinación). Usar la Normal para ayudar a la fricción a dar la vuelta.", "consecuencia_de_error": "Autos saliéndose de la carretera en curvas rápidas."},
                    "mecanica": {"uso": "Diseño de álabes de turbina. La fuerza centrípeta (tensión en la raíz) es gigantesca.", "consecuencia_de_error": "Álabe que se desprende y destruye el motor."},
                    "mecatronica": {"uso": "Giroscopios y volantes de reacción para orientar satélites.", "consecuencia_de_error": "Pérdida de control de actitud."},
                    "aeronautica": {"uso": "Virajes. El avión se inclina (bank) para que la Sustentación horizontal actúe como fuerza centrípeta.", "consecuencia_de_error": "Pérdida de altitud o viraje descoordinado."},
                    "electrica": {"uso": "Generadores. El bobinado del rotor sufre fuerzas centrípetas enormes.", "consecuencia_de_error": "Cortocircuitos por deformación de bobinas."}
                }
            }
        ]
    },

    "FIS-04": {
        "nombre_completo": "Trabajo, Energía y Potencia",
        "prerequisitos": ["FIS-03"],
        "quiz": [
            {
                "pregunta": "La energía no se crea ni se destruye, solo se...",
                "respuesta": "transforma",
                "opciones": ["transforma", "pierde", "crea", "almacena"]
            },
            {
                "pregunta": "¿En qué unidad del SI se mide el Trabajo y la Energía?",
                "respuesta": "joule",
                "opciones": ["joule", "watt", "newton", "pascal"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Definición de Trabajo Mecánico (W)",
                "definicion": "En física, 'Trabajo' no es cansancio, es transferencia de energía. Ocurre SOLO si una Fuerza mueve un objeto una Distancia. W = F * d * cos(θ). Si empujas una pared y no se mueve, d=0, el trabajo es CERO.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Empujas una caja con 50N por 10 metros en la misma dirección (θ=0°).\nW = 50 * 10 * cos(0°) = 500 Joules.\nSi cargas la caja y caminas horizontalmente (fuerza vertical, movimiento horizontal, θ=90°), W = 50 * 10 * 0 = 0 Joules.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si aplicas 20N para mover un objeto 5m en la misma dirección, ¿cuánto trabajo haces?",
                        "respuesta_correcta": "100",
                        "opciones": ["100", "4", "25", "0"]
                    },
                    "similares": [
                        {"pregunta": "Si empujas con 100N pero el objeto no se mueve, el trabajo es...", "respuesta_correcta": "0", "opciones": ["0", "100", "infinito", "10"]},
                        {"pregunta": "La unidad de Trabajo es el Newton-metro, también llamado...", "respuesta_correcta": "joule", "opciones": ["joule", "watt", "pascal", "volt"]},
                        {"pregunta": "Si la fuerza es perpendicular al movimiento (cos 90°), el trabajo es...", "respuesta_correcta": "0", "opciones": ["0", "1", "maximo", "negativo"]},
                        {"pregunta": "Levantas 10N a 2m de altura. Trabajo realizado:", "respuesta_correcta": "20", "opciones": ["20", "5", "12", "0"]},
                        {"pregunta": "El trabajo puede ser negativo (ej. fricción). (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de 'costo computacional' (Trabajo virtual). Aunque no es mecánico, la analogía de 'procesamiento por ciclo' se usa para medir eficiencia.", "consecuencia_de_error": "Algoritmos que consumen demasiada batería."},
                    "quimica": {"uso": "Trabajo de expansión de un gas (W = P * ΔV). El gas empuja el pistón al expandirse.", "consecuencia_de_error": "Imposible calcular la eficiencia de un motor de combustión."},
                    "civil": {"uso": "Cálculo de maquinaria. Cuánto trabajo cuesta mover X toneladas de tierra a Y altura.", "consecuencia_de_error": "Alquiler de grúas con capacidad insuficiente."},
                    "mecanica": {"uso": "Diseño de levas. Calcular el trabajo necesario para comprimir resortes de válvulas.", "consecuencia_de_error": "Pérdida de potencia del motor por resortes muy duros."},
                    "mecatronica": {"uso": "Selección de baterías. La batería almacena Energía (Joules) para hacer Trabajo mecánico.", "consecuencia_de_error": "El robot se queda sin batería a mitad de la tarea."},
                    "aeronautica": {"uso": "Trabajo realizado por el Arrastre (Drag). Es energía que el motor debe reponer quemando combustible.", "consecuencia_de_error": "Cálculo erróneo de alcance máximo del avión."},
                    "electrica": {"uso": "Definición de Voltaje. Trabajo por unidad de carga (Joules/Coulomb).", "consecuencia_de_error": "No entender qué es realmente el voltaje (presión eléctrica)."}
                }
            },
            {
                "subtema_titulo": "2. Energía Cinética (K)",
                "definicion": "Es la energía del MOVIMIENTO. K = ½ * m * v². Nota que depende de la velocidad AL CUADRADO. Un auto a doble velocidad tiene CUATRO veces más energía (y necesita 4 veces más distancia para frenar).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Auto de 1000kg a 20 m/s.\nK = 0.5 * 1000 * (20)² = 500 * 400 = 200,000 Joules (200 kJ).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si la velocidad se triplica, la energía cinética aumenta... veces.",
                        "respuesta_correcta": "9",
                        "opciones": ["9", "3", "6", "1.5"]
                    },
                    "similares": [
                        {"pregunta": "Objeto de 2kg a 3 m/s. K = 0.5 * 2 * 9 = ...", "respuesta_correcta": "9", "opciones": ["9", "6", "18", "3"]},
                        {"pregunta": "Un objeto en reposo tiene energía cinética igual a...", "respuesta_correcta": "0", "opciones": ["0", "1", "m", "g"]},
                        {"pregunta": "¿La energía cinética puede ser negativa? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Si m=4 y v=2, K=?", "respuesta_correcta": "8", "opciones": ["8", "16", "4", "2"]},
                        {"pregunta": "La energía cinética depende de la dirección del movimiento. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de daño en juegos. El daño suele basarse en K (v²), no en momento (v).", "consecuencia_de_error": "Choques rápidos que no hacen suficiente daño."},
                    "quimica": {"uso": "Teoría de colisiones. Las moléculas solo reaccionan si chocan con suficiente Energía Cinética (Energía de Activación).", "consecuencia_de_error": "La reacción química no ocurre."},
                    "civil": {"uso": "Diseño de barreras de contención. Deben disipar la K de un camión a toda velocidad.", "consecuencia_de_error": "Barreras que se rompen y no detienen el vehículo."},
                    "mecanica": {"uso": "Volantes de inercia (Flywheels). Almacenan K rotacional. K = ½ I ω².", "consecuencia_de_error": "Explosión del volante por exceso de velocidad (fuerza centrífuga)."},
                    "mecatronica": {"uso": "Seguridad en robots colaborativos (Cobots). Se limita la velocidad para que la K en un impacto accidental no hiera al humano.", "consecuencia_de_error": "Lesiones a operarios humanos."},
                    "aeronautica": {"uso": "Energía de frenado. Los frenos de carbono deben absorber la inmensa K del aterrizaje y convertirla en calor.", "consecuencia_de_error": "Frenos incendiados o avión que no para."},
                    "electrica": {"uso": "Generación eólica. La K del viento mueve las aspas. La potencia depende del cubo de la velocidad del viento.", "consecuencia_de_error": "Mala estimación de producción energética."}
                }
            },
            {
                "subtema_titulo": "3. Energía Potencial Gravitacional (U)",
                "definicion": "Energía ALMACENADA por la altura. U = m * g * h. Es el trabajo que la gravedad 'puede' hacer si dejas caer el objeto.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Elevas un bloque de 10kg a 5m de altura.\nU = 10 * 9.8 * 5 = 490 Joules. (Esta energía se liberará si cae).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un bloque de 5kg está a 2m de altura (g=10). ¿U?",
                        "respuesta_correcta": "100",
                        "opciones": ["100", "10", "25", "50"]
                    },
                    "similares": [
                        {"pregunta": "Si bajas el objeto al suelo (h=0), su energía potencial es...", "respuesta_correcta": "0", "opciones": ["0", "100", "m", "g"]},
                        {"pregunta": "Si duplicas la altura, la energía potencial se...", "respuesta_correcta": "duplica", "opciones": ["duplica", "cuadruplica", "triplica", "mantiene"]},
                        {"pregunta": "Un objeto en el suelo tiene U=0. Si cavas un hoyo, su U será... (positiva/negativa)", "respuesta_correcta": "negativa", "opciones": ["negativa", "positiva"]},
                        {"pregunta": "La energía potencial depende de la masa. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Masa 1kg a 10m (g=9.8). U=?", "respuesta_correcta": "98", "opciones": ["98", "10", "1", "9.8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Juegos de plataformas. Calcular daño por caída basándose en la altura (U convertida en K).", "consecuencia_de_error": "Caídas desde el espacio que no matan al jugador."},
                    "quimica": {"uso": "Analogía con estados de oxidación. Electrones en niveles altos tienen más 'potencial' para reaccionar.", "consecuencia_de_error": "Mal entendimiento de la reactividad."},
                    "civil": {"uso": "Hidroeléctricas. La energía eléctrica generada depende de la altura (h) de la presa (U del agua).", "consecuencia_de_error": "Presa que no genera la potencia esperada."},
                    "mecanica": {"uso": "Montacargas y grúas. Dimensionar motores para levantar cargas (aumentar U).", "consecuencia_de_error": "El motor no puede levantar la carga."},
                    "mecatronica": {"uso": "Brazos robóticos. Mantener un brazo estirado consume energía para combatir la gravedad (o requiere contrapesos).", "consecuencia_de_error": "Motores sobrecalentados por sostener peso estático."},
                    "aeronautica": {"uso": "Gestión de energía. Un avión puede cambiar altura (U) por velocidad (K) picando.", "consecuencia_de_error": "Piloto que no entiende que la altura es 'energía en el banco'."},
                    "electrica": {"uso": "Bombeo hidráulico. Se usa electricidad sobrante para subir agua a un tanque (batería gravitacional) y recuperarla luego.", "consecuencia_de_error": "Ineficiencia en el almacenamiento de energía."}
                }
            },
            {
                "subtema_titulo": "4. Energía Potencial Elástica (Resortes)",
                "definicion": "Energía almacenada en un resorte comprimido o estirado. U_s = ½ * k * x². (k = constante del resorte, x = deformación).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Resorte con k=100 N/m comprimido 0.2m.\nU_s = 0.5 * 100 * (0.2)² = 50 * 0.04 = 2 Joules.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si estiras un resorte el doble (2x), la energía almacenada se multiplica por...",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "2", "8", "16"]
                    },
                    "similares": [
                        {"pregunta": "La 'k' representa la ... del resorte.", "respuesta_correcta": "rigidez", "opciones": ["rigidez", "longitud", "masa", "friccion"]},
                        {"pregunta": "En un resorte sin deformar (x=0), la energía es...", "respuesta_correcta": "0", "opciones": ["0", "k", "1", "maxima"]},
                        {"pregunta": "k=10, x=2. U = 0.5 * 10 * 4 = ...", "respuesta_correcta": "20", "opciones": ["20", "10", "40", "5"]},
                        {"pregunta": "La energía elástica siempre es positiva. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Se usa en relojes de cuerda para almacenar energía. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Simulación de telas y cabello ('soft body physics'). Se modelan como mallas de resortes.", "consecuencia_de_error": "Ropa que atraviesa el cuerpo o se comporta como metal."},
                    "quimica": {"uso": "Espectroscopia IR. Los enlaces químicos vibran como resortes. La 'k' es la fuerza del enlace.", "consecuencia_de_error": "Identificación incorrecta de grupos funcionales."},
                    "civil": {"uso": "Diseño sismorresistente. Edificios sobre aisladores de base que actúan como resortes.", "consecuencia_de_error": "Edificio rígido que se rompe en lugar de oscilar."},
                    "mecanica": {"uso": "Suspensión de vehículos. Absorber la energía del bache (K) y almacenarla en el resorte (U_s).", "consecuencia_de_error": "Auto inestable o incómodo."},
                    "mecatronica": {"uso": "Robots flexibles (Soft Robotics) y actuadores elásticos en serie (SEA) para interactuar seguros con humanos.", "consecuencia_de_error": "Robot rígido que lastima al chocar."},
                    "aeronautica": {"uso": "Tren de aterrizaje. Amortiguadores oleoneumáticos que actúan como resortes no lineales.", "consecuencia_de_error": "Rebote del avión al aterrizar."},
                    "electrica": {"uso": "Micro-electromecánica (MEMS). Acelerómetros que usan resortes microscópicos de silicio.", "consecuencia_de_error": "El sensor no detecta el movimiento."}
                }
            },
            {
                "subtema_titulo": "5. Conservación de la Energía Mecánica",
                "definicion": "Si no hay fricción, la Energía Mecánica Total (E = K + U) se mantiene constante. La energía no se pierde, se transforma de altura (U) a velocidad (K) y viceversa. ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Montaña rusa. Arriba (h=20m, v=0), E = mgh. Abajo (h=0, v=?), E = ½mv². Iguala mgh = ½mv² -> v = √(2gh) = √(2*9.8*20) ≈ 19.8 m/s.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Dejas caer una bola. A medida que baja, pierde Energía Potencial y gana Energía...",
                        "respuesta_correcta": "cinetica",
                        "opciones": ["cinetica", "electrica", "termica", "elastica"]
                    },
                    "similares": [
                        {"pregunta": "En un péndulo, la velocidad es máxima en el punto más... (alto/bajo)", "respuesta_correcta": "bajo", "opciones": ["bajo", "alto", "medio", "extremo"]},
                        {"pregunta": "Si no hay fricción, la energía total al inicio es ... a la del final.", "respuesta_correcta": "igual", "opciones": ["igual", "menor", "mayor", "cero"]},
                        {"pregunta": "Para que un objeto suba más alto, necesita más velocidad inicial. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "v = raiz(2gh) es la velocidad de caída libre desde altura h. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si hay fricción, la energía mecánica se conserva. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Optimización de física en juegos. Usar conservación es más barato (computacionalmente) que integrar F=ma.", "consecuencia_de_error": "Juego lento o inestable."},
                    "quimica": {"uso": "Primera Ley de Termodinámica. La energía interna se conserva en reacciones adiabáticas.", "consecuencia_de_error": "Balances de energía erróneos en reactores."},
                    "civil": {"uso": "Flujo de agua en tuberías (Bernoulli es conservación de energía). Presión + K + U = cte.", "consecuencia_de_error": "Tuberías que estallan o grifos sin presión."},
                    "mecanica": {"uso": "Diseño de montañas rusas. Asegurar que el carro tenga energía para completar el loop.", "consecuencia_de_error": "El carro se queda atascado a mitad del recorrido."},
                    "mecatronica": {"uso": "Robots saltadores. Almacenan energía en resorte y la liberan de golpe (K).", "consecuencia_de_error": "El robot no salta la altura requerida."},
                    "aeronautica": {"uso": "Maniobras de combate. Intercambiar altura por velocidad (Zoom climb o Dive).", "consecuencia_de_error": "Quedarse sin velocidad (energía) en un combate."},
                    "electrica": {"uso": "Circuitos LC (Osciladores). La energía oscila entre campo eléctrico (Capacitor) y magnético (Inductor) sin perderse (idealmente).", "consecuencia_de_error": "Oscilador que se apaga."}
                }
            },
            {
                "subtema_titulo": "6. Teorema Trabajo-Energía",
                "definicion": "El Trabajo Neto realizado sobre un objeto es igual a su CAMBIO de Energía Cinética. W_neto = ΔK = Kf - Ki. Es útil cuando hay fuerzas variables o no conocemos el tiempo.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un auto de 1000kg frena de 20m/s a 0. ¿Trabajo de los frenos?\nW = Kf - Ki = 0 - ½(1000)(20)² = -200,000 J. (Trabajo negativo porque los frenos quitan energía).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si el trabajo neto es positivo, la velocidad del objeto... (aumenta/disminuye)",
                        "respuesta_correcta": "aumenta",
                        "opciones": ["aumenta", "disminuye", "se mantiene", "se anula"]
                    },
                    "similares": [
                        {"pregunta": "Si W_neto = 0, la velocidad... (cambia/sigue igual)", "respuesta_correcta": "sigue igual", "opciones": ["sigue igual", "aumenta", "disminuye", "oscila"]},
                        {"pregunta": "Para detener un objeto, debes hacer trabajo... (positivo/negativo)", "respuesta_correcta": "negativo", "opciones": ["negativo", "positivo", "nulo", "infinito"]},
                        {"pregunta": "El trabajo de la fricción siempre reduce la energía cinética. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Disparar una bala: Los gases hacen trabajo positivo sobre la bala. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Trabajo = Cambio de K. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Calcular distancia de frenado en simuladores de conducción.", "consecuencia_de_error": "Frenado irrealista."},
                    "quimica": {"uso": "Trabajo eléctrico en electrólisis para causar una reacción (cambiar la energía libre).", "consecuencia_de_error": "Voltaje insuficiente para la reacción."},
                    "civil": {"uso": "Análisis de impacto. El trabajo de deformación del parachoques debe absorber la energía cinética del choque.", "consecuencia_de_error": "Diseño inseguro de barreras viales."},
                    "mecanica": {"uso": "Prensas hidráulicas y martillos de forja. El trabajo del martillo deforma la pieza.", "consecuencia_de_error": "Pieza no forjada correctamente."},
                    "mecatronica": {"uso": "Frenado regenerativo. El motor hace trabajo negativo, convierte K en electricidad.", "consecuencia_de_error": "Batería no se recarga al frenar."},
                    "aeronautica": {"uso": "Catapultas de portaaviones. Trabajo enorme en corta distancia para dar K al avión.", "consecuencia_de_error": "Avión cae al mar por falta de velocidad."},
                    "electrica": {"uso": "Aceleradores de partículas (Cern). Campos eléctricos hacen trabajo sobre protones para darles K.", "consecuencia_de_error": "Partículas sin energía para la colisión."}
                }
            },
            {
                "subtema_titulo": "7. Potencia (Rapidez del Trabajo)",
                "definicion": "No es lo mismo subir una montaña en 1 hora que en 10 horas. El Trabajo es el mismo, pero la POTENCIA es diferente. P = Trabajo / Tiempo. Se mide en Watts (W) o Caballos de Fuerza (HP). 1 HP ≈ 746 W.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Grúa levanta 1000N a 10m en 5s.\nTrabajo W = 1000 * 10 = 10,000 J.\nPotencia P = 10,000 J / 5 s = 2,000 Watts (2 kW).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un motor de 100W hace 100J de trabajo en... segundos.",
                        "respuesta_correcta": "1",
                        "opciones": ["1", "10", "100", "0.1"]
                    },
                    "similares": [
                        {"pregunta": "1 Kilowatt son ... Watts.", "respuesta_correcta": "1000", "opciones": ["1000", "100", "10", "10000"]},
                        {"pregunta": "Si haces el mismo trabajo en menos tiempo, tu potencia es... (mayor/menor)", "respuesta_correcta": "mayor", "opciones": ["mayor", "menor", "igual", "cero"]},
                        {"pregunta": "Fórmula de potencia mecánica: P = Fuerza * ...", "respuesta_correcta": "velocidad", "opciones": ["velocidad", "tiempo", "masa", "distancia"]},
                        {"pregunta": "¿Qué consume más potencia: levantar lento o rápido?", "respuesta_correcta": "rapido", "opciones": ["rapido", "lento", "igual", "ninguno"]},
                        {"pregunta": "Unidad de potencia en el sistema inglés.", "respuesta_correcta": "hp", "opciones": ["hp", "btu", "joule", "newton"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Overclocking. Aumentar la velocidad (tiempo menor) aumenta el consumo de potencia (Watts) y calor.", "consecuencia_de_error": "CPU quemado."},
                    "quimica": {"uso": "Potencia de un reactor (calor por tiempo). Definir la capacidad de enfriamiento necesaria.", "consecuencia_de_error": "Reactor se sobrecalienta (Runaway)."},
                    "civil": {"uso": "Potencia de bombas de agua para subir agua a un rascacielos.", "consecuencia_de_error": "Agua no llega a los pisos altos en horas pico."},
                    "mecanica": {"uso": "Curvas de potencia de motores. Un auto necesita HP para mantener velocidad alta contra el viento.", "consecuencia_de_error": "Vehículo que no alcanza la velocidad máxima deseada."},
                    "mecatronica": {"uso": "Selección de servomotores. Un motor pequeño puede levantar mucho peso (con engranajes), pero muy lento (poca potencia).", "consecuencia_de_error": "Robot demasiado lento para la línea de producción."},
                    "aeronautica": {"uso": "Potencia al eje (Turboprop) vs Empuje (Jet).", "consecuencia_de_error": "Confusión en especificaciones de motores."},
                    "electrica": {"uso": "Facturación. Pagas por Energía (kWh), no por Potencia (kW), pero los cables se diseñan por Potencia.", "consecuencia_de_error": "Fusibles fundidos por exceso de carga."}
                }
            },
            {
                "subtema_titulo": "8. Eficiencia (Rendimiento)",
                "definicion": "Nada es perfecto. La Eficiencia (η) es la relación entre lo que obtienes y lo que pagas. η = (Potencia Salida / Potencia Entrada) * 100%. Siempre es menor al 100% debido a pérdidas (calor, fricción).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un motor eléctrico consume 1000W de electricidad (Entrada) y entrega 800W de fuerza mecánica (Salida).\nEficiencia = (800 / 1000) * 100% = 80%. (20% se perdió como calor).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un foco consume 100W y da 5W de luz, ¿cuál es su eficiencia?",
                        "respuesta_correcta": "5%",
                        "opciones": ["5%", "95%", "100%", "20%"]
                    },
                    "similares": [
                        {"pregunta": "¿Es posible una máquina con 110% de eficiencia? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "La energía 'perdida' en una máquina usualmente se convierte en...", "respuesta_correcta": "calor", "opciones": ["calor", "luz", "ruido", "nada"]},
                        {"pregunta": "Entrada=50, Salida=40. Eficiencia = ... %", "respuesta_correcta": "80", "opciones": ["80", "90", "20", "10"]},
                        {"pregunta": "Eficiencia ideal (teórica) máxima.", "respuesta_correcta": "100%", "opciones": ["100%", "infinity", "0%", "50%"]},
                        {"pregunta": "Un motor eficiente se calienta... (mas/menos)", "respuesta_correcta": "menos", "opciones": ["menos", "mas", "igual", "mucho"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Eficiencia de algoritmos (Big O). Un algoritmo ineficiente desperdicia ciclos de CPU.", "consecuencia_de_error": "Aplicación lenta que drena la batería del celular."},
                    "quimica": {"uso": "Rendimiento de reacción. Cuánto producto obtuviste vs el teórico.", "consecuencia_de_error": "Procesos industriales no rentables."},
                    "civil": {"uso": "Eficiencia energética de edificios (aislamiento térmico, luz natural).", "consecuencia_de_error": "Edificios caros de mantener (climatización)."},
                    "mecanica": {"uso": "Motores térmicos. Un motor de gasolina tiene eficiencia ~30%. El resto es calor desperdiciado.", "consecuencia_de_error": "Necesidad de radiadores gigantes."},
                    "mecatronica": {"uso": "Transmisiones. Los engranajes pierden potencia. Si el motor da 100W, a la rueda llegan 90W.", "consecuencia_de_error": "Subdimensionamiento del motor al ignorar pérdidas."},
                    "aeronautica": {"uso": "Relación de planeo (Lift/Drag). Mide la eficiencia aerodinámica.", "consecuencia_de_error": "Avión que consume demasiado combustible."},
                    "electrica": {"uso": "Transformadores y fuentes conmutadas. Buscar eficiencias >90% para no desperdiciar energía.", "consecuencia_de_error": "Equipos electrónicos que se sobrecalientan."}
                }
            }
        ]
    },

    "FIS-05": {
        "nombre_completo": "Electricidad Básica: Circuitos y Ley de Ohm",
        "prerequisitos": ["FIS-04"],
        "quiz": [
            {
                "pregunta": "La unidad de Potencia eléctrica es el...",
                "respuesta": "watt",
                "opciones": ["watt", "joule", "volt", "ampere"]
            },
            {
                "pregunta": "En un circuito en serie, si se funde un foco, los demás... (se apagan/siguen igual)",
                "respuesta": "se apagan",
                "opciones": ["se apagan", "siguen igual", "brillan mas", "parpadean"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Carga Eléctrica y Ley de Coulomb",
                "definicion": "La materia tiene una propiedad llamada 'Carga' (q). Cargas iguales se repelen, opuestas se atraen. La Ley de Coulomb calcula esa fuerza: F = k * (q1*q2) / r². Es análoga a la gravedad, pero muchísimo más fuerte.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Dos cargas se atraen con 10N. Si reduces la distancia a la mitad (r/2), la fuerza se cuadruplica (ley del cuadrado inverso).\nNueva Fuerza = 10 * 4 = 40N.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si duplicas la distancia entre dos cargas, la fuerza se reduce a... (1/2, 1/4, 1/8)",
                        "respuesta_correcta": "1/4",
                        "opciones": ["1/4", "1/2", "1/8", "4"]
                    },
                    "similares": [
                        {"pregunta": "La unidad de carga eléctrica es el...", "respuesta_correcta": "coulomb", "opciones": ["coulomb", "volt", "ampere", "ohm"]},
                        {"pregunta": "Protones y Electrones se... (atraen/repelen)", "respuesta_correcta": "atraen", "opciones": ["atraen", "repelen", "anulan", "ignoran"]},
                        {"pregunta": "Dos electrones juntos se... (atraen/repelen)", "respuesta_correcta": "repelen", "opciones": ["repelen", "atraen", "fusionan", "orbitan"]},
                        {"pregunta": "La fuerza eléctrica depende de la distancia al cuadrado. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si q1 se duplica, la fuerza se...", "respuesta_correcta": "duplica", "opciones": ["duplica", "cuadruplica", "reduce", "mantiene"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Discos duros y memoria Flash. Almacenan información atrapando cargas (electrones) en celdas microscópicas.", "consecuencia_de_error": "Pérdida de datos o corrupción de memoria."},
                    "quimica": {"uso": "Enlaces iónicos. La fuerza que mantiene unido al NaCl es puramente atracción de Coulomb (Na+ y Cl-).", "consecuencia_de_error": "Predicción errónea de puntos de fusión en sales."},
                    "civil": {"uso": "Precipitadores electrostáticos en chimeneas industriales para atrapar polvo y reducir contaminación.", "consecuencia_de_error": "Emisión de partículas tóxicas al ambiente."},
                    "mecanica": {"uso": "Pintura electrostática (Powder coating). Se carga la pintura y se conecta la pieza a tierra para una adherencia perfecta.", "consecuencia_de_error": "Acabado de pintura irregular y desperdicio de material."},
                    "mecatronica": {"uso": "Impresoras láser y fotocopiadoras. Usan cargas estáticas para adherir el tóner al papel.", "consecuencia_de_error": "Impresiones manchadas o en blanco."},
                    "aeronautica": {"uso": "Descargadores estáticos en las alas. Disipan la carga acumulada por fricción con el aire para no interferir con la radio.", "consecuencia_de_error": "Pérdida de comunicaciones por estática."},
                    "electrica": {"uso": "Diseño de aisladores en líneas de alta tensión. Evitar que la fuerza eléctrica 'rompa' el aire (arco eléctrico).", "consecuencia_de_error": "Cortocircuitos masivos y apagones."}
                }
            },
            {
                "subtema_titulo": "2. Voltaje, Corriente y Resistencia",
                "definicion": "La tríada sagrada:\n- Voltaje (V): Presión o empuje (Volts).\n- Corriente (I): Flujo de electrones (Amperes).\n- Resistencia (R): Oposición al flujo (Ohms).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Analogía del agua: Voltaje es la altura del tanque (presión). Corriente es el caudal de agua (litros/seg). Resistencia es qué tan delgada es la tubería. ",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Lo que mata no es el voltaje, es la... (corriente/resistencia)",
                        "respuesta_correcta": "corriente",
                        "opciones": ["corriente", "resistencia", "potencia", "frecuencia"]
                    },
                    "similares": [
                        {"pregunta": "La unidad de resistencia es el...", "respuesta_correcta": "ohm", "opciones": ["ohm", "volt", "ampere", "watt"]},
                        {"pregunta": "Para medir corriente, el multímetro se conecta en... (serie/paralelo)", "respuesta_correcta": "serie", "opciones": ["serie", "paralelo", "mixto", "directo"]},
                        {"pregunta": "Para medir voltaje, el multímetro se conecta en... (serie/paralelo)", "respuesta_correcta": "paralelo", "opciones": ["paralelo", "serie", "abierto", "cerrado"]},
                        {"pregunta": "Un material con resistencia casi cero se llama...", "respuesta_correcta": "conductor", "opciones": ["conductor", "aislante", "semiconductor", "resistor"]},
                        {"pregunta": "Un material con resistencia infinita se llama...", "respuesta_correcta": "aislante", "opciones": ["aislante", "conductor", "metal", "cable"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Niveles lógicos. 5V es un '1', 0V es un '0'. El ruido eléctrico puede confundirlos.", "consecuencia_de_error": "Errores de bits en transmisión de datos."},
                    "quimica": {"uso": "Potencial Redox. El voltaje de una celda indica la tendencia de una reacción química a ocurrir.", "consecuencia_de_error": "Baterías que no entregan el voltaje nominal."},
                    "civil": {"uso": "Corrosión galvánica. Diferencia de voltaje entre dos metales en contacto causa corrosión acelerada.", "consecuencia_de_error": "Tuberías o estructuras que se corroen en meses."},
                    "mecanica": {"uso": "Sensores de presión (piezorresistivos). La presión cambia la resistencia, lo que cambia el voltaje de salida.", "consecuencia_de_error": "Lecturas de presión erróneas en un motor."},
                    "mecatronica": {"uso": "PWM (Pulse Width Modulation). Controlar motores encendiendo y apagando el voltaje muy rápido.", "consecuencia_de_error": "Control de velocidad del robot inestable."},
                    "aeronautica": {"uso": "Sistemas 'Fly-by-wire'. Los movimientos del piloto son señales de voltaje enviadas a computadoras.", "consecuencia_de_error": "Fallo catastrófico si los cables pierden aislamiento."},
                    "electrica": {"uso": "Generación y Transporte. Se eleva el voltaje para bajar la corriente y reducir las pérdidas en los cables.", "consecuencia_de_error": "Pérdida de energía masiva en la red eléctrica."}
                }
            },
            {
                "subtema_titulo": "3. La Ley de Ohm (V = IR)",
                "definicion": "La ecuación más importante de la electricidad. Relaciona las tres magnitudes. Voltaje = Corriente * Resistencia. Si subes el voltaje, sube la corriente. Si subes la resistencia, baja la corriente.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Tienes una batería de 9V y un foco de 3 Ohms. ¿Corriente?\nI = V / R = 9V / 3Ω = 3 Amperes.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si V=10V y R=5Ω, ¿cuánta corriente fluye?",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "50", "0.5", "5"]
                    },
                    "similares": [
                        {"pregunta": "Si quieres bajar la corriente a la mitad manteniendo V, debes ... la resistencia.", "respuesta_correcta": "duplicar", "opciones": ["duplicar", "reducir", "mantener", "eliminar"]},
                        {"pregunta": "V=IR. Si I=2A y R=10Ω, V=...", "respuesta_correcta": "20", "opciones": ["20", "5", "0.2", "12"]},
                        {"pregunta": "I = V/R. Si R tiende a 0 (cortocircuito), I tiende a...", "respuesta_correcta": "infinito", "opciones": ["infinito", "cero", "uno", "constante"]},
                        {"pregunta": "Gráfica V vs I. La pendiente representa la...", "respuesta_correcta": "resistencia", "opciones": ["resistencia", "potencia", "carga", "energia"]},
                        {"pregunta": "Calcula R si V=12 y I=4.", "respuesta_correcta": "3", "opciones": ["3", "48", "0.33", "8"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cálculo de resistencias para LEDs de estado en un router o PC.", "consecuencia_de_error": "LEDs quemados o muy tenues."},
                    "quimica": {"uso": "Conductimetría. Medir la resistencia de una solución para saber la concentración de iones (sales).", "consecuencia_de_error": "Análisis de calidad del agua incorrecto."},
                    "civil": {"uso": "Suelo. Medir la resistividad del suelo para diseñar la puesta a tierra de un edificio.", "consecuencia_de_error": "Sistema de tierra ineficaz, riesgo de electrocución."},
                    "mecanica": {"uso": "Bujías de precalentamiento en motores diésel. Son resistencias puras que siguen la ley de Ohm.", "consecuencia_de_error": "Motor diésel que no arranca en frío."},
                    "mecatronica": {"uso": "Divisores de voltaje. Usar dos resistencias para bajar 5V a 3.3V para un sensor.", "consecuencia_de_error": "Quemar un sensor de 3.3V conectándolo a 5V."},
                    "aeronautica": {"uso": "Calefacción de tubos Pitot. Resistencias que evitan que se congelen los sensores de velocidad.", "consecuencia_de_error": "Indicación de velocidad falsa y accidente (ej. AF447)."},
                    "electrica": {"uso": "Cortocircuitos. Si R es muy baja, I sube enormemente, disparando los 'breakers' (fusibles).", "consecuencia_de_error": "Incendio eléctrico si la protección no actúa."}
                }
            },
            {
                "subtema_titulo": "4. Potencia Eléctrica (Ley de Joule)",
                "definicion": "La Potencia (P) es la rapidez con la que se consume energía. P = V * I. Se mide en Watts. También P = I²R (importante para calor). La electricidad se convierte en calor, luz o movimiento.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Una plancha consume 10A a 120V.\nP = 120V * 10A = 1200 Watts (1.2 kW). Esta energía se disipa como calor.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un dispositivo de 10V consume 2A. ¿Potencia en Watts?",
                        "respuesta_correcta": "20",
                        "opciones": ["20", "5", "12", "0.2"]
                    },
                    "similares": [
                        {"pregunta": "Si duplicas la corriente en un cable, el calor generado (P=I²R) se multiplica por...", "respuesta_correcta": "4", "opciones": ["4", "2", "8", "16"]},
                        {"pregunta": "1 Caballo de Fuerza (HP) equivale aprox a ... Watts.", "respuesta_correcta": "746", "opciones": ["746", "1000", "500", "100"]},
                        {"pregunta": "La compañía eléctrica te cobra por... (Potencia/Energía)", "respuesta_correcta": "energia", "opciones": ["energia", "potencia", "corriente", "voltaje"]},
                        {"pregunta": "Un foco de 100W brilla más que uno de 60W. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Calcula I si P=50W y V=10V.", "respuesta_correcta": "5", "opciones": ["5", "500", "0.2", "50"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Diseño de fuentes de poder (PSU). Sumar los Watts de CPU + GPU + Discos.", "consecuencia_de_error": "La PC se apaga cuando juegas (pico de potencia)."},
                    "quimica": {"uso": "Electrólisis industrial. El costo de producir Aluminio o Hidrógeno depende de los kWh consumidos.", "consecuencia_de_error": "Proceso no rentable económicamente."},
                    "civil": {"uso": "Instalaciones eléctricas residenciales. Calcular la carga total (Watts) para pedir el servicio a la compañía.", "consecuencia_de_error": "Sobrecarga del transformador del barrio."},
                    "mecanica": {"uso": "Motores eléctricos. La potencia mecánica (HP) sale de la potencia eléctrica (VI) por la eficiencia.", "consecuencia_de_error": "Motor que no puede mover la carga."},
                    "mecatronica": {"uso": "Drivers de motores (Puente H). Deben soportar la potencia y disipar el calor generado.", "consecuencia_de_error": "Driver quemado por sobrecalentamiento."},
                    "aeronautica": {"uso": "Generadores del avión. Deben suministrar potencia a todo: radares, luces, cafeteras.", "consecuencia_de_error": "Desconexión de sistemas no esenciales en vuelo (load shedding)."},
                    "electrica": {"uso": "Líneas de transmisión. Se usa alto voltaje para bajar la corriente y reducir las pérdidas por calor (I²R).", "consecuencia_de_error": "Pérdida de energía masiva en la red eléctrica."}
                }
            },
            {
                "subtema_titulo": "5. Circuitos en Serie",
                "definicion": "Componentes conectados uno tras otro, como una cadena. Reglas: 1. La Corriente es la MISMA en todos. 2. El Voltaje se reparte (suma de voltajes = total). 3. Resistencia Total = R1 + R2.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Dos resistencias R1=10Ω y R2=10Ω en serie a 20V.\nR_total = 20Ω.\nCorriente Total = 20V / 20Ω = 1A.\nVoltaje en R1 = 1A * 10Ω = 10V. (El voltaje se partió a la mitad).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si quitas un foco de una serie navideña antigua, ¿qué pasa con los demás?",
                        "respuesta_correcta": "se apagan",
                        "opciones": ["se apagan", "brillan mas", "siguen igual", "parpadean"]
                    },
                    "similares": [
                        {"pregunta": "En serie, la resistencia total siempre es ... que cualquier resistencia individual.", "respuesta_correcta": "mayor", "opciones": ["mayor", "menor", "igual", "mitad"]},
                        {"pregunta": "R1=5, R2=5 en serie. Rt=?", "respuesta_correcta": "10", "opciones": ["10", "2.5", "5", "25"]},
                        {"pregunta": "En un circuito serie, el voltaje es constante en todos los puntos. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "En un circuito serie, la corriente es constante. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Tres baterías de 1.5V en serie dan... V.", "respuesta_correcta": "4.5", "opciones": ["4.5", "1.5", "3", "6"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Baterías de laptops. Celdas en serie para sumar voltaje (ej. 3.7V + 3.7V + ...).", "consecuencia_de_error": "Si una celda falla, toda la batería muere."},
                    "quimica": {"uso": "Celdas electrolíticas en serie para producción masiva (ej. proceso Cloro-Sosa).", "consecuencia_de_error": "Si se bloquea una celda, se detiene toda la línea."},
                    "civil": {"uso": "Sensores de seguridad en serie (interruptores de límite). Si cualquiera se activa (abre), la máquina para.", "consecuencia_de_error": "Lógica de seguridad fallida (seguro positivo)."},
                    "mecanica": {"uso": "Fusibles. Se conectan en serie con el equipo para protegerlo. Si el fusible se abre, la corriente para.", "consecuencia_de_error": "Si el fusible se conecta en paralelo, no protege nada."},
                    "mecatronica": {"uso": "Divisor de Voltaje (sensor de luz LDR). Una resistencia fija y una variable en serie.", "consecuencia_de_error": "Lectura no lineal o saturada del sensor."},
                    "aeronautica": {"uso": "Luces de pista. A menudo conectadas en serie con transformadores de aislamiento para mantener brillo uniforme.", "consecuencia_de_error": "Falla de iluminación de pista."},
                    "electrica": {"uso": "Amperímetros. Se deben conectar en serie para medir la corriente que pasa 'a través' de ellos.", "consecuencia_de_error": "Conectar un amperímetro en paralelo causa un cortocircuito inmediato y funde el fusible del metro."}
                }
            },
            {
                "subtema_titulo": "6. Circuitos en Paralelo",
                "definicion": "Componentes conectados a los mismos dos puntos (como peldaños de una escalera). Reglas: 1. El Voltaje es el MISMO en todos. 2. La Corriente se reparte. 3. 1/Rt = 1/R1 + 1/R2. (La Rt disminuye).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Tu casa. Todos los enchufes están a 120V (paralelo). Si conectas la TV (1A) y el Microondas (10A), la corriente total suma 11A, pero ambos reciben 120V.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En tu casa, si apagas la luz de la sala, la de la cocina sigue encendida. Están en...",
                        "respuesta_correcta": "paralelo",
                        "opciones": ["paralelo", "serie", "mixto", "cortocircuito"]
                    },
                    "similares": [
                        {"pregunta": "En paralelo, el voltaje en cada rama es...", "respuesta_correcta": "igual", "opciones": ["igual", "diferente", "cero", "variable"]},
                        {"pregunta": "Dos resistencias de 10Ω en paralelo dan una total de... Ω.", "respuesta_correcta": "5", "opciones": ["5", "20", "10", "1"]},
                        {"pregunta": "En paralelo, la resistencia total es ... que la resistencia más pequeña.", "respuesta_correcta": "menor", "opciones": ["menor", "mayor", "igual", "doble"]},
                        {"pregunta": "La corriente total es la suma de las corrientes de rama. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Conectar baterías en paralelo aumenta la... (voltaje/capacidad)", "respuesta_correcta": "capacidad", "opciones": ["capacidad", "voltaje", "resistencia", "frecuencia"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesadores multinúcleo. Trabajan en paralelo para aumentar el rendimiento total.", "consecuencia_de_error": "Cuellos de botella si el software no está paralelizado."},
                    "quimica": {"uso": "Reactores en paralelo. Si uno falla o entra en mantenimiento, los otros siguen produciendo.", "consecuencia_de_error": "Mayor complejidad de control de flujos."},
                    "civil": {"uso": "Sistema de tuberías de agua de una ciudad. Red en paralelo para mantener presión uniforme.", "consecuencia_de_error": "Pérdida de presión si todos abren el grifo al mismo tiempo."},
                    "mecanica": {"uso": "Resortes en paralelo (suspensión reforzada). Suman su rigidez (k_total = k1 + k2).", "consecuencia_de_error": "Suspensión demasiado dura."},
                    "mecatronica": {"uso": "Fuentes de poder redundantes. Dos fuentes conectadas en paralelo (con diodos) por si una falla.", "consecuencia_de_error": "Apagado del sistema crítico si falla la fuente única."},
                    "aeronautica": {"uso": "Sistemas hidráulicos redundantes (A, B, C). Si falla uno, los otros (en paralelo) mueven los alerones.", "consecuencia_de_error": "Pérdida de control del avión."},
                    "electrica": {"uso": "La Red Eléctrica. Toda la ciudad está en paralelo. Tú decides cuánta corriente jalar al encender cosas.", "consecuencia_de_error": "Sobrecarga de transformadores si todos consumen mucho a la vez."}
                }
            },
            {
                "subtema_titulo": "7. Resistividad y Calibre de Cables (AWG)",
                "definicion": "No todos los conductores son iguales. La Resistencia depende del material (Resistividad, ρ), la Longitud (L) y el Área (A). R = ρ * (L/A). Cables más largos -> Más R. Cables más gruesos -> Menos R.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ¿Por qué usamos cables gruesos para el arranque del auto?\nEl motor de arranque pide mucha corriente (100A). Si el cable es delgado (A pequeña), la Resistencia (R) es alta. Por Ohm (V=IR), se pierde mucho voltaje en el cable y el motor no gira.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si duplicas el largo de un cable, su resistencia se...",
                        "respuesta_correcta": "duplica",
                        "opciones": ["duplica", "reduce", "cuadruplica", "mantiene"]
                    },
                    "similares": [
                        {"pregunta": "Si duplicas el área (grosor) de un cable, su resistencia se...", "respuesta_correcta": "reduce", "opciones": ["reduce", "duplica", "mantiene", "anula"]},
                        {"pregunta": "¿Qué cable es más grueso: calibre 12 o calibre 22 AWG? (Regla inversa)", "respuesta_correcta": "12", "opciones": ["12", "22", "son iguales", "depende del material"]},
                        {"pregunta": "La resistividad (ρ) depende de... (forma/material)", "respuesta_correcta": "material", "opciones": ["material", "forma", "longitud", "area"]},
                        {"pregunta": "El cobre tiene menor resistividad que el hierro. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Un cable caliente tiene ... resistencia que uno frío. (mayor/menor)", "respuesta_correcta": "mayor", "opciones": ["mayor", "menor", "igual", "cero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cables Ethernet y USB. Tienen una longitud máxima (ej. 100m para Ethernet) debido a la resistencia del cable.", "consecuencia_de_error": "Pérdida de señal o datos si el cable es muy largo."},
                    "quimica": {"uso": "Sensores de conductividad. Miden la 'resistividad' del agua para saber qué tan pura es (menos iones = más resistiva).", "consecuencia_de_error": "Agua contaminada en procesos farmacéuticos."},
                    "civil": {"uso": "Corrosión en concreto armado. La resistividad del concreto afecta la velocidad de corrosión de la varilla.", "consecuencia_de_error": "Diagnóstico erróneo de la salud estructural."},
                    "mecanica": {"uso": "Galgas extensiométricas (Strain gauges). Al estirarse, el alambre se vuelve más largo y delgado -> R aumenta. Así se mide la deformación.", "consecuencia_de_error": "Medición incorrecta de esfuerzos en una prueba de carga."},
                    "mecatronica": {"uso": "Cableado de robots. Usar cables muy delgados para motores potentes causa caídas de voltaje y calentamiento.", "consecuencia_de_error": "Motores sin fuerza e incendios en el cableado."},
                    "aeronautica": {"uso": "Reducción de peso. Usar aluminio en lugar de cobre para cables grandes (menos denso, aunque más resistivo, se compensa con área).", "consecuencia_de_error": "Ahorro de peso crucial para la eficiencia del avión."},
                    "electrica": {"uso": "Líneas de transmisión. Se usan cables gruesos de aluminio con alma de acero. Cálculo preciso de R para pérdidas.", "consecuencia_de_error": "Sobrecalentamiento y 'sagging' (el cable se cuelga y toca árboles)."}
                }
            },
            {
                "subtema_titulo": "8. Leyes de Kirchhoff (Mallas y Nodos)",
                "definicion": "Para circuitos complejos (no solo serie/paralelo). \n1. Ley de Corrientes (Nodos): Todo lo que entra sale (ΣI_entra = ΣI_sale).\n2. Ley de Voltajes (Mallas): La suma de voltajes en un ciclo cerrado es cero (La energía que ganas en la batería la pierdes en las resistencias).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo (Nodo): Entran 5A por un cable. El cable se divide en dos. Si por uno van 3A, por el otro TIENEN que ir 2A. (Conservación de carga).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En un nodo, si entra 10A y salen 4A por un camino, ¿cuánto sale por el otro?",
                        "respuesta_correcta": "6",
                        "opciones": ["6", "4", "14", "10"]
                    },
                    "similares": [
                        {"pregunta": "La Ley de Voltajes de Kirchhoff se basa en la conservación de la... (carga/energia)", "respuesta_correcta": "energia", "opciones": ["energia", "carga", "masa", "momento"]},
                        {"pregunta": "La Ley de Corrientes de Kirchhoff se basa en la conservación de la... (carga/energia)", "respuesta_correcta": "carga", "opciones": ["carga", "energia", "voltaje", "potencia"]},
                        {"pregunta": "En una malla cerrada, la suma algebraica de voltajes es...", "respuesta_correcta": "0", "opciones": ["0", "1", "infinita", "variable"]},
                        {"pregunta": "Si subes 12V en la batería y caes 5V en R1, ¿cuánto caes en R2 para cerrar el ciclo?", "respuesta_correcta": "7", "opciones": ["7", "17", "5", "12"]},
                        {"pregunta": "Kirchhoff se usa cuando Ohm simple no basta. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Análisis de redes complejas de computadoras (teoría de grafos). Flujo de datos en nodos (routers).", "consecuencia_de_error": "Congestión de red y pérdida de paquetes."},
                    "quimica": {"uso": "Balance de masa en plantas químicas complejas con recirculación. (Lo que entra al reactor = lo que sale).", "consecuencia_de_error": "Acumulación de material peligroso en el sistema."},
                    "civil": {"uso": "Redes de distribución de agua (Hardy Cross method). Es análogo a Kirchhoff: suma de presiones (voltajes) en un ciclo es cero.", "consecuencia_de_error": "Tuberías que no entregan agua a ciertas casas."},
                    "mecanica": {"uso": "Sistemas térmicos. Flujo de calor en nodos (intercambiadores). Suma de calor que entra = calor que sale.", "consecuencia_de_error": "Sobrecalentamiento de componentes."},
                    "mecatronica": {"uso": "Análisis de circuitos de control con múltiples fuentes y sensores interconectados.", "consecuencia_de_error": "Imposible predecir voltajes en puntos clave del circuito."},
                    "aeronautica": {"uso": "Sistema eléctrico del avión con múltiples generadores y buses de distribución.", "consecuencia_de_error": "Fallo en la gestión de carga eléctrica en emergencia."},
                    "electrica": {"uso": "Es la herramienta definitiva. Todo software de simulación (SPICE) resuelve matrices basadas en Kirchhoff.", "consecuencia_de_error": "Imposible diseñar circuitos integrados o redes eléctricas nacionales."}
                }
            }
        ]
    },

    # --- QUÍMICA ---
    "QUIM-01": {
        "nombre_completo": "Estructura Atómica y Tabla Periódica",
        "prerequisitos": ["ARITMETICA"],
        "quiz": [
            {
                "pregunta": "El número atómico (Z) representa la cantidad de...",
                "respuesta": "protones",
                "opciones": ["protones", "neutrones", "electrones", "masa"]
            },
            {
                "pregunta": "Los elementos de la columna 18 (Gases Nobles) son conocidos por ser químicamente...",
                "respuesta": "inertes",
                "opciones": ["inertes", "reactivos", "explosivos", "metales"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. El Átomo: Protones, Neutrones y Electrones",
                "definicion": "El átomo es la unidad base. Tiene un núcleo (Protones (+) y Neutrones (0)) y una nube de Electrones (-) orbitando. El 'Número Atómico' (Z) es la cantidad de Protones y define QUÉ elemento es.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: El Carbono siempre tiene Z=6 (6 Protones). Si es neutro, tiene 6 Electrones.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un átomo tiene 11 protones, ¿qué elemento es? (Consulta tabla: Na, Mg, Al)",
                        "respuesta_correcta": "na",
                        "opciones": ["na", "mg", "al", "cl"]
                    },
                    "similares": [
                        {"pregunta": "El número de protones define la identidad del elemento. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La carga de un electrón es... (positiva/negativa)", "respuesta_correcta": "negativa", "opciones": ["negativa", "positiva"]},
                        {"pregunta": "Si un átomo neutro tiene 8 protones, tiene ... electrones.", "respuesta_correcta": "8", "opciones": ["8", "16", "0", "10"]},
                        {"pregunta": "¿Qué partícula no tiene carga eléctrica?", "respuesta_correcta": "neutron", "opciones": ["neutron", "proton", "electron", "fotón"]},
                        {"pregunta": "La masa del electrón es despreciable comparada con el protón. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Semiconductores. El 'dopaje' (añadir átomos con más/menos electrones) altera la conductividad del Silicio para crear transistores.", "consecuencia_de_error": "Sin entender esto, no existirían los procesadores ni la memoria RAM."},
                    "quimica": {"uso": "Identificación de sustancias. La espectroscopía identifica elementos basándose en cómo sus electrones absorben energía.", "consecuencia_de_error": "Imposible determinar qué contaminantes hay en una muestra de agua."},
                    "civil": {"uso": "Densímetros nucleares. Usan fuentes radiactivas (núcleos inestables) para medir la compactación del suelo en carreteras.", "consecuencia_de_error": "Carreteras mal compactadas que se hunden con el tráfico."},
                    "mecanica": {"uso": "Ciencia de Materiales. La diferencia entre Hierro y Aluminio radica puramente en su número de protones y electrones.", "consecuencia_de_error": "Elegir un material pesado (Fe) cuando se necesitaba uno ligero (Al)."},
                    "mecatronica": {"uso": "Sensores piezoeléctricos. La deformación de la estructura atómica genera un desplazamiento de carga (electrones) que se lee como voltaje.", "consecuencia_de_error": "Mal diseño de sensores de vibración o presión."},
                    "aeronautica": {"uso": "Materiales compuestos. Entender cómo los átomos de Carbono forman fibras ultra resistentes para el fuselaje.", "consecuencia_de_error": "Estructuras pesadas o frágiles ante impactos."},
                    "electrica": {"uso": "Conductividad. Los metales (Cobre, Oro) tienen electrones 'libres' que se mueven fácil. Los aislantes (Plástico) no.", "consecuencia_de_error": "Usar un material que no conduce bien para líneas de transmisión, causando pérdidas."}
                }
            },
            {
                "subtema_titulo": "2. Isótopos y Masa Atómica (A)",
                "definicion": "Átomos del MISMO elemento (mismo Z, protones) pero con diferente número de NEUTRONES. Esto cambia su 'Masa Atómica' (A = Protones + Neutrones). Algunos isótopos son radiactivos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Carbono-12 (6p, 6n) es estable. Carbono-14 (6p, 8n) es radiactivo e inestable.\nMasa (A) del C-14 = 6 + 8 = 14.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un átomo con 17 protones y 20 neutrones tiene una masa atómica (A) de...",
                        "respuesta_correcta": "37",
                        "opciones": ["37", "17", "20", "3.7"]
                    },
                    "similares": [
                        {"pregunta": "Los isótopos difieren en el número de...", "respuesta_correcta": "neutrones", "opciones": ["neutrones", "protones", "electrones", "niveles"]},
                        {"pregunta": "Hidrógeno-3 (Tritio) tiene 1 protón. ¿Cuántos neutrones tiene? (A=3)", "respuesta_correcta": "2", "opciones": ["2", "1", "3", "0"]},
                        {"pregunta": "El Uranio-235 y Uranio-238 son isótopos. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La masa atómica en la tabla periódica es un promedio de los isótopos. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si Z=6 y A=13, ¿cuántos neutrones hay?", "respuesta_correcta": "7", "opciones": ["7", "6", "13", "19"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Relojes atómicos (Cesio-133). Usan la frecuencia de resonancia de un isótopo específico para medir el tiempo con precisión GPS.", "consecuencia_de_error": "Sin relojes atómicos, el GPS tendría un error de kilómetros."},
                    "quimica": {"uso": "Trazadores isotópicos. Usar isótopos para 'marcar' moléculas y seguir su camino en una reacción o en el cuerpo humano.", "consecuencia_de_error": "Diagnósticos médicos fallidos en medicina nuclear."},
                    "civil": {"uso": "Pruebas no destructivas (Gammagrafía). Usar isótopos radiactivos (Iridio-192) para 'ver' dentro de soldaduras de puentes.", "consecuencia_de_error": "Fallas ocultas en soldaduras estructurales que causan colapsos."},
                    "mecanica": {"uso": "Detección de fugas. Se inyectan isótopos en tuberías o motores para encontrar micro-fugas.", "consecuencia_de_error": "Fugas de fluidos peligrosos no detectadas."},
                    "mecatronica": {"uso": "Baterías nucleares (RTG). Usan el calor del decaimiento de isótopos (Plutonio) para alimentar robots en el espacio (ej. Curiosity).", "consecuencia_de_error": "El robot se queda sin energía en Marte durante la noche o el invierno."},
                    "aeronautica": {"uso": "Inspección de turbinas. Uso de isótopos para radiografiar los álabes y buscar grietas internas.", "consecuencia_de_error": "Explosión de motor en vuelo por fatiga de material."},
                    "electrica": {"uso": "Generación nuclear. La fisión del Uranio-235 libera calor para mover turbinas y generar electricidad.", "consecuencia_de_error": "Accidentes nucleares si no se controla la reacción del isótopo."}
                }
            },
            {
                "subtema_titulo": "3. Configuración Electrónica (Orbitales s, p, d, f)",
                "definicion": "Los electrones no giran en círculos, viven en 'orbitales' (zonas de probabilidad) con formas raras (s, p, d, f). La configuración dice dónde están los electrones. El orden de llenado sigue el diagrama de Moeller (1s, 2s, 2p, 3s...).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Nitrógeno (Z=7).\nLlenado: 1s² (caben 2), 2s² (caben 2), 2p³ (sobran 3).\nConfiguración: 1s² 2s² 2p³.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuántos electrones caben como máximo en un orbital tipo 's'?",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "6", "10", "1"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuántos electrones caben máximo en el subnivel 'p'?", "respuesta_correcta": "6", "opciones": ["6", "2", "10", "14"]},
                        {"pregunta": "El Carbono (6 electrones) termina su configuración en... (s/p/d)", "respuesta_correcta": "p", "opciones": ["p", "s", "d", "f"]},
                        {"pregunta": "Configuración del Helio (2 e-): 1s...", "respuesta_correcta": "2", "opciones": ["2", "1", "3", "4"]},
                        {"pregunta": "La capa de valencia es la capa de energía más... (interna/externa)", "respuesta_correcta": "externa", "opciones": ["externa", "interna", "media", "nuclear"]},
                        {"pregunta": "Los orbitales 'd' pueden alojar hasta ... electrones.", "respuesta_correcta": "10", "opciones": ["10", "5", "14", "6"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Computación Cuántica. Los 'qubits' aprovechan propiedades cuánticas definidas por la configuración electrónica (espín).", "consecuencia_de_error": "Errores en algoritmos cuánticos."},
                    "quimica": {"uso": "Predicción de enlaces. Los orbitales (s, p) se 'hibridan' (ej. sp3) para formar las geometrías de las moléculas (ej. tetraédrica).", "consecuencia_de_error": "No entender por qué el metano es una pirámide y no plano."},
                    "civil": {"uso": "Pigmentos y pinturas. El color viene de electrones saltando entre orbitales. Metales de transición (orbitales d) dan colores vivos.", "consecuencia_de_error": "Pinturas que se degradan o cambian de color con el sol (UV)."},
                    "mecanica": {"uso": "Magnetismo. Los materiales magnéticos (Hierro, Níquel) tienen electrones desapareados en sus orbitales 'd'.", "consecuencia_de_error": "Imposible diseñar imanes permanentes o electroimanes."},
                    "mecatronica": {"uso": "Láseres. Funcionan excitando electrones a orbitales superiores y forzando su caída simultánea.", "consecuencia_de_error": "Láseres ineficientes o de frecuencia incorrecta."},
                    "aeronautica": {"uso": "Aleaciones de Titanio. Sus propiedades mecánicas excepcionales vienen de su configuración electrónica de metal de transición.", "consecuencia_de_error": "Fallas estructurales a alta temperatura."},
                    "electrica": {"uso": "Aislantes vs Conductores. En los conductores, las bandas de energía (orbitales) se solapan; en aislantes, están muy separadas (Band Gap).", "consecuencia_de_error": "Fallo de aislamiento a altos voltajes."}
                }
            },
            {
                "subtema_titulo": "4. Tabla Periódica: Metales, No Metales y Metaloides",
                "definicion": "La tabla se divide en regiones. Izquierda: Metales (conductores, dúctiles, pierden e-). Derecha: No Metales (aislantes, frágiles, ganan e-). Frontera: Metaloides (semiconductores).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Silicio (Si). Está en la escalera de la frontera. Es un metaloide. Brilla como metal pero es frágil y semiconductor. Perfecto para chips.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El Hierro (Fe) es un... (metal/no metal/metaloide)",
                        "respuesta_correcta": "metal",
                        "opciones": ["metal", "no metal", "metaloide", "gas noble"]
                    },
                    "similares": [
                        {"pregunta": "El Oxígeno (O) es un... (metal/no metal)", "respuesta_correcta": "no metal", "opciones": ["no metal", "metal", "metaloide", "liquido"]},
                        {"pregunta": "El Silicio (Si) y Germanio (Ge) son...", "respuesta_correcta": "metaloides", "opciones": ["metaloides", "metales", "gases", "liquidos"]},
                        {"pregunta": "Los metales son buenos conductores de calor y electricidad. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La mayoría de los elementos en la tabla son... (metales/no metales)", "respuesta_correcta": "metales", "opciones": ["metales", "no metales", "gases", "liquidos"]},
                        {"pregunta": "El elemento más electronegativo (Fluor) está a la... (izquierda/derecha)", "respuesta_correcta": "derecha", "opciones": ["derecha", "izquierda", "centro", "abajo"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Hardware. El Silicio (metaloide) es la base. El Oro (metal) se usa en contactos por no oxidarse. El plástico (no metal) aísla.", "consecuencia_de_error": "Usar metales oxidables en contactos de CPU causa fallas de conexión."},
                    "quimica": {"uso": "Síntesis. Metales + No Metales = Sales. No Metal + No Metal = Moléculas orgánicas.", "consecuencia_de_error": "Intentar hacer una sal mezclando dos metales (formaría aleación, no reacción)."},
                    "civil": {"uso": "Estructuras. Metales (Acero) para resistir tensión. Cerámicos/Piedra (No metales/Óxidos) para resistir compresión.", "consecuencia_de_error": "Usar concreto (frágil) para soportar tensión sin refuerzo metálico (colapso)."},
                    "mecanica": {"uso": "Disipación de calor. Metales (Aluminio, Cobre) para radiadores. Polímeros (No metales) para mangos o carcasas térmicas.", "consecuencia_de_error": "Motores que se sobrecalientan o herramientas que queman la mano."},
                    "mecatronica": {"uso": "Sensores. Termopares usan la unión de dos metales diferentes para medir temperatura.", "consecuencia_de_error": "Lecturas de temperatura erróneas."},
                    "aeronautica": {"uso": "Fuselajes. Aluminio y Titanio (Metales) vs Fibra de Carbono (No metal). La fibra no conduce electricidad igual, requiere mallas para rayos.", "consecuencia_de_error": "Avión de fibra de carbono dañado severamente por un rayo."},
                    "electrica": {"uso": "Cableado. Cobre (Metal) para el núcleo. PVC (No metal) para el recubrimiento.", "consecuencia_de_error": "Cortocircuitos si el recubrimiento es conductor o se degrada."}
                }
            },
            {
                "subtema_titulo": "5. Electrones de Valencia y Grupos",
                "definicion": "Los electrones en la capa MÁS externa. Coinciden con el número de Grupo (columnas 1, 2, 13-18 usan dígitos finales 1-8). Determinan CÓMO se enlaza el átomo. Todos quieren tener 8 (Regla del Octeto).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Cloro (Grupo 17). Tiene 7 electrones de valencia. Le falta 1 para llegar a 8. Es muy reactivo buscando ese electrón.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El Carbono está en el Grupo 14. ¿Cuántos electrones de valencia tiene?",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "14", "2", "8"]
                    },
                    "similares": [
                        {"pregunta": "Los Gases Nobles (Grupo 18) tienen ... electrones de valencia (excepto He).", "respuesta_correcta": "8", "opciones": ["8", "18", "0", "2"]},
                        {"pregunta": "El Sodio (Grupo 1) tiene ... electrón de valencia.", "respuesta_correcta": "1", "opciones": ["1", "11", "2", "7"]},
                        {"pregunta": "Los elementos del mismo grupo tienen propiedades químicas... (similares/diferentes)", "respuesta_correcta": "similares", "opciones": ["similares", "diferentes", "opuestas", "nulas"]},
                        {"pregunta": "Para cumplir el octeto, al Oxígeno (6 valencia) le faltan... e-.", "respuesta_correcta": "2", "opciones": ["2", "6", "8", "4"]},
                        {"pregunta": "El Aluminio (Grupo 13) tiende a perder sus ... electrones de valencia.", "respuesta_correcta": "3", "opciones": ["3", "13", "5", "1"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Dopaje de chips. Silicio (4 valencia) dopado con Fósforo (5 valencia) crea semiconductor tipo-N (sobra un electrón).", "consecuencia_de_error": "Chips que no funcionan como semiconductores."},
                    "quimica": {"uso": "Predicción de fórmulas. Si Na tiene 1 (lo da) y Cl tiene 7 (toma 1), la fórmula es NaCl (1 a 1).", "consecuencia_de_error": "Escribir fórmulas imposibles como NaCl₂."},
                    "civil": {"uso": "Aditivos de concreto. Polímeros diseñados por su valencia para interactuar con el agua y el cemento.", "consecuencia_de_error": "Concreto que no fragua o es muy poroso."},
                    "mecanica": {"uso": "Lubricantes. El Grafito (Carbono) lubrica porque sus capas tienen electrones deslocalizados que permiten deslizamiento.", "consecuencia_de_error": "Fricción y desgaste en maquinaria."},
                    "mecatronica": {"uso": "LEDs RGB. Diferentes materiales semiconductores (con diferentes valencias/band gaps) producen diferentes colores de luz.", "consecuencia_de_error": "No poder generar el color deseado."},
                    "aeronautica": {"uso": "Combustión. El Carbono (4 valencia) e Hidrógeno (1 valencia) del combustible se reorganizan con Oxígeno para liberar energía.", "consecuencia_de_error": "Combustión incompleta (humo negro) y pérdida de empuje."},
                    "electrica": {"uso": "Baterías. El Litio (1 valencia) es excelente porque cede su electrón muy fácilmente y es muy ligero.", "consecuencia_de_error": "Baterías pesadas o con poca capacidad."}
                }
            },
            {
                "subtema_titulo": "6. Electronegatividad y Radio Atómico",
                "definicion": "Tendencias periódicas. \nElectronegatividad: Qué tan fuerte atrae electrones un átomo (El Flúor es el más 'agresivo'). Aumenta hacia arriba y derecha.\nRadio Atómico: Tamaño del átomo. Aumenta hacia abajo y izquierda.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: En el enlace H-F, el Flúor (4.0) es mucho más electronegativo que el Hidrógeno (2.1). El F 'jala' los electrones, creando un polo negativo.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál elemento es más electronegativo: Flúor (F) o Francio (Fr)?",
                        "respuesta_correcta": "fluor",
                        "opciones": ["fluor", "francio", "son iguales", "depende"]
                    },
                    "similares": [
                        {"pregunta": "La electronegatividad aumenta hacia la... (izquierda/derecha)", "respuesta_correcta": "derecha", "opciones": ["derecha", "izquierda", "abajo", "diagonal"]},
                        {"pregunta": "El radio atómico aumenta hacia... (arriba/abajo)", "respuesta_correcta": "abajo", "opciones": ["abajo", "arriba", "derecha", "centro"]},
                        {"pregunta": "Si dos átomos tienen electronegatividad muy diferente, forman un enlace... (iónico/covalente)", "respuesta_correcta": "ionico", "opciones": ["ionico", "covalente", "metalico", "nulo"]},
                        {"pregunta": "Los gases nobles tienen electronegatividad... (muy alta/nula o muy baja)", "respuesta_correcta": "nula", "opciones": ["nula", "muy alta", "media", "variable"]},
                        {"pregunta": "¿Qué átomo es más grande: Litio o Cesio (mismo grupo)?", "respuesta_correcta": "cesio", "opciones": ["cesio", "litio", "iguales", "hidrogeno"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Materiales dieléctricos (aislantes) en capacitores. Dependen de la polarización (electronegatividad) de los átomos.", "consecuencia_de_error": "Capacitores con fugas o baja capacidad."},
                    "quimica": {"uso": "Polaridad. Determina si una molécula es soluble en agua (polar) o en aceite (no polar).", "consecuencia_de_error": "Fármacos que no se disuelven en la sangre."},
                    "civil": {"uso": "Impermeabilizantes. Materiales hidrofóbicos (baja electronegatividad/no polares) repelen el agua (polar).", "consecuencia_de_error": "Filtraciones de agua en techos y cimientos."},
                    "mecanica": {"uso": "Adhesión. Los pegamentos funcionan por fuerzas intermoleculares causadas por diferencias de electronegatividad.", "consecuencia_de_error": "Uniones pegadas que se despegan bajo carga."},
                    "mecatronica": {"uso": "Sensores de humedad. Detectan moléculas de agua (polares) interactuando con una superficie.", "consecuencia_de_error": "Fallo en control ambiental."},
                    "aeronautica": {"uso": "Recubrimientos anti-hielo. Materiales diseñados para que el agua no se adhiera (juego de polaridades).", "consecuencia_de_error": "Acumulación de hielo en alas, pérdida de sustentación."},
                    "electrica": {"uso": "Serie Galvánica. La diferencia de potencial entre metales (relacionada con su tendencia a perder e-) dicta el voltaje.", "consecuencia_de_error": "Elegir pares de metales que generan poco voltaje en una batería."}
                }
            },
            {
                "subtema_titulo": "7. Iones: Cationes y Aniones",
                "definicion": "Cuando un átomo pierde o gana electrones, se vuelve un ION.\n- Pierde e- (negativo) -> Se vuelve positivo (CATIÓN).\n- Gana e- (negativo) -> Se vuelve negativo (ANIÓN).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Na pierde 1 e- -> Na⁺ (Catión).\nCl gana 1 e- -> Cl⁻ (Anión).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si un átomo neutro gana 2 electrones, su carga será...",
                        "respuesta_correcta": "-2",
                        "opciones": ["-2", "+2", "0", "-1"]
                    },
                    "similares": [
                        {"pregunta": "Un ion con carga positiva se llama...", "respuesta_correcta": "cation", "opciones": ["cation", "anion", "neutrino", "isotopo"]},
                        {"pregunta": "Un ion con carga negativa se llama...", "respuesta_correcta": "anion", "opciones": ["anion", "cation", "proton", "nucleo"]},
                        {"pregunta": "Los metales tienden a formar... (cationes/aniones)", "respuesta_correcta": "cationes", "opciones": ["cationes", "aniones", "neutrones", "gases"]},
                        {"pregunta": "El Ca (Grupo 2) pierde 2 electrones y forma el ion...", "respuesta_correcta": "Ca+2", "opciones": ["Ca+2", "Ca-2", "Ca", "Ca+1"]},
                        {"pregunta": "En la electrólisis, los cationes van hacia el cátodo (negativo). (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Pantallas LCD/OLED. Campos eléctricos mueven iones o moléculas cargadas para dejar pasar luz.", "consecuencia_de_error": "Píxeles muertos o colores incorrectos."},
                    "quimica": {"uso": "pH. Es la concentración de cationes Hidrógeno (H⁺) en una solución.", "consecuencia_de_error": "Reacciones enzimáticas que se detienen por acidez incorrecta."},
                    "civil": {"uso": "Cloruros en concreto. Los aniones Cl⁻ penetran y atacan la varilla de acero (formando óxido expansivo).", "consecuencia_de_error": "El concreto 'revienta' desde adentro (cáncer del concreto)."},
                    "mecanica": {"uso": "Corrosión Galvánica. Flujo de iones entre dos metales diferentes en contacto con agua.", "consecuencia_de_error": "Pernos oxidados que se rompen."},
                    "mecatronica": {"uso": "Músculos artificiales (EAP). Polímeros electroactivos que se deforman al mover iones en su interior.", "consecuencia_de_error": "Actuadores robóticos que no se contraen."},
                    "aeronautica": {"uso": "Baterías de arranque. Flujo masivo de iones para arrancar las turbinas o APU.", "consecuencia_de_error": "Imposibilidad de arrancar motores en tierra remota."},
                    "electrica": {"uso": "Capacitores electrolíticos. Usan un líquido iónico para lograr alta capacitancia.", "consecuencia_de_error": "Si se conectan al revés, los iones gasifican y el capacitor explota."}
                }
            }
        ]
    },

    "QUIM-02": {
        "nombre_completo": "Enlaces Químicos y Propiedades de los Materiales",
        "prerequisitos": ["QUIM-01"],
        "quiz": [
            {
                "pregunta": "¿Qué tipo de enlace implica compartir electrones?",
                "respuesta": "covalente",
                "opciones": ["covalente", "ionico", "metalico", "nuclear"]
            },
            {
                "pregunta": "¿Qué fuerza mantiene unidas a las moléculas de agua entre sí (no a los átomos)?",
                "respuesta": "puentes de hidrogeno",
                "opciones": ["puentes de hidrogeno", "covalente", "ionico", "magnetica"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Regla del Octeto y Estructuras de Lewis",
                "definicion": "La meta de (casi) todo átomo es tener 8 electrones en su capa de valencia (como los Gases Nobles). Para lograrlo, ganan, pierden o comparten electrones. Las Estructuras de Lewis son diagramas que muestran estos electrones como puntos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Cloro (Grupo 17, 7e⁻). Le falta 1.\nSi se encuentran dos Cloros, comparten 1 par. :Cl-Cl:. Ahora ambos 'sienten' que tienen 8.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El Carbono (Grupo 14) tiene 4 electrones de valencia. ¿Cuántos enlaces necesita formar para llegar a 8?",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "2", "6", "1"]
                    },
                    "similares": [
                        {"pregunta": "El Hidrógeno es la excepción, se llena con ... electrones (como el Helio).", "respuesta_correcta": "2", "opciones": ["2", "8", "1", "0"]},
                        {"pregunta": "El Nitrógeno (Grupo 15, 5e⁻) necesita formar ... enlaces.", "respuesta_correcta": "3", "opciones": ["3", "5", "1", "2"]},
                        {"pregunta": "En la estructura de Lewis, un par de puntos entre átomos representa un...", "respuesta_correcta": "enlace", "opciones": ["enlace", "nucleo", "proton", "ion"]},
                        {"pregunta": "Los gases nobles no reaccionan porque ya tienen... electrones (excepto He).", "respuesta_correcta": "8", "opciones": ["8", "2", "10", "6"]},
                        {"pregunta": "El Oxígeno (6e⁻) suele formar ... enlaces.", "respuesta_correcta": "2", "opciones": ["2", "6", "1", "4"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Lógica de semiconductores. El Silicio (4 enlaces) dopado busca cumplir el octeto, dejando huecos o electrones libres.", "consecuencia_de_error": "Fallo en el diseño de transistores a nivel atómico."},
                    "quimica": {"uso": "Predicción de reactividad. Si una molécula no cumple el octeto (radical libre), será extremadamente reactiva y peligrosa.", "consecuencia_de_error": "Reacciones explosivas no planeadas."},
                    "civil": {"uso": "Química del cemento. La hidratación busca estados estables (octetos) en los silicatos de calcio.", "consecuencia_de_error": "Hormigón que no fragua o pierde resistencia."},
                    "mecanica": {"uso": "Estabilidad de lubricantes. Los aceites sintéticos se diseñan molecularmente para ser estables (octetos completos) a altas temperaturas.", "consecuencia_de_error": "Aceite que se degrada (oxida) rápido y daña el motor."},
                    "mecatronica": {"uso": "Sensores de gases. Detectan moléculas inestables (que buscan electrones) oxidándose en la superficie del sensor.", "consecuencia_de_error": "Sensor que no detecta fugas de gas tóxico."},
                    "aeronautica": {"uso": "Combustibles. La energía liberada al quemar jet-fuel viene de romper enlaces y formar otros nuevos más estables (CO₂ y H₂O cumpliendo octeto).", "consecuencia_de_error": "Cálculo erróneo de la densidad energética del combustible."},
                    "electrica": {"uso": "Aislantes (polímeros). Son cadenas largas donde todos los átomos cumplen el octeto fuertemente, sin dejar electrones libres para conducir.", "consecuencia_de_error": "Ruptura del dieléctrico y cortocircuito."}
                }
            },
            {
                "subtema_titulo": "2. Enlace Iónico (Transferencia de Electrones)",
                "definicion": "Ocurre entre un Metal y un No Metal con gran diferencia de electronegatividad (>1.7). El metal 'regala' electrones al no metal. Se forman iones (+ y -) que se atraen y forman redes cristalinas (sólidos, duros, frágiles).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: NaCl (Sal). El Na regala 1e⁻ al Cl. Se forma Na⁺ y Cl⁻. Se atraen electrostáticamente formando un cristal cúbico.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El compuesto KBr (Potasio-Metal, Bromo-No Metal) tiene enlace...",
                        "respuesta_correcta": "ionico",
                        "opciones": ["ionico", "covalente", "metalico", "polar"]
                    },
                    "similares": [
                        {"pregunta": "Los compuestos iónicos tienen puntos de fusión... (altos/bajos)", "respuesta_correcta": "altos", "opciones": ["altos", "bajos", "nulos", "negativos"]},
                        {"pregunta": "En estado sólido, los compuestos iónicos conducen electricidad. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Disueltos en agua, los compuestos iónicos conducen electricidad. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Son materiales duros pero... (elásticos/frágiles)", "respuesta_correcta": "fragiles", "opciones": ["fragiles", "elasticos", "ductiles", "maleables"]},
                        {"pregunta": "La fuerza que mantiene unido el enlace iónico es...", "respuesta_correcta": "electrostatica", "opciones": ["electrostatica", "magnetica", "gravitacional", "nuclear"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Baterías Li-Ion. Los iones de Litio viajan entre el cátodo y el ánodo. No es un 'enlace' fijo, es movilidad iónica.", "consecuencia_de_error": "Batería que se incendia o no carga."},
                    "quimica": {"uso": "Síntesis de sales. La mayoría de los reactivos inorgánicos son iónicos.", "consecuencia_de_error": "Precipitación no deseada en soluciones."},
                    "civil": {"uso": "Cerámicas y vidrios. Son redes iónicas/covalentes. Su fragilidad (no se doblan, se rompen) dicta cómo se usan en construcción.", "consecuencia_de_error": "Usar ladrillo (cerámico) para soportar tensión (se rompe) en lugar de compresión."},
                    "mecanica": {"uso": "Aislantes térmicos cerámicos (Zirconia). Enlaces fuertes que no vibran fácil (no transmiten calor).", "consecuencia_de_error": "Componentes fundidos por calor excesivo."},
                    "mecatronica": {"uso": "Piezoeléctricos (PZT). Cerámicas iónicas que generan voltaje al deformarse (el desplazamiento de iones crea campo eléctrico).", "consecuencia_de_error": "Sensores de ultrasonido fallidos."},
                    "aeronautica": {"uso": "Recubrimientos de barrera térmica (TBC) en turbinas. Protegen el metal del calor extremo.", "consecuencia_de_error": "Fusión de álabes de turbina."},
                    "electrica": {"uso": "Aisladores de alta tensión (vidrio/cerámica). Deben resistir arcos eléctricos sin conducir.", "consecuencia_de_error": "Fuga de corriente a tierra en torres de transmisión."}
                }
            },
            {
                "subtema_titulo": "3. Enlace Covalente No Polar (Compartición Equitativa)",
                "definicion": "Entre No Metales iguales o con electronegatividad similar (diferencia < 0.4). Comparten electrones equitativamente. No hay polos (+/-). Son hidrofóbicos (no se mezclan con agua).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Gas Oxígeno (O₂), Nitrógeno (N₂), Metano (CH₄). En el O=O, ambos jalan los electrones con la misma fuerza.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El aceite es una molécula covalente no polar. ¿Se mezcla con el agua (polar)? (si/no)",
                        "respuesta_correcta": "no",
                        "opciones": ["no", "si"]
                    },
                    "similares": [
                        {"pregunta": "El enlace H-H en el hidrógeno gaseoso es...", "respuesta_correcta": "covalente no polar", "opciones": ["covalente no polar", "ionico", "metalico", "polar"]},
                        {"pregunta": "Los plásticos (polímeros) como el polietileno son mayormente... (polares/no polares)", "respuesta_correcta": "no polares", "opciones": ["no polares", "polares", "ionicos", "metales"]},
                        {"pregunta": "¿Conducen electricidad los compuestos covalentes puros? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Tienen puntos de fusión generalmente más ... que los iónicos.", "respuesta_correcta": "bajos", "opciones": ["bajos", "altos", "iguales", "extremos"]},
                        {"pregunta": "El Cloro gas (Cl₂) tiene enlace...", "respuesta_correcta": "covalente no polar", "opciones": ["covalente no polar", "polar", "ionico", "metalico"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Grasa térmica para CPUs. Generalmente basada en silicona o compuestos no polares que llenan huecos microscópicos.", "consecuencia_de_error": "Sobrecalentamiento del procesador."},
                    "quimica": {"uso": "Disolventes orgánicos (Hexano, Tolueno). Se usan para disolver grasas o realizar reacciones que el agua inhibiría.", "consecuencia_de_error": "Explosiones o reacciones fallidas por usar el solvente incorrecto."},
                    "civil": {"uso": "Impermeabilizantes asfálticos. El asfalto es hidrocarburo no polar, por eso repele el agua.", "consecuencia_de_error": "Filtraciones y humedad en edificios."},
                    "mecanica": {"uso": "Lubricantes y aceites. Son cadenas largas de hidrocarburos no polares. 'Slippery' a nivel molecular.", "consecuencia_de_error": "Fricción metal-metal y agarrotamiento del motor."},
                    "mecatronica": {"uso": "Recubrimientos conformados (Conformal coating) para proteger circuitos de la humedad (agua).", "consecuencia_de_error": "Corrosión de circuitos en ambientes húmedos."},
                    "aeronautica": {"uso": "Combustible (Jet A-1). Es queroseno, una mezcla de hidrocarburos no polares.", "consecuencia_de_error": "Contaminación del combustible con agua (que no se mezcla y se congela)."},
                    "electrica": {"uso": "Aceites de transformador. Dieléctricos no polares que enfrían y aíslan.", "consecuencia_de_error": "Arco eléctrico dentro del transformador."}
                }
            },
            {
                "subtema_titulo": "4. Enlace Covalente Polar (Compartición Desigual)",
                "definicion": "Entre No Metales con electronegatividad diferente (0.4 a 1.7). Uno 'jala' más los electrones, creando un polo negativo (δ-) y otro positivo (δ+). Son solubles en agua.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Agua (H₂O). El Oxígeno jala fuerte a los electrones. El O es δ- y los H son δ+. Esto la hace el 'solvente universal'.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En el enlace H-Cl, el Cloro es más electronegativo. ¿Quién tiene la carga parcial negativa?",
                        "respuesta_correcta": "cloro",
                        "opciones": ["cloro", "hidrogeno", "ambos", "ninguno"]
                    },
                    "similares": [
                        {"pregunta": "Las moléculas polares se alinean en un campo eléctrico. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "El agua es una molécula... (polar/no polar)", "respuesta_correcta": "polar", "opciones": ["polar", "no polar", "ionica", "neutra"]},
                        {"pregunta": "Lo similar disuelve a lo... (similar/opuesto)", "respuesta_correcta": "similar", "opciones": ["similar", "opuesto", "distinto", "extraño"]},
                        {"pregunta": "El Amoniaco (NH₃) es polar. ¿Se disuelve en agua?", "respuesta_correcta": "si", "opciones": ["si", "no"]},
                        {"pregunta": "La diferencia de electronegatividad crea un momento...", "respuesta_correcta": "dipolar", "opciones": ["dipolar", "magnetico", "inercial", "angular"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Pantallas LCD (Cristal Líquido). Son moléculas polares que giran cuando aplicas un voltaje, bloqueando o pasando luz.", "consecuencia_de_error": "Pantalla negra o que no responde."},
                    "quimica": {"uso": "Extracción líquido-líquido. Separar compuestos polares de no polares usando agua y aceite.", "consecuencia_de_error": "No poder purificar un fármaco o producto químico."},
                    "civil": {"uso": "Aditivos para concreto. Superplastificantes son moléculas polares que dispersan las partículas de cemento.", "consecuencia_de_error": "Concreto difícil de trabajar o débil."},
                    "mecanica": {"uso": "Refrigerantes (Glicol/Agua). Son polares y tienen alto calor específico para absorber calor.", "consecuencia_de_error": "Sistema de enfriamiento ineficiente."},
                    "mecatronica": {"uso": "Sensores de humedad capacitivos. El agua (polar) cambia la capacitancia del sensor.", "consecuencia_de_error": "Lectura de humedad incorrecta."},
                    "aeronautica": {"uso": "Descongelantes. El glicol (polar) se une al agua e impide que forme cristales de hielo en las alas.", "consecuencia_de_error": "Formación de hielo y caída del avión."},
                    "electrica": {"uso": "Calentamiento por microondas. Las ondas hacen rotar las moléculas polares de agua, generando calor por fricción.", "consecuencia_de_error": "Materiales secos (sin agua polar) no se calientan bien en microondas."}
                }
            },
            {
                "subtema_titulo": "5. Enlace Metálico (Mar de Electrones)",
                "definicion": "Los átomos de metal se agrupan y 'sueltan' sus electrones de valencia a un fondo común. Los electrones fluyen libremente ('deslocalizados') alrededor de los núcleos fijos. Esto explica la conductividad y maleabilidad.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Un cable de Cobre. Los electrones no pertenecen a ningún átomo en particular, fluyen como agua a través de la red de núcleos de cobre cuando aplicas voltaje.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Los metales conducen electricidad porque tienen electrones...",
                        "respuesta_correcta": "libres",
                        "opciones": ["libres", "fijos", "ionicos", "covalentes"]
                    },
                    "similares": [
                        {"pregunta": "Propiedad de los metales de hacerse hilos (alambres).", "respuesta_correcta": "ductilidad", "opciones": ["ductilidad", "dureza", "brillo", "fragilidad"]},
                        {"pregunta": "Propiedad de los metales de hacerse láminas.", "respuesta_correcta": "maleabilidad", "opciones": ["maleabilidad", "ductilidad", "resistencia", "densidad"]},
                        {"pregunta": "Si golpeas un metal, se deforma. Si golpeas un cristal iónico, se...", "respuesta_correcta": "rompe", "opciones": ["rompe", "dobla", "estira", "funde"]},
                        {"pregunta": "El enlace metálico es ... (direccional/no direccional).", "respuesta_correcta": "no direccional", "opciones": ["no direccional", "direccional", "polar", "lineal"]},
                        {"pregunta": "Aleación de Hierro y Carbono.", "respuesta_correcta": "acero", "opciones": ["acero", "bronce", "laton", "aluminio"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Disipadores de calor. El enlace metálico conduce calor excelentemente (vibración de núcleos + electrones libres).", "consecuencia_de_error": "CPU frito por mal disipador."},
                    "quimica": {"uso": "Catálisis. La superficie 'rica en electrones' de metales como Platino o Paladio facilita reacciones químicas.", "consecuencia_de_error": "Convertidores catalíticos de autos que no limpian el humo."},
                    "civil": {"uso": "Estructuras de acero. La ductilidad permite que el edificio se deforme en un sismo sin colapsar súbitamente (absorbe energía).", "consecuencia_de_error": "Falla frágil catastrófica."},
                    "mecanica": {"uso": "Aleaciones. Mezclar metales altera el 'mar de electrones' y la red, cambiando dureza y resistencia.", "consecuencia_de_error": "Piezas que se desgastan muy rápido o se rompen."},
                    "mecatronica": {"uso": "Blindaje electromagnético (Jaula de Faraday). El mar de electrones redistribuye los campos externos, protegiendo la electrónica interna.", "consecuencia_de_error": "Ruido eléctrico e interferencia en robots."},
                    "aeronautica": {"uso": "Fatiga del metal. Aunque dúctil, el enlace metálico puede desarrollar micro-grietas con ciclos repetidos de carga.", "consecuencia_de_error": "Descompresión explosiva o pérdida de alas en vuelo (ej. Comet)."},
                    "electrica": {"uso": "Transmisión de energía. Solo el enlace metálico permite transportar corrientes masivas a largas distancias.", "consecuencia_de_error": "Pérdidas por resistencia si el metal tiene impurezas."}
                }
            },
            {
                "subtema_titulo": "6. Fuerzas Intermoleculares (Van der Waals y Puentes de H)",
                "definicion": "No son enlaces 'dentro' de la molécula, sino atracciones 'entre' moléculas. Son débiles pero definen el estado físico (sólido, líquido, gas). \n- Van der Waals: En todas, muy débiles.\n- Puentes de Hidrógeno: Fuerte atracción entre H y (N, O, F).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: El agua hierve a 100°C (muy alto para su peso) porque tiene Puentes de Hidrógeno que 'pegan' las moléculas entre sí. El Metano (CH₄) no tiene puentes, así que es gas a temperatura ambiente.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué fuerza es más fuerte: un enlace Covalente o un Puente de Hidrógeno?",
                        "respuesta_correcta": "covalente",
                        "opciones": ["covalente", "puente de hidrogeno", "van der waals", "dipolo"]
                    },
                    "similares": [
                        {"pregunta": "El ADN se mantiene unido (doble hélice) gracias a...", "respuesta_correcta": "puentes de hidrogeno", "opciones": ["puentes de hidrogeno", "enlaces ionicos", "covalentes", "metalicos"]},
                        {"pregunta": "Las fuerzas de Van der Waals aumentan con el ... de la molécula.", "respuesta_correcta": "tamaño", "opciones": ["tamaño", "color", "olor", "sabor"]},
                        {"pregunta": "El hielo flota porque los puentes de hidrógeno crean una estructura ... densa.", "respuesta_correcta": "menos", "opciones": ["menos", "mas", "igual", "muy"]},
                        {"pregunta": "Los geckos caminan por paredes gracias a fuerzas de...", "respuesta_correcta": "van der waals", "opciones": ["van der waals", "gravedad", "magnetismo", "pegamento"]},
                        {"pregunta": "Para evaporar agua, debes romper los...", "respuesta_correcta": "puentes de hidrogeno", "opciones": ["puentes de hidrogeno", "enlaces covalentes", "atomos", "electrones"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Nanotecnología y auto-ensamblaje. A escala nano, las fuerzas de Van der Waals son dominantes.", "consecuencia_de_error": "Nano-robots que se pegan a todo y no funcionan (stiction)."},
                    "quimica": {"uso": "Puntos de ebullición. Determinan cómo separar el petróleo en gasolina, diésel, etc. (Destilación fraccionada).", "consecuencia_de_error": "Combustibles impuros o mal separados."},
                    "civil": {"uso": "Asfalto. Las fuerzas intermoleculares mantienen unida la mezcla bituminosa. El calor las debilita (asfalto blando).", "consecuencia_de_error": "Carreteras que se deforman (ahuellamiento) en verano."},
                    "mecanica": {"uso": "Viscosidad de lubricantes. Es la resistencia a fluir causada por fricción intermolecular.", "consecuencia_de_error": "Aceite que se vuelve 'agua' al calentarse y no protege."},
                    "mecatronica": {"uso": "Cristales líquidos (LCD). Las fuerzas intermoleculares débiles permiten que las moléculas giren con poco voltaje.", "consecuencia_de_error": "Pantallas con tiempos de respuesta lentos."},
                    "aeronautica": {"uso": "Comportamiento de polímeros a baja temperatura. El frío reduce la energía cinética y las fuerzas intermoleculares 'congelan' el plástico (transición vítrea).", "consecuencia_de_error": "Sellos (O-rings) que se rompen en el frío (Causa del Challenger)."},
                    "electrica": {"uso": "Capacitores de supercondensador. Almacenan energía en la 'doble capa' eléctrica, gobernada por fuerzas intermoleculares.", "consecuencia_de_error": "Baterías de carga rápida ineficientes."}
                }
            },
            {
                "subtema_titulo": "7. Geometría Molecular (VSEPR)",
                "definicion": "Los pares de electrones se repelen. La forma de la molécula es aquella que mantiene los electrones lo más lejos posible. \n- 2 pares: Lineal (180°).\n- 3 pares: Trigonal (120°).\n- 4 pares: Tetraédrica (109.5°).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: CO₂. El C tiene 2 dobles enlaces (cuentan como 2 regiones). Se ponen opuestos -> O=C=O. Forma LINEAL.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El Metano (CH₄) tiene 4 enlaces y 0 pares libres. Su forma es...",
                        "respuesta_correcta": "tetraedrica",
                        "opciones": ["tetraedrica", "lineal", "plana", "octaedrica"]
                    },
                    "similares": [
                        {"pregunta": "El agua (H₂O) tiene 2 enlaces y 2 pares libres. Su forma es... (lineal/angular)", "respuesta_correcta": "angular", "opciones": ["angular", "lineal", "tetraedrica", "plana"]},
                        {"pregunta": "El ángulo en una molécula lineal es...", "respuesta_correcta": "180", "opciones": ["180", "90", "120", "109"]},
                        {"pregunta": "La forma define si una molécula es polar o no. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "El BF₃ (3 enlaces) es trigonal...", "respuesta_correcta": "plana", "opciones": ["plana", "piramidal", "lineal", "curva"]},
                        {"pregunta": "VSEPR significa Repulsión de Pares de Electrones de la Capa de...", "respuesta_correcta": "valencia", "opciones": ["valencia", "conduccion", "nucleo", "interna"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Materiales ópticos. La geometría molecular afecta cómo la luz (polarización) interactúa con el material.", "consecuencia_de_error": "Fibra óptica con pérdidas o dispersión."},
                    "quimica": {"uso": "Diseño de fármacos (Llave-Cerradura). La molécula del medicamento debe tener la forma exacta para encajar en la proteína objetivo.", "consecuencia_de_error": "Medicamento ineficaz o con efectos secundarios."},
                    "civil": {"uso": "Zeolitas y filtros moleculares. Materiales con poros de forma geométrica precisa para filtrar agua o aire.", "consecuencia_de_error": "Filtros que no atrapan los contaminantes."},
                    "mecanica": {"uso": "Polímeros. La geometría de la cadena (lineal vs ramificada) define si el plástico es duro (HDPE) o bolsa suave (LDPE).", "consecuencia_de_error": "Envase que se rompe o no tiene la rigidez necesaria."},
                    "mecatronica": {"uso": "Sensores bioquímicos. Detectan la forma de moléculas específicas.", "consecuencia_de_error": "Falsos positivos en biosensores."},
                    "aeronautica": {"uso": "Materiales furtivos (Stealth). Estructuras moleculares que absorben ondas de radar en lugar de reflejarlas.", "consecuencia_de_error": "Avión detectable por radar."},
                    "electrica": {"uso": "Dieléctricos. Moléculas polares que pueden rotar (geometría) absorben energía en microondas/radiofrecuencia.", "consecuencia_de_error": "Calentamiento indeseado de aislantes en alta frecuencia."}
                }
            }
        ]
    },

    "QUIM-03": {
        "nombre_completo": "Estequiometría: El Cálculo de la Materia",
        "prerequisitos": ["QUIM-02"],
        "quiz": [
            {
                "pregunta": "¿Qué ley fundamental obliga a balancear las ecuaciones químicas?",
                "respuesta": "conservacion de la materia",
                "opciones": ["conservacion de la materia", "ley de la gravedad", "ley de ohm", "termodinamica"]
            },
            {
                "pregunta": "El reactivo que se acaba primero y detiene la reacción se llama...",
                "respuesta": "limitante",
                "opciones": ["limitante", "en exceso", "catalizador", "producto"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. El Mol y el Número de Avogadro",
                "definicion": "Los átomos son demasiado pequeños para contarlos uno por uno. El 'Mol' es la unidad de conteo del químico (como una 'docena' o una 'resma'). 1 Mol = 6.022 x 10²³ partículas (Número de Avogadro). Permite pasar del mundo microscópico (átomos) al macroscópico (gramos).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: ¿Cuántos átomos hay en 2 moles de Hierro?\n2 moles * (6.022 x 10²³ átomos/mol) = 1.2044 x 10²⁴ átomos.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si tienes 0.5 moles de un gas, ¿cuántas partículas tienes? (mitad de Avogadro: 3.011x10^23)",
                        "respuesta_correcta": "3.011x10^23",
                        "opciones": ["3.011x10^23", "6.022x10^23", "1.5x10^23", "12x10^23"]
                    },
                    "similares": [
                        {"pregunta": "El número 6.022 x 10^23 se conoce como Número de...", "respuesta_correcta": "avogadro", "opciones": ["avogadro", "newton", "bohr", "dalton"]},
                        {"pregunta": "Un mol de Agua y un mol de Oro tienen el mismo número de partículas. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Un mol de Agua y un mol de Oro pesan lo mismo. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "¿Qué unidad mide la 'cantidad de sustancia' en el SI?", "respuesta_correcta": "mol", "opciones": ["mol", "kg", "litro", "gramo"]},
                        {"pregunta": "Para pesar átomos en un laboratorio, usamos la unidad de...", "respuesta_correcta": "gramos", "opciones": ["gramos", "umas", "toneladas", "libras"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de datos masivos. Un mol es análogo a un 'Exabyte' de datos; una unidad enorme para manejar cantidades inmensas de bits individuales.", "consecuencia_de_error": "Desbordamiento de memoria (Buffer Overflow) al no dimensionar la cantidad de datos."},
                    "quimica": {"uso": "Conversión fundamental. Sin el mol, no podríamos relacionar lo que pesa una balanza (gramos) con la reacción química (átomos).", "consecuencia_de_error": "Imposible realizar cualquier experimento cuantitativo."},
                    "civil": {"uso": "Materiales a nanoescala. Entender que en un gramo de nanotubos de carbono hay trillones de estructuras individuales.", "consecuencia_de_error": "Mal cálculo de propiedades en materiales avanzados."},
                    "mecanica": {"uso": "Gases ideales (PV=nRT). La 'n' son los moles. La presión de un neumático depende de la cantidad de moles de aire dentro.", "consecuencia_de_error": "Explosión de neumáticos o recipientes a presión."},
                    "mecatronica": {"uso": "Fabricación de semiconductores. Se cuenta el número exacto de átomos de dopante (impurezas) por centímetro cúbico.", "consecuencia_de_error": "Chips defectuosos que no conducen electricidad correctamente."},
                    "aeronautica": {"uso": "Atmósfera estándar. La densidad del aire (moles por volumen) disminuye con la altura, afectando el rendimiento del motor.", "consecuencia_de_error": "Cálculo erróneo de la sustentación y empuje a gran altitud."},
                    "electrica": {"uso": "Carga eléctrica (Faraday). 1 Mol de electrones tiene una carga de 96,485 Coulombs (Constante de Faraday).", "consecuencia_de_error": "Cálculo erróneo de la duración de una batería."}
                }
            },
            {
                "subtema_titulo": "2. Masa Molar (g/mol)",
                "definicion": "Es el puente entre el Mol y los Gramos. Es lo que pesa 1 mol de una sustancia. Se calcula sumando las masas atómicas de la Tabla Periódica.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Masa molar del Ácido Sulfúrico (H₂SO₄).\nH (1g) x 2 + S (32g) x 1 + O (16g) x 4\n= 2 + 32 + 64 = 98 g/mol. (1 mol pesa 98g).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Calcula la masa molar del Metano (CH₄). (C=12, H=1)",
                        "respuesta_correcta": "16",
                        "opciones": ["16", "13", "18", "20"]
                    },
                    "similares": [
                        {"pregunta": "Masa molar del Agua (H₂O). (H=1, O=16)", "respuesta_correcta": "18", "opciones": ["18", "17", "20", "16"]},
                        {"pregunta": "Masa molar del Dióxido de Carbono (CO₂). (C=12, O=16)", "respuesta_correcta": "44", "opciones": ["44", "28", "32", "14"]},
                        {"pregunta": "Si tienes 44g de CO₂, ¿cuántos moles tienes?", "respuesta_correcta": "1", "opciones": ["1", "2", "0.5", "10"]},
                        {"pregunta": "Masa molar del Oxígeno gaseoso (O₂). (O=16)", "respuesta_correcta": "32", "opciones": ["32", "16", "8", "48"]},
                        {"pregunta": "Para convertir de gramos a moles, se ... por la masa molar.", "respuesta_correcta": "divide", "opciones": ["divide", "multiplica", "suma", "resta"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Compresión de archivos. Un archivo 'zip' (mol) tiene un tamaño definido. Si sabes el tamaño total y el del zip, sabes cuántos archivos hay.", "consecuencia_de_error": "Estimación incorrecta de espacio en disco."},
                    "quimica": {"uso": "Preparación de soluciones. Para hacer una solución 1M de NaCl, necesito pesar exactamente 58.44g.", "consecuencia_de_error": "Reactivos con concentración incorrecta, reacción fallida."},
                    "civil": {"uso": "Curado del concreto. Calcular cuánta agua se necesita para hidratar 'x' kilos de cemento basándose en su composición química.", "consecuencia_de_error": "Concreto quebradizo por falta de agua o poroso por exceso."},
                    "mecanica": {"uso": "Emisiones de CO₂. Un auto quema 'x' gramos de gasolina (C₈H₁₈). La masa molar permite calcular cuántos gramos de CO₂ salen por el escape.", "consecuencia_de_error": "Incumplimiento de normativas ambientales (Euro 6, EPA)."},
                    "mecatronica": {"uso": "Sensores de gases (ppm). Los sensores a menudo detectan moles, pero las normas de seguridad están en mg/m³ (gramos).", "consecuencia_de_error": "Falsa sensación de seguridad ante gases tóxicos."},
                    "aeronautica": {"uso": "Combustible de cohetes. El empuje depende de la masa molar de los gases de escape (mientras menor sea la masa molar, mayor el empuje, ej. H₂).", "consecuencia_de_error": "Diseño ineficiente de toberas de cohete."},
                    "electrica": {"uso": "Electrodeposición (Chapado). Cuántos gramos de oro se depositan por cada mol de electrones que pasa.", "consecuencia_de_error": "Recubrimiento de oro demasiado delgado o costoso."}
                }
            },
            {
                "subtema_titulo": "3. Balanceo de Ecuaciones (La Receta)",
                "definicion": "La materia no se crea ni se destruye. Una ecuación química debe tener el MISMO número de átomos de cada elemento a la izquierda (reactivos) y a la derecha (productos). Se ajustan los COEFICIENTES (números grandes al frente).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Combustión de Propano. C₃H₈ + O₂ -> CO₂ + H₂O\n1. C: 3 izq -> Poner 3 en CO₂.\n2. H: 8 izq -> Poner 4 en H₂O (4*2=8).\n3. O: Der tiene (3*2) + (4*1) = 10. Poner 5 en O₂.\nResultado: C₃H₈ + 5O₂ -> 3CO₂ + 4H₂O.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Balancea: H₂ + Cl₂ -> __ HCl. (Coeficiente faltante)",
                        "respuesta_correcta": "2",
                        "opciones": ["2", "1", "3", "4"]
                    },
                    "similares": [
                        {"pregunta": "Balancea: __ Mg + O₂ -> 2MgO.", "respuesta_correcta": "2", "opciones": ["2", "1", "4", "3"]},
                        {"pregunta": "En 2H₂ + O₂ -> 2H₂O, hay ... átomos de Hidrógeno en total a cada lado.", "respuesta_correcta": "4", "opciones": ["4", "2", "8", "6"]},
                        {"pregunta": "Balancea: N₂ + __ H₂ -> 2NH₃.", "respuesta_correcta": "3", "opciones": ["3", "2", "1", "6"]},
                        {"pregunta": "Los subíndices (números pequeños) se pueden cambiar al balancear. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "La ecuación debe cumplir la Ley de Conservación de la...", "respuesta_correcta": "materia", "opciones": ["materia", "energia", "carga", "velocidad"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Balanceo de carga en servidores. Las peticiones que entran (inputs) deben ser procesadas y salir (outputs) sin perderse.", "consecuencia_de_error": "Servidor colapsado o pérdida de datos (dropped packets)."},
                    "quimica": {"uso": "Es el paso 0. No se puede calcular nada sin la ecuación balanceada.", "consecuencia_de_error": "Cálculos estequiométricos totalmente erróneos."},
                    "civil": {"uso": "Tratamiento de aguas. Neutralización de ácido: HCl + NaOH -> NaCl + H₂O. Necesitas proporciones exactas 1:1.", "consecuencia_de_error": "Agua potable que sale ácida o básica a la ciudad."},
                    "mecanica": {"uso": "Relación estequiométrica Aire/Combustible (AFR). Para gasolina es 14.7:1 (masa). Viene de balancear C₈H₁₈ + O₂.", "consecuencia_de_error": "Motor que contamina mucho o pierde potencia."},
                    "mecatronica": {"uso": "Control de procesos. Si entran 10 kg/s de material A y 5 kg/s de B, deben salir 15 kg/s de producto.", "consecuencia_de_error": "Desborde de tanques o reactores."},
                    "aeronautica": {"uso": "Combustión en turbinas. Balancear para asegurar que todo el combustible se queme dentro de la cámara y no en la turbina.", "consecuencia_de_error": "Fuego en la tobera y daño a los álabes."},
                    "electrica": {"uso": "Reacciones redox en baterías. Pb + PbO₂ + 2H₂SO₄ -> 2PbSO₄ + 2H₂O. El balanceo dice cuántos electrones se mueven.", "consecuencia_de_error": "Mal cálculo de la capacidad de la batería."}
                }
            },
            {
                "subtema_titulo": "4. Cálculos Estequiométricos (El Mapa del Tesoro)",
                "definicion": "Pasos para resolver cualquier problema: 1. Convertir dato conocido a MOLES. 2. Usar coeficientes de la ecuación balanceada (Relación Mol-Mol). 3. Convertir resultado a la unidad deseada (Gramos, Litros, etc.). ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: 2H₂ + O₂ -> 2H₂O. ¿Cuántos gramos de H₂O produce 4g de H₂?\n1. Moles H₂: 4g / 2g/mol = 2 moles H₂.\n2. Relación: 2 moles H₂ producen 2 moles H₂O (1:1). -> Tenemos 2 moles H₂O.\n3. Gramos H₂O: 2 moles * 18g/mol = 36g H₂O.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Ec: C + O₂ -> CO₂. ¿Cuántos moles de CO₂ producen 3 moles de Carbono?",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "1", "12", "44"]
                    },
                    "similares": [
                        {"pregunta": "Ec: 2Na + Cl₂ -> 2NaCl. 2 moles de Na producen ... moles de NaCl.", "respuesta_correcta": "2", "opciones": ["2", "1", "4", "0.5"]},
                        {"pregunta": "Ec: N₂ + 3H₂ -> 2NH₃. 3 moles de H₂ producen ... moles de NH₃.", "respuesta_correcta": "2", "opciones": ["2", "3", "1", "6"]},
                        {"pregunta": "El primer paso en estequiometría siempre es convertir a...", "respuesta_correcta": "moles", "opciones": ["moles", "gramos", "litros", "atomos"]},
                        {"pregunta": "La relación molar se saca de los ... de la ecuación balanceada.", "respuesta_correcta": "coeficientes", "opciones": ["coeficientes", "subindices", "pesos", "volumenes"]},
                        {"pregunta": "Si 1 mol de A produce 2 de B. 5 moles de A producen ... de B.", "respuesta_correcta": "10", "opciones": ["10", "5", "2.5", "20"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Gestión de recursos. 'Si 1 usuario consume 20MB de RAM, ¿cuánta RAM necesito para 1000 usuarios?'", "consecuencia_de_error": "Caída del servidor por falta de memoria."},
                    "quimica": {"uso": "Producción industrial. Calcular cuántas toneladas de materia prima comprar para cumplir un pedido de producto.", "consecuencia_de_error": "Faltante de producto o exceso de inventario costoso."},
                    "civil": {"uso": "Explosivos en demolición/minería. Calcular la cantidad exacta de explosivo para mover X toneladas de roca.", "consecuencia_de_error": "Explosión insuficiente o daño a estructuras vecinas."},
                    "mecanica": {"uso": "Convertidores catalíticos. Calcular la superficie de platino necesaria para convertir los gases de escape de un motor de X litros.", "consecuencia_de_error": "Vehículo no pasa la verificación vehicular."},
                    "mecatronica": {"uso": "Dosificación automática de medicamentos. El robot calcula volumen basado en la concentración y dosis requerida.", "consecuencia_de_error": "Sobredosis o subdosificación del paciente."},
                    "aeronautica": {"uso": "Sistemas de soporte vital (ISS). Calcular cuánto LiOH se necesita para absorber el CO₂ exhalado por 3 astronautas en 6 meses.", "consecuencia_de_error": "Acumulación de CO₂ mortal en la estación espacial."},
                    "electrica": {"uso": "Producción de Hidrógeno por electrólisis. Calcular cuánta agua y electricidad se necesitan para llenar un tanque de H₂.", "consecuencia_de_error": "Diseño ineficiente de la planta de electrólisis."}
                }
            },
            {
                "subtema_titulo": "5. Reactivo Limitante (El Cuello de Botella)",
                "definicion": "El reactivo que se acaba primero determina cuánto producto se forma. El otro reactivo queda 'en exceso'. Es como hacer sándwiches: si tienes 100 panes y 1 jamón, solo puedes hacer 1 sándwich. El jamón es el limitante. ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: N₂ + 3H₂ -> 2NH₃. Tienes 2 moles N₂ y 3 moles H₂.\n- N₂ necesita 3 H₂ por cada 1. Con 2 N₂ necesitarías 6 H₂. Solo tienes 3.\n- ¡Falta H₂! El H₂ es el limitante. Se formarán 2 moles de NH₃ (basado en el H₂).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para hacer bicis (1 cuadro + 2 ruedas). Tienes 5 cuadros y 8 ruedas. ¿Cuántas bicis puedes armar?",
                        "respuesta_correcta": "4",
                        "opciones": ["4", "5", "8", "2.5"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuál es el reactivo limitante en el ejemplo de las bicis?", "respuesta_correcta": "ruedas", "opciones": ["ruedas", "cuadros", "ambos", "ninguno"]},
                        {"pregunta": "El reactivo en exceso es el que...", "respuesta_correcta": "sobra", "opciones": ["sobra", "falta", "limita", "reacciona"]},
                        {"pregunta": "La cantidad de producto depende del reactivo...", "respuesta_correcta": "limitante", "opciones": ["limitante", "exceso", "mayor", "menor"]},
                        {"pregunta": "Ec: A + B -> C. Tienes 5 moles A y 100 moles B. Limitante:", "respuesta_correcta": "a", "opciones": ["a", "b", "c", "ninguno"]},
                        {"pregunta": "Identificar el limitante es crucial para calcular el rendimiento teórico. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Cuellos de botella (Bottlenecks). En una PC, si el CPU es rápido pero el Disco Duro es lento, el sistema es lento. El disco es el limitante.", "consecuencia_de_error": "Gastar dinero mejorando el componente equivocado (CPU)."},
                    "quimica": {"uso": "Optimización de costos. Se diseña la reacción para que el reactivo más caro sea el limitante (se consuma todo) y el barato sobre.", "consecuencia_de_error": "Tirar reactivo caro a la basura (en exceso)."},
                    "civil": {"uso": "Cronograma de obra (Ruta Crítica). La tarea que retrasa todo el proyecto es la 'limitante'.", "consecuencia_de_error": "Retrasos en la entrega del edificio."},
                    "mecanica": {"uso": "Combustión pobre/rica. En un auto, si hay poco aire (limitante), la gasolina no se quema bien (exceso) y sale humo negro.", "consecuencia_de_error": "Contaminación y desperdicio de combustible."},
                    "mecatronica": {"uso": "Líneas de ensamblaje. La estación más lenta define la velocidad de toda la línea.", "consecuencia_de_error": "Acumulación de piezas en una estación y robots parados en otras."},
                    "aeronautica": {"uso": "Motores Cohete. Se ajusta la mezcla para que sea 'rica en combustible' (oxidante limitante) para bajar la temperatura y proteger la tobera.", "consecuencia_de_error": "Tobera derretida por exceso de temperatura."},
                    "electrica": {"uso": "Capacidad de Baterías. La reacción se detiene cuando se agota el material activo en el ánodo o cátodo (el limitante).", "consecuencia_de_error": "Batería que muere súbitamente."}
                }
            },
            {
                "subtema_titulo": "6. Rendimiento Porcentual (Eficiencia)",
                "definicion": "En papel todo es perfecto (Rendimiento Teórico), pero en la realidad hay pérdidas. Rendimiento % = (Real / Teórico) * 100. Nunca es > 100%.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Calculaste que obtendrías 100g de producto (Teórico), pero al pesarlo en el laboratorio solo obtuviste 80g (Real).\n% Rendimiento = (80 / 100) * 100 = 80%.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Esperabas 50g y obtuviste 25g. ¿Cuál es el % de rendimiento?",
                        "respuesta_correcta": "50",
                        "opciones": ["50", "25", "75", "200"]
                    },
                    "similares": [
                        {"pregunta": "El rendimiento real suele ser ... que el teórico.", "respuesta_correcta": "menor", "opciones": ["menor", "mayor", "igual", "doble"]},
                        {"pregunta": "¿Es posible obtener 110% de rendimiento real? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Si el rendimiento es bajo, indica que el proceso es...", "respuesta_correcta": "ineficiente", "opciones": ["ineficiente", "perfecto", "rapido", "exotermico"]},
                        {"pregunta": "Cálculo: (Real / Teórico) * 100.", "respuesta_correcta": "rendimiento", "opciones": ["rendimiento", "error", "pureza", "masa"]},
                        {"pregunta": "Pérdidas al trasvasar líquidos afectan el rendimiento... (real/teórico)", "respuesta_correcta": "real", "opciones": ["real", "teorico", "ambos", "ninguno"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Throughput de red. Ancho de banda teórico (1 Gbps) vs Real (600 Mbps). Eficiencia del 60%.", "consecuencia_de_error": "Prometer velocidades de internet que no se pueden cumplir."},
                    "quimica": {"uso": "Industria Farmacéutica. Un bajo rendimiento en la síntesis de un medicamento encarece enormemente el precio final.", "consecuencia_de_error": "Medicamentos impagables o procesos no viables."},
                    "civil": {"uso": "Desperdicio de material. Compras 100 ladrillos, se rompen 5. Rendimiento de instalación 95%.", "consecuencia_de_error": "Quedarse corto de material a mitad de la obra."},
                    "mecanica": {"uso": "Eficiencia Térmica de un motor. Energía del combustible vs Energía de movimiento. (Típico 25-30%).", "consecuencia_de_error": "Alto consumo de combustible."},
                    "mecatronica": {"uso": "Eficiencia de paneles solares. Energía solar incidente vs Electricidad generada (aprox 20%).", "consecuencia_de_error": "Paneles insuficientes para alimentar el sistema."},
                    "aeronautica": {"uso": "Eficiencia propulsiva. Cuánta energía del jet se convierte en empuje útil.", "consecuencia_de_error": "Diseño de motores ruidosos e ineficientes."},
                    "electrica": {"uso": "Eficiencia de transformadores. Potencia Entrada vs Salida. Un buen trafo tiene >95%.", "consecuencia_de_error": "Calor excesivo y desperdicio de energía eléctrica."}
                }
            },
            {
                "subtema_titulo": "7. Fórmula Empírica y Molecular",
                "definicion": "Fórmula Empírica: La proporción más simple de átomos (ej. CH₂O). Fórmula Molecular: La cantidad real en la molécula (ej. C₆H₁₂O₆, glucosa). Es la 'ingeniería inversa' de una sustancia desconocida.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Análisis dice que hay 1 Carbono por cada 2 Hidrógenos. Empírica: CH₂.\nSi la masa molar real es 28 g/mol (y CH₂ pesa 14), la molécula real es el doble: C₂H₄ (Etileno).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La fórmula empírica del Peróxido de Hidrógeno (H₂O₂) es...",
                        "respuesta_correcta": "HO",
                        "opciones": ["HO", "H2O", "HO2", "H2O2"]
                    },
                    "similares": [
                        {"pregunta": "La fórmula molecular es siempre un múltiplo entero de la empírica. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Fórmula empírica de C₂H₆ (Etano).", "respuesta_correcta": "CH3", "opciones": ["CH3", "CH2", "C2H6", "CH"]},
                        {"pregunta": "Fórmula empírica de la Glucosa (C₆H₁₂O₆).", "respuesta_correcta": "CH2O", "opciones": ["CH2O", "CHO", "C6H12O6", "C2H4O2"]},
                        {"pregunta": "Si la empírica es CH y la masa molecular es 78, la fórmula es C...H...", "respuesta_correcta": "C6H6", "opciones": ["C6H6", "C2H2", "C5H5", "CH"]},
                        {"pregunta": "Se usa para identificar sustancias desconocidas en criminalística. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Compresión de datos. Empírica es el patrón comprimido, Molecular es el archivo original expandido.", "consecuencia_de_error": "Pérdida de información al descomprimir."},
                    "quimica": {"uso": "Análisis forense y control de calidad. Determinar qué polvo blanco desconocido se encontró en la escena.", "consecuencia_de_error": "Identificación errónea de drogas o venenos."},
                    "civil": {"uso": "Análisis de cemento antiguo en restauración. Determinar la composición original para replicarla.", "consecuencia_de_error": "Usar un mortero incompatible que dañe el edificio histórico."},
                    "mecanica": {"uso": "Análisis de fallas. Analizar la composición de una pieza rota para ver si el proveedor usó la aleación correcta.", "consecuencia_de_error": "Repetir la falla por no detectar material fraudulento."},
                    "mecatronica": {"uso": "Ingeniería inversa de chips. Analizar las capas de materiales semiconductores para entender cómo fue fabricado.", "consecuencia_de_error": "Violación de patentes o copia fallida."},
                    "aeronautica": {"uso": "Investigación de accidentes. Analizar residuos de combustión para ver si hubo explosivos o fallo de motor.", "consecuencia_de_error": "Conclusiones erróneas sobre la causa del accidente."},
                    "electrica": {"uso": "Análisis de aceites de transformador. Detectar gases disueltos (proporciones moleculares) para predecir fallas internas.", "consecuencia_de_error": "Explosión de transformador no prevista."}
                }
            }
        ]
    },

    "QUIM-04": {
        "nombre_completo": "Nomenclatura Inorgánica: El Lenguaje de la Química",
        "prerequisitos": ["QUIM-03"],
        "quiz": [
            {
                "pregunta": "¿Cuál es el nombre del compuesto HCl (en agua)?",
                "respuesta": "acido clorhidrico",
                "opciones": ["acido clorhidrico", "cloruro de hidrogeno", "cloro liquido", "acido clorico"]
            },
            {
                "pregunta": "El compuesto NaOH es una 'base' o 'hidróxido', ¿cuál es su nombre?",
                "respuesta": "hidroxido de sodio",
                "opciones": ["hidroxido de sodio", "oxido de sodio", "hidruro de sodio", "sosa acida"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Estados de Oxidación (La base del nombre)",
                "definicion": "Es un número (positivo o negativo) que indica la carga aparente de un átomo en un compuesto. Es la clave para saber cómo combinar los átomos. Reglas: O casi siempre es -2, H es +1, Elementos libres son 0.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Calcular el estado del Azufre (S) en H₂SO₄.\n1. H: +1 (x2 = +2). O: -2 (x4 = -8).\n2. Suma total debe ser 0: (+2) + S + (-8) = 0.\n3. S - 6 = 0 -> S = +6.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el estado de oxidación del Carbono en el CO₂? (O=-2)",
                        "respuesta_correcta": "+4",
                        "opciones": ["+4", "+2", "-4", "0"]
                    },
                    "similares": [
                        {"pregunta": "Estado de oxidación del Oxígeno en la mayoría de compuestos.", "respuesta_correcta": "-2", "opciones": ["-2", "-1", "+1", "+2"]},
                        {"pregunta": "Estado de oxidación del Sodio (Grupo 1) en sales.", "respuesta_correcta": "+1", "opciones": ["+1", "+2", "-1", "0"]},
                        {"pregunta": "Estado de oxidación del N en el NH₃ (H=+1).", "respuesta_correcta": "-3", "opciones": ["-3", "+3", "+5", "0"]},
                        {"pregunta": "La suma de los estados de oxidación en una molécula neutra es...", "respuesta_correcta": "0", "opciones": ["0", "1", "-1", "variable"]},
                        {"pregunta": "Estado de oxidación del Cloro en NaCl.", "respuesta_correcta": "-1", "opciones": ["-1", "+1", "+7", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Lógica de estados. Análogo a definir el 'tipo' de variable (signed/unsigned). Define la capacidad de combinación.", "consecuencia_de_error": "Imposible predecir la fórmula química."},
                    "quimica": {"uso": "Balanceo Redox. Las reacciones de óxido-reducción se basan enteramente en el cambio de este número.", "consecuencia_de_error": "No poder balancear reacciones de baterías o combustión."},
                    "civil": {"uso": "Corrosión. El hierro pasa de Fe(0) a Fe(+2) y Fe(+3). El estado de oxidación te dice qué tan oxidado está el metal.", "consecuencia_de_error": "Fallo en el diagnóstico de patologías del concreto."},
                    "mecanica": {"uso": "Tratamientos térmicos. Entender cómo la atmósfera del horno (reductora vs oxidante) afecta la superficie del acero.", "consecuencia_de_error": "Piezas con la dureza superficial incorrecta."},
                    "mecatronica": {"uso": "Sensores electroquímicos. El voltaje que lee el sensor depende directamente del cambio de estado de oxidación en el electrodo.", "consecuencia_de_error": "Calibración errónea del sensor."},
                    "aeronautica": {"uso": "Anodizado. Se fuerza al Aluminio a un estado de oxidación específico (Al₂O₃) para protegerlo.", "consecuencia_de_error": "Piezas de aluminio que se corroen en ambiente salino."},
                    "electrica": {"uso": "Potencial de celda. El voltaje de una batería es la diferencia de potencial de oxidación entre dos metales.", "consecuencia_de_error": "Selección incorrecta de materiales para ánodo/cátodo."}
                }
            },
            {
                "subtema_titulo": "2. Óxidos Básicos y Ácidos (Anhídridos)",
                "definicion": "Compuestos binarios con Oxígeno.\n- Óxido Básico: Metal + O (ej. CaO). Reacciona con agua para formar Bases.\n- Óxido Ácido: No Metal + O (ej. SO₃). Reacciona con agua para formar Ácidos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Fe₂O₃ (Hierro +3, Oxígeno -2).\nNombre Stock: Óxido de Hierro (III).\nNombre Tradicional: Óxido Férrico ('ico' para la valencia mayor del hierro, 3).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Nombra el compuesto CO (Monóxido de Carbono). ¿Es un óxido básico o ácido?",
                        "respuesta_correcta": "acido",
                        "opciones": ["acido", "basico", "neutro", "sal"]
                    },
                    "similares": [
                        {"pregunta": "El compuesto Na₂O se llama Óxido de...", "respuesta_correcta": "sodio", "opciones": ["sodio", "potasio", "nitrogeno", "azufre"]},
                        {"pregunta": "El SO₂ es un óxido... (básico/ácido)", "respuesta_correcta": "acido", "opciones": ["acido", "basico", "anfotero", "neutro"]},
                        {"pregunta": "Nombre común del Fe₂O₃ (lo que le pasa a los clavos viejos).", "respuesta_correcta": "oxido", "opciones": ["oxido", "sal", "acido", "base"]},
                        {"pregunta": "Fórmula del Óxido de Calcio (Cal viva).", "respuesta_correcta": "CaO", "opciones": ["CaO", "Ca2O", "CaO2", "CaOH"]},
                        {"pregunta": "Los óxidos de no metales causan la lluvia... (ácida/básica)", "respuesta_correcta": "acida", "opciones": ["acida", "basica", "neutra", "salina"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Fabricación de chips. El SiO₂ (Óxido de Silicio) es el aislante fundamental en los transistores (MOSFET).", "consecuencia_de_error": "Cortocircuitos dentro del microprocesador."},
                    "quimica": {"uso": "Catálisis. Muchos catalizadores industriales son óxidos metálicos (ej. TiO₂, V₂O₅).", "consecuencia_de_error": "Procesos químicos lentos o ineficientes."},
                    "civil": {"uso": "Cemento. Es una mezcla compleja de óxidos de Calcio, Silicio y Aluminio.", "consecuencia_de_error": "Hormigón sin resistencia estructural."},
                    "mecanica": {"uso": "Abrasivos. La Alúmina (Al₂O₃) es un óxido muy duro usado en lijas y discos de corte.", "consecuencia_de_error": "Herramientas que no cortan el material."},
                    "mecatronica": {"uso": "Varistores (MOV). Hechos de Óxido de Zinc (ZnO), protegen circuitos contra picos de voltaje.", "consecuencia_de_error": "Circuitos quemados por descargas eléctricas."},
                    "aeronautica": {"uso": "Cerámicas técnicas. Óxidos que soportan temperaturas de motor jet donde los metales se funden.", "consecuencia_de_error": "Fallo catastrófico de turbinas."},
                    "electrica": {"uso": "Superconductores de alta temperatura. Son cerámicas complejas de óxidos de cobre (YBCO).", "consecuencia_de_error": "Pérdida de la propiedad superconductora."}
                }
            },
            {
                "subtema_titulo": "3. Hidróxidos (Bases)",
                "definicion": "Se forman cuando un Óxido Básico reacciona con agua. Tienen el grupo funcional OH⁻ (Hidroxilo). Son jabonosos y tienen pH > 7. Fórmula general: M(OH)ₙ.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Mg(OH)₂.\nMagnesio (+2) y OH (-1). Se cruzan las valencias.\nNombre: Hidróxido de Magnesio (Leche de magnesia).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué compuesto se usa para destapar cañerías (NaOH)?",
                        "respuesta_correcta": "hidroxido de sodio",
                        "opciones": ["hidroxido de sodio", "acido clorhidrico", "cloruro de sodio", "amoniaco"]
                    },
                    "similares": [
                        {"pregunta": "Fórmula del Hidróxido de Calcio (Cal apagada).", "respuesta_correcta": "Ca(OH)2", "opciones": ["Ca(OH)2", "CaOH", "Ca2OH", "CaO"]},
                        {"pregunta": "El grupo OH tiene carga...", "respuesta_correcta": "-1", "opciones": ["-1", "+1", "-2", "0"]},
                        {"pregunta": "Los hidróxidos neutralizan a los...", "respuesta_correcta": "acidos", "opciones": ["acidos", "sales", "oxidos", "gases"]},
                        {"pregunta": "Nombre de Al(OH)₃.", "respuesta_correcta": "hidroxido de aluminio", "opciones": ["hidroxido de aluminio", "oxido de aluminio", "hidruro de aluminio", "aluminato"]},
                        {"pregunta": "Las bases vuelven el papel tornasol de color...", "respuesta_correcta": "azul", "opciones": ["azul", "rojo", "verde", "amarillo"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Grabado húmedo (Wet Etching). El KOH (Hidróxido de Potasio) graba el Silicio cristalográficamente.", "consecuencia_de_error": "Estructuras MEMS (sensores) mal formadas."},
                    "quimica": {"uso": "Saponificación. Grasas + NaOH = Jabón + Glicerina.", "consecuencia_de_error": "Jabón cáustico que quema la piel."},
                    "civil": {"uso": "Estabilización de suelos. Se mezcla tierra arcillosa con Cal (Ca(OH)₂) para endurecerla antes de construir carreteras.", "consecuencia_de_error": "Carreteras que se hunden por suelo inestable."},
                    "mecanica": {"uso": "Lubricantes. Las grasas de litio son aceites espesados con jabones de LiOH.", "consecuencia_de_error": "Grasa que se escurre y deja de lubricar."},
                    "mecatronica": {"uso": "Baterías Alcalinas. El electrolito es una pasta de KOH (base fuerte).", "consecuencia_de_error": "Fugas de la batería que corroen los contactos del robot."},
                    "aeronautica": {"uso": "Decapado de pintura. Los removedores de pintura de aviación suelen ser fuertemente alcalinos.", "consecuencia_de_error": "Daño al sustrato de aluminio si no se neutraliza."},
                    "electrica": {"uso": "Neutralización de derrames de ácido de baterías en bancos de respaldo (UPS).", "consecuencia_de_error": "Daño ambiental y corrosión del piso de la subestación."}
                }
            },
            {
                "subtema_titulo": "4. Ácidos (Hidrácidos y Oxiácidos)",
                "definicion": "Sustancias que liberan H⁺ en agua. pH < 7.\n- Hidrácidos: H + No Metal (sin oxígeno). Ej: HCl (Ácido Clorhídrico).\n- Oxiácidos: H + No Metal + O. Ej: H₂SO₄ (Ácido Sulfúrico).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Nombrar HNO₃ (N con valencia +5, la mayor).\nEs un oxiácido del Nitrógeno.\nTerminación 'ico' para la mayor. -> Ácido Nítrico.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Fórmula del ácido estomacal (Ácido Clorhídrico).",
                        "respuesta_correcta": "HCl",
                        "opciones": ["HCl", "H2SO4", "HNO3", "HF"]
                    },
                    "similares": [
                        {"pregunta": "El H₂SO₄ es el ácido...", "respuesta_correcta": "sulfurico", "opciones": ["sulfurico", "sulfuroso", "sulfhidrico", "persulfurico"]},
                        {"pregunta": "Los ácidos vuelven el papel tornasol de color...", "respuesta_correcta": "rojo", "opciones": ["rojo", "azul", "verde", "negro"]},
                        {"pregunta": "El ácido usado en baterías de auto es el...", "respuesta_correcta": "sulfurico", "opciones": ["sulfurico", "clorhidrico", "citrico", "acetico"]},
                        {"pregunta": "Ácido derivado del CO₂ (presente en refrescos).", "respuesta_correcta": "carbonico", "opciones": ["carbonico", "carboxilico", "carburoso", "acetico"]},
                        {"pregunta": "Terminación de sal para un ácido 'hídrico' (ej. Clorhídrico -> Clor...)", "respuesta_correcta": "uro", "opciones": ["uro", "ato", "ito", "ico"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Grabado de PCB. El Cloruro Férrico en medio ácido disuelve el cobre para crear las pistas.", "consecuencia_de_error": "Pistas en corto o circuitos abiertos."},
                    "quimica": {"uso": "El rey de la industria. El H₂SO₄ se usa para refinar petróleo, hacer fertilizantes y plásticos.", "consecuencia_de_error": "Indicador de bajo desarrollo industrial."},
                    "civil": {"uso": "Ataque ácido al concreto. Aguas residuales o lluvia ácida reaccionan con la cal del cemento, desintegrándolo.", "consecuencia_de_error": "Tuberías de drenaje de concreto que colapsan."},
                    "mecanica": {"uso": "Pickling (Decapado). Baño en ácido para quitar óxido al acero antes de soldar o pintar.", "consecuencia_de_error": "Mala soldadura o pintura que se cae."},
                    "mecatronica": {"uso": "Baterías de Plomo-Ácido. El electrolito es H₂SO₄. Su densidad indica la carga.", "consecuencia_de_error": "Batería muerta o sulfatada."},
                    "aeronautica": {"uso": "Anodizado del aluminio. Se hace sumergiendo la pieza en ácido sulfúrico y aplicando corriente.", "consecuencia_de_error": "Piezas sin protección contra la corrosión."},
                    "electrica": {"uso": "Limpieza de contactos. Ácidos débiles para quitar óxido de cobre en conectores viejos.", "consecuencia_de_error": "Alta resistencia de contacto y calentamiento."}
                }
            },
            {
                "subtema_titulo": "5. Sales Binarias (Neutras)",
                "definicion": "Metal + No Metal. Se forman al sustituir el H de un Hidrácido por un Metal. Terminación 'URO'. No tienen oxígeno.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Na + Cl -> NaCl (Cloruro de Sodio).\nEjemplo: Fe + S -> FeS (Sulfuro de Hierro (II)).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Nombra el compuesto KI (Potasio y Yodo).",
                        "respuesta_correcta": "yoduro de potasio",
                        "opciones": ["yoduro de potasio", "yodato de potasio", "potasio de yodo", "sal de yodo"]
                    },
                    "similares": [
                        {"pregunta": "CaCl₂ se llama... de Calcio.", "respuesta_correcta": "cloruro", "opciones": ["cloruro", "clorato", "clorito", "clorhidrico"]},
                        {"pregunta": "La terminación 'uro' indica ausencia de...", "respuesta_correcta": "oxigeno", "opciones": ["oxigeno", "metal", "hidrogeno", "enlace"]},
                        {"pregunta": "AgBr (usado en fotografía antigua) es Bromuro de...", "respuesta_correcta": "plata", "opciones": ["plata", "oro", "mercurio", "cobre"]},
                        {"pregunta": "Las sales binarias son compuestos iónicos. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "AlCl₃ es Cloruro de...", "respuesta_correcta": "aluminio", "opciones": ["aluminio", "hierro", "sodio", "potasio"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Sensores infrarrojos. Usan sales como PbS (Sulfuro de Plomo) para detectar calor.", "consecuencia_de_error": "Cámaras térmicas ciegas."},
                    "quimica": {"uso": "Reactivos de precipitación. AgNO₃ + NaCl -> AgCl (sólido blanco).", "consecuencia_de_error": "Análisis químico cualitativo fallido."},
                    "civil": {"uso": "Sales de deshielo (CaCl₂). Bajan el punto de congelación del agua en carreteras.", "consecuencia_de_error": "Corrosión acelerada de puentes y autos."},
                    "mecanica": {"uso": "Lubricantes sólidos. MoS₂ (Disulfuro de Molibdeno) reduce fricción a presiones extremas.", "consecuencia_de_error": "Desgaste de engranajes bajo carga pesada."},
                    "mecatronica": {"uso": "Semiconductores compuestos. GaAs (Arseniuro de Galio) para chips de alta velocidad y LEDs.", "consecuencia_de_error": "Electrónica lenta para comunicaciones 5G."},
                    "aeronautica": {"uso": "Corrosión por sales marinas (NaCl, MgCl₂) en aviones navales.", "consecuencia_de_error": "Necesidad de aleaciones especiales y lavado frecuente."},
                    "electrica": {"uso": "Electrolitos sólidos. Sales que conducen iones en estado sólido para nuevas baterías.", "consecuencia_de_error": "Baterías más seguras (sin líquido inflamable)."}
                }
            },
            {
                "subtema_titulo": "6. Oxisales (Sales con Oxígeno)",
                "definicion": "Metal + No Metal + Oxígeno. Vienen de los Oxiácidos. El H se cambia por un Metal. Terminaciones: 'ito' (menor valencia) y 'ato' (mayor valencia). Regla mnemotécnica: 'El pito del pato' (ico->ato, oso->ito).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Del Ácido Sulfúr-ico (H₂SO₄) viene el sulf-ato. Si unimos con Cobre: CuSO₄ (Sulfato de Cobre).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "El CaCO₃ (piedra caliza) se llama... de Calcio.",
                        "respuesta_correcta": "carbonato",
                        "opciones": ["carbonato", "carburo", "carbonito", "oxido"]
                    },
                    "similares": [
                        {"pregunta": "Del ácido nítrico vienen los... (nitritos/nitratos)", "respuesta_correcta": "nitratos", "opciones": ["nitratos", "nitritos", "nitruros", "nitroxidos"]},
                        {"pregunta": "CuSO₄ es Sulfato de...", "respuesta_correcta": "cobre", "opciones": ["cobre", "calcio", "carbono", "cobalto"]},
                        {"pregunta": "El Hipoclorito de Sodio (NaClO) es el ingrediente del...", "respuesta_correcta": "cloro", "opciones": ["cloro", "jabon", "acido", "alcohol"]},
                        {"pregunta": "KMnO₄ es Permanganato de...", "respuesta_correcta": "potasio", "opciones": ["potasio", "plata", "polonio", "fosforo"]},
                        {"pregunta": "Las oxisales contienen oxígeno. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Fósforos en pantallas CRT/Fluorescentes. Recubrimientos de oxisales que emiten luz.", "consecuencia_de_error": "Pantallas sin imagen."},
                    "quimica": {"uso": "Fertilizantes (Nitratos, Fosfatos, Sulfatos). Aportan N, P, K a las plantas.", "consecuencia_de_error": "Baja producción agrícola."},
                    "civil": {"uso": "Yeso (Sulfato de Calcio hidratado). Material esencial para interiores y acabados.", "consecuencia_de_error": "Paredes que se deshacen con la humedad."},
                    "mecanica": {"uso": "Fosfatado. Tratamiento superficial del acero con ácido fosfórico para evitar corrosión.", "consecuencia_de_error": "Piezas que se oxidan antes de pintarse."},
                    "mecatronica": {"uso": "Cristales piezoeléctricos (Titanato de Bario). Sensores y actuadores de precisión.", "consecuencia_de_error": "Microscopios de fuerza atómica que no funcionan."},
                    "aeronautica": {"uso": "Generadores de oxígeno químico. Clorato de sodio que libera O₂ al calentarse (máscaras de emergencia).", "consecuencia_de_error": "Falta de oxígeno en descompresión."},
                    "electrica": {"uso": "Pasta térmica. A veces usa óxidos y sales para conducir calor sin conducir electricidad.", "consecuencia_de_error": "Cortocircuito si la pasta es conductora."}
                }
            }
        ]
    },

    "QUIM-05": {
        "nombre_completo": "Soluciones y Concentración",
        "prerequisitos": ["QUIM-04"],
        "quiz": [
            {
                "pregunta": "En una solución de 'agua con sal', ¿quién es el soluto?",
                "respuesta": "sal",
                "opciones": ["sal", "agua", "ambos", "ninguno"]
            },
            {
                "pregunta": "La 'Molaridad' (M) se define como moles de soluto por ... de solución.",
                "respuesta": "litro",
                "opciones": ["litro", "kilo", "mol", "mililitro"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Soluto, Solvente y Solubilidad",
                "definicion": "Una solución es una mezcla homogénea. El 'Soluto' es lo que se disuelve (menor cantidad). El 'Solvente' es el medio que disuelve (mayor cantidad, comúnmente agua). La 'Solubilidad' es el límite máximo de soluto que el solvente acepta antes de saturarse.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Aire. Es una solución gaseosa.\nSolvente: Nitrógeno (~78%).\nSolutos: Oxígeno (~21%), Argón, CO₂.\nAunque respiramos oxígeno, químicamente 'vivimos' en una solución de Nitrógeno.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En un jarabe para la tos (azúcar en agua), el azúcar es el...",
                        "respuesta_correcta": "soluto",
                        "opciones": ["soluto", "solvente", "precipitado", "residuo"]
                    },
                    "similares": [
                        {"pregunta": "En una aleación de Bronce (Cobre + Estaño), el Cobre (mayoría) es el...", "respuesta_correcta": "solvente", "opciones": ["solvente", "soluto", "mezcla", "impureza"]},
                        {"pregunta": "Si añades más soluto del que el solvente puede disolver, la solución está...", "respuesta_correcta": "saturada", "opciones": ["saturada", "diluida", "concentrada", "insaturada"]},
                        {"pregunta": "El agua se conoce como el solvente... (universal/nulo)", "respuesta_correcta": "universal", "opciones": ["universal", "polar", "organico", "debil"]},
                        {"pregunta": "La solubilidad de los sólidos usualmente ... con la temperatura.", "respuesta_correcta": "aumenta", "opciones": ["aumenta", "disminuye", "se mantiene", "desaparece"]},
                        {"pregunta": "El 'precipitado' es soluto que no se pudo...", "respuesta_correcta": "disolver", "opciones": ["disolver", "filtrar", "evaporar", "congelar"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Limpieza de obleas de silicio. Se usan solventes ultrapuros para disolver contaminantes microscópicos (solutos) de la superficie.", "consecuencia_de_error": "Chips defectuosos por partículas de polvo."},
                    "quimica": {"uso": "Cristalización. Se satura una solución caliente y se enfría para que el soluto 'sobre' y forme cristales puros.", "consecuencia_de_error": "Imposible purificar sustancias sólidas."},
                    "civil": {"uso": "Fraguado del concreto. El agua es el solvente/reactivo. Si el agua tiene sales (solutos malos), la estructura cristalina se debilita.", "consecuencia_de_error": "Concreto que se desmorona ('cáncer del concreto')."},
                    "mecanica": {"uso": "Aleaciones. El Acero es una solución sólida de Carbono (soluto) en Hierro (solvente). Si te pasas de solubilidad, el carbono forma grafito (hierro colado).", "consecuencia_de_error": "Material frágil en lugar de dúctil."},
                    "mecatronica": {"uso": "Tintas conductivas. Partículas de plata (soluto) en un polímero líquido (solvente) para imprimir circuitos.", "consecuencia_de_error": "Circuitos abiertos o con alta resistencia."},
                    "aeronautica": {"uso": "Formación de nubes/estelas. El aire frío (solvente) se satura de vapor de agua (soluto) y condensa.", "consecuencia_de_error": "Formación de hielo en carburadores o alas."},
                    "electrica": {"uso": "Dieléctricos líquidos. El aceite de transformador no debe tener agua (soluto) disuelta, pues conduce electricidad.", "consecuencia_de_error": "Arco eléctrico y explosión del transformador."}
                }
            },
            {
                "subtema_titulo": "2. Concentración Porcentual (% Masa y % Volumen)",
                "definicion": "Forma simple de expresar concentración. \n- % Masa/Masa: (g soluto / g total) * 100.\n- % Volumen/Volumen: (mL soluto / mL total) * 100. Usado en líquidos comerciales.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Alcohol al 70% (v/v). Significa que en 100 mL de botella, hay 70 mL de etanol puro y 30 mL de agua.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si tienes 10g de sal y 90g de agua, el peso total es 100g. ¿Cuál es el % en masa de la sal?",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "90", "100", "1"]
                    },
                    "similares": [
                        {"pregunta": "Una botella de vino de 750mL al 10% tiene ... mL de alcohol.", "respuesta_correcta": "75", "opciones": ["75", "7.5", "750", "10"]},
                        {"pregunta": "Para hacer 100g de solución al 5%, necesitas ... g de soluto.", "respuesta_correcta": "5", "opciones": ["5", "95", "100", "0.5"]},
                        {"pregunta": "El aire tiene 21% de oxígeno. En 100 Litros de aire, hay ... Litros de O₂.", "respuesta_correcta": "21", "opciones": ["21", "79", "100", "0.21"]},
                        {"pregunta": "La suma de los porcentajes de todos los componentes debe ser...", "respuesta_correcta": "100", "opciones": ["100", "1", "0", "infinito"]},
                        {"pregunta": "El suero fisiológico es 0.9% m/v. En 100mL hay ... g de sal.", "respuesta_correcta": "0.9", "opciones": ["0.9", "9", "90", "0.09"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Pastas térmicas. Vienen especificadas por % de partículas de plata/cerámica en silicona.", "consecuencia_de_error": "Mala conductividad térmica."},
                    "quimica": {"uso": "Reactivos comerciales. El ácido clorhídrico concentrado se vende al 37% m/m.", "consecuencia_de_error": "Calcular mal la cantidad de ácido puro para una reacción."},
                    "civil": {"uso": "Humedad del suelo. Se mide en % de agua por peso de tierra seca.", "consecuencia_de_error": "Construir sobre suelo saturado que se licuará en un sismo."},
                    "mecanica": {"uso": "Refrigerante de motor. Mezcla 50% Etilenglicol y 50% Agua. Si baja el %, se congela o hierve antes.", "consecuencia_de_error": "Motor fundido o bloque de motor partido por hielo."},
                    "mecatronica": {"uso": "Alcohol isopropílico para limpieza de PCBs. Se usa 99% para que evapore rápido. El de farmacia (70%) deja agua.", "consecuencia_de_error": "Cortocircuitos por residuos de humedad."},
                    "aeronautica": {"uso": "Atmósfera de cabina. Aunque la presión baja, el % de oxígeno se mantiene en 21%.", "consecuencia_de_error": "Hipoxia (falta de oxígeno) en pilotos si el sistema de presurización falla."},
                    "electrica": {"uso": "Soldadura (Estaño-Plomo). La clásica era 60/40 (60% Sn). El porcentaje define el punto de fusión.", "consecuencia_de_error": "Soldadura fría o quebradiza."}
                }
            },
            {
                "subtema_titulo": "3. Partes por Millón (ppm)",
                "definicion": "Para concentraciones MUY pequeñas (trazas). 1 ppm = 1 mg de soluto en 1 Litro (o 1 kg) de solución. Es como un porcentaje pero con base 1 millón. Fundamental en medio ambiente y seguridad.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Límite de Cloro en piscina: 3 ppm.\nSignifica máximo 3 miligramos de Cloro por cada Litro de agua. (3 mg/L).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si tienes 5 mg de contaminante en 1 Litro de agua, la concentración es... ppm.",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "1", "0.5", "5000"]
                    },
                    "similares": [
                        {"pregunta": "1 ppm equivale a 1 ... por Litro.", "respuesta_correcta": "miligramo", "opciones": ["miligramo", "gramo", "kilogramo", "mol"]},
                        {"pregunta": "Si el CO₂ atmosférico es 400 ppm, en 1 millón de moléculas de aire, hay ... de CO₂.", "respuesta_correcta": "400", "opciones": ["400", "1", "4", "0.04"]},
                        {"pregunta": "1% equivale a ... ppm. (1 en 100 vs 1 en 1,000,000).", "respuesta_correcta": "10000", "opciones": ["10000", "100", "1000", "1"]},
                        {"pregunta": "ppm se usa para soluciones muy... (concentradas/diluidas)", "respuesta_correcta": "diluidas", "opciones": ["diluidas", "concentradas", "saturadas", "viscosas"]},
                        {"pregunta": "El agua potable permite máximo 0.01 ppm de Arsénico. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Salas limpias (Clean rooms) para fabricar CPUs. Se mide el polvo en partículas por pie cúbico (similar a ppm).", "consecuencia_de_error": "Un grano de polvo arruina un procesador de $500."},
                    "quimica": {"uso": "Análisis de trazas. Detectar pesticidas en alimentos o metales pesados en sangre.", "consecuencia_de_error": "Envenenamiento no detectado."},
                    "civil": {"uso": "Calidad del agua. Dureza, cloruros y sulfatos se miden en ppm.", "consecuencia_de_error": "Agua que corroe tuberías o daña riñones."},
                    "mecanica": {"uso": "Análisis de aceite usado. Metales de desgaste (Hierro, Cobre) en ppm indican qué pieza del motor está fallando.", "consecuencia_de_error": "Falla catastrófica de motor no prevista."},
                    "mecatronica": {"uso": "Sensores de gas (MQ-series). Calibrados en ppm para detectar fugas de gas natural o CO.", "consecuencia_de_error": "Explosión por fuga de gas no detectada a tiempo."},
                    "aeronautica": {"uso": "Calidad de combustible. El agua en el Jet-A1 se permite solo hasta ciertas ppm.", "consecuencia_de_error": "Hielo en los filtros de combustible y apagado de motores."},
                    "electrica": {"uso": "Gas SF6 en subestaciones. La humedad en el gas aislante se mide en ppm. Si sube, el gas conduce.", "consecuencia_de_error": "Arco eléctrico gigante en subestación de alta tensión."}
                }
            },
            {
                "subtema_titulo": "4. Molaridad (M)",
                "definicion": "La unidad REINA de la química. Molaridad (M) = Moles de soluto / Litros de Solución. Relaciona el volumen (lo que mides en una probeta) con los moles (lo que reacciona químicamente).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: 2 moles de NaCl en 0.5 Litros de agua.\nM = 2 moles / 0.5 L = 4 Molar (4 M).\nCada litro de esa agua contiene 4 moles de sal.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Disuelves 3 moles de HCl en 3 Litros. ¿Cuál es la Molaridad?",
                        "respuesta_correcta": "1",
                        "opciones": ["1", "3", "9", "0.33"]
                    },
                    "similares": [
                        {"pregunta": "Fórmula: M = n / ...", "respuesta_correcta": "v", "opciones": ["v", "m", "t", "p"]},
                        {"pregunta": "Si tienes una solución 2M, hay ... moles en cada litro.", "respuesta_correcta": "2", "opciones": ["2", "1", "0.5", "4"]},
                        {"pregunta": "0.5 moles en 0.25 Litros. M = 0.5/0.25 = ...", "respuesta_correcta": "2", "opciones": ["2", "0.5", "1", "0.125"]},
                        {"pregunta": "Para preparar 1L de solución 1M de NaOH (Masa=40g/mol), pesas ... gramos.", "respuesta_correcta": "40", "opciones": ["40", "1", "20", "80"]},
                        {"pregunta": "La Molaridad cambia si cambia la temperatura (el volumen se expande). (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Baterías de flujo para data centers. La capacidad de energía depende de la Molaridad de los electrolitos en los tanques.", "consecuencia_de_error": "Respaldo de energía insuficiente."},
                    "quimica": {"uso": "TODAS las reacciones en solución. HCl(ac) + NaOH(ac). Si no sabes la Molaridad, no sabes cuánto mezclar.", "consecuencia_de_error": "Explosiones o reacciones incompletas."},
                    "civil": {"uso": "Ataque químico al concreto. La agresividad de un suelo sulfatado depende de la Molaridad de los iones sulfato.", "consecuencia_de_error": "Elección de cemento incorrecto y degradación de cimientos."},
                    "mecanica": {"uso": "Anodizado de aluminio. Se requiere una Molaridad exacta de Ácido Sulfúrico para crear poros del tamaño correcto.", "consecuencia_de_error": "Piezas que no se pueden teñir o sin protección."},
                    "mecatronica": {"uso": "Biosensores de glucosa. Miden la corriente generada por la reacción de la glucosa, proporcional a su Molaridad en sangre.", "consecuencia_de_error": "Lectura de glucosa errónea para un diabético."},
                    "aeronautica": {"uso": "Decapado químico (Chemical Milling). La velocidad a la que el ácido come el aluminio depende de su Molaridad.", "consecuencia_de_error": "Piezas de avión con espesor de pared incorrecto (muy delgadas o pesadas)."},
                    "electrica": {"uso": "Electrolito de baterías Plomo-Ácido. La densidad (y voltaje) está ligada a la Molaridad del H₂SO₄.", "consecuencia_de_error": "Diagnóstico incorrecto del estado de carga."}
                }
            },
            {
                "subtema_titulo": "5. Diluciones (C1V1 = C2V2)",
                "definicion": "Añadir solvente (agua) para bajar la concentración. La cantidad de soluto (moles) NO cambia, solo se esparce en más volumen. Fórmula: Conc_inicial * Vol_inicial = Conc_final * Vol_final.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Tienes ácido 10M. Quieres preparar 2 Litros al 1M.\n10M * V1 = 1M * 2L.\nV1 = (1 * 2) / 10 = 0.2 Litros.\nTomas 0.2L del concentrado y añades agua hasta llegar a 2L.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Tienes 50mL de jabón 100%. Lo diluyes hasta 500mL. ¿Cuál es la nueva concentración?",
                        "respuesta_correcta": "10%",
                        "opciones": ["10%", "20%", "50%", "5%"]
                    },
                    "similares": [
                        {"pregunta": "Al diluir, los moles de soluto... (aumentan/disminuyen/se conservan)", "respuesta_correcta": "se conservan", "opciones": ["se conservan", "aumentan", "disminuyen", "desaparecen"]},
                        {"pregunta": "C1=2M, V1=1L. Si añades 1L de agua (V2=2L), C2 será...", "respuesta_correcta": "1", "opciones": ["1", "0.5", "4", "2"]},
                        {"pregunta": "Siempre se añade el ácido al agua, nunca al revés. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Se usa para preparar soluciones patrón de calibración. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "10mL de solución 5M se diluyen a 50mL. C2 = (10*5)/50 = ...", "respuesta_correcta": "1", "opciones": ["1", "5", "0.1", "2.5"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Gestión de señales. Atenuación. Si una señal es muy fuerte (concentrada), se atenúa (diluye) para no saturar el receptor.", "consecuencia_de_error": "Distorsión de audio o pérdida de datos RF."},
                    "quimica": {"uso": "Trabajo diario. Se compran reactivos concentrados (baratos de transportar) y se diluyen para usar.", "consecuencia_de_error": "Soluciones peligrosamente fuertes o inútilmente débiles."},
                    "civil": {"uso": "Tratamiento de efluentes. Diluir un vertido tóxico con agua limpia para cumplir la norma (aunque es trampa legal, la física es dilución).", "consecuencia_de_error": "Multas ambientales severas."},
                    "mecanica": {"uso": "Refrigerante soluble (Taladrina). Se compra aceite concentrado y se diluye 1:20 con agua para tornos CNC.", "consecuencia_de_error": "Herramienta que se quema o se oxida."},
                    "mecatronica": {"uso": "Fertirrigación automática. Robots que inyectan fertilizante concentrado en el flujo de agua principal.", "consecuencia_de_error": "Quemar los cultivos por exceso de sales."},
                    "aeronautica": {"uso": "Inyección de agua-metanol. En despegue, se inyecta mezcla diluida para enfriar y aumentar densidad del aire.", "consecuencia_de_error": "Pérdida de potencia en despegue (Hot & High)."},
                    "electrica": {"uso": "Mantenimiento de baterías. Rellenar con agua destilada diluye el electrolito que se concentró al evaporarse el agua.", "consecuencia_de_error": "Placas de batería expuestas y dañadas."}
                }
            }
        ]
    },

    # --- PROGRAMACIÓN ---
    "PROG-01": {
        "nombre_completo": "Pensamiento Algorítmico: Lógica antes del Código",
        "prerequisitos": [],
        "quiz": [
            {
                "pregunta": "¿Un diagrama de flujo es una representación gráfica de un algoritmo?",
                "respuesta": "si",
                "opciones": ["si", "no", "depende del lenguaje", "solo en python"]
            },
            {
                "pregunta": "La técnica de dividir un problema grande en partes pequeñas se llama...",
                "respuesta": "descomposicion",
                "opciones": ["descomposicion", "abstraccion", "iteracion", "reconocimiento"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. ¿Qué es un Algoritmo?",
                "definicion": "Un algoritmo NO es código. Es una secuencia finita de pasos ordenados y sin ambigüedades para resolver un problema. Es la 'receta'. Tiene una Entrada (Ingredientes), un Proceso (Pasos) y una Salida (Platillo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Algoritmo para 'Cruzar la calle'.\n1. INICIO.\n2. Mirar a la izquierda.\n3. Mirar a la derecha.\n4. SI viene auto, ESPERAR y volver al paso 2.\n5. SI NO viene auto, CAMINAR.\n6. FIN.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un algoritmo debe tener un fin, no puede ser eterno. Esta propiedad se llama...",
                        "respuesta_correcta": "finito",
                        "opciones": ["finito", "infinito", "bucle", "constante"]
                    },
                    "similares": [
                        {"pregunta": "Los datos que recibe un algoritmo se llaman... (Entrada/Salida)", "respuesta_correcta": "entrada", "opciones": ["entrada", "salida", "proceso", "variable"]},
                        {"pregunta": "El resultado que entrega un algoritmo se llama... (Entrada/Salida)", "respuesta_correcta": "salida", "opciones": ["salida", "entrada", "error", "bug"]},
                        {"pregunta": "Un algoritmo debe ser preciso y no tener... (ambigüedad/pasos)", "respuesta_correcta": "ambiguedad", "opciones": ["ambiguedad", "pasos", "datos", "fin"]},
                        {"pregunta": "Un manual de instrucciones de LEGO es un ejemplo de...", "respuesta_correcta": "algoritmo", "opciones": ["algoritmo", "programa", "codigo", "base de datos"]},
                        {"pregunta": "¿El orden de los pasos importa en un algoritmo? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Diseño de software. Antes de programar una App, se define el algoritmo de navegación del usuario.", "consecuencia_de_error": "Apps confusas donde el usuario se queda 'atrapado' sin saber qué hacer."},
                    "quimica": {"uso": "Protocolos de laboratorio. Pasos exactos para una titulación. Si dice 'añadir gota a gota', es una instrucción algorítmica precisa.", "consecuencia_de_error": "Explosión o resultado inválido por añadir reactivo muy rápido."},
                    "civil": {"uso": "Proceso constructivo. 1. Cimentación, 2. Estructura, 3. Acabados. Es un algoritmo secuencial estricto.", "consecuencia_de_error": "Intentar poner el techo antes que las columnas (imposible físico)."},
                    "mecanica": {"uso": "Ciclo de 4 tiempos de un motor (Admisión, Compresión, Explosión, Escape). Es un algoritmo cíclico.", "consecuencia_de_error": "Motor fuera de tiempo que dobla las válvulas."},
                    "mecatronica": {"uso": "Secuencia de encendido de un robot. 1. Checar batería, 2. Calibrar sensores, 3. Esperar comando.", "consecuencia_de_error": "Robot que se mueve sin control al encenderse."},
                    "aeronautica": {"uso": "Listas de chequeo (Checklists). 'Flaps: Set 10', 'Motores: Estables'. Son algoritmos de seguridad escritos con sangre.", "consecuencia_de_error": "Despegue inseguro y accidente aéreo."},
                    "electrica": {"uso": "Protocolo de desenergización (LOTO). 1. Apagar equipo, 2. Bloquear interruptor, 3. Medir voltaje cero.", "consecuencia_de_error": "Electrocución del técnico por saltarse un paso."}
                }
            },
            {
                "subtema_titulo": "2. Descomposición (Divide y Vencerás)",
                "definicion": "La habilidad más importante del ingeniero. Consiste en romper un problema complejo en sub-problemas más pequeños y manejables hasta que sean fáciles de resolver.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Problema 'Construir una casa'.\nDescomposición:\n1. Cimientos (Excavar, Colar).\n2. Paredes (Ladrillos, Cemento).\n3. Techo (Vigas, Tejas).\nCada uno es un problema separado más fácil.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si divides 'Hacer un videojuego' en 'Hacer gráficos', 'Hacer música' y 'Programar', estás usando...",
                        "respuesta_correcta": "descomposicion",
                        "opciones": ["descomposicion", "integracion", "compilacion", "abstraccion"]
                    },
                    "similares": [
                        {"pregunta": "La descomposición hace los problemas complejos más... (difíciles/fáciles)", "respuesta_correcta": "faciles", "opciones": ["faciles", "dificiles", "largos", "costosos"]},
                        {"pregunta": "Resolver cada sub-problema por separado permite trabajar en... (serie/paralelo)", "respuesta_correcta": "paralelo", "opciones": ["paralelo", "serie", "bucle", "caos"]},
                        {"pregunta": "Un problema gigante que no se descompone se llama... (modular/monolítico)", "respuesta_correcta": "monolitico", "opciones": ["monolitico", "modular", "agil", "microservicio"]},
                        {"pregunta": "En programación, descomponer lleva a crear... (variables/funciones)", "respuesta_correcta": "funciones", "opciones": ["funciones", "variables", "bucles", "errores"]},
                        {"pregunta": "La estrategia se llama 'Divide y ...'", "respuesta_correcta": "venceras", "opciones": ["venceras", "perderas", "sumaras", "restaras"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Arquitectura de Microservicios. Netflix no es un solo programa, son cientos de servicios pequeños (Login, Video, Recomendaciones) trabajando juntos.", "consecuencia_de_error": "Si falla una parte, se cae todo el sistema (como Facebook en 2021)."},
                    "quimica": {"uso": "Síntesis orgánica (Retrosíntesis). Se parte de la molécula compleja final y se 'rompe' mentalmente en reactivos más simples.", "consecuencia_de_error": "No saber por dónde empezar a fabricar un medicamento complejo."},
                    "civil": {"uso": "Estructura de Desglose del Trabajo (WBS). Dividir un proyecto de aeropuerto en miles de tareas asignables.", "consecuencia_de_error": "Caos administrativo y sobrecostos por tareas olvidadas."},
                    "mecanica": {"uso": "Despiece (Exploded View). Ver un motor como un conjunto de pistones, bielas y tornillos individuales.", "consecuencia_de_error": "Imposible diseñar o reparar una máquina compleja si se ve como un solo bloque."},
                    "mecatronica": {"uso": "Diseño modular. El brazo, la base y la garra se diseñan por separado y luego se integran.", "consecuencia_de_error": "Si falla la garra, hay que tirar todo el robot en lugar de cambiar el módulo."},
                    "aeronautica": {"uso": "Sistemas del avión. El sistema hidráulico es independiente del eléctrico y del de combustible.", "consecuencia_de_error": "Falla en cascada: un corto eléctrico apaga los motores."},
                    "electrica": {"uso": "Subestaciones. Se divide la red de una ciudad en sectores. Si falla un transformador, solo se apaga una colonia, no toda la ciudad.", "consecuencia_de_error": "Apagón generalizado (Blackout) por una falla local."}
                }
            },
            {
                "subtema_titulo": "3. Reconocimiento de Patrones y Abstracción",
                "definicion": "Patrones: Identificar similitudes entre problemas distintos para reutilizar soluciones. Abstracción: Ignorar los detalles irrelevantes y enfocarse en lo importante (el modelo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Todos los autos tienen volante y pedales (Patrón). No necesito saber cómo funciona el motor de combustión interna para conducir (Abstracción).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si creas una función 'CalcularArea' que sirve para cuadrados y rectángulos, estás usando reconocimiento de...",
                        "respuesta_correcta": "patrones",
                        "opciones": ["patrones", "errores", "datos", "hardware"]
                    },
                    "similares": [
                        {"pregunta": "Ignorar el color de un auto para calcular su velocidad es un ejemplo de...", "respuesta_correcta": "abstraccion", "opciones": ["abstraccion", "descomposicion", "programacion", "detalle"]},
                        {"pregunta": "Usar una fórmula matemática general en lugar de resolver cada caso es usar...", "respuesta_correcta": "patrones", "opciones": ["patrones", "suerte", "fuerza bruta", "memoria"]},
                        {"pregunta": "Un mapa del metro es una ... de la ciudad real (quita calles, deja conexiones).", "respuesta_correcta": "abstraccion", "opciones": ["abstraccion", "foto", "copia", "error"]},
                        {"pregunta": "Encontrar la similitud entre dos problemas ayuda a... (duplicar/reutilizar) la solución.", "respuesta_correcta": "reutilizar", "opciones": ["reutilizar", "duplicar", "borrar", "complicar"]},
                        {"pregunta": "La abstracción oculta la... (simplicidad/complejidad)", "respuesta_correcta": "complejidad", "opciones": ["complejidad", "simplicidad", "verdad", "mentira"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Programación Orientada a Objetos (POO). Creas una clase 'Vehículo' (Abstracción) y luego 'Coche' y 'Moto' heredan de ella.", "consecuencia_de_error": "Código repetitivo y difícil de actualizar."},
                    "quimica": {"uso": "Grupos Funcionales. Todos los 'Alcoholes' (-OH) reaccionan similar. No necesitas estudiar cada alcohol por separado, estudias el patrón.", "consecuencia_de_error": "Tener que memorizar millones de reacciones individuales."},
                    "civil": {"uso": "Tipificación de suelos. Se clasifica el suelo en 'Arcilla', 'Arena' o 'Roca' (Patrón) para decidir la cimentación, ignorando detalles menores.", "consecuencia_de_error": "Hacer pruebas costosas innecesarias para cada metro de terreno."},
                    "mecanica": {"uso": "Elementos de máquina estándar. Usar tornillos M10 estándar en lugar de diseñar un tornillo nuevo para cada máquina.", "consecuencia_de_error": "Costos de fabricación astronómicos."},
                    "mecatronica": {"uso": "Librerías de control. Usar un bloque 'PID' genérico (Patrón) para controlar temperatura, velocidad o posición indistintamente.", "consecuencia_de_error": "Reinventar la rueda matemática para cada sensor."},
                    "aeronautica": {"uso": "Simuladores de vuelo. Modelan la física del aire (Abstracción) sin simular cada molécula de nitrógeno.", "consecuencia_de_error": "Simulaciones que requieren supercomputadoras imposibles."},
                    "electrica": {"uso": "Leyes de circuitos. Ohm y Kirchhoff son abstracciones que ignoran la mecánica cuántica de los electrones pero funcionan para diseñar.", "consecuencia_de_error": "Complejidad matemática inmanejable para diseñar un simple interruptor."}
                }
            },
            {
                "subtema_titulo": "4. Diagramas de Flujo (Flowcharts)",
                "definicion": "Representación visual de un algoritmo. Figuras estándar:\n- Óvalo: Inicio/Fin.\n- Rectángulo: Proceso (Hacer algo).\n- Rombo: Decisión (Pregunta Si/No).\n- Flechas: Dirección del flujo.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Algoritmo 'Lámpara no sirve'.\n[Inicio] -> <Enchufada?> --No--> [Enchufar] -> [Fin].\n|--Si--> <Foco quemado?> --Si--> [Cambiar foco].\n",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué figura representa una decisión (pregunta) en un diagrama de flujo?",
                        "respuesta_correcta": "rombo",
                        "opciones": ["rombo", "rectangulo", "ovalo", "circulo"]
                    },
                    "similares": [
                        {"pregunta": "El óvalo representa el... o el final.", "respuesta_correcta": "inicio", "opciones": ["inicio", "proceso", "decision", "dato"]},
                        {"pregunta": "El rectángulo representa una... (acción/pregunta)", "respuesta_correcta": "accion", "opciones": ["accion", "pregunta", "pausa", "salida"]},
                        {"pregunta": "Las líneas que conectan los bloques se llaman...", "respuesta_correcta": "flechas", "opciones": ["flechas", "cables", "tuberias", "nodos"]},
                        {"pregunta": "Un diagrama de flujo ayuda a visualizar la... del programa.", "respuesta_correcta": "logica", "opciones": ["logica", "memoria", "velocidad", "interfaz"]},
                        {"pregunta": "¿Puede un diagrama de flujo tener dos 'Inicios'? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Documentación. Antes de codificar, se diagrama la lógica para que todo el equipo la entienda.", "consecuencia_de_error": "Programar 'a ciegas', creando código enredado (Spaghetti code)."},
                    "quimica": {"uso": "Diagramas de Proceso (PFD). Muestran el flujo de materias primas a través de la planta química.", "consecuencia_de_error": "Operadores que no saben qué válvula cerrar en una emergencia."},
                    "civil": {"uso": "Diagramas de Gantt y Pert. Muestran el flujo temporal de la construcción y las dependencias entre tareas.", "consecuencia_de_error": "Equipos de trabajo parados esperando a que otros terminen."},
                    "mecanica": {"uso": "Diagramas hidráulicos/neumáticos. Usan símbolos estándar para mostrar el flujo de aceite/aire.", "consecuencia_de_error": "Conectar mangueras mal y reventar sellos."},
                    "mecatronica": {"uso": "Máquinas de Estado. Diagramas que muestran los estados del robot (Reposo, Moviendo, Error) y las flechas son las transiciones.", "consecuencia_de_error": "Robot que se queda 'trabado' en un estado desconocido."},
                    "aeronautica": {"uso": "Procedimientos de emergencia en cabina (QRH). Son diagramas de flujo impresos para que los pilotos sigan bajo estrés.", "consecuencia_de_error": "Error humano fatal al no seguir el procedimiento correcto."},
                    "electrica": {"uso": "Diagramas unifilares. Muestran el flujo de energía desde la planta hasta los enchufes.", "consecuencia_de_error": "Sobrecarga de circuitos por no visualizar la distribución de carga."}
                }
            },
            {
                "subtema_titulo": "5. Pseudocódigo",
                "definicion": "Es escribir el algoritmo en 'lenguaje humano' estructurado, sin preocuparse por la sintaxis estricta de un lenguaje de programación (como los puntos y comas). Es el paso intermedio entre el diagrama y el código.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Sumar números hasta llegar a 100.\n`Suma = 0`\n`MIENTRAS Suma < 100 HACER:`\n`   Pedir numero`\n`   Suma = Suma + numero`\n`FIN MIENTRAS`\n`Imprimir Suma`",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En pseudocódigo, 'LEER x' significa que el programa... (muestra/recibe) un dato.",
                        "respuesta_correcta": "recibe",
                        "opciones": ["recibe", "muestra", "borra", "guarda"]
                    },
                    "similares": [
                        {"pregunta": "'IMPRIMIR x' significa que el programa... un dato.", "respuesta_correcta": "muestra", "opciones": ["muestra", "recibe", "calcula", "esconde"]},
                        {"pregunta": "El pseudocódigo puede ser entendido por una computadora directamente. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Sirve para planear la lógica sin preocuparse por la...", "respuesta_correcta": "sintaxis", "opciones": ["sintaxis", "memoria", "electricidad", "pantalla"]},
                        {"pregunta": "'SI x > 5 ENTONCES' es un ejemplo de una estructura...", "respuesta_correcta": "condicional", "opciones": ["condicional", "repetitiva", "secuencial", "final"]},
                        {"pregunta": "El pseudocódigo es universal, no depende de un lenguaje específico. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Entrevistas técnicas. Se pide resolver problemas en pseudocódigo para evaluar la lógica, no la memoria de sintaxis.", "consecuencia_de_error": "Contratar programadores que saben sintaxis pero no saben pensar."},
                    "quimica": {"uso": "Recetas de formulación. Son pseudocódigos para operarios humanos: 'Mezclar A y B hasta cambio de color'.", "consecuencia_de_error": "Variabilidad en la calidad del producto final."},
                    "civil": {"uso": "Normas de construcción. Son algoritmos escritos en texto legal: 'SI la viga es de acero, ENTONCES usar factor X'.", "consecuencia_de_error": "Diseños fuera de norma legal."},
                    "mecanica": {"uso": "Lógica de PLC (Ladder logic). Se piensa primero en pseudocódigo: 'Si sensor activo y botón presionado, encender pistón'.", "consecuencia_de_error": "Programación errónea de la automatización."},
                    "mecatronica": {"uso": "Diseño de controladores. Se escribe la matemática del control en pseudocódigo antes de traducirla a C++.", "consecuencia_de_error": "Errores matemáticos difíciles de encontrar en el código final."},
                    "aeronautica": {"uso": "Reglas de vuelo. 'SI hay tráfico a la derecha, ENTONCES ceder el paso'.", "consecuencia_de_error": "Colisión en el aire."},
                    "electrica": {"uso": "Lógica de protecciones. 'SI corriente > 100A POR mas de 2 segundos, ENTONCES abrir circuito'.", "consecuencia_de_error": "Daño a equipos por protecciones mal configuradas."}
                }
            }
        ]
    },

    "PROG-02": {
        "nombre_completo": "Variables, Tipos de Datos y Operadores",
        "prerequisitos": ["PROG-01"],
        "quiz": [
            {
                "pregunta": "Una variable que almacena '10.5' es de tipo 'float' o 'integer'?",
                "respuesta": "float",
                "opciones": ["float", "integer", "string", "boolean"]
            },
            {
                "pregunta": "La operación '10' + '5' (suma de strings) da como resultado:",
                "respuesta": "105",
                "opciones": ["105", "15", "error", "50"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. ¿Qué es una Variable? (Asignación)",
                "definicion": "Una variable es una 'caja' en la memoria con un NOMBRE (etiqueta) y un VALOR. El operador `=` es ASIGNACIÓN: guarda lo de la derecha en la caja de la izquierda. El nombre no debe tener espacios ni empezar con números.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: `puntos = 10`. (Crea caja 'puntos', mete 10). \n`puntos = puntos + 5`. (Saca 10, suma 5, guarda 15).\nError común: `10 = puntos` (No puedes guardar 'puntos' dentro del número 10).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si `a = 5` y luego `b = a`, ¿cuánto vale `b`?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "a", "b", "0"]
                    },
                    "similares": [
                        {"pregunta": "Si `x = 10` y luego `x = x + 1`, el nuevo valor de x es...", "respuesta_correcta": "11", "opciones": ["11", "10", "1", "x"]},
                        {"pregunta": "En `vida = 100`, el nombre de la variable es...", "respuesta_correcta": "vida", "opciones": ["vida", "100", "=", "int"]},
                        {"pregunta": "El operador de asignación es...", "respuesta_correcta": "=", "opciones": ["=", "==", "+", ":"]},
                        {"pregunta": "Una variable llamada `mi variable` (con espacio) es válida. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Para guardar 'Hola' en la variable `saludo`, escribes `saludo ... 'Hola'`.", "respuesta_correcta": "=", "opciones": ["=", "==", "<-", ":"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Manejo de sesiones. `usuario_actual = 'Juan'`. Mantiene la sesión activa.", "consecuencia_de_error": "Mezclar datos de dos usuarios diferentes."},
                    "quimica": {"uso": "Simulaciones. `concentracion = 0.5`. Se actualiza en cada paso de tiempo.", "consecuencia_de_error": "Simulación estática que no evoluciona."},
                    "civil": {"uso": "Cálculo estructural. `carga_viva = 200`. Se usa en múltiples fórmulas.", "consecuencia_de_error": "Tener que recalcular todo a mano si cambia la carga."},
                    "mecanica": {"uso": "CNC. `posicion_x = 100.5`. La máquina se mueve a donde diga la variable.", "consecuencia_de_error": "Colisión de la herramienta."},
                    "mecatronica": {"uso": "Odometría. `distancia = distancia + sensor`. Acumula el movimiento.", "consecuencia_de_error": "El robot pierde su ubicación."},
                    "aeronautica": {"uso": "FMS. `combustible_total = tanque1 + tanque2`. Suma sensores.", "consecuencia_de_error": "Lectura falsa de combustible."},
                    "electrica": {"uso": "Medidores inteligentes. `kwh_total = kwh_total + consumo`.", "consecuencia_de_error": "Facturación incorrecta."}
                }
            },
            {
                "subtema_titulo": "2. Tipos de Datos Primitivos (Int, Float, String, Bool)",
                "definicion": "La computadora necesita saber QUÉ hay en la caja.\n- **Int:** Enteros (contar cosas).\n- **Float:** Decimales (medir cosas).\n- **String:** Texto (mensajes).\n- **Bool:** Lógica (True/False).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: `a = 5` (int), `b = \"5\"` (str).\n`a + a` = 10 (Suma numérica).\n`b + b` = \"55\" (Pegar texto/Concatenar).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué tipo de dato es el valor `False`?",
                        "respuesta_correcta": "boolean",
                        "opciones": ["boolean", "string", "int", "float"]
                    },
                    "similares": [
                        {"pregunta": "El número `-50` es de tipo... (int/float)", "respuesta_correcta": "int", "opciones": ["int", "float", "bool", "char"]},
                        {"pregunta": "El texto `\"3.14\"` (con comillas) es de tipo...", "respuesta_correcta": "string", "opciones": ["string", "float", "int", "bool"]},
                        {"pregunta": "Para medir temperatura (ej. 36.5), usas...", "respuesta_correcta": "float", "opciones": ["float", "int", "string", "bool"]},
                        {"pregunta": "El resultado de `10 > 5` es de tipo...", "respuesta_correcta": "boolean", "opciones": ["boolean", "int", "float", "string"]},
                        {"pregunta": "Si sumas un `int` y un `float`, el resultado es...", "respuesta_correcta": "float", "opciones": ["float", "int", "error", "string"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Bases de datos. Definir campos (Nombre=String, Edad=Int) ahorra espacio.", "consecuencia_de_error": "No poder ordenar por edad numéricamente."},
                    "quimica": {"uso": "Precisión. Usar `float` para ppm. Un `int` truncaría 0.05 a 0.", "consecuencia_de_error": "Cálculos de concentración que dan cero erróneamente."},
                    "civil": {"uso": "Coordenadas GPS. Deben ser `double` (float de alta precisión).", "consecuencia_de_error": "Errores de metros en la ubicación de una columna."},
                    "mecanica": {"uso": "Códigos G. Coordenadas son `float`, número de herramienta es `int`.", "consecuencia_de_error": "La máquina busca la herramienta '3.5' (inexistente)."},
                    "mecatronica": {"uso": "Sensores. Digitales (1/0) son `bool`, Analógicos (0-5V) son `float`.", "consecuencia_de_error": "Perder la precisión de un sensor al usar int."},
                    "aeronautica": {"uso": "Lógica. `tren_abajo` es `bool`. No puede estar 'medio abajo'.", "consecuencia_de_error": "Fallo en lógica de seguridad de aterrizaje."},
                    "electrica": {"uso": "Estado de relés. `encendido = True`. Base del control digital.", "consecuencia_de_error": "Ambigüedad en interruptores de potencia."}
                }
            },
            {
                "subtema_titulo": "3. Conversión de Tipos (Casting)",
                "definicion": "Cambiar un dato de un tipo a otro. Es CRÍTICO al leer sensores o inputs (que suelen llegar como texto). Funciones comunes: `int()`, `float()`, `str()`.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Tienes el texto `num = \"10\"`. Si haces `num + 5`, da error.\nSolución: `int(num) + 5` -> `10 + 5` -> `15`.\nEjemplo: `float(5)` convierte el entero `5` en decimal `5.0`.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el resultado de `int(\"5\") + 5`?",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "55", "error", "5"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuál es el resultado de `str(10) + \"5\"`? (concatenar)", "respuesta_correcta": "105", "opciones": ["105", "15", "error", "10"]},
                        {"pregunta": "`int(3.9)` trunca el decimal y devuelve...", "respuesta_correcta": "3", "opciones": ["3", "4", "3.9", "error"]},
                        {"pregunta": "Para convertir el número 10 a texto \"10\", usas la función...", "respuesta_correcta": "str", "opciones": ["str", "int", "float", "text"]},
                        {"pregunta": "Si conviertes \"Hola\" a int, ocurre un... (resultado/error)", "respuesta_correcta": "error", "opciones": ["error", "cero", "null", "uno"]},
                        {"pregunta": "`bool(0)` devuelve...", "respuesta_correcta": "false", "opciones": ["false", "true", "error", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Formularios web. Todo lo que el usuario escribe es `string`. Hay que convertir la 'edad' a `int` para verificarla.", "consecuencia_de_error": "El programa crashea al intentar sumar la edad."},
                    "quimica": {"uso": "Leer archivos CSV de datos. Los números vienen como texto y deben convertirse a `float` para graficar.", "consecuencia_de_error": "Gráficas vacías o errores de cálculo."},
                    "civil": {"uso": "Importar coordenadas de Excel. Convertir texto de celdas a números flotantes para AutoCAD.", "consecuencia_de_error": "El plano no se dibuja."},
                    "mecanica": {"uso": "Lectura de encoders. El contador es `int`, pero para calcular velocidad (distancia/tiempo) se debe pasar a `float`.", "consecuencia_de_error": "División entera que da cero (ej. 1/2 = 0 en vez de 0.5)."},
                    "mecatronica": {"uso": "Comunicación Serial. El Arduino envía caracteres ASCII ('A', '1'). Hay que convertirlos a valores numéricos.", "consecuencia_de_error": "El robot interpreta el número '100' como tres caracteres separados."},
                    "aeronautica": {"uso": "Protocolos de datos (ARINC 429). Decodificar paquetes binarios a valores flotantes legibles (altitud).", "consecuencia_de_error": "Datos ilegibles en pantalla."},
                    "electrica": {"uso": "Conversor ADC. Convierte un voltaje analógico (físico) a un número entero (digital) para procesar.", "consecuencia_de_error": "Pérdida de resolución en la medición."}
                }
            },
            {
                "subtema_titulo": "4. Entrada y Salida (Input/Print)",
                "definicion": "Cómo el programa habla con el mundo exterior.\n- **Output (`print`):** Muestra información en pantalla.\n- **Input (`input`):** Pide información al usuario (siempre llega como Texto/String).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Programa de saludo.\n`nombre = input(\"Tu nombre: \")` (Usuario escribe 'Ana')\n`print(\"Hola \" + nombre)` -> Imprime \"Hola Ana\".",
                "ejercicio": {
                    "principal": {
                        "pregunta": "La función `input()` siempre devuelve el dato como tipo...",
                        "respuesta_correcta": "string",
                        "opciones": ["string", "int", "float", "void"]
                    },
                    "similares": [
                        {"pregunta": "Para mostrar un mensaje en pantalla usas la función...", "respuesta_correcta": "print", "opciones": ["print", "input", "show", "echo"]},
                        {"pregunta": "Si hago `x = input()` y escribo 5, ¿`x + x` es 10 o 55?", "respuesta_correcta": "55", "opciones": ["55", "10", "error", "5"]},
                        {"pregunta": "Para pedir un número y sumarlo, primero debo usar `input` y luego...", "respuesta_correcta": "int", "opciones": ["int", "print", "str", "float"]},
                        {"pregunta": "En sistemas embebidos, `print` suele enviar datos por el puerto...", "respuesta_correcta": "serial", "opciones": ["serial", "paralelo", "vga", "hdmi"]},
                        {"pregunta": "`print(\"A\", \"B\")` muestra A y B separados por un...", "respuesta_correcta": "espacio", "opciones": ["espacio", "coma", "punto", "salto"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Consola de comandos (CLI). Servidores Linux se manejan 100% con input/print de texto.", "consecuencia_de_error": "Imposible administrar servidores remotos."},
                    "quimica": {"uso": "Dataloggers. El `print` escribe los datos del experimento en un archivo de texto (.log).", "consecuencia_de_error": "Perder los datos del experimento si se va la luz."},
                    "civil": {"uso": "Interfaces de usuario simples para scripts de cálculo rápido de vigas.", "consecuencia_de_error": "Usuario ingresa datos incorrectos sin saber qué se le pide."},
                    "mecanica": {"uso": "HMI (Human Machine Interface). Pantallas donde el operador ingresa parámetros (input) y ve el estado (print).", "consecuencia_de_error": "Operador ciego ante el estado de la máquina."},
                    "mecatronica": {"uso": "Debugging. Usar `print(sensor)` para ver qué está 'viendo' el robot en la consola.", "consecuencia_de_error": "Imposible arreglar el robot sin saber qué pasa por su 'mente'."},
                    "aeronautica": {"uso": "FMS (Flight Management System). Teclado (input) y Pantalla (output) para configurar la ruta.", "consecuencia_de_error": "Entrada de coordenadas erróneas."},
                    "electrica": {"uso": "Displays LCD. Mostrar voltaje y corriente medidos en un panel.", "consecuencia_de_error": "Información confusa para el técnico."}
                }
            },
            {
                "subtema_titulo": "5. Operadores Aritméticos y Lógicos",
                "definicion": "Herramientas para manipular las variables.\n- **Aritméticos:** `+`, `-`, `*`, `/` y Módulo `%` (residuo).\n- **Lógicos:** `==` (igual), `!=` (diferente), `>`, `<`, `AND`, `OR`.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo Módulo: `10 % 3`. \n10 entre 3 es 3, y sobra 1. Resultado: 1.\nEjemplo Lógico: `(10 > 5) AND (2 == 2)` -> `True AND True` -> `True`.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Cuál es el resultado de `7 % 2` (residuo)?",
                        "respuesta_correcta": "1",
                        "opciones": ["1", "0", "3.5", "7"]
                    },
                    "similares": [
                        {"pregunta": "Resultado de `(5 > 3) AND (2 < 4)`... (true/false)", "respuesta_correcta": "true", "opciones": ["true", "false"]},
                        {"pregunta": "El operador para verificar igualdad es... (=/==)", "respuesta_correcta": "==", "opciones": ["==", "=", "!=", "<>"]},
                        {"pregunta": "Resultado de `10 / 2` en división estándar.", "respuesta_correcta": "5", "opciones": ["5", "5.0", "2", "10"]},
                        {"pregunta": "`NOT true` es igual a...", "respuesta_correcta": "false", "opciones": ["false", "true", "null", "error"]},
                        {"pregunta": "Si `a = 5`, `a != 5` devuelve... (true/false)", "respuesta_correcta": "false", "opciones": ["false", "true"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Criptografía (Operador Módulo y XOR).", "consecuencia_de_error": "Datos inseguros."},
                    "quimica": {"uso": "Seguridad. `if (temp > 100) OR (presion > 50)`. Alarma si cualquiera falla.", "consecuencia_de_error": "Usar AND requeriría que fallen ambas para sonar (peligroso)."},
                    "civil": {"uso": "Verificación de normas. `if (resistencia >= norma)`.", "consecuencia_de_error": "Aprobar materiales inseguros."},
                    "mecanica": {"uso": "Sincronización. `%` calcula ciclos de rotación.", "consecuencia_de_error": "Desincronización de levas."},
                    "mecatronica": {"uso": "Máquinas de estado. `if (boton == 1) AND (motor_parado == True)`.", "consecuencia_de_error": "Máquina arranca en momento inseguro."},
                    "aeronautica": {"uso": "Redundancia. `if (sensor1_falla) AND (sensor2_falla)`.", "consecuencia_de_error": "Falsas alarmas en cabina."},
                    "electrica": {"uso": "Lógica digital. Los operadores son representaciones de transistores físicos.", "consecuencia_de_error": "Diseño de chips defectuoso."}
                }
            }
        ]
    },

    "PROG-03": {
        "nombre_completo": "Control de Flujo: Condicionales Avanzados",
        "prerequisitos": ["PROG-02"],
        "quiz": [
            {
                "pregunta": "¿Qué palabra clave se usa para tomar una decisión en programación?",
                "respuesta": "if",
                "opciones": ["if", "for", "while", "var"]
            },
            {
                "pregunta": "El bloque de código 'else' se ejecuta cuando la condición 'if' es...",
                "respuesta": "falsa",
                "opciones": ["falsa", "verdadera", "nula", "positiva"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. La Sentencia 'If' (Si...)",
                "definicion": "La base de la decisión. Ejecuta un bloque de código solo si una condición es `True`. En Python, el bloque se define por la **indentación** (sangría).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: `temperatura = 110`\n`if temperatura > 100:`\n`    print('Alerta')`\n(Imprime 'Alerta' porque 110 > 100 es True).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si `x = 5`, ¿se ejecuta el bloque `if x == 10:`? (si/no)",
                        "respuesta_correcta": "no",
                        "opciones": ["no", "si"]
                    },
                    "similares": [
                        {"pregunta": "La condición de un IF debe ser una expresión... (booleana/numérica)", "respuesta_correcta": "booleana", "opciones": ["booleana", "numerica", "texto", "lista"]},
                        {"pregunta": "El código dentro del IF debe estar... (indentado/comentado)", "respuesta_correcta": "indentado", "opciones": ["indentado", "pegado", "entre llaves", "oculto"]},
                        {"pregunta": "Si la condición es False, el programa se... el bloque IF.", "respuesta_correcta": "salta", "opciones": ["salta", "repite", "cierra", "borra"]},
                        {"pregunta": "`if True:` siempre se ejecuta. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Se usa para tomar decisiones simples.", "respuesta_correcta": "if", "opciones": ["if", "else", "for", "print"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Validación simple. `if usuario == 'admin': dar_permisos()`.", "consecuencia_de_error": "Acceso no autorizado a funciones críticas."},
                    "quimica": {"uso": "Límite de seguridad. `if presion > max: abrir_valvula()`.", "consecuencia_de_error": "Explosión por sobrepresión en el reactor."},
                    "civil": {"uso": "Verificación. `if factor_seguridad < 1: rechazar_diseño()`.", "consecuencia_de_error": "Aprobación de una estructura que colapsará."},
                    "mecanica": {"uso": "Termostato. `if temp_motor > 90: activar_fan()`.", "consecuencia_de_error": "Motor fundido por sobrecalentamiento."},
                    "mecatronica": {"uso": "Sensor de choque. `if contacto == True: parar()`.", "consecuencia_de_error": "Daño al robot o al entorno por no detenerse."},
                    "aeronautica": {"uso": "Alertas. `if combustible < reserva: sonar_alarma()`.", "consecuencia_de_error": "Piloto sin consciencia de la emergencia."},
                    "electrica": {"uso": "Fusible digital. `if corriente > limite: cortar_rele()`.", "consecuencia_de_error": "Incendio eléctrico por sobrecorriente."}
                }
            },
            {
                "subtema_titulo": "2. Sentencias 'Else' y 'Elif' (Caminos Alternativos)",
                "definicion": "`Else`: Qué hacer si el `if` falla (caso contrario). `Elif`: Probar otra condición si la anterior falló. Crea una cadena de descarte mutuamente excluyente.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Semáforo.\n`if luz == 'roja': parar()`\n`elif luz == 'amarilla': precaucion()`\n`else: avanzar()` (Si no es roja ni amarilla, asume verde).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si `x=3`, en `if x>5: 'A' else: 'B'`, ¿qué se imprime?",
                        "respuesta_correcta": "B",
                        "opciones": ["B", "A", "AB", "nada"]
                    },
                    "similares": [
                        {"pregunta": "`elif` significa 'Else ...'", "respuesta_correcta": "If", "opciones": ["If", "Then", "End", "Loop"]},
                        {"pregunta": "Solo se puede tener un `else` por bloque `if`. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si el `if` es verdadero, ¿se evalúa el `elif` siguiente? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Sirve para manejar el caso 'por defecto' o 'si todo falla'.", "respuesta_correcta": "else", "opciones": ["else", "elif", "if", "then"]},
                        {"pregunta": "En una cadena if-elif-else, ¿cuántos bloques se ejecutan máximo?", "respuesta_correcta": "1", "opciones": ["1", "todos", "2", "ninguno"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Manejo de errores. `if archivo_existe: leer() else: mostrar_error()`.", "consecuencia_de_error": "El programa se cierra inesperadamente (crash)."},
                    "quimica": {"uso": "Clasificación de pH. `if ph<7: 'Acido' elif ph>7: 'Base' else: 'Neutro'`.", "consecuencia_de_error": "Etiquetado químico erróneo."},
                    "civil": {"uso": "Estado de carga. `if carga > critica: 'Falla' else: 'Seguro'`.", "consecuencia_de_error": "Falsa sensación de seguridad."},
                    "mecanica": {"uso": "Cambios automáticos. `if rpm > alta: subir_marcha elif rpm < baja: bajar`.", "consecuencia_de_error": "Motor forzado o apagado."},
                    "mecatronica": {"uso": "Navegación. `if obstaculo: girar else: avanzar`.", "consecuencia_de_error": "Robot atascado o que no se mueve."},
                    "aeronautica": {"uso": "Fases de vuelo. `if en_tierra: modo_tierra elif en_aire: modo_vuelo`.", "consecuencia_de_error": "Activar sistemas de tierra (ej. reversas) en pleno vuelo."},
                    "electrica": {"uso": "Carga de batería. `if voltaje < 12: cargar else: mantener`.", "consecuencia_de_error": "Sobrecarga de baterías (explosión)."}
                }
            },
            {
                "subtema_titulo": "3. Operadores Lógicos (AND, OR, NOT)",
                "definicion": "Permiten evaluar múltiples condiciones a la vez.\n- **AND:** Todo debe ser verdad.\n- **OR:** Basta con que una sea verdad.\n- **NOT:** Invierte (Verdadero se vuelve Falso).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Acceso nuclear.\n`if (llave_1 == True) AND (llave_2 == True): lanzar()`.\nSi solo tienes la llave 1, (True AND False) es False. No lanza.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "`True AND False` da como resultado...",
                        "respuesta_correcta": "false",
                        "opciones": ["false", "true", "error", "null"]
                    },
                    "similares": [
                        {"pregunta": "`True OR False` da como resultado...", "respuesta_correcta": "true", "opciones": ["true", "false", "error", "null"]},
                        {"pregunta": "`NOT True` da como resultado...", "respuesta_correcta": "false", "opciones": ["false", "true", "null", "error"]},
                        {"pregunta": "Para que `A AND B` sea true, necesitamos...", "respuesta_correcta": "ambas", "opciones": ["ambas", "una", "ninguna", "la primera"]},
                        {"pregunta": "Para que `A OR B` sea true, necesitamos...", "respuesta_correcta": "una", "opciones": ["una", "ambas", "ninguna", "la ultima"]},
                        {"pregunta": "`NOT (5 > 10)` es... (true/false)", "respuesta_correcta": "true", "opciones": ["true", "false"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Permisos. `if es_admin OR es_moderador: borrar_post()`.", "consecuencia_de_error": "Usuarios normales borrando contenido."},
                    "quimica": {"uso": "Reacción. `if (catalizador) AND (temp > 50): iniciar`.", "consecuencia_de_error": "La reacción no inicia cuando debería."},
                    "civil": {"uso": "Cargas combinadas. `if (sismo) AND (viento_huracan): usar_factor_extremo`.", "consecuencia_de_error": "Subestimar riesgo en tormentas."},
                    "mecanica": {"uso": "Prensa de seguridad. `if boton1 AND boton2: bajar_prensa`. (Bimando).", "consecuencia_de_error": "Operario pierde una mano si un botón se atora."},
                    "mecatronica": {"uso": "Parada emergencia. `if boton_paro OR sensor_barrera: stop`.", "consecuencia_de_error": "Máquina no se detiene ante un peligro."},
                    "aeronautica": {"uso": "Configuración de aterrizaje. `if (tren_arriba) AND (altitud_baja): alarma_proximidad`.", "consecuencia_de_error": "Aterrizaje de panza sin advertencia."},
                    "electrica": {"uso": "UPS. `if (NOT red_activa): encender_bateria`.", "consecuencia_de_error": "Servidores apagados durante corte de luz."}
                }
            },
            {
                "subtema_titulo": "4. Switch / Match Case (Selección Múltiple)",
                "definicion": "Cuando tienes que comparar una variable contra MUCHOS valores posibles (ej. un menú), usar `if-elif-elif...` es lento y desordenado. `Switch` (o `Match` en Python 3.10+) es la estructura ideal para 'Máquinas de Estado'.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Menú de opciones.\n`match opcion:`\n`   case 1: iniciar()`\n`   case 2: config()`\n`   case _: print('Error')` (Caso por defecto/wildcard).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En una estructura Match/Switch, el caso por defecto (si ninguno coincide) se suele marcar con...",
                        "respuesta_correcta": "default",
                        "opciones": ["default", "else", "case", "break"]
                    },
                    "similares": [
                        {"pregunta": "Es más ordenado que usar muchos `elif`. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Se usa para comparar una variable contra múltiples... (rangos/valores constantes)", "respuesta_correcta": "valores constantes", "opciones": ["valores constantes", "variables", "funciones", "ecuaciones"]},
                        {"pregunta": "En Python moderno, la palabra clave es... (switch/match)", "respuesta_correcta": "match", "opciones": ["match", "switch", "case", "select"]},
                        {"pregunta": "Ideal para programar máquinas de... (estados/tiempo)", "respuesta_correcta": "estados", "opciones": ["estados", "bucles", "calculo", "fisica"]},
                        {"pregunta": "Si `opcion=2` y hay un `case 2:`, ¿se ejecuta ese bloque? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Menús de UI. Manejar clics en botones (Guardar, Abrir, Salir).", "consecuencia_de_error": "Interfaz que no responde o ejecuta la acción equivocada."},
                    "quimica": {"uso": "Sel ector de modo en un espectrómetro (Modo UV, Modo IR, Modo Visible).", "consecuencia_de_error": "Instrumento midiendo en el rango incorrecto."},
                    "civil": {"uso": "Software de cálculo. Seleccionar tipo de material (Concreto, Acero, Madera) para aplicar la fórmula correcta.", "consecuencia_de_error": "Usar la densidad del acero para una viga de madera."},
                    "mecanica": {"uso": "Selector de marchas (P, R, N, D). Cada caso activa una válvula hidráulica distinta.", "consecuencia_de_error": "Auto que avanza estando en Reversa."},
                    "mecatronica": {"uso": "Máquina de Estados de un Robot. (Case 'Idle', Case 'Moving', Case 'Error'). Es el cerebro del robot.", "consecuencia_de_error": "Robot que se queda 'trabado' en un estado desconocido."},
                    "aeronautica": {"uso": "Modos del Piloto Automático (Heading, Nav, Approach, Altitude Hold).", "consecuencia_de_error": "El avión sigue el rumbo pero no la altitud deseada."},
                    "electrica": {"uso": "Multímetro digital. El selector rotativo cambia el circuito interno (Voltaje, Corriente, Resistencia).", "consecuencia_de_error": "Quemar el multímetro al medir voltaje en modo resistencia."}
                }
            },
            {
                "subtema_titulo": "5. Operador Ternario (If en una línea)",
                "definicion": "Es una forma ultra-compacta de escribir un `if-else` simple para asignar un valor. Estructura: `valor = A si condicion else B`. Muy usado para valores por defecto o limpieza de datos.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Asignar estado.\nNormal: `if edad >= 18: status='Mayor' else: status='Menor'`\nTernario: `status = 'Mayor' if edad >= 18 else 'Menor'`.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Resuelve: `x = 10 if 5 > 2 else 0`. ¿Cuánto vale x?",
                        "respuesta_correcta": "10",
                        "opciones": ["10", "0", "5", "2"]
                    },
                    "similares": [
                        {"pregunta": "`y = 'Par' if 4%2==0 else 'Impar'`. y es...", "respuesta_correcta": "par", "opciones": ["par", "impar", "error", "null"]},
                        {"pregunta": "Sirve para simplificar asignaciones condicionales. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Sustituye a un bloque completo de... (if-else/while)", "respuesta_correcta": "if-else", "opciones": ["if-else", "for", "switch", "def"]},
                        {"pregunta": "`a = 5 if False else 2`. a vale...", "respuesta_correcta": "2", "opciones": ["2", "5", "false", "error"]},
                        {"pregunta": "Hace el código más compacto pero a veces menos legible. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Configuración. `puerto = config_puerto if config_puerto else 8080`. Asigna puerto default si no hay configuración.", "consecuencia_de_error": "Servidor no arranca por falta de configuración."},
                    "quimica": {"uso": "Limpieza de datos. `concentracion = lectura if lectura > 0 else 0.0`. Evita concentraciones negativas por ruido del sensor.", "consecuencia_de_error": "Cálculos con valores físicos imposibles."},
                    "civil": {"uso": "Factores de seguridad. `factor = 1.5 if es_hospital else 1.2`.", "consecuencia_de_error": "Aplicar normas residenciales a edificios críticos."},
                    "mecanica": {"uso": "Válvulas. `estado = 'Abierta' if presion > 100 else 'Cerrada'`.", "consecuencia_de_error": "Válvula en estado indeterminado."},
                    "mecatronica": {"uso": "Control PWM. `potencia = 255 if calculo > 255 else calculo`. Evita desbordamiento (clamping).", "consecuencia_de_error": "El motor se detiene al recibir un valor inválido."},
                    "aeronautica": {"uso": "Displays. `color = 'Rojo' if alarma else 'Verde'`. Cambia el color de un indicador en cabina.", "consecuencia_de_error": "El piloto no nota una condición crítica."},
                    "electrica": {"uso": "Lectura ADC. `voltaje = lectura * 5.0 / 1023.0 if lectura_valida else 0.0`.", "consecuencia_de_error": "Ruido eléctrico interpretado como señal válida."}
                }
            }
        ]
    },

    "PROG-04": {
        "nombre_completo": "Control de Flujo: Bucles e Iteraciones",
        "prerequisitos": ["PROG-03"],
        "quiz": [
            {
                "pregunta": "¿Qué tipo de bucle usarías si sabes que quieres repetir algo exactamente 10 veces?",
                "respuesta": "for",
                "opciones": ["for", "while", "if", "switch"]
            },
            {
                "pregunta": "¿Qué tipo de bucle usarías si quieres repetir algo 'mientras' una condición sea verdadera?",
                "respuesta": "while",
                "opciones": ["while", "for", "do-until", "foreach"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. El Bucle 'While' (Iteración Indefinida)",
                "definicion": "Repite un bloque de código MIENTRAS una condición sea verdadera. Es como un `if` que se recarga. Se usa cuando NO sabes cuándo terminará el proceso (ej. esperar a que un usuario pulse una tecla).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Llenar un tanque.\n`litros = 0`\n`while litros < 100:`\n`    litros = litros + 10`\n`    print('Llenando...')`\n(Repite la suma hasta llegar a 100).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si `x=0` entonces `while x < 3: x=x+1`. ¿Cuál es el valor final de x?",
                        "respuesta_correcta": "3",
                        "opciones": ["3", "2", "4", "0"]
                    },
                    "similares": [
                        {"pregunta": "Se usa cuando no conocemos el número de iteraciones. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Si la condición inicial es Falsa, el `while` se ejecuta... veces.", "respuesta_correcta": "0", "opciones": ["0", "1", "infinito", "error"]},
                        {"pregunta": "Necesita una condición de salida para evitar ser...", "respuesta_correcta": "infinito", "opciones": ["infinito", "nulo", "corto", "lento"]},
                        {"pregunta": "`while True:` requiere un `...` para detenerse.", "respuesta_correcta": "break", "opciones": ["break", "continue", "pass", "exit"]},
                        {"pregunta": "Es ideal para esperar eventos de sensores. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Game Loop. `while juego_activo:` actualiza la física y gráficos constantemente.", "consecuencia_de_error": "El juego se cierra solo o se congela si el bucle termina por error."},
                    "quimica": {"uso": "Monitoreo. `while temperatura < setpoint: calentar()`. Mantiene el reactor en el estado deseado.", "consecuencia_de_error": "Reactor frío o reacción incompleta."},
                    "civil": {"uso": "Simulación de tráfico. `while autos_en_fila > 0: pasar_auto()`. Simula el vaciado de una intersección.", "consecuencia_de_error": "Mal diseño de tiempos de semáforo."},
                    "mecanica": {"uso": "Pruebas de fatiga. `while pieza_no_rota: aplicar_fuerza()`. Cuenta ciclos hasta la falla.", "consecuencia_de_error": "No determinar la vida útil real de la pieza."},
                    "mecatronica": {"uso": "Homing. `while sensor_final_carrera == False: mover_motor()`. Calibra la posición inicial.", "consecuencia_de_error": "El robot choca contra los límites mecánicos."},
                    "aeronautica": {"uso": "Espera en tierra. `while permiso_despegue == False: esperar()`. Lógica de torre de control.", "consecuencia_de_error": "Colisión en pista."},
                    "electrica": {"uso": "Carga de capacitor. `while voltaje_cap < 5V: cargar()`. Simula la carga transitoria.", "consecuencia_de_error": "Circuito que no alcanza el voltaje operativo."}
                }
            },
            {
                "subtema_titulo": "2. El Bucle 'For' (Iteración Definida)",
                "definicion": "Repite un bloque un número ESPECÍFICO de veces o recorre una colección de datos. En Python, `for i in range(N)` ejecuta el código N veces (del 0 al N-1). Es más seguro que el `while` porque garantiza terminar.",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Imprimir números del 0 al 2.\n`for i in range(3):`\n`    print(i)`\nSalida: 0, 1, 2. (El 3 no se incluye).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En `for i in range(5)`, ¿cuántas veces se ejecuta el código?",
                        "respuesta_correcta": "5",
                        "opciones": ["5", "4", "6", "0"]
                    },
                    "similares": [
                        {"pregunta": "¿Cuál es el primer valor de `i` en `range(5)`?", "respuesta_correcta": "0", "opciones": ["0", "1", "5", "-1"]},
                        {"pregunta": "¿Cuál es el último valor de `i` en `range(5)`?", "respuesta_correcta": "4", "opciones": ["4", "5", "3", "0"]},
                        {"pregunta": "Para contar de 1 a 10 usas `range(1, ...)`", "respuesta_correcta": "11", "opciones": ["11", "10", "9", "12"]},
                        {"pregunta": "Es ideal para recorrer listas o vectores. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "La variable `i` se incrementa automáticamente. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesar listas. `for usuario in base_de_datos: enviar_email()`.", "consecuencia_de_error": "Usuarios que no reciben notificaciones."},
                    "quimica": {"uso": "Análisis de muestras. `for muestra in bandeja_autosampler: analizar(muestra)`.", "consecuencia_de_error": "Saltarse muestras en un lote de producción."},
                    "civil": {"uso": "Cálculo de vigas. `for viga in estructura: calcular_esfuerzo(viga)`.", "consecuencia_de_error": "Dejar elementos estructurales sin verificar."},
                    "mecanica": {"uso": "Análisis de Elementos Finitos (FEA). `for nodo in malla: resolver_fuerza(nodo)`.", "consecuencia_de_error": "Simulación incompleta del estrés en la pieza."},
                    "mecatronica": {"uso": "Movimiento paso a paso. `for paso in range(100): mover_stepper()`.", "consecuencia_de_error": "El robot se mueve una distancia incorrecta."},
                    "aeronautica": {"uso": "Chequeo de instrumentos. `for sensor in lista_sensores: verificar_estado(sensor)`.", "consecuencia_de_error": "Despegar con un instrumento fallido."},
                    "electrica": {"uso": "Muestreo de señal. `for t in tiempo: leer_voltaje(t)`.", "consecuencia_de_error": "Reconstrucción incompleta de la onda eléctrica."}
                }
            },
            {
                "subtema_titulo": "3. Control de Bucles: Break y Continue",
                "definicion": "Modifican el comportamiento normal.\n- **Break:** Rompe el bucle inmediatamente (salida de emergencia).\n- **Continue:** Salta lo que queda de la vuelta actual y va a la siguiente (ignorar paso).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo Break: Buscar un número.\n`for n in lista:`\n`   if n == buscado: break` (Deja de buscar al encontrarlo).\nEjemplo Continue: Imprimir solo impares.\n`for n in range(10):`\n`   if n % 2 == 0: continue` (Salta los pares).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "¿Qué sentencia detiene el bucle por completo?",
                        "respuesta_correcta": "break",
                        "opciones": ["break", "continue", "stop", "end"]
                    },
                    "similares": [
                        {"pregunta": "¿Qué sentencia salta solo la iteración actual?", "respuesta_correcta": "continue", "opciones": ["continue", "break", "skip", "next"]},
                        {"pregunta": "Si usas `break` en un bucle infinito, el programa... (se cuelga/continúa)", "respuesta_correcta": "continua", "opciones": ["continua", "se cuelga"]},
                        {"pregunta": "Se usa para optimizar búsquedas (parar al encontrar).", "respuesta_correcta": "break", "opciones": ["break", "continue", "for", "if"]},
                        {"pregunta": "Se usa para filtrar datos no deseados dentro del bucle.", "respuesta_correcta": "continue", "opciones": ["continue", "break", "return", "else"]},
                        {"pregunta": "En `while True: if error: break`, el bucle termina si hay error. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Búsqueda en base de datos. Usar `break` al encontrar el usuario ahorra tiempo de CPU.", "consecuencia_de_error": "Sistema lento que revisa millones de registros innecesariamente."},
                    "quimica": {"uso": "Filtrado de datos. `if lectura_sensor == 'Error': continue`. Ignora lecturas malas.", "consecuencia_de_error": "Promediar valores de error en los resultados finales."},
                    "civil": {"uso": "Optimización. `if costo > presupuesto: continue`. Ignorar materiales muy caros en la búsqueda.", "consecuencia_de_error": "Proponer diseños fuera de presupuesto."},
                    "mecanica": {"uso": "Parada de emergencia. `if vibracion > limite: break`. Detener la prueba inmediatamente.", "consecuencia_de_error": "Destrucción de la máquina de pruebas."},
                    "mecatronica": {"uso": "Búsqueda de 'Home'. `if sensor_tocado: break`. El motor para apenas toca el fin de carrera.", "consecuencia_de_error": "El motor sigue empujando y quema el sensor."},
                    "aeronautica": {"uso": "TCAS (Anticolisión). `if amenaza_detectada: break_nav_loop_and_evade()`.", "consecuencia_de_error": "El avión sigue su ruta en lugar de evadir."},
                    "electrica": {"uso": "Protección térmica. `if temp > max: break`. Cortar la corriente si se calienta.", "consecuencia_de_error": "Incendio del dispositivo."}
                }
            },
            {
                "subtema_titulo": "4. Bucles Anidados (Nested Loops)",
                "definicion": "Un bucle dentro de otro. Por cada vuelta del bucle externo, el interno se ejecuta completo. Se usa para trabajar con matrices, tablas o imágenes (X, Y). Cuidado: Son lentos (Complejidad O(N²)).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Coordenadas (x, y) de 2x2.\n`for x in range(2):`\n`   for y in range(2):`\n`      print(x, y)`\nSalida: (0,0), (0,1), (1,0), (1,1).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si el bucle externo gira 3 veces y el interno 4, ¿cuántas veces corre el código interno?",
                        "respuesta_correcta": "12",
                        "opciones": ["12", "7", "4", "3"]
                    },
                    "similares": [
                        {"pregunta": "Se usan para recorrer matrices o tablas. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "En procesamiento de imágenes, un bucle recorre filas y el otro...", "respuesta_correcta": "columnas", "opciones": ["columnas", "pixeles", "colores", "bytes"]},
                        {"pregunta": "Tener 3 bucles anidados es generalmente... (rápido/lento)", "respuesta_correcta": "lento", "opciones": ["lento", "rapido"]},
                        {"pregunta": "En un reloj digital, el bucle de minutos está dentro del bucle de horas. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Para imprimir una tabla de multiplicar del 1 al 10, usas bucles anidados. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Procesamiento de imágenes. Bucle X y Bucle Y para leer cada píxel.", "consecuencia_de_error": "Imposible aplicar filtros o reconocer objetos."},
                    "quimica": {"uso": "Interacciones moleculares. Calcular la fuerza de cada átomo contra todos los demás átomos.", "consecuencia_de_error": "Simulaciones moleculares incompletas."},
                    "civil": {"uso": "Análisis matricial. Resolver matrices de rigidez [K] en estructuras.", "consecuencia_de_error": "Cálculo estructural imposible en edificios complejos."},
                    "mecanica": {"uso": "Mecanizado CNC 3D. Bucles para X, Y y Z para tallar una superficie compleja.", "consecuencia_de_error": "Pieza con forma incorrecta."},
                    "mecatronica": {"uso": "Visión robótica. Escanear una cuadrícula para buscar un objeto.", "consecuencia_de_error": "El robot no encuentra el objeto en el campo de visión."},
                    "aeronautica": {"uso": "CFD (Dinámica de Fluidos). Calcular flujo en cada celda de una malla 3D alrededor del ala.", "consecuencia_de_error": "Modelo aerodinámico impreciso."},
                    "electrica": {"uso": "Matrices de LEDs. Controlar cada LED individual en un letrero luminoso (Barrido de filas/columnas).", "consecuencia_de_error": "Letrero que no muestra el mensaje correcto."}
                }
            },
            {
                "subtema_titulo": "5. Bucles Infinitos (Riesgo y Utilidad)",
                "definicion": "Un bucle cuya condición NUNCA se vuelve falsa (`while True:`). \n- **Error:** El programa se cuelga y no responde.\n- **Utilidad:** Es la base de sistemas que siempre deben estar prendidos (Servidores, Arduinos).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo Arduino (Útil): `void loop() { ... }`. El código se repite por siempre para leer sensores.\nEjemplo Error: `x=1; while x>0: print(x)`. Como x siempre es positivo y no cambia, imprime por siempre.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Un bucle infinito accidental causa que el programa se... (cierre/cuelgue)",
                        "respuesta_correcta": "cuelgue",
                        "opciones": ["cuelgue", "cierre", "optimice", "guarde"]
                    },
                    "similares": [
                        {"pregunta": "Para salir de un `while True` intencional, se usa la orden...", "respuesta_correcta": "break", "opciones": ["break", "continue", "exit", "pass"]},
                        {"pregunta": "El software de un semáforo usa un bucle infinito. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Un bucle infinito consume CPU al 100% si no tiene pausas. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "`for i in range(10)` puede ser infinito? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "En sistemas embebidos (robots), el bucle principal DEBE ser infinito. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Servidores Web. Están en un bucle infinito esperando peticiones (requests).", "consecuencia_de_error": "Si el bucle termina, el servidor se apaga y la web se cae."},
                    "quimica": {"uso": "Dataloggers de larga duración. Registran temperatura cada segundo indefinidamente.", "consecuencia_de_error": "Si el logger se detiene, se pierden datos del experimento."},
                    "civil": {"uso": "Monitoreo sísmico. El sensor debe estar en bucle infinito 'escuchando' vibraciones.", "consecuencia_de_error": "No detectar un terremoto a tiempo."},
                    "mecanica": {"uso": "Controladores de motor (Idle). El motor en ralentí está en un bucle manteniendo las RPM mínimas.", "consecuencia_de_error": "El motor se apaga en cada semáforo."},
                    "mecatronica": {"uso": "Arduino/Microcontroladores. El `void loop()` es infinito por diseño. El robot siempre está 'vivo'.", "consecuencia_de_error": "El robot hace su tarea una vez y se 'muere'."},
                    "aeronautica": {"uso": "Computadora de vuelo. Ejecuta ciclos de control cientos de veces por segundo, por siempre.", "consecuencia_de_error": "Pérdida de control del avión (pantalla azul en el cielo)."},
                    "electrica": {"uso": "Relés de protección. Monitorean la red infinitamente buscando fallas.", "consecuencia_de_error": "Falla no detectada y daño masivo a la red."}
                }
            }
        ]
    },

    "PROG-05": {
        "nombre_completo": "Funciones y Modularidad: Organizando el Caos",
        "prerequisitos": ["PROG-04"],
        "quiz": [
            {
                "pregunta": "Una función se define con la palabra clave...",
                "respuesta": "def",
                "opciones": ["def", "func", "function", "void"]
            },
            {
                "pregunta": "El valor que 'devuelve' una función se especifica con la palabra clave:",
                "respuesta": "return",
                "opciones": ["return", "print", "back", "output"]
            }
        ],
        "refuerzo": [
            {
                "subtema_titulo": "1. Definición y Llamada (DRY - Don't Repeat Yourself)",
                "definicion": "Una función es un bloque de código con nombre que realiza una tarea específica. Se 'define' una vez y se 'llama' (ejecuta) las veces que quieras. Evita copiar y pegar código (Principio DRY).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Función para saludar.\n`def saludar():`\n`    print('Hola Ingeniero')`\n\nLlamada: `saludar()` (Imprime 'Hola Ingeniero').",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En Python, las funciones se definen con la palabra clave...",
                        "respuesta_correcta": "def",
                        "opciones": ["def", "fun", "define", "code"]
                    },
                    "similares": [
                        {"pregunta": "Para ejecutar una función, debes escribir su nombre seguido de...", "respuesta_correcta": "parentesis", "opciones": ["parentesis", "corchetes", "dos puntos", "comillas"]},
                        {"pregunta": "El principio de 'No Repetirse' se conoce por las siglas...", "respuesta_correcta": "dry", "opciones": ["dry", "wet", "solid", "oop"]},
                        {"pregunta": "Una función puede ser llamada múltiples veces. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Las funciones ayudan a organizar y ... el código.", "respuesta_correcta": "limpiar", "opciones": ["limpiar", "alargar", "complicar", "ocultar"]},
                        {"pregunta": "Si defines `def x():` pero nunca la llamas, el código de adentro se ejecuta... veces.", "respuesta_correcta": "0", "opciones": ["0", "1", "infinitas", "aleatorio"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Microservicios. Cada función es un servicio independiente (Login, Pago, Chat) que se puede arreglar sin romper los demás.", "consecuencia_de_error": "Código 'espagueti' imposible de mantener."},
                    "quimica": {"uso": "Rutinas de calibración. `calibrar_ph_metro()` se llama al inicio de cada experimento automáticamente.", "consecuencia_de_error": "Experimentos con instrumentos descalibrados."},
                    "civil": {"uso": "Cálculo de vigas. `calcular_momento()` se llama 500 veces para las 500 vigas del edificio.", "consecuencia_de_error": "Tener que corregir una fórmula en 500 lugares si cambia la norma."},
                    "mecanica": {"uso": "Ciclos de mecanizado. `taladrar_agujero()` se reutiliza para cada uno de los 8 cilindros del bloque motor.", "consecuencia_de_error": "Código CNC kilométrico y propenso a errores manuales."},
                    "mecatronica": {"uso": "Movimientos pregrabados. `mover_home()` lleva al robot a la posición segura. Se usa al encender y al acabar.", "consecuencia_de_error": "El robot inicia en una posición peligrosa."},
                    "aeronautica": {"uso": "Conversión de unidades. `pies_a_metros()` se usa en todo el sistema de navegación.", "consecuencia_de_error": "Errores de conversión manual (como el Mars Climate Orbiter)."},
                    "electrica": {"uso": "Lectura de sensores. `leer_voltaje_rms()` encapsula la matemática compleja de la raíz cuadrática media.", "consecuencia_de_error": "Código ilegible lleno de fórmulas matemáticas repetidas."}
                }
            },
            {
                "subtema_titulo": "2. Parámetros y Argumentos (Inputs)",
                "definicion": "Las funciones pueden recibir datos para procesar. Los 'Parámetros' son las variables en la definición (`def suma(a, b)`). Los 'Argumentos' son los valores reales que envías al llamar (`suma(5, 10)`).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: `def cuadrado(numero):`\n`    print(numero * numero)`\nLlamada: `cuadrado(5)` -> Imprime 25.\nLlamada: `cuadrado(10)` -> Imprime 100.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "En `def area(base, altura):`, 'base' y 'altura' son...",
                        "respuesta_correcta": "parametros",
                        "opciones": ["parametros", "argumentos", "resultados", "constantes"]
                    },
                    "similares": [
                        {"pregunta": "En `area(10, 20)`, los números 10 y 20 son...", "respuesta_correcta": "argumentos", "opciones": ["argumentos", "parametros", "nombres", "tipos"]},
                        {"pregunta": "Una función puede tener múltiples parámetros separados por...", "respuesta_correcta": "comas", "opciones": ["comas", "puntos", "espacios", "guiones"]},
                        {"pregunta": "Si `def f(x): print(x)`, y llamo `f(5)`, imprime...", "respuesta_correcta": "5", "opciones": ["5", "x", "f", "error"]},
                        {"pregunta": "¿Es obligatorio que una función tenga parámetros? (si/no)", "respuesta_correcta": "no", "opciones": ["no", "si"]},
                        {"pregunta": "Pasar menos argumentos de los requeridos causa un...", "respuesta_correcta": "error", "opciones": ["error", "warning", "null", "cero"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Autenticación. `login(usuario, password)`. La misma función sirve para millones de usuarios distintos.", "consecuencia_de_error": "Tener que escribir una función distinta para cada usuario."},
                    "quimica": {"uso": "Leyes de gases. `calcular_presion(T, V, n)`. Cambias los insumos y te da el resultado para ese gas.", "consecuencia_de_error": "Cálculos rígidos que solo sirven para un caso específico."},
                    "civil": {"uso": "Cimentación. `diseñar_zapata(carga, tipo_suelo)`. La función adapta el diseño según el suelo.", "consecuencia_de_error": "Usar el mismo diseño de zapata en roca y en arcilla (colapso)."},
                    "mecanica": {"uso": "Engranajes. `generar_perfil_diente(modulo, numero_dientes)`. Genera la geometría CAD exacta.", "consecuencia_de_error": "Engranajes que no encajan."},
                    "mecatronica": {"uso": "Control de motores. `mover_motor(id_motor, velocidad, sentido)`. Una función controla todos los motores.", "consecuencia_de_error": "Confundir qué motor se debe mover."},
                    "aeronautica": {"uso": "Plan de vuelo. `calcular_combustible(distancia, viento, peso)`. Adapta la carga de combustible al clima.", "consecuencia_de_error": "Avión con combustible insuficiente para el viento en contra."},
                    "electrica": {"uso": "Filtros. `aplicar_filtro_pasa_bajos(señal, frecuencia_corte)`. Procesa cualquier señal de audio.", "consecuencia_de_error": "Filtros estáticos que no se pueden ajustar."}
                }
            },
            {
                "subtema_titulo": "3. Valor de Retorno (Return vs Print)",
                "definicion": "El `return` saca un valor de la función para que el programa lo use después. El `print` solo muestra texto en pantalla y el dato se pierde. Las funciones útiles suelen usar `return`. ",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: `def suma(a, b): return a + b`.\nUso: `resultado = suma(5, 5) + 10`. (resultado vale 20).\nSi usaras `print`, `suma(5, 5) + 10` daría Error, porque no puedes sumar 'Texto' + 10.",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Si una función no tiene `return`, devuelve por defecto el valor...",
                        "respuesta_correcta": "none",
                        "opciones": ["none", "0", "null", "false"]
                    },
                    "similares": [
                        {"pregunta": "`return` finaliza la ejecución de la función inmediatamente. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Para guardar el resultado de una función en una variable, la función debe usar...", "respuesta_correcta": "return", "opciones": ["return", "print", "save", "input"]},
                        {"pregunta": "`print` envía datos a la pantalla, `return` envía datos al...", "respuesta_correcta": "programa", "opciones": ["programa", "usuario", "teclado", "archivo"]},
                        {"pregunta": "`def f(): return 5`. `x = f() + f()`. x vale...", "respuesta_correcta": "10", "opciones": ["10", "5", "25", "error"]},
                        {"pregunta": "¿Puedes tener múltiples `return` en una función (ej. dentro de if/else)? (si/no)", "respuesta_correcta": "si", "opciones": ["si", "no"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "APIs. Una función `get_usuario()` debe RETORNAR los datos (JSON) para que la web los muestre, no imprimirlos en la consola del servidor.", "consecuencia_de_error": "El frontend no recibe los datos."},
                    "quimica": {"uso": "Cálculo intermedio. `calcular_moles()` devuelve un número que luego usa `calcular_molaridad()`.", "consecuencia_de_error": "Imposible encadenar cálculos."},
                    "civil": {"uso": "Análisis. `obtener_maximo_sismo()` devuelve un valor que se usa para `diseñar_columna()`.", "consecuencia_de_error": "Datos aislados que no se integran en el diseño final."},
                    "mecanica": {"uso": "Simulación. `calcular_friccion()` devuelve una fuerza que se resta en la ecuación `F=ma`.", "consecuencia_de_error": "La simulación no tiene en cuenta la fricción."},
                    "mecatronica": {"uso": "Sensores. `leer_distancia()` retorna un `float` (cm) que el robot usa para decidir si frenar.", "consecuencia_de_error": "El robot 'imprime' la distancia pero no la 'siente', y choca."},
                    "aeronautica": {"uso": "Navegación. `calcular_rumbo()` devuelve grados que se envían al piloto automático.", "consecuencia_de_error": "El avión vuela a ciegas."},
                    "electrica": {"uso": "Protección. `checar_corriente()` retorna `True` si es segura o `False` si hay peligro.", "consecuencia_de_error": "El sistema no sabe cuándo cortar la energía."}
                }
            },
            {
                "subtema_titulo": "4. Alcance de Variables (Scope: Local vs Global)",
                "definicion": "- **Local:** Variable creada DENTRO de una función. Solo existe allí. Se borra al terminar.\n- **Global:** Creada FUERA. Visible por todos. (¡Cuidado! Modificarlas dentro de funciones causa bugs difíciles de rastrear).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo:\n`g = 10` (Global)\n`def func():`\n`   L = 5` (Local)\n`   print(g)` (OK, lee global)\n`print(L)` (ERROR, L no existe fuera de func).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Una variable local con el mismo nombre que una global, ¿cuál tiene prioridad dentro de la función?",
                        "respuesta_correcta": "local",
                        "opciones": ["local", "global", "ninguna", "error"]
                    },
                    "similares": [
                        {"pregunta": "Las variables locales se destruyen cuando la función...", "respuesta_correcta": "termina", "opciones": ["termina", "empieza", "retorna", "imprime"]},
                        {"pregunta": "Es una buena práctica usar muchas variables globales. (verdadero/falso)", "respuesta_correcta": "falso", "opciones": ["falso", "verdadero"]},
                        {"pregunta": "Para modificar una global dentro de una función en Python, usas la palabra clave...", "respuesta_correcta": "global", "opciones": ["global", "local", "static", "extern"]},
                        {"pregunta": "El uso de variables locales ahorra memoria. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "Las variables locales protegen el código de interferencias externas. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Seguridad. Las contraseñas deben ser variables locales dentro de la función de login y borrarse inmediatamente.", "consecuencia_de_error": "Contraseñas quedando en memoria global accesibles a hackers."},
                    "quimica": {"uso": "Iteraciones. `temp` en una función de simulación debe ser local para no afectar la temperatura global del sistema por error.", "consecuencia_de_error": "Corrupción de datos entre experimentos simulados."},
                    "civil": {"uso": "Cálculo independiente. La variable `carga` al diseñar la Viga A no debe afectar el cálculo de la Viga B.", "consecuencia_de_error": "Errores de arrastre en el diseño estructural."},
                    "mecanica": {"uso": "Subrutinas. Una función que calcula el diámetro de un tornillo no debe cambiar por error el diámetro del eje principal.", "consecuencia_de_error": "Piezas que no ensamblan."},
                    "mecatronica": {"uso": "Control concurrente. Si dos brazos robots usan la misma variable global `posicion`, se interferirán.", "consecuencia_de_error": "Colisión entre robots."},
                    "aeronautica": {"uso": "Redundancia. Cada computadora de vuelo usa sus propias variables locales. Si una falla, no corrompe a la otra.", "consecuencia_de_error": "Fallo total del sistema de control."},
                    "electrica": {"uso": "Interrupciones. Las variables dentro de una interrupción (ISR) deben manejarse con cuidado (volatile) respecto a las globales.", "consecuencia_de_error": "Comportamiento errático del microcontrolador."}
                }
            },
            {
                "subtema_titulo": "5. Librerías y Módulos (Import)",
                "definicion": "No reinventes la rueda. Las librerías son colecciones de funciones escritas por expertos. En Python, usas `import`. Ejemplos: `math` (matemáticas), `random` (azar), `time` (tiempo).",
                "diagrama": "",  # 🖼️ INICIALIZADO
                "ejemplo_resuelto": "Ejemplo: Calcular raíz cuadrada.\nSin librería: (Difícil de programar).\nCon librería:\n`import math`\n`resultado = math.sqrt(25)` (Usa la función `sqrt` del módulo `math`).",
                "ejercicio": {
                    "principal": {
                        "pregunta": "Para usar funciones de matemáticas avanzadas en Python, importas el módulo...",
                        "respuesta_correcta": "math",
                        "opciones": ["math", "calc", "algebra", "nums"]
                    },
                    "similares": [
                        {"pregunta": "Para generar números aleatorios, importas...", "respuesta_correcta": "random", "opciones": ["random", "chance", "dice", "math"]},
                        {"pregunta": "Para hacer pausas en el programa (delay), importas...", "respuesta_correcta": "time", "opciones": ["time", "wait", "sleep", "clock"]},
                        {"pregunta": "Las librerías permiten reutilizar código de otros. (verdadero/falso)", "respuesta_correcta": "verdadero", "opciones": ["verdadero", "falso"]},
                        {"pregunta": "En `math.pi`, `pi` es una... (función/constante) del módulo.", "respuesta_correcta": "constante", "opciones": ["constante", "funcion", "clase", "variable"]},
                        {"pregunta": "La función `random.randint(1, 10)` devuelve un entero entre 1 y...", "respuesta_correcta": "10", "opciones": ["10", "9", "11", "0"]}
                    ]
                },
                "aplicaciones": {
                    "sistemas": {"uso": "Librerías de encriptación (`hashlib`). Nunca escribas tu propia encriptación, usa la estándar.", "consecuencia_de_error": "Sistemas vulnerables y hackeables."},
                    "quimica": {"uso": "Librerías de ciencia de datos (`pandas`, `scipy`). Para analizar millones de datos moleculares.", "consecuencia_de_error": "Análisis manual lento e impreciso."},
                    "civil": {"uso": "Librerías de elementos finitos (`OpenSees`). Para simular terremotos sin programar la física desde cero.", "consecuencia_de_error": "Reinventar la rueda con errores matemáticos."},
                    "mecanica": {"uso": "Librerías CAD (`FreeCAD api`). Generar geometría 3D mediante código.", "consecuencia_de_error": "Diseño manual tedioso."},
                    "mecatronica": {"uso": "Librerías de visión (`OpenCV`). Permite al robot 'ver' y reconocer objetos con funciones ya hechas.", "consecuencia_de_error": "Años de desarrollo para lograr que el robot reconozca una pelota."},
                    "aeronautica": {"uso": "Librerías de atmósfera estándar. Calculan densidad y presión a cualquier altura automáticamente.", "consecuencia_de_error": "Errores en cálculos de altitud."},
                    "electrica": {"uso": "Librerías de FFT (`numpy.fft`). Transformada rápida de Fourier para analizar señales eléctricas.", "consecuencia_de_error": "Imposible analizar la calidad de la energía (armónicos)."}
                }
            }
        ]
    }
}