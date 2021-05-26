from tkinter import *
import requests

ventana = Tk()
ventana.title("¿Qué tiempo hace?")
ventana.geometry("500x500")
#ventana.configure(bg='#D5F5E3')

#b480e14c2eadb4123bd9e057221f2ee5
#api.openweathermap.org/data/2.5/weather?q={city name}

def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(temp) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "La ciudad está mal escrita, inténtelo de nuevo"

def Clima_json(ciudad):
    try:
        api_key = "b480e14c2eadb4123bd9e057221f2ee5"
        url = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": api_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(url, params= parametros)
        clima = response.json()
        mostrar_respuesta(clima)
    except:
        print("Error")


texto_ciudad = Entry(ventana, font=("Courier", 20, "normal"), justify="center")
texto_ciudad.pack(padx=30, pady=30)
texto_ciudad.focus_set()

obtener_clima = Button(ventana, text="Obtener Tiempo", font=("Courier", 20, "normal"), command= lambda : Clima_json(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=("Courier", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura = Label(font=("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font=("Courier", 20, "normal"))
descripcion.pack(padx=10, pady=10)

ventana.mainloop()

#Fuente: https://www.youtube.com/watch?v=UDA2wTas9QQ
#Fuente: https://home.openweathermap.org