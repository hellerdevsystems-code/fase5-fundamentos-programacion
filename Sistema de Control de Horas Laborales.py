# Nombre del estudiante: Heller David Orozco Charris
# Grupo: 213022_134
# Programa: Ingeniería de Sistemas
# Código Fuente: Autoría propia


# Sistema de Control de Horas Laborales

print("\033[96m===========================================\033[0m")
print("\033[94m     SISTEMA DE CONTROL DE HORAS LABORALES\033[0m")
print("\033[96m===========================================\033[0m")


# Matriz de datos

recursos = [

    ["Carlos", 8, 8, 9, 8, 10],
    ["María", 7, 8, 8, 7, 8],
    ["Andrés", 9, 9, 8, 9, 10],
    ["Luisa", 6, 7, 8, 7, 6]

]


# Función para calcular horas

def calcular_horas_semana(horas):

    total = sum(horas)

    return total


# Función para clasificar jornada

def clasificar_jornada(total_horas):

    if total_horas > 40:

        return "\033[91mSobretiempo\033[0m"

    else:

        return "\033[92mHorario Estándar\033[0m"


# Reporte Final

print("\n\033[95m========== REPORTE SEMANAL ==========\033[0m\n")


for recurso in recursos:

    nombre = recurso[0]

    horas = recurso[1:]

    total = calcular_horas_semana(horas)

    clasificacion = clasificar_jornada(total)


    print(f"\033[93mEmpleado:\033[0m {nombre}")

    print(f"\033[94mTotal de horas trabajadas:\033[0m {total}")

    print(f"\033[92mClasificación:\033[0m {clasificacion}")

    print("\033[96m--------------------------------------\033[0m")