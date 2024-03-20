from bs4 import BeautifulSoup

import uuid
import requests
import json

class Producto():
    
    @staticmethod
    def scraping_url_ferrolux(url: str ='https://ferrolux.com.ar/productos/todos') -> list:
        
        """Scrapea y guarda enlaces de todos los productos Ferrolux en una lista usando BeautifulSoup."""
        
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Genera una excepción para códigos de estado distintos de 200

        soup = BeautifulSoup(respuesta.content, "html.parser")

        elementos_row = soup.find_all("h4")
        elementos_imagen = elementos_row
        url_productos = []
        for elemento_a in elementos_imagen:
            for elemento in elemento_a:
                link_imagen = elemento["href"]
                if link_imagen:  # Comprueba si existe el atributo href
                    url_productos.append(link_imagen)
                else:
                    print(f"No se encontro nada en el 'href' del                     elemeneto: \n {elemento} ")
        return url_productos

    @staticmethod
    def extrac_attributes(url_producto_ferrolux: str) -> dict:

        # Realizar la petición GET
        response = requests.get(url_producto_ferrolux)

        # Comprobar el código de estado
        if response.status_code == 200:
        #    La petición ha sido exitosa
    
            # Extraer el HTML
            html = response.content
    
            # Crear un objeto BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
    
            # Seleccionar el elemento padre
            ficha = soup.find(id="ficha")
            li_color = soup.find_all(class_= 'list-inline-item')
    
            #Extraer los datos
            
            codigo_producto = ficha.find_all('h1')[0].text
            nombre = ficha.find_all("ul")[0].find_all("li")[0].text
            colores = [li.get("style") for li in li_color]
            estilo = ficha.find("h2").text
            descripcion = ficha.find('p', class_='descripcion').text
            precio = ""
            
            tag_imagenes =soup.find_all('img', class_="sp-thumbnail")
            
            url_imagenes = [url_imagen['data-src'] for url_imagen in tag_imagenes]
            
            data = {
                "codigo_producto": codigo_producto,
                "nombre": nombre,
                "descripcion": descripcion,
                "colores": colores,
                "estilo": estilo,
                #"url_imagen": url_imagen,
                "url_imagenes": url_imagenes,
                "precio": precio,
                "url_producto": url_producto_ferrolux,
                "lista": "iluminacion"
            }
            return data
        else:
            # La petición ha fallado
            print(f"Error: {response.status_code}")
            exit()
    
if __name__ == "__main__":
    urls = Producto.scraping_url_ferrolux()
    print(urls[0])
    data = Producto.extrac_attributes('https://ferrolux.com.ar/ficha/producto/1674')
    print(json.dumps(data, indent=4))
