# ================================================================
#        CYBERSECURITY RISK ANALYZER
#        REGRESION LINEAL + MACHINE LEARNING
# ================================================================
#
# Proyecto: Ingenieria en Sistemas / Ciberseguridad
#
# IMPORTANTE:
# Instala las librerias antes de ejecutar:
#
# pip install pandas matplotlib scikit-learn
#
# ================================================================


# ================================================================
# LIBRERIAS
# ================================================================

import os

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)


# ================================================================
# INFORMACION DEL PROYECTO
# ================================================================

INFORMACION = {

    "version": "1.0",

    "autor": "Christian guillen gonzalez",

    "carrera": "Ingenieria en Sistemas / Ciberseguridad",

    "objetivo":
        "Estimar el riesgo de ciberseguridad "
        "utilizando Regresion Lineal.",

    "dataset":
        "Conjunto de datos utilizado para entrenar "
        "el modelo. Los datos son simulados.",

    "machine_learning":
        "El modelo aprende la relacion entre las "
        "variables de seguridad y el nivel de riesgo.",

    "mae":
        "Indica el error promedio entre el valor "
        "real y el valor predicho.",

    "r2":
        "Indica que tan bien el modelo se ajusta "
        "a los datos.",

    "metodologia":
        "Crear datos, dividirlos, entrenar el modelo, "
        "realizar predicciones, evaluar los resultados "
        "y probar nuevos datos."
}


# ================================================================
# COLORES
# ================================================================

RESET = "\033[0m"

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CIAN = "\033[96m"
BLANCO = "\033[97m"

NEGRITA = "\033[1m"
GRIS = "\033[90m"


# ================================================================
# LIMPIAR PANTALLA
# ================================================================

def limpiar_pantalla():

    if os.name == "nt":

        os.system("cls")

    else:

        os.system("clear")


# ================================================================
# TITULO
# ================================================================

def titulo(texto, numero=""):

    limpiar_pantalla()

    print(
        CIAN
        + NEGRITA
        + "\n"
        + "=" * 64
        + RESET
    )

    if numero != "":

        texto_completo = numero + " | " + texto

    else:

        texto_completo = texto

    print(
        CIAN
        + NEGRITA
        + texto_completo.center(64)
        + RESET
    )

    print(
        CIAN
        + NEGRITA
        + "=" * 64
        + RESET
    )


# ================================================================
# ESTADO DEL SISTEMA
# ================================================================

def estado_sistema():

    print(
        VERDE
        + "  [ ONLINE ] "
        + RESET
        + "| "
        + CIAN
        + "ML ENGINE "
        + RESET
        + "READY"
        + " | "
        + CIAN
        + "SECURITY "
        + RESET
        + "ACTIVE"
    )


# ================================================================
# SEPARADOR
# ================================================================

def separador():

    print(
        AZUL
        + "-" * 64
        + RESET
    )


# ================================================================
# CONTINUAR
# ================================================================

def continuar():

    print()

    input(
        AMARILLO
        + "  Presiona ENTER para continuar..."
        + RESET
    )

    limpiar_pantalla()


# ================================================================
# BANNER
# ================================================================

def banner():

    print(
        CIAN
        + NEGRITA
        + """
================================================================
||                                                            ||
||              CYBERSECURITY RISK ANALYZER                  ||
||                                                            ||
||              MACHINE LEARNING                             ||
||              REGRESION LINEAL                             ||
||                                                            ||
================================================================
"""
        + RESET
    )


# ================================================================
# PEDIR NUMEROS
# ================================================================

def pedir_numero(
    mensaje,
    minimo=0,
    maximo=None
):

    while True:

        entrada = input(
            CIAN
            + "  "
            + mensaje
            + RESET
        ).strip()

        try:

            valor = float(entrada)

        except ValueError:

            print(
                ROJO
                + "\n  [ERROR] Introduce solamente un numero."
                + RESET
            )

            continue


        if valor < minimo:

            print(
                ROJO
                + "\n  [ERROR] El valor no puede ser menor que "
                + str(minimo)
                + "."
                + RESET
            )

            continue


        if (
            maximo is not None
            and valor > maximo
        ):

            print(
                ROJO
                + "\n  [ERROR] El valor no puede ser mayor que "
                + str(maximo)
                + "."
                + RESET
            )

            continue


        return valor


# ================================================================
# MENU DE INFORMACION
# ================================================================

def menu_informacion():

    while True:

        titulo(
            "CENTRO DE INFORMACION"
        )

        estado_sistema()

        print()

        print(
            CIAN
            + "[1]"
            + RESET
            + " Objetivo"
        )

        print(
            CIAN
            + "[2]"
            + RESET
            + " Dataset"
        )

        print(
            CIAN
            + "[3]"
            + RESET
            + " Machine Learning"
        )

        print(
            CIAN
            + "[4]"
            + RESET
            + " Metricas"
        )

        print(
            CIAN
            + "[5]"
            + RESET
            + " Metodologia"
        )

        print(
            CIAN
            + "[6]"
            + RESET
            + " Volver"
        )

        separador()

        opcion = input(
            "\n  Selecciona una opcion: "
        ).strip()


        # ========================================================
        # OBJETIVO
        # ========================================================

        if opcion == "1":

            titulo(
                "OBJETIVO"
            )

            estado_sistema()

            print(
                "\n  OBJETIVO DEL PROYECTO"
            )

            separador()

            print(
                "\n  "
                + INFORMACION["objetivo"]
            )

            print(
                "\n  El programa utiliza informacion "
                "relacionada con"
            )

            print(
                "  seguridad para calcular una "
                "estimacion del riesgo."
            )

            continuar()


        # ========================================================
        # DATASET
        # ========================================================

        elif opcion == "2":

            titulo(
                "DATASET"
            )

            estado_sistema()

            print(
                "\n  QUE ES UN DATASET?"
            )

            separador()

            print(
                "\n  "
                + INFORMACION["dataset"]
            )

            print(
                "\n  VARIABLES:"
            )

            print(
                "\n  - Vulnerabilidades"
            )

            print(
                "  - Incidentes"
            )

            print(
                "  - Sistemas actualizados"
            )

            print(
                "  - Riesgo"
            )

            continuar()


        # ========================================================
        # MACHINE LEARNING
        # ========================================================

        elif opcion == "3":

            titulo(
                "MACHINE LEARNING"
            )

            estado_sistema()

            print(
                "\n  MODELO:"
            )

            print(
                VERDE
                + "  Regresion Lineal"
                + RESET
            )

            print(
                "\n  "
                + INFORMACION["machine_learning"]
            )

            print(
                "\n  DATOS DE ENTRADA:"
            )

            print(
                "  - Vulnerabilidades"
            )

            print(
                "  - Incidentes"
            )

            print(
                "  - Sistemas actualizados"
            )

            print(
                "\n  RESULTADO:"
            )

            print(
                "  - Riesgo estimado"
            )

            continuar()


        # ========================================================
        # METRICAS
        # ========================================================

        elif opcion == "4":

            titulo(
                "METRICAS"
            )

            estado_sistema()

            print(
                "\n  MAE"
            )

            print(
                "  "
                + INFORMACION["mae"]
            )

            print(
                "\n  R2"
            )

            print(
                "  "
                + INFORMACION["r2"]
            )

            continuar()


        # ========================================================
        # METODOLOGIA
        # ========================================================

        elif opcion == "5":

            titulo(
                "METODOLOGIA"
            )

            estado_sistema()

            print(
                "\n  "
                + INFORMACION["metodologia"]
            )

            print(
                "\n  PROCESO:"
            )

            separador()

            print(
                "  1. Crear dataset"
            )

            print(
                "  2. Separar los datos"
            )

            print(
                "  3. Entrenar modelo"
            )

            print(
                "  4. Realizar predicciones"
            )

            print(
                "  5. Evaluar resultados"
            )

            print(
                "  6. Probar nuevos datos"
            )

            continuar()


        # ========================================================
        # VOLVER
        # ========================================================

        elif opcion == "6":

            break


        else:

            print(
                ROJO
                + "\n  [ERROR] Opcion no valida."
                + RESET
            )

            input(
                "\n  Presiona ENTER para continuar..."
            )


# ================================================================
# INICIAR PROGRAMA
# ================================================================

def iniciar_programa():


    # ============================================================
    # 01 - DATASET
    # ============================================================

    titulo(
        "DATASET",
        "01"
    )

    estado_sistema()

    print(
        "\n  Cargando datos..."
    )


    # Dataset pequeño para facilitar
    # la explicacion del proyecto.

    datos = {

        "vulnerabilidades":
        [
            10, 20, 30, 40, 50,
            60, 70, 80, 90, 100
        ],

        "incidentes":
        [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10
        ],

        "sistemas_actualizados":
        [
            95, 90, 85, 80, 75,
            70, 65, 60, 55, 50
        ],

        "riesgo":
        [
            10, 18, 27, 35, 44,
            53, 62, 70, 81, 90
        ]
    }


    df = pd.DataFrame(datos)


    print(
        VERDE
        + "\n  [OK] Dataset cargado correctamente."
        + RESET
    )

    print()

    print(
        df.to_string(index=False)
    )


    continuar()


    # ============================================================
    # 02 - NUEVO CASO
    # ============================================================

    titulo(
        "NUEVO CASO",
        "02"
    )

    estado_sistema()


    print(
        "\n  Introduce los datos de una "
        "organizacion ficticia."
    )


    print(
        "\n  Los valores que introduzcas aqui "
        "seran utilizados"
    )

    print(
        "  directamente para calcular la prediccion."
    )


    separador()


    vulnerabilidades = pedir_numero(
        "Vulnerabilidades: "
    )


    incidentes = pedir_numero(
        "Incidentes: "
    )


    sistemas_actualizados = pedir_numero(
        "Sistemas actualizados (%): ",
        0,
        100
    )


    print(
        VERDE
        + "\n  [OK] Datos registrados correctamente."
        + RESET
    )


    continuar()


    # ============================================================
    # 03 - PREPARAR MACHINE LEARNING
    # ============================================================

    titulo(
        "MACHINE LEARNING",
        "03"
    )

    estado_sistema()


    print(
        "\n  Preparando los datos..."
    )


    # Variables de entrada.

    X = df[
        [
            "vulnerabilidades",
            "incidentes",
            "sistemas_actualizados"
        ]
    ]


    # Variable que queremos predecir.

    y = df["riesgo"]


    # Dividir dataset.

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.20,

        random_state=42
    )


    print(
        "\n  Datos para entrenamiento: "
        + str(len(X_train))
    )


    print(
        "  Datos para prueba: "
        + str(len(X_test))
    )


    continuar()


    # ============================================================
    # 04 - ENTRENAMIENTO
    # ============================================================

    titulo(
        "ENTRENAMIENTO",
        "04"
    )

    estado_sistema()


    print(
        "\n  Entrenando Regresion Lineal..."
    )


    modelo = LinearRegression()


    modelo.fit(
        X_train,
        y_train
    )


    print(
        VERDE
        + "\n  [OK] Modelo entrenado correctamente."
        + RESET
    )


    continuar()


    # ============================================================
    # 05 - PREDICCIONES DEL MODELO
    # ============================================================

    titulo(
        "PREDICCIONES",
        "05"
    )

    estado_sistema()


    # Predicciones sobre los datos de prueba.

    predicciones = modelo.predict(
        X_test
    )


    print(
        "\n  RIESGO REAL     RIESGO PREDICHO"
    )


    separador()


    for real, predicho in zip(
        y_test,
        predicciones
    ):

        print(
            "     "
            + f"{real:>6.2f}"
            + "           "
            + f"{predicho:>6.2f}"
        )


    continuar()


    # ============================================================
    # 06 - EVALUACION
    # ============================================================

    titulo(
        "EVALUACION",
        "06"
    )

    estado_sistema()


    mae = mean_absolute_error(
        y_test,
        predicciones
    )


    r2 = r2_score(
        y_test,
        predicciones
    )


    print(
        "\n  RESULTADOS DEL MODELO"
    )


    separador()


    print(
        CIAN
        + "\n  MAE : "
        + f"{mae:.2f}"
        + RESET
    )


    print(
        VERDE
        + "\n  R2  : "
        + f"{r2:.2f}"
        + RESET
    )


    continuar()


    # ============================================================
    # 07 - GRAFICO
    # ============================================================

    titulo(
        "GRAFICO",
        "07"
    )

    estado_sistema()


    print(
        "\n  Los puntos azules representan "
        "las predicciones."
    )


    print(
        "  La linea roja representa una "
        "prediccion ideal."
    )


    print(
        "\n  Mientras mas cerca esten los puntos "
        "de la linea,"
    )


    print(
        "  mejor es la aproximacion del modelo."
    )


    plt.figure(
        figsize=(9, 6)
    )


    plt.scatter(

        y_test,

        predicciones,

        color="#00BFFF",

        edgecolors="black",

        s=100,

        label="Predicciones"
    )


    minimo = min(

        float(y_test.min()),

        float(predicciones.min())
    )


    maximo = max(

        float(y_test.max()),

        float(predicciones.max())
    )


    if minimo == maximo:

        minimo -= 1

        maximo += 1


    plt.plot(

        [minimo, maximo],

        [minimo, maximo],

        color="red",

        linestyle="--",

        linewidth=2,

        label="Prediccion ideal"
    )


    plt.xlabel(
        "Riesgo real"
    )


    plt.ylabel(
        "Riesgo predicho"
    )


    plt.title(
        "Riesgo real vs Riesgo predicho"
    )


    plt.legend()

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()


    plt.show()


    continuar()


    # ============================================================
    # 08 - PREDICCION DINAMICA
    # ============================================================

    titulo(
        "RESULTADO FINAL",
        "08"
    )

    estado_sistema()


    print(
        "\n  Analizando los datos introducidos..."
    )


    # ============================================================
    # CREAR NUEVO CASO
    # ============================================================

    nuevo_caso = pd.DataFrame({

        "vulnerabilidades":
        [
            vulnerabilidades
        ],

        "incidentes":
        [
            incidentes
        ],

        "sistemas_actualizados":
        [
            sistemas_actualizados
        ]
    })


    # ============================================================
    # MOSTRAR DATOS INTRODUCIDOS
    # ============================================================

    print(
        "\n  DATOS ANALIZADOS"
    )


    separador()


    print(
        "\n  Vulnerabilidades      : "
        + f"{vulnerabilidades:.0f}"
    )


    print(
        "  Incidentes            : "
        + f"{incidentes:.0f}"
    )


    print(
        "  Sistemas actualizados : "
        + f"{sistemas_actualizados:.0f}%"
    )


    # ============================================================
    # REALIZAR PREDICCION
    # ============================================================

    riesgo = modelo.predict(
        nuevo_caso
    )[0]


    # Asegurar que el resultado este entre 0 y 100.

    riesgo = max(
        0,
        min(
            100,
            float(riesgo)
        )
    )


    # ============================================================
    # DETERMINAR NIVEL
    # ============================================================

    if riesgo < 30:

        nivel = "BAJO"

        color = VERDE

        recomendacion = (
            "Mantener las medidas de seguridad actuales."
        )


    elif riesgo < 60:

        nivel = "MEDIO"

        color = AMARILLO

        recomendacion = (
            "Revisar las medidas de seguridad "
            "y corregir posibles problemas."
        )


    elif riesgo < 80:

        nivel = "ALTO"

        color = ROJO

        recomendacion = (
            "Priorizar la correccion de "
            "vulnerabilidades."
        )


    else:

        nivel = "MUY ALTO"

        color = ROJO

        recomendacion = (
            "Realizar una revision de seguridad "
            "lo antes posible."
        )


    # ============================================================
    # MOSTRAR RESULTADO
    # ============================================================

    print(
        "\n"
        + CIAN
        + "================================================"
        + RESET
    )


    print(
        VERDE
        + NEGRITA
        + "              RESULTADO DEL MODELO"
        + RESET
    )


    print(
        CIAN
        + "================================================"
        + RESET
    )


    print(
        "\n              RIESGO ESTIMADO"
    )


    print(
        VERDE
        + NEGRITA
        + f"\n                  {riesgo:.2f}%"
        + RESET
    )


    print(
        "\n"
        + color
        + NEGRITA
        + f"                  NIVEL: {nivel}"
        + RESET
    )


    print(
        "\n"
        + CIAN
        + "================================================"
        + RESET
    )


    print(
        "\n  Recomendacion:"
    )


    print(
        "  "
        + recomendacion
    )


    print(
        "\n"
        + GRIS
        + "  El resultado fue calculado por "
          "el modelo de Regresion Lineal."
        + RESET
    )


    continuar()


# ================================================================
# MENU PRINCIPAL
# ================================================================

def menu_principal():

    while True:

        limpiar_pantalla()


        banner()


        estado_sistema()


        print(
            "\n  MAIN CONTROL PANEL"
        )


        separador()


        print(
            "\n  "
            + CIAN
            + "[1]"
            + RESET
            + "  Iniciar analisis"
        )


        print(
            "  "
            + CIAN
            + "[2]"
            + RESET
            + "  Centro de informacion"
        )


        print(
            "  "
            + CIAN
            + "[3]"
            + RESET
            + "  Salir"
        )


        separador()


        print(
            "\n  Sistema: CYBER-RISK-ML"
        )


        print(
            "  Version: "
            + INFORMACION["version"]
        )


        print(
            "  Estado: Operational"
        )


        opcion = input(
            "\n  Selecciona una opcion: "
        ).strip()


        # ========================================================
        # INICIAR
        # ========================================================

        if opcion == "1":

            iniciar_programa()


        # ========================================================
        # INFORMACION
        # ========================================================

        elif opcion == "2":

            menu_informacion()


        # ========================================================
        # SALIR
        # ========================================================

        elif opcion == "3":

            limpiar_pantalla()


            print(
                CIAN
                + NEGRITA
                + """
================================================================
                    SYSTEM SHUTDOWN
================================================================
"""
                + RESET
            )


            print(
                "\n  Programa cerrado correctamente."
            )


            print(
                "\n  Datos utilizados: simulados."
            )


            break


        # ========================================================
        # ERROR
        # ========================================================

        else:

            print(
                ROJO
                + "\n  [ERROR] Opcion no valida."
                + RESET
            )


            input(
                "\n  Presiona ENTER para continuar..."
            )


# ================================================================
# EJECUCION
# ================================================================

if __name__ == "__main__":

    try:

        menu_principal()


    except KeyboardInterrupt:

        limpiar_pantalla()

        print(
            "\n"
            + AMARILLO
            + "Programa detenido por el usuario."
            + RESET
        )


    except Exception as error:

        limpiar_pantalla()

        print(
            "\n"
            + ROJO
            + "[ERROR INESPERADO]"
            + RESET
        )

        print(
            "\nDetalle del error:"
        )

        print(
            error
        )
