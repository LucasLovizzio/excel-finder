import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation
import pandas as pd

#Data Frame



df = pd.read_csv("data.csv", sep=";", on_bad_lines="skip")



class Buscador_de_codigos(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.code = ttk.IntVar(value=0)
        self.data = []
        self.color = master_window.style.colors
  
        instruction_text = "Ingrese el codigo a buscar: "
        instruction = ttk.Label(self, text=instruction_text, width=50)
        instruction.pack(fill=X, pady=10)
  
        self.create_form_entry("Codigo: ", self.code)
        
        self.create_button_box()
        
        self.table = self.create_table()
  
  
  
    #Create text/numerical inputs   
    def create_form_entry(self,label,variable):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)
        
        form_field_label = ttk.Label(master = form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)
        
        form_input = ttk.Entry(master=form_field_container, textvariable=variable)
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)
        
        add_regex_validation(form_input, r'^[0-9_]*$')
        
        return form_input
    
    
    
    
    #Create buttons
    def create_button_box(self):
        
        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))
        
        cancel_button = ttk.Button(
            master=button_container,
            text="Cancelar",
            command=self.on_cancel,
            style="danger.TButton",
            width=7
            
        )
        cancel_button.pack(side=RIGHT, padx=5)
        
        cancel_button = ttk.Button(
            master=button_container,
            text="Ingresar",
            command=self.on_submit,
            style="success.TButton",
            width=7
        )
        cancel_button.pack(side=RIGHT, padx=5)
        return





    # Action when user clicks submit button
    def on_submit(self):
        """Print the contents to console and return the values."""
        
        codigo = str(self.code.get())
        
        result = df[df['Cód. Artículo'] == codigo]
        
        if type(result['Descripción'].values[0]) == float:
            result['Descripción'].values[0] = "No tiene"
            desc = result['Descripción'].values[0]
        else:
            desc = result['Descripción'].values[0]
        
        if type(result['Desc. Adicional'].values[0]) == float:
            result['Desc. Adicional'].values[0] = "No tiene"
            desc_adicional = result['Desc. Adicional'].values[0]
        else:
            desc_adicional = result['Desc. Adicional'].values[0]
        
        if type(result['Sinónimo'].values[0]) == float:
            result['Sinónimo'].values[0] = "No tiene"
            sinonimo = result['Sinónimo'].values[0]
            
        else:
            sinonimo = result['Sinónimo'].values[0]
        
        precio = result['Precio'].values[0]
        

        ult_modificacion = result['Fecha de última modificación'].values[0]
        
        print("Código:", codigo)
        print("Descripción: ", desc)
        print("Desc. Adicional: ", desc_adicional)
        print("Sinónimo: ", sinonimo)
        print("Precio: ", precio)
        print("Fecha de última modificación: ", ult_modificacion)
        
        self.data.append((codigo, desc, desc_adicional, sinonimo, precio, ult_modificacion))
        self.table.destroy()
        self.table = self.create_table()
        return codigo
    
    
    
    
    
    # Action when users clicks cancel button
    def on_cancel(self):
        self.quit()
    
    def create_table(self):
        coldata = [
            {"text": "Codigo"},
            {"text": "Descripción", "stretch": False},
            {"text": "Desc. Adicional"},
            {"text": "Sinónimo"},
            {"text": "Precio", "stretch": False},
            {"text": "Fecha de última modificación", "stretch": False}
        ]
        print(self.data)

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.color.light, None),
        )

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table





if __name__ == "__main__":
    app = ttk.Window(title="Buscador de codigos",
                     themename="superhero",
                     resizable=(False, False))
    Buscador_de_codigos(app)
    app.mainloop()