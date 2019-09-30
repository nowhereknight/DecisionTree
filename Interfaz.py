import tkinter as tk
import tkinter.ttk as ttk
import ArbolClasificacion as ac
import pandas as pd
import numpy as np

etiquetas = ["sexo", "prom_bacho","prom_s","bachillerato","ingreso_mensual","trabaja","tiempo_iv","n_habitantes","padre_esco","madre_esco","n_hermanos","dependencia_economica","razon_ingenieria","A_TIEMPO"]

def on_select(event=None):
    global etiquetas, probability
    consulta=[]
    print('----------------------------')

    if event: # <-- this works only with bind because `command=` doesn't send event
        print("event.widget:", event.widget.get())

    for i, x in enumerate(all_comboboxes):
        option = x.get().split(".")
        consulta.append(int(option[0]))
    data=pd.read_csv('2012.csv')
    #Utilizando pandas nos retorna un DataFrame así que lo convertimos a una lista de listas que va a ser nuestro trainning data
    training_data=np.array(data).tolist()
    miArbol = ac.crearArbol(training_data)
    probabilidades=ac.imprimirHoja(ac.clasificar(consulta, miArbol))
    print(probabilidades)
    if ( 0 in probabilidades.keys() ):
        probabilidad="Alguien tiene que estudiar más"
    else:
        print("A")
        probabilidad="Tienes todas las de ganar. No le quites las ganas"
    probability.config(text=probabilidad)
# --- main ---

root = tk.Tk()
root.geometry("500x800")
root.resizable(0,0)
root.configure(background='white')

all_comboboxes = []
a = tk.Label(root, text="Bienvenido")
a.pack()

a = tk.Label(root, text="1. ¿Cuál es tu sexo?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Hombre",
								"2. Mujer",
								))
cb.set("1. Hombre")
cb.configure(width=20)
cb.pack()
all_comboboxes.append(cb)

b = tk.Label(root, text="2. ¿Cuál fue tu promedio de calificaciones de secundaria?")
b.pack()

cb = ttk.Combobox(root, values=(
								"1. Entre 6.0 y 6.5",
								"2. Entre 6.5 y 7.0",
								"3. Entre 7.0 y 7.5", 
								"4. Entre 7.5 y 8.0",
								"5. Entre 8.0 y 8.5",
								"6. Entre 8.5 y 9.0",
								"7.Entre 9.0 y 9.5",
								"8.Entre 9.5 y 10.0"))
cb.set("1. Entre 6.0 y 6.5")
cb.configure(width=30)

cb.pack()
all_comboboxes.append(cb)


a = tk.Label(root, text="3. ¿Cuál fue tu promedio de calificaciones de bachillerato?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Entre 6.0 y 6.5",
								"2. Entre 6.5 y 7.0",
								"3. Entre 7.0 y 7.5", 
								"4. Entre 7.5 y 8.0",
								"5. Entre 8.0 y 8.5",
								"6. Entre 8.5 y 9.0",
								"7. Entre 9.0 y 9.5",
								"8. Entre 9.5 y 10.0"))
cb.set("1. Entre 6.0 y 6.5")
cb.configure(width=30)
cb.pack()

all_comboboxes.append(cb)

a = tk.Label(root, text="4. ¿En qué institución estudiaste el bachillerato?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Escuela Nacional Preparatoria de la UNAM (ENP)",
								"2. Colegio de Ciencias y Humanidades de la UNAM (CCH)",
								"3. Colegio de Bachilleres en ZMCM (Col. Bach)", 
								"4. Bachillerato Tecnológico en ZMCM (CECyT, CEBETIS; CBETA u otro)",
								"5. Institución Privada en la CMDX",
								"6. Institución pública fuera de la ZMCM",
								"7. Institución privada fuera de la ZMCM",
								"8. Preparatoria Abierta (SEP o Col. Bach)",
								"9. Institución en el extranjero",
								"10. Otro"
								))
cb.set("1. Escuela Nacional Preparatoria de la UNAM (ENP)")
cb.configure(width=50)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="5. ¿Cuál es tu promedio mensual aproximado?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Menos de $3,000",
								"2. Entre $3,000 y $5,000",
								"3. Entre $5,000 y $7,000", 
								"4. Entre $7,000 y $9,000",
								"5. Entre $9,000 y $11,000",
								"6. Más de 11,000"))
cb.set("1. Menos de $3,000")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="6. ¿Trabajas?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Si, permanentemente",
								"2. Si, eventualmente",
								"3. No"))
cb.set("1. Si, permanentemente")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="7. ¿Cuánto tiempo empleas diariamente en transporte para ir y venir a la universidad?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Entre 15 minutos y media hora",
								"2. Entre media hora y una hora",
								"3. Entre una hora y hora y media", 
								"4. Entre hora y media y dos horas",
								"5. Entre dos horas y media, y tres horas",
								"6. Más de tres horas"))
cb.set("1. Entre 15 minutos y media hora")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="8. ¿Cuántas personas habitan dónde vives?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Una",
								"2. Dos",
								"3. Tres", 
								"4. Cuatro",
								"5. Cinco",
								"6. Seis",
								"7. Siete o más"))
cb.set("1. Una")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="9. ¿Cuál es el nivel máximo de estudios de tu padre?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Sin instrucción formal",
								"2. Primaria sin terminar",
								"3. Primaria terminada", 
								"4. Secundaria terminada",
								"5. Bachillerato terminado",
								"6. Inició licenciatura",
								"7. Terminó una licenciatura pero no se titulo",
								"8. Licenciatura titulado(a)",
								"9. Estudios de Postgrado",
								))
cb.set("1. Sin instrucción formal")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="10. ¿Cuál es el nivel máximo de estudios de tu madre?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Sin instrucción formal",
								"2. Primaria sin terminar",
								"3. Primaria terminada", 
								"4. Secundaria terminada",
								"5. Bachillerato terminado",
								"6. Inició licenciatura",
								"7. Terminó una licenciatura pero no se titulo",
								"8. Licenciatura titulado(a)",
								"9. Estudios de Postgrado",
								))
cb.set("1. Sin instrucción formal")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="11. ¿Cuántos hermanos tienes?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Ninguno(a)",
								"2. Uno",
								"3. Dos", 
								"4. Tres",
								"5. Cuatro",
								"6. Cinco",
								"7. Más de cinco"))
cb.set("1. Ninguno(a)")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="12. ¿Principalmente de quién dependes económicamente?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. De tu padre",
								"2. De tu madre",
								"3. De ambos padres", 
								"4. Unicamente de ti mismo",
								"5. De algún hermano(a)",
								"6. De otro familiar",
								"7. De un tutor que no es tu familiar",
								"8. Otro"))
cb.set("1. De tu padre")
cb.configure(width=30)
cb.pack()
all_comboboxes.append(cb)

a = tk.Label(root, text="13. ¿Cuál es la principal razón por la que elegiste la carrera de ingeniería?")
a.pack()
cb = ttk.Combobox(root, values=(
								"1. Porque te ofrece un buen futuro económico y social",
								"2. Porque es una carrera necesaria para el desarrollo del país",
								"3. Porque tus padres, hermanos o profesores te alientan a estudiarla", 
								"4. Porque te consideras una persona creativa y sistemática",
								"5. Porque siempre has sido bueno en matemáticas",
								"6. Porque siempre has tenido facilidad para actividades como examinar, armar, arreglar, etc...",
								"7. Porque conoces ingenieros y te consideras afin a ellos",
								"8. Porque conoces los compos de acción del ingeniero",
								"9. No tienes clara la razón",
								"10. No es la carrera que elegiste"
								))
cb.set("1. Porque te ofrece un buen futuro económico y social")
cb.configure(width=50)
cb.pack()
all_comboboxes.append(cb)

probability = tk.Label(root, text="   ")
probability.pack()


b = tk.Button(root, text="Calcular probabilidad", command=on_select)
b.pack()

root.mainloop()