import pandas as pd
import matplotlib.pyplot as plt

import math
import random


#-----------------------------------------interfaz------------------------------------
def menu():
    print("\t╔════════════════════════════════════════╗")
    print("\t║         B i e n v e n i d o s          ║")
    print("\t╚════════════════════════════════════════╝")
    print()
    print("\t╔══════════════════════════════════════════════════════════════════════╗")
    print("\t║  Seleccione una opción:                                              ║")
    print("\t║                                                                      ║")
    print("\t║  1) Relación entre la cantidad de personas y  residuos por año       ║")
    print("\t║  2) Cantidad total de residuos sólidos municipales por región y año  ║")
    print("\t║  3) Cantidad de residuos sólidos municipales  por departamento y año ║")
    print("\t║  4) Cantidad de residuos por año                                     ║")
    print("\t║  5) Desencriptar con (Clave Pública)                                 ║")
    print("\t║  6) Salir                                                            ║")
    print("\t║                                                                      ║")
    print("\t╚══════════════════════════════════════════════════════════════════════╝")


#-------------------------funciones----------------------------

data = pd.read_csv("data.csv",sep= ';')
print(data)
print(data[['N_SEC','UBIGEO','REG_NAT','DEPARTAMENTO','PROVINCIA','DISTRITO','POB_TOTAL','POB_URBANA','POB_RURAL','QRESIDUOS_MUN','PERIODO']])
print(data.info())
print(data.iloc[:2,:3])



#--------------------------opciones--------------------------------












#-----------------------------------main-----------------------------