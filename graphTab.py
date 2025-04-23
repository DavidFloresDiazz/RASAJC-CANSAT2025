import customtkinter as ctk
import tkinter as tk
from appFunctions import graphs

class graphTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.configure(fg_color="#283747")
        self.dia_input = ctk.StringVar(value="01")
        self.mes_input = ctk.StringVar(value="01")
        self.year_input = ctk.StringVar(value="2024")
        self.check_alt = ctk.StringVar(value="on")
        self.check_temp = ctk.StringVar(value="on")
        self.check_hum = ctk.StringVar(value="on")
        self.check_prss = ctk.StringVar(value="on")
        self.check_calcalt = ctk.StringVar(value="on")
        self.check_calccd = ctk.StringVar(value="on")
        self.check_v = ctk.StringVar(value="on")
        self.check_dv = ctk.StringVar(value="on")
        self.check_dh = ctk.StringVar(value="on")
        self.check_dcd = ctk.StringVar(value="on")
        
        OpMenDay = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.dia_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
        OpMenDay.place(relx=0.4, rely=0.147, anchor=tk.CENTER)
        OpMenMon = ctk.CTkOptionMenu(self, bg_color="#5D6D7E", variable=self.mes_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",])
        OpMenMon.place(relx=0.5, rely=0.147, anchor=tk.CENTER)
        OpMenYear = ctk.CTkOptionMenu(self,  bg_color="#5D6D7E", variable=self.year_input, width=50, height=16, fg_color="#34495E", text_color="lightgrey", corner_radius=0, values=["2024", "2025"])
        OpMenYear.place(relx=0.6, rely=0.147, anchor=tk.CENTER)
        

        Label1 = ctk.CTkLabel(self, text="Fecha de los datos:", bg_color="#283747", text_color="lightgrey")
        Label1.place(relx=0.3, rely=0.146, anchor=tk.CENTER)
        Label2 = ctk.CTkLabel(self, text="Introduces la fecha de los datos que quieres y devuelve unas gráficas con las datos seleccionados", bg_color="#283747", text_color="lightgrey", font=("Arial",17))
        Label2.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        
        checkbox_alt = ctk.CTkCheckBox(self, text="Altitude", variable=self.check_alt, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_alt.place(relx=0.34,rely=0.4)
        checkbox_temp = ctk.CTkCheckBox(self, text="Temperature", variable=self.check_temp, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_temp.place(relx=0.54,rely=0.4)
        checkbox_hum = ctk.CTkCheckBox(self, text="Humidity", variable=self.check_hum, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_hum.place(relx=0.44,rely=0.4)
        checkbox_prss = ctk.CTkCheckBox(self, text="Pressure", variable=self.check_prss, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_prss.place(relx=0.54,rely=0.5)
        checkbox_calcalt = ctk.CTkCheckBox(self, text="Calc. Height", variable=self.check_calcalt, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_calcalt.place(relx=0.44,rely=0.5)
        checkbox_calccd = ctk.CTkCheckBox(self, text="Calc. Cd", variable=self.check_calccd, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_calccd.place(relx=0.34,rely=0.5)
        checkbox_v = ctk.CTkCheckBox(self, text="Speed", variable=self.check_v, onvalue="on", offvalue="off", text_color="lightgrey")
        checkbox_v.place(relx=0.34,rely=0.6)

        B2 = ctk.CTkButton(self, 
                   command=lambda: graphs(OpMenYear.get(), OpMenMon.get(), OpMenDay.get(), checkbox_temp.get(), checkbox_alt.get(), checkbox_prss.get(), checkbox_hum.get(), checkbox_calcalt.get(), checkbox_calccd.get(), checkbox_v.get()),
                   bg_color="#283747",
                   corner_radius=5,
                   font=("Inter", 13),
                   fg_color="#1C2833",
                   text_color="#D7DBDD",
                   hover_color="#17202A",
                   text="Procesar")
        B2.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

