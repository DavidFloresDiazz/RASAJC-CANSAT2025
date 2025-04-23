import tkinter as tk



from appFunctions import * 

class helpTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#283747")
        Label8 = ctk.CTkLabel(self, text_color="lightgrey", text="En esta pestaña explicaremos con más detalles cada parte de la app",
                      font=("Arial",17))
        Label8.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        Label10 = ctk.CTkLabel(self, text_color="lightgrey", text="""
        Para este programa se necesitará un archivo txt o csv con el siguiente formato:
        Counter, Temperatura (Cº), Presión (KPa), Humedad (%), Iluminence (lm), Latitud (Sistema decimal), Longitud (Sistema Decimal), Altitud (m), Velocidad (m/h)
                               """)
        Label10.place(relx=0.5, rely = 0.15, anchor=tk.CENTER)

        Label11 = ctk.CTkLabel(self, text_color="lightgrey", text="""
        Explicación de los apartados:
                               """, font=("Arial", 17))
        Label11.place(relx=0.5, rely = 0.3, anchor=tk.CENTER)

        Label9 = ctk.CTkLabel(self, text_color="lightgrey", text="""
        Gráficos --> En esta parte tu introduce un archivo txt (o csv) y te va a sacar los datos seleccionados


        Txt a Csv --> Seleccionas como input un arhhivo txt y un directorio de salida, el archivo que te saca 
        se guarda como "<Ruta seleccionada>/Archivo_procesado.csv"


        Humedad del Combustible Fino Muerto --> Aqui primero tendras que poner un archivo csv o txt como input, 
        y basandose en el documente del Ministerio de Medio Ambiente te saca automaticamente el indice de humedad
        del combustible fino muerto
                              """)
        Label9.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        Label10 = ctk.CTkLabel(self, text_color="lightgrey", text="""
        En nuestro repositorio de GitHub encontraras más explicaciones asi como un archivo con datos de prueba.
        Nuestro Repositorio se llama CANSATStratoSense y esta bajo el usuario DavidFloresDiazz
                              """)
        Label10.place(relx=0.5, rely=0.7, anchor=tk.CENTER)