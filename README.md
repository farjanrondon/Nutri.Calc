# Nutri.Calc v1.0
Nutri.Calc is an assistant for nutritionists, by means of which you can calculate important data for later storage in spreadsheets.
Nutri.Calc es un asistente para nutricionistas, mediante el cual se pueden calcular datos importantes para su posterior almacenamiento en hojas de cálculo.


## Funciones del programa.

La primera versión de Nutri.Calc, tiene como función general ser un ayudante de nutricionistas, el cual posea la capacidad de realizar tareas realmente básicas, principalmente en el cálculo de valores importantes, necesarios y de primera mano para cualquier profesional del área de la nutrición, y además de esto la clara facilidad de realizar esta tarea de la manera más óptima y fácil posible. Siendo más específico tenemos:

1. Calcular Índice de Masa Corporal (IMC).  
2. Calcular Porcentaje de Grasa (%Grasa).  
3. Calcular Requerimiento Calórico Total (RCT).  
4. Calcular Requerimiento Calórico Total a Usar (RCT a usar).  
5. Visualización de tablas:  
	- Actividad Física (FAO 2004).  
	- Calificación del Porcentaje de Grasa de Hombres.  
	- Calificación del Porcentaje de Grasa de Mujeres.  
	- Macronutrientes.  
 
6. Guardar datos de cada paciente con identificación y numero de consulta si se requiere, en una hoja de cálculo (Formato .xlsx, Excel).  


# Formulas usadas para calcular cada dato.

  Formula del Índice de Masa Corporal:
  IMC = p/(e⁄(100))^2   
  IMC = Índice de Masa Corporal.
  p = Peso (kilogramos).
  e = Estatura (centímetros).

  Formula del Porcentaje de Grasa (Mujeres):
  %MGrasa = (0.439*ccint)+(0.221*edad)-9.4
  %MGrasa = Porcentaje de Grada de Mujeres.
  ccint = Circunferencia de Cintura (centímetros).
  edad = Edad (años).

  Formula del Porcentaje de Grasa (Hombres):
  %HGrasa = (0.567*ccint)+(0.101*edad)-31.8
  %HGrasa = Porcentaje de Grada de Hombres.
  ccint = Circunferencia de Cintura (centímetros).
  edad = Edad (años).

  Formula del Requerimiento Calórico Total (Mujeres):
  RCTm = ((9.99*pU) + (6.25*e) - (4.92*edad) - 161) * actFisica
  RCTm = Requerimiento Calórico Total de Mujeres.
  pU = Peso a Usar (kilogramos).
  edad = Edad (años).
  actFisica = Actividad Física.
  e = Estatura (centímetros).

  Formula del Requerimiento Calórico Total (Hombres):
  RCTh = ((9.99*pU) + (6.25*e) - (4.92*edad) + 5) * actFisica
  RCTh = Requerimiento Calórico Total de Hombres.
  pU = Peso a Usar (kilogramos).
  edad = Edad (años).
  actFisica = Actividad Física.
  e = Estatura (centímetros).

  Formula del Requerimiento Calórico Total a Usar:
  RCTaUsar = RCT + restriccion
  RCTaUsar = Requerimiento Calórico Total a Usar.
  RCT = Requerimiento Calórico Total de Hombre o Mujer según sea el caso.
  restriccion = Restricción.


# Método de cálculo y uso del programa.

Para disfrutar al máximo la experiencia y las funciones y utilidades del programa, es importante conocer el funcionamiento de este, entre los datos más importantes destacan inicialmente el IMC y el %Grasa, ya que para conocer estos dos hace falta indicarle al programa los siguientes datos:
	
  1. Edad (años).
	2. Estatura (centímetros).
	3. Peso (kilogramos).
	4. Peso a usar (kilogramos).
	5. Circunferencia de Cintura (centímetros).
	6. Circunferencia de Abdomen (centímetros).
	7. Circunferencia de Cadera (centímetros).
	8. Circunferencia de Cuello (centímetros).

Luego de haber ingresado estos datos, deberá seleccionar el sexo de su paciente, ya con esto se le mostrará en las casillas correspondientes el IMC y el %Grasa de su paciente. 

Posterior a esto, hacer uso de las tablas, las cuales se pueden ubicar fácilmente en el menú superior, para determinar la Calificación del Porcentaje de Grasa del sujeto, además de hacer uso de la tabla de Actividad Física para darle un valor numérico correspondiente a dicha actividad física, también deberá colocarle la respectiva Restricción y Proteínas (en unidad de gramos), al paciente.

Finalmente, para conocer el RCT y el RCT a Usar, deberá dar clic nuevamente al sexo de su paciente, es importante que vea los botones de 'Masculino' y 'Femenino', como el botón de 'Calcular', de manera que con seleccionar el sexo sea motivo suficiente para accionar los cálculos del programa.

Ya para este punto puede dejar esos datos a un lado o muy bien colocar el nombre de su paciente en la casilla 'Nombre' y el número de la consulta en la casilla 'N° de Consulta' y luego dar a 'Archivo' en el menú y luego dar a 'Guardar Datos', donde luego se nos abrirá una ventana en la cual se nos pedirá que indiquemos el sitio de la computadora donde queremos guardar el archivo Excel (formato .xlsx) y con qué nombre queremos guardar dicho archivo. Los datos dentro de dicho archivo se guardarán automáticamente de manera ordenada.
