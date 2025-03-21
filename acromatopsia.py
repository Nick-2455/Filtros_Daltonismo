import cv2
import numpy as np
import matplotlib.pyplot as plt

#matríz para que el filtro funcione
def apply_acromatopsia_filter(imagen):
    #en mi caso, necesito convertir a escala de grises, porque el daltonismo que manejo, es el de la gente que literalmente no ve colores
    kernel = np.array([[0.299, 0.587, 0.114],
                        [0.299, 0.587, 0.114],
                        [0.299, 0.587, 0.114]])
    
    imagen_filtro = cv2.transform(imagen, kernel) #transforma usando la matríz
    imagen_filtro = np.clip(imagen_filtro, 0, 255).astype(np.uint8) #aseguro que el rango esté de 0 a 255 y convierte a uint8
    return imagen_filtro

#declaro imagen, para usar una imagen diferente, se tiene que cambiar a "carpeta/imagen.tipo"
imagen = cv2.imread("imagenes/fresas.jpeg", cv2.IMREAD_COLOR)

#mensaje de error por si no se detecta imagen
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

#aplica el filtro de escala de grises
colorblind_result = apply_acromatopsia_filter(imagen)


fig, axes = plt.subplots(1, 2, figsize=(10, 4)) #crea la figura con las 2 imágenes para su comparación
imagenes = [cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB), cv2.cvtColor(colorblind_result, cv2.COLOR_BGR2RGB)] #convierte BGR a RGB
titles = ["imagen Original", "Filtro Acromatopsia"] #títulos de las imágenes

#muestra las imagenes en el mismo gráfico
for ax, img, title in zip(axes, imagenes, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off") #oculta los ejes

plt.tight_layout() #ajusta el diseño
plt.show() #muestra la figura con las 2 imágenes
exit() #finaliza la ejecución del código
