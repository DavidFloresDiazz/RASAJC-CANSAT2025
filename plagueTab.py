import customtkinter as ctk
import tkinter as tk
from appFunctions import * 

class plagueTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#283747")
        ruta_output = ctk.StringVar()
        ruta_input = ctk.StringVar()
        self.dia_input = ctk.StringVar(value="01")
        self.mes_input = ctk.StringVar(value="01")
        self.year_input = ctk.StringVar(value="2024")

        def abrirarchivo():
            file = ctk.filedialog.askopenfilename(initialdir="/", title="Seleccione el archivo de entrada")
            ruta_input.set(file) 

        Label1 = ctk.CTkLabel(self, text="Input:", bg_color="#283747", text_color="lightgrey")
        Label1.place(relx=0.38, rely=0.146, anchor=tk.CENTER)

        E3 = ctk.CTkEntry(master=self,textvariable=ruta_input, bg_color="#5D6D7E", width=300, height=16, border_color="black", placeholder_text_color="#34495E", fg_color="#34495E", text_color="lightgrey", corner_radius=0)
        E3.place(relx=0.5, rely=0.146, anchor=tk.CENTER)

        

        B5 = ctk.CTkButton(self, 
                   command=abrirarchivo,
                   bg_color="#283747",
                   corner_radius=5,
                   font=("Inter", 13),
                   fg_color="#1C2833",
                   text_color="#D7DBDD",
                   hover_color="#17202A",
                   text="Abrir Archivo")

        B5.place(relx=0.5, rely=0.22, anchor=tk.CENTER)


        B4 = ctk.CTkButton(self, 
                   command= lambda: calculate_plague_percentage(E3.get(), OpMenYear.get(), OpMenMon.get(), OpMenDay.get()),
                   bg_color="#283747",
                   corner_radius=5,
                   font=("Inter", 13),
                   fg_color="#1C2833",
                   text_color="#D7DBDD",
                   hover_color="#17202A",
                   text="Procesar")
        B4.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


        OpMenDay = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.dia_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
        OpMenDay.place(relx=0.4, rely=0.3, anchor=tk.CENTER)
        OpMenMon = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.mes_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",])
        OpMenMon.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        OpMenYear = ctk.CTkOptionMenu(self,  bg_color="#5D6D7E", variable=self.year_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["2024", "2025"])
        OpMenYear.place(relx=0.6, rely=0.3, anchor=tk.CENTER)


        Label7 = ctk.CTkLabel(self, text="Fecha de los datos:", bg_color="#283747", text_color="lightgrey")
        Label7.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

        Label2 = ctk.CTkLabel(self, text="Plague Tab", bg_color="#283747", text_color="lightgrey", font=("Arial",17))
        Label2.place(relx=0.5, rely=0.05, anchor=tk.CENTER)