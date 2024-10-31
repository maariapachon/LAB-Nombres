import csv
from collections import namedtuple
import matplotlib.pyplot as plt

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año, nombre, frecuencia, genero')

def leer_frecuencias_nombres(ruta_fichero):
    frecuencias = []
    with open('ruta_fichero', encoding='utf-8') as fichero:
        lector = csv.reader(fichero)
        next(lector)
        for FrecuenciaNombre, año, nombre, frecuencia, genero in lector:
            año = int(año)
            nombre = str(nombre)
            frecuencia = int(frecuencia)
            genero = str(genero)
            tupla = (FrecuenciaNombre, año, nombre, frecuencia, genero)
            frecuencias.append(tupla)
    return frecuencias

def filtrar_por_genero(datos, genero):
    resultado = []
    for registro in datos:
        if registro.genero == genero:
            resultado.append(registro)
    return resultado

def calcular_nombres(datos, genero=None):
    nombres = set()
    for registro in datos:
        if registro.genero == genero or genero is None:
            nombres.add(registro.nombre)
    return nombres

def calcular_top_nombres_de_año(datos, año, genero=None):
    filtrados = [registro for registro in datos if registro.año == año and (registro.genero == genero or genero is None)]
    filtrados.sort(key=lambda x: x.frecuencia, reverse=True)
    return [(registro.nombre, registro.frecuencia) for registro in filtrados[10]]

def calcular_nombres_ambos_generos(datos):
    nombres_hombres = calcular_nombres(datos, 'Hombre')
    nombres_mujeres = calcular_nombres(datos, 'Mujer')
    return nombres_hombres.intersection(nombres_mujeres)

def calcular_nombres_compuestos(datos, genero=None):
    nombres_compuestos = set()
    for registro in datos:
        if '' in registro.nombre and (registro.genero == genero or genero is None):
            nombres_compuestos.add(registro.nombre)
    return nombres_compuestos

def calcular_frecuencia_media_nombre_años(datos, nombre, año_inicial, año_final):
    frecuencias = [registro.frecuencia for registro in datos if registro.nombre == nombre and año_inicial <= registro.año < año_final]
    if frecuencias:
        return sum(frecuencias) / len(frecuencias)
    return 0

def calcular_nombres_mas_frecuente_año_genero(datos, año, genero):
    filtrados = [registro for registro in datos if registro.año == año and registro.genero == genero]
    if filtrados:
        return max(filtrados, key=lambda x: x. frecuencia).nombre
    return ''

def calcular_año_mas_frecuencia_nombre(datos, nombre):
    filtrados = [registro for registro in datos if registro.nombre == nombre]
    if filtrados:
        return max(filtrados, key=lambda x: x.frecuencia).año
    return 0

def calcular_nombres_mas_frecuentes(datos, genero, decada, n=5):
    inicio = decada
    fin = decada + 10
    filtrados = [registro for registro in datos if inicio <= registro.año < fin and registro.genero == genero]
    filtrados.sort(key=lambda x: x.frecuencia, reverse=True)
    return [(registro.nombre, registro.frecuencia) for registro in filtrados[:n]]

def calcular_año_frecuencia_por_nombre(datos, genero):
    resultado = {}
    for registro in datos:
        if registro.genero == genero:
            if registro.nombre not in resultado:
                resultado[registro.nombre] = []
            resultado[registro.nombre].append((registro.año, registro.frecuencia))
    return resultado

def calcular_nombres_mas_frecuente_por_año(datos, genero):
    resultado = []
    años = set(registro.año for registro in datos)
    for año in años:
        filtrados = [registro for registro in datos if registro.año == año and registro.genero == genero]
        if filtrados:
            nombre_frecuente = max(filtrados, key=lambda x: x.frecuencia)
            resultado.append((año, nombre_frecuente.nombre, nombre_frecuente.frecuencia))
    return resultado

def calcular_frecuencia_por_año(datos, nombre):
    resultado = {}
    for registro in datos:
        if registro.nombre == nombre:
            if registro.año not in resultado:
                resultado[registro.año] = 0
            resultado[registro.año] += registro.frecuencia
    return sorted(resultado.items())

def mostrar_evolucion_por_año(datos, nombre):
    años, frecuencias = zip(*calcular_frecuencia_por_año(datos, nombre))
    plt.plot(años, frecuencias)
    plt.title(f"Evolucion del nombre '{nombre}'")
    plt.show()

def calcular_frecuencias_por_nombre(datos):
    frecuencias = {}
    for registro in datos:
        if registro.nombre not in frecuencias:
            frecuencias[registro.nombre] = 0
        frecuencias[registro.nombre] += registro.frecuencia
    return frecuencias

def mostrar_frecuencias_nombres(datos, limite=10):
    frecuencias = calcular_frecuencias_por_nombre(datos)
    nombres = sorted(frecuencias.keys(), key=lambda x: frecuencias[x], reverse=True)[:limite]
    plt.bar(nombres, [frecuencias[nombre] for nombre in nombres])
    plt.xticks(rotation=80)
    plt.title(f'Frecuencia de los {limite} nombres más comunes')
    plt.show()

