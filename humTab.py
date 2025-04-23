import customtkinter as ctk
import tkinter as tk
from appFunctions import * 

class humTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#283747")
        self.dia_input = ctk.StringVar(value="01")
        self.mes_input = ctk.StringVar(value="01")
        self.year_input = ctk.StringVar(value="2024")
        
        Label7 = ctk.CTkLabel(self, text="Fecha de los datos:", bg_color="#283747", text_color="lightgrey")
        Label7.place(relx=0.3, rely=0.146, anchor=tk.CENTER)

        
        Label5 = ctk.CTkLabel(self, text="Introduces la fecha de los datos que quieres, te saca el indice de humedad del combustible fino muerto", bg_color="#283747", text_color="lightgrey", font=("Arial",17))
        Label5.place(relx=0.5, rely=0.05, anchor=tk.CENTER)


        OpMenDay = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.dia_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
        OpMenDay.place(relx=0.4, rely=0.147, anchor=tk.CENTER)
        OpMenMon = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.mes_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",])
        OpMenMon.place(relx=0.5, rely=0.147, anchor=tk.CENTER)
        OpMenYear = ctk.CTkOptionMenu(self,  bg_color="#5D6D7E", variable=self.year_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["2024", "2025"])
        OpMenYear.place(relx=0.6, rely=0.147, anchor=tk.CENTER)


        
        orient = ctk.CTkOptionMenu(self, values=["S", "N", "E", "O"])
        orient.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        expos = ctk.CTkOptionMenu(self, values=["E0", "E1", "SS"])
        expos.place(relx=0.5, rely=0.55, anchor=tk.CENTER)





        B4 = ctk.CTkButton(self, 
                   command= lambda: fireindex(OpMenYear.get(), OpMenMon.get(), OpMenDay.get(), orient.get(), expos.get()),
                   bg_color="#283747",
                   corner_radius=5,
                   font=("Inter", 13),
                   fg_color="#1C2833",
                   text_color="#D7DBDD",
                   hover_color="#17202A",
                   text="Procesar")
        B4.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
