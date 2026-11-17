from coches import cochesBD

from tkinter import Label,Entry,Button,Tk,messagebox,StringVar,Frame


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()

    ##.  ... Vistas de Coches ....
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"\n...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Coche...").pack(pady=10)

        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="# de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Guardar",command=lambda:{self.insertar_controller(),self.insertar_view()}).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del Coche a Eliminar...").pack(pady=10)

        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.btn_buscar=Button(self.ventana,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
        self.btn_buscar.pack(pady=5)

        self.btn_eliminar=Button(self.ventana,text="Eliminar",state="disabled",command=lambda:{self.eliminar_controller(),self.eliminar_view()})
        self.btn_eliminar.pack(pady=5)

        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    # CORRECCION: ahora solo pide el ID y el boton Buscar.
    # Las cajas para los datos nuevos se "abren" abajo cuando el ID existe.
    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del Coche a modificar...").pack(pady=10)

        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.btn_buscar=Button(self.ventana,text="Buscar",command=lambda:self.buscar_controller("modificar"))
        self.btn_buscar.pack(pady=5)

        # NUEVO: espacio vacio donde despues apareceran las cajas de modificar
        self.frame_campos=Frame(self.ventana)
        self.frame_campos.pack(pady=5)

        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    # NUEVO: crea las cajas dentro del Frame, ya llenas con los datos actuales del coche
    def mostrar_campos_modificar(self,coche):
        # Si ya habia cajas, se borran para no repetirlas
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

        # Se bloquea el ID para que no se cambie despues de buscarlo
        self.id.config(state="disabled")
        self.btn_buscar.config(state="disabled")

        # coche = (id, marca, color, modelo, velocidad, potencia, asientos)
        self.var_marca=StringVar(value=coche[1])
        self.var_color=StringVar(value=coche[2])
        self.var_modelo=StringVar(value=coche[3])
        self.var_velocidad=StringVar(value=coche[4])
        self.var_potencia=StringVar(value=coche[5])
        self.var_asientos=StringVar(value=coche[6])

        Label(self.frame_campos,text="Nueva Marca: ").pack(pady=3)
        self.marca=Entry(self.frame_campos,textvariable=self.var_marca)
        self.marca.focus()
        self.marca.pack(pady=3)

        Label(self.frame_campos,text="Nuevo Color: ").pack(pady=3)
        self.color=Entry(self.frame_campos,textvariable=self.var_color)
        self.color.pack(pady=3)

        Label(self.frame_campos,text="Nuevo Modelo: ").pack(pady=3)
        self.modelo=Entry(self.frame_campos,textvariable=self.var_modelo)
        self.modelo.pack(pady=3)

        Label(self.frame_campos,text="Nueva Velocidad: ").pack(pady=3)
        self.velocidad=Entry(self.frame_campos,textvariable=self.var_velocidad)
        self.velocidad.pack(pady=3)

        Label(self.frame_campos,text="Nueva Potencia: ").pack(pady=3)
        self.potencia=Entry(self.frame_campos,textvariable=self.var_potencia)
        self.potencia.pack(pady=3)

        Label(self.frame_campos,text="Nuevo # de Asientos: ").pack(pady=3)
        self.asientos=Entry(self.frame_campos,textvariable=self.var_asientos)
        self.asientos.pack(pady=3)

        Button(self.frame_campos,text="Guardar",command=lambda:{self.modificar_controller(),self.modificar_view()}).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: Consultar los Coches :::").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<15}{'ID':<15}{'Marca':<15} {'Color':<15}{'Modelo':<15}{'Velocidad':<15}{'Potencia':<15}{'# Asientos':<15}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    # CORRECCION: ahora solo se usa para el boton Eliminar
    def cambiar_estado_btn(self,estado,tipo_accion):
        if tipo_accion=="eliminar":
            if estado:
                self.btn_eliminar.config(state="normal")
            else:
                self.btn_eliminar.config(state="disabled")

    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...¡Atencion!...",message=f"...¿Desea {tipo} este registro?...")
        if resp=="yes":
            return True
        else:
            return False

    # ... Contralador de Coches ...
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento!...")

    def insertar_controller(self):
        coche1=cochesBD.cochesBD(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta=cochesBD.cochesBD.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)

    def consultar_controller(self,filas):
        registros=cochesBD.cochesBD.consultar()
        if len(registros)>0:
            num_coches=1
            for fila in registros:
                filas=filas+f"\n{num_coches:<15}{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}"
                num_coches+=1
        else:
            filas="... ¡No existen datos que mostrar por el momento ...!"
        return filas

    def modificar_controller(self):
        id=self.id.get()
        coche1=cochesBD.cochesBD(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1

    # CORRECCION: si es "eliminar" habilita el boton; si es "modificar" abre las cajas
    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=cochesBD.cochesBD.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...¡ Registro Encontrado !...",message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion}!...")
            if tipo_accion=="eliminar":
                self.cambiar_estado_btn(True,tipo_accion)
            elif tipo_accion=="modificar":
                self.mostrar_campos_modificar(coche1[0])
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            if tipo_accion=="eliminar":
                self.cambiar_estado_btn(False,tipo_accion)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    
    



