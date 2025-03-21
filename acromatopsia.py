import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_acromatopsia_filter(image):
    # Convertir la imagen a escala de grises
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Convertir la imagen en un formato BGR para mantener compatibilidad con la visualización
    corrected_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)
    
    return corrected_image

image = cv2.imread('imagenes/fresas.jpeg', cv2.IMREAD_COLOR)

if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

colorblind_result = apply_acromatopsia_filter(image)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cv2.cvtColor(colorblind_result, cv2.COLOR_BGR2RGB)]
titles = ["Imagen Original", "Filtro Acromatopsia"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
exit()
