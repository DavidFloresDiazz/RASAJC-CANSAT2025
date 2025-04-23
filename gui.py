import customtkinter as ctk
from graphTab import graphTab
from humTab import humTab
from plagueTab import plagueTab
from helpTab import helpTab

class AppGUI(ctk.CTk):
    def __init__(self):
      super().__init__()
      self.title("Plag-Alert")
      self.tabview = ctk.CTkTabview(self,
                       fg_color="#283747", 
                       bg_color="#17202A",
                       corner_radius=10, 
                       segmented_button_fg_color="#34495E", 
                       segmented_button_selected_color="#1C2833", 
                       segmented_button_unselected_color="#283747", 
                       segmented_button_unselected_hover_color="#212F3D", 
                       segmented_button_selected_hover_color="#1C2833")
      self.tabview.pack(fill="both", expand=True, padx=0, pady=0)
        # Agregar pestañas
      graphtab = self.tabview.add("Gráficos")

      humtab = self.tabview.add("Humedad del Combustible Fino Muerto")

      plaguetab = self.tabview.add("Imagenes de Plagas")

      helptab = self.tabview.add("Ayuda")
        # Insertar frames en cada pestaña
      
      graphTab(graphtab).pack(fill="both", expand=True)
      humTab(humtab).pack(fill="both", expand=True)
      plagueTab(plaguetab).pack(fill="both", expand=True)
      helpTab(helptab).pack(fill="both", expand=True)
      