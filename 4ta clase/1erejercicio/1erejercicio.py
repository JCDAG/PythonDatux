import requests
import sqlite3

def guardar_db(valores):
    conn = sqlite3.connect('tipo_cambio.db')
    co = conn.cursor()
    data = "INSERT INTO sunat (moneda, origen, venta, compra) VALUES (?, ?, ?, ?)"
    co.execute(data, (valores['moneda'], valores['origen'], valores['venta'], valores['compra']))
    conn.commit()
    conn.close()

def sunat():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    respuesta = requests.get(url)
    return respuesta.json()

valores = sunat()

guardar_db(valores)