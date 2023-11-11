
from PIL import Image
import sys
def print_image(image_path):
    try:
        image = Image.open(image_path)

        # Escalar la imagen para que se ajuste a la consola (ajustar según sea necesario)
        new_width = 70
        new_height = int((new_width / float(image.size[0])) * image.size[1])
        resized_image = image.resize((new_width, new_height))

        # Convertir la imagen a escala de grises
        resized_image = resized_image.convert("L")

        # Lista de caracteres para representar diferentes niveles de gris
        chars = "@%#*+=-:. "

        # Imprimir la imagen en la consola
        for i in range(new_height):
            for j in range(new_width):
                pixel_value = resized_image.getpixel((j, i))
                # Normalizar el valor de píxel a un rango entre 0 y 9
                normalized_pixel = int(pixel_value / 25.5)
                # Asegurarse de que el índice esté dentro del rango
                char_index = min(normalized_pixel, len(chars) - 1)
                # Obtener el carácter correspondiente al valor de píxel
                char = chars[char_index]
                sys.stdout.write(char)
            sys.stdout.write('\n')

    except Exception as e:
        print(f"Error: {e}")
# Ruta de la imagen que deseas imprimir
image_path = "foto.jpg"  # Reemplaza con la ruta de tu imagen




        
