
from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog as fd
import webbrowser



def default_edad(event):

	textoActual = e_edad.get()

	if (textoActual == "años"):
		e_edad.delete(0, END)
		e_edad.config(fg = 'black')

	elif (textoActual == ""):
		e_edad.insert(0,"años")
		e_edad.config(fg = 'grey')



def default_estatura(event):

	textoActual = e_estatura.get()

	if (textoActual == "cm"):
		e_estatura.delete(0, END)
		e_estatura.config(fg = 'black')

	elif (textoActual == ""):
		e_estatura.insert(0,"cm")
		e_estatura.config(fg = 'grey')



def default_peso(event):

	textoActual = e_peso.get()

	if (textoActual == "kg"):
		e_peso.delete(0, END)
		e_peso.config(fg = 'black')

	elif (textoActual == ""):
		e_peso.insert(0,"kg")
		e_peso.config(fg = 'grey')



def default_pesoToUse(event):

	textoActual = e_pesoToUse.get()

	if (textoActual == "kg"):
		e_pesoToUse.delete(0, END)
		e_pesoToUse.config(fg = 'black')

	elif (textoActual == ""):
		e_pesoToUse.insert(0,"kg")
		e_pesoToUse.config(fg = 'grey')



def default_cintura(event):

	textoActual = e_cintura.get()

	if (textoActual == "cm"):
		e_cintura.delete(0, END)
		e_cintura.config(fg = 'black')

	elif (textoActual == ""):
		e_cintura.insert(0,"cm")
		e_cintura.config(fg = 'grey')



def default_abdomen(event):

	textoActual = e_abdomen.get()

	if (textoActual == "cm"):
		e_abdomen.delete(0, END)
		e_abdomen.config(fg = 'black')

	elif (textoActual == ""):
		e_abdomen.insert(0,"cm")
		e_abdomen.config(fg = 'grey')



def default_cadera(event):

	textoActual = e_cadera.get()

	if (textoActual == "cm"):
		e_cadera.delete(0, END)
		e_cadera.config(fg = 'black')

	elif (textoActual == ""):
		e_cadera.insert(0,"cm")
		e_cadera.config(fg = 'grey')



def default_cuello(event):

	textoActual = e_cuello.get()

	if (textoActual == "cm"):
		e_cuello.delete(0, END)
		e_cuello.config(fg = 'black')

	elif (textoActual == ""):
		e_cuello.insert(0,"cm")
		e_cuello.config(fg = 'grey')



def calcular():

	if (var_sexo.get() == 1):

		imc = float(var_peso.get()) / ((float(var_estatura.get()) / 100) ** 2)
		gc = (0.567 * float(var_cintura.get())) + (0.101 * float(var_edad.get())) - 31.8
		
		try:

			act_fisica = float(var_actFisica.get())
			proteinas = float(var_proteinas.get())
			restriccion = float(var_restriccion.get())

			#

		except (ValueError):

			return var_imc.set(f'{imc:.2f}'), var_grasa.set(f'{gc:.2f}')

			#


		act_fisica = float(var_actFisica.get())
		proteinas = float(var_proteinas.get())
		rct = ((9.99 * float(var_pesoToUse.get())) + (6.25 * float(var_estatura.get())) - (4.92 * float(var_edad.get())) + 5) * act_fisica
		restriccion = float(var_restriccion.get())
		rctToUse = rct + restriccion

		return var_imc.set(f'{imc:.2f}'), var_grasa.set(f'{gc:.2f}'), var_rct.set(f'{rct:.2f}'), var_rctToUse.set(f'{rctToUse:.2f}')

	if (var_sexo.get() == 0):

		imc = float(var_peso.get()) / ((float(var_estatura.get()) / 100) ** 2)
		gc = (0.439 * float(var_cintura.get())) + (0.221 * float(var_edad.get())) - 9.4

		try:

			act_fisica = float(var_actFisica.get())
			proteinas = float(var_proteinas.get())
			restriccion = float(var_restriccion.get())

			#

		except (ValueError):

			return var_imc.set(f'{imc:.2f}'), var_grasa.set(f'{gc:.2f}')

			#

		act_fisica = float(var_actFisica.get())
		proteinas = float(var_proteinas.get())
		rct = ((9.99 * float(var_pesoToUse.get())) + (6.25 * float(var_estatura.get())) - (4.92 * float(var_edad.get())) - 161) * act_fisica
		restriccion = float(var_restriccion.get())
		rctToUse = rct + restriccion

		return var_imc.set(f'{imc:.2f}'), var_grasa.set(f'{gc:.2f}'), var_rct.set(f'{rct:.2f}'), var_rctToUse.set(f'{rctToUse:.2f}')



def salir():

	salir = messagebox.askquestion('Salir','¿Desea salir del programa?')

	if (salir == 'yes'):

		root.destroy()



def default_consulta(event):

	textoActual = e_consulta.get()

	if (textoActual == "N° de Consulta"):
		e_consulta.delete(0, END)
		e_consulta.config(fg = 'black')

	elif (textoActual == ""):
		e_consulta.insert(0,"N° de Consulta")
		e_consulta.config(fg = 'grey')



def default_nombre(event):

	textoActual = e_nombre.get()

	if (textoActual == "Nombre"):
		e_nombre.delete(0, END)
		e_nombre.config(fg = 'black')

	elif (textoActual == ""):
		e_nombre.insert(0,"Nombre")
		e_nombre.config(fg = 'grey')



def default_proteinas(event):

	textoActual = e_proteinas.get()

	if (textoActual == "g"):
		e_proteinas.delete(0, END)
		e_proteinas.config(fg = 'black')

	elif (textoActual == ""):
		e_proteinas.insert(0,"g")
		e_proteinas.config(fg = 'grey')



def save_():

	dicc = {

	'Nombre':var_nombre.get(),
	'N° de Consulta':var_consulta.get(),
	'Edad (años)':var_edad.get(),
	'Estatura (cm)':var_estatura.get(),
	'Peso (kg)':var_peso.get(),
	'Peso a Usar (kg)':var_pesoToUse.get(),
	'C. Cintura (cm)':var_cintura.get(),
	'C. Abdomen (cm)':var_abdomen.get(),
	'C. Cadera (cm)':var_cadera.get(),
	'C. Cuello (cm)':var_cuello.get(),
	'IMC':var_imc.get(),
	f'% Grasa':var_grasa.get(),
	'Act. Física':var_actFisica.get(),
	'Proteinas (g)':var_proteinas.get(),
	'RCT':var_rct.get(),
	'Restricción':var_restriccion.get(),
	'RCT a Usar':var_rctToUse.get()

	}

	serieToSave = pd.Series(dicc)

		

	archivoAguardar = fd.asksaveasfilename(
		title='Guardar consulta numero ' + var_consulta.get() + ' de ' + var_nombre.get() + '.',
		defaultextension='.xlsx',
		filetypes=(('Archivo Excel', '*.xlsx'), ('All Files', '*.*'))
		)

	serieToSave.to_excel(archivoAguardar)



def tabla_actFisica():

	root_tabla = Toplevel()

	root_tabla.config(width=250, height=150)
	root_tabla.resizable(0,0)

	root_tabla.title('Actividad Física')

	dirr_tabla = './resources/tabla de actividad fisica [GIF].gif'
	tabla_img = PhotoImage(file=dirr_tabla)

	label_tabla = Label(root_tabla, image=tabla_img)
	label_tabla.pack()

	root_tabla.mainloop()



def tabla_grasaMen():

	root_tabla = Toplevel()

	root_tabla.config(width=250, height=150)
	root_tabla.resizable(0,0)

	root_tabla.title(f'%Grasa (Hombres)')

	dirr_tabla = './resources/tabla de calificacion grasa hombres [GIF].gif'
	tabla_img = PhotoImage(file=dirr_tabla)

	label_tabla = Label(root_tabla, image=tabla_img)
	label_tabla.pack()

	root_tabla.mainloop()



def tabla_grasaWomen():

	root_tabla = Toplevel()

	root_tabla.config(width=250, height=150)
	root_tabla.resizable(0,0)

	root_tabla.title(f'%Grasa (Mujeres)')

	dirr_tabla = './resources/tabla de calificacion grasa mujeres [GIF].gif'
	tabla_img = PhotoImage(file=dirr_tabla)

	label_tabla = Label(root_tabla, image=tabla_img)
	label_tabla.pack()

	root_tabla.mainloop()



def tabla_macronutrientres():

	root_tabla = Toplevel()

	root_tabla.config(width=250, height=150)
	root_tabla.resizable(0,0)

	root_tabla.title('Macronutrientes')

	dirr_tabla = './resources/tabla macronutrientes [GIF].gif'
	tabla_img = PhotoImage(file=dirr_tabla)

	label_tabla = Label(root_tabla, image=tabla_img)
	label_tabla.pack()

	root_tabla.mainloop()



def informacion():

	url = 'https://farjanrondon.github.io/'
	webbrowser.open(url, new=2, autoraise=True)




root = Tk()
#root.geometry('500x400')
root.title('Nutri.Calc')
root.resizable(0,0)






# Variables a usar:

var_sexo = IntVar()
var_edad = StringVar()
var_estatura = StringVar()
var_peso = StringVar()
var_pesoToUse = StringVar()
var_cintura = StringVar()
var_abdomen = StringVar()
var_cadera = StringVar()
var_cuello = StringVar()
var_nombre = StringVar()
var_consulta = StringVar()


var_imc = StringVar()
var_grasa = StringVar()
var_actFisica = StringVar()
var_proteinas = StringVar()
var_rct = StringVar()
var_restriccion = StringVar()
var_rctToUse = StringVar()

#






frame1 = Frame(root)
# 'frame1' contiene los datos a ingresar y resultados.
frame1.grid(column=0, row=0)


frame_1 = Frame(frame1)
# 'frame_1' contiene solo los datos a ingresar.
frame_1.grid(column=0, row=0)
 
# Labels:
l_edad = Label(frame_1, text='Edad')
l_edad.grid(column=0, row=0, sticky='w')
l_edad.config(font=('Calibri', 15))

l_estatura = Label(frame_1, text='Estatura')
l_estatura.grid(column=0, row=1, sticky='w')
l_estatura.config(font=('Calibri', 15))

l_peso = Label(frame_1, text='Peso')
l_peso.grid(column=0, row=2, sticky='w')
l_peso.config(font=('Calibri', 15))

l_pesoToUse = Label(frame_1, text='Peso a usar')
l_pesoToUse.grid(column=0, row=3, sticky='w')
l_pesoToUse.config(font=('Calibri', 15))

l_cintura = Label(frame_1, text='C. Cintura')
l_cintura.grid(column=0, row=4, sticky='w')
l_cintura.config(font=('Calibri', 15))

l_abdomen = Label(frame_1, text='C. Abdomen')
l_abdomen.grid(column=0, row=5, sticky='w')
l_abdomen.config(font=('Calibri', 15))

l_cadera = Label(frame_1, text='C. Cadera')
l_cadera.grid(column=0, row=6, sticky='w')
l_cadera.config(font=('Calibri', 15))

l_cuello = Label(frame_1, text='C. Cuello')
l_cuello.grid(column=0, row=7, sticky='w')
l_cuello.config(font=('Calibri', 15))
#


# Entradas:
e_edad = Entry(frame_1)
e_edad.grid(column=1, row=0, padx=5)
e_edad.config(justify='right', font=('Calibri', 15), textvariable=var_edad)
e_edad.config(fg='grey')
e_edad.insert(0, 'años')
e_edad.bind("<FocusIn>", default_edad)
e_edad.bind("<FocusOut>", default_edad)

e_estatura = Entry(frame_1)
e_estatura.grid(column=1, row=1, padx=5)
e_estatura.config(justify='right', font=('Calibri', 15), textvariable=var_estatura)
e_estatura.config(fg='grey')
e_estatura.insert(0, 'cm')
e_estatura.bind("<FocusIn>", default_estatura)
e_estatura.bind("<FocusOut>", default_estatura)

e_peso = Entry(frame_1)
e_peso.grid(column=1, row=2, padx=5)
e_peso.config(justify='right', font=('Calibri', 15), textvariable=var_peso)
e_peso.config(fg='grey')
e_peso.insert(0, 'kg')
e_peso.bind("<FocusIn>", default_peso)
e_peso.bind("<FocusOut>", default_peso)

e_pesoToUse = Entry(frame_1)
e_pesoToUse.grid(column=1, row=3, padx=5)
e_pesoToUse.config(justify='right', font=('Calibri', 15), textvariable=var_pesoToUse)
e_pesoToUse.config(fg='grey')
e_pesoToUse.insert(0, 'kg')
e_pesoToUse.bind("<FocusIn>", default_pesoToUse)
e_pesoToUse.bind("<FocusOut>", default_pesoToUse)

e_cintura = Entry(frame_1)
e_cintura.grid(column=1, row=4, padx=5)
e_cintura.config(justify='right', font=('Calibri', 15), textvariable=var_cintura)
e_cintura.config(fg='grey')
e_cintura.insert(0, 'cm')
e_cintura.bind("<FocusIn>", default_cintura)
e_cintura.bind("<FocusOut>", default_cintura)

e_abdomen = Entry(frame_1)
e_abdomen.grid(column=1, row=5, padx=5)
e_abdomen.config(justify='right', font=('Calibri', 15), textvariable=var_abdomen)
e_abdomen.config(fg='grey')
e_abdomen.insert(0, 'cm')
e_abdomen.bind("<FocusIn>", default_abdomen)
e_abdomen.bind("<FocusOut>", default_abdomen)

e_cadera = Entry(frame_1)
e_cadera.grid(column=1, row=6, padx=5)
e_cadera.config(justify='right', font=('Calibri', 15), textvariable=var_cadera)
e_cadera.config(fg='grey')
e_cadera.insert(0, 'cm')
e_cadera.bind("<FocusIn>", default_cadera)
e_cadera.bind("<FocusOut>", default_cadera)

e_cuello = Entry(frame_1)
e_cuello.grid(column=1, row=7, padx=5)
e_cuello.config(justify='right', font=('Calibri', 15), textvariable=var_cuello)
e_cuello.config(fg='grey')
e_cuello.insert(0, 'cm')
e_cuello.bind("<FocusIn>", default_cuello)
e_cuello.bind("<FocusOut>", default_cuello)
#

#
frame_separador_1_2 = Frame(frame1)
frame_separador_1_2.grid(column=1, row=0, padx=15)
frame_separador_1_2.config(height=200, width=1, bg='black')
#

frame_2 = Frame(frame1)
# 'frame_2' contiene los resultados.
frame_2.grid(column=2, row=0)


# Labels:
l_imc = Label(frame_2, text='IMC')
l_imc.grid(column=0, row=0, sticky='e')
l_imc.config(font=('Calibri', 15))

l_grasa = Label(frame_2, text=f'%Grasa')
l_grasa.grid(column=0, row=1, sticky='e')
l_grasa.config(font=('Calibri', 15))

l_actFisica = Label(frame_2, text='Act. Física')
l_actFisica.grid(column=0, row=2, sticky='e')
l_actFisica.config(font=('Calibri', 15))

l_proteinas = Label(frame_2, text='Proteinas (g)')
l_proteinas.grid(column=0, row=3, sticky='e')
l_proteinas.config(font=('Calibri', 15))

l_restriccion = Label(frame_2, text='Restricción')
l_restriccion.grid(column=0, row=4, sticky='e')
l_restriccion.config(font=('Calibri', 15))

l_rct = Label(frame_2, text='RCT')
l_rct.grid(column=0, row=5, sticky='e')
l_rct.config(font=('Calibri', 15))

l_rctToUse = Label(frame_2, text='RCT a usar')
l_rctToUse.grid(column=0, row=6, sticky='e')
l_rctToUse.config(font=('Calibri', 15))
#


# Entradas:
e_imc = Entry(frame_2)
e_imc.grid(column=1, row=0, padx=5)
e_imc.config(font=('Calibri', 15), state='disable', justify='right')

e_grasa = Entry(frame_2)
e_grasa.grid(column=1, row=1, padx=5)
e_grasa.config(font=('Calibri', 15), state='disable', justify='right')

e_actFisica = Entry(frame_2)
e_actFisica.grid(column=1, row=2, padx=5)
e_actFisica.config(font=('Calibri', 15), justify='right', textvariable=var_actFisica)

e_proteinas = Entry(frame_2)
e_proteinas.grid(column=1, row=3, padx=5)
e_proteinas.config(font=('Calibri', 15), justify='right', textvariable=var_proteinas)
e_proteinas.config(fg='grey')
e_proteinas.insert(0, 'g')
e_proteinas.bind("<FocusIn>", default_proteinas)
e_proteinas.bind("<FocusOut>", default_proteinas)

e_restriccion = Entry(frame_2)
e_restriccion.grid(column=1, row=4, padx=5)
e_restriccion.config(font=('Calibri', 15), justify='right', textvariable=var_restriccion)

e_rct = Entry(frame_2)
e_rct.grid(column=1, row=5, padx=5)
e_rct.config(font=('Calibri', 15), state='disable', justify='right')

e_rctToUse = Entry(frame_2)
e_rctToUse.grid(column=1, row=6, padx=5)
e_rctToUse.config(font=('Calibri', 15), state='disable', justify='right')
#



frame2 = Frame(root)
# 'frame2' contiene un separador la seleccion del sexo.
frame2.grid(column=0, row=1)



frame_separador_3_12 = Frame(frame2)
frame_separador_3_12.grid(column=0, row=0, pady=15)
frame_separador_3_12.config(height=1, width=620, bg='black')



frame_3 = Frame(frame2)
# 'frame_3' contiene la opcion para seleccionar el sexo.
frame_3.grid(column=0, row=2)

# Botones:
b_masculino = Radiobutton(frame_3, text='Masculino')
b_masculino.grid(column=0, row=0)
b_masculino.config(variable=var_sexo, value=1)

b_femenino = Radiobutton(frame_3, text='Femenino')
b_femenino.grid(column=0, row=1)
b_femenino.config(variable=var_sexo, value=0)
#


e_imc.config(textvariable=var_imc)
e_grasa.config(textvariable=var_grasa)
#e_actFisica.config(textvariable=var_actFisica)
#e_proteinas.config(textvariable=var_proteinas)
e_rct.config(textvariable=var_rct)
#e_restriccion.config(textvariable=var_restriccion)
e_rctToUse.config(textvariable=var_rctToUse)
#




e_nombre = Entry(frame_3)
e_nombre.grid(column=1, row=0, padx=5)
e_nombre.config(justify='center', font=('Calibri', 10), textvariable=var_nombre)
e_nombre.config(fg='grey')
e_nombre.insert(0, 'Nombre')
e_nombre.bind("<FocusIn>", default_nombre)
e_nombre.bind("<FocusOut>", default_nombre)

e_consulta = Entry(frame_3)
e_consulta.grid(column=1, row=1, padx=5)
e_consulta.config(justify='center', font=('Calibri', 10), textvariable=var_consulta)
e_consulta.config(fg='grey')
e_consulta.insert(0, 'N° de Consulta')
e_consulta.bind("<FocusIn>", default_consulta)
e_consulta.bind("<FocusOut>", default_consulta)



dicc = {

	'Nombre':var_nombre.get(),
	'N° de Consulta':var_consulta.get(),
	'Edad (años)':var_edad.get(),
	'Estatura (cm)':var_estatura.get(),
	'Peso (kg)':var_peso.get(),
	'Peso a Usar (kg)':var_pesoToUse.get(),
	'C. Cintura (cm)':var_cintura.get(),
	'C. Abdomen (cm)':var_abdomen.get(),
	'C. Cadera (cm)':var_cadera.get(),
	'C. Cuello (cm)':var_cuello.get(),
	'IMC':var_imc.get(),
	f'% Grasa':var_grasa.get(),
	'Act. Física':var_actFisica.get(),
	'Proteinas (g)':var_proteinas.get(),
	'RCT':var_rct.get(),
	'Restricción':var_restriccion.get(),
	'RCT a Usar':var_rctToUse.get()

}

serieToSave = pd.Series(dicc)




# Ejecutamos la funcion calcular cada vez que se ingrese o indique un nuevo dato:
b_masculino.config(command=calcular)
b_femenino.config(command=calcular)
#


# MENU:

mMenu = Menu(root)
root.config(menu=mMenu)

menu_archivo = Menu(mMenu)
#menu_editar = Menu(mMenu)
menu_tablas = Menu(mMenu)
menu_ayuda = Menu(mMenu)

mMenu.add_cascade(label='Archivo', menu=menu_archivo)
#mMenu.add_cascade(label='Editar', menu=menu_editar)
mMenu.add_cascade(label='Tablas', menu=menu_tablas)
mMenu.add_cascade(label='Ayuda', menu=menu_ayuda)

menu_archivo.config(tearoff=0)
#menu_editar.config(tearoff=0)
menu_tablas.config(tearoff=0)
menu_ayuda.config(tearoff=0)

menu_archivo.add_command(label='Guardar Datos', command=save_)
menu_archivo.add_command(label='Salir', command=salir)

#menu_editar.add_command(label='Vaciar Entradas')

menu_tablas.add_command(label='Actividad Física (FAO 2004)', command=tabla_actFisica)
menu_tablas.add_separator()
menu_tablas.add_command(label=f'Clasif. % Grasa (Hombre)', command=tabla_grasaMen)
menu_tablas.add_command(label=f'Clasif. % Grasa (Mujer)', command=tabla_grasaWomen)
menu_tablas.add_separator()
menu_tablas.add_command(label='Macronutrientes', command=tabla_macronutrientres)

menu_ayuda.add_command(label='v1.0', state='disable')
menu_ayuda.add_separator()
menu_ayuda.add_command(label='Info', command=informacion)

#


root.mainloop()