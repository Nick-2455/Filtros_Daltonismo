import cv2
import numpy as np
import matplotlib.pyplot as plt

# Se define la funcion para hacer el filtro de protanopia
def apply_protanopia_filter(image):
    # Matriz de transformación para Protanopía
    protanopia_kernel = np.array([
        [0.152, 1.053, -0.205],
        [0.115, 0.786, 0.099],
        [0.000, 0.000, 1.000]
    ])
    
    # Aplicar la transformación

    # Se realizar la multiplicacion Matricial
    protanopia_image = image @ protanopia_kernel.T 
    protanopia_image = np.clip(protanopia_image, 0, 255).astype(np.uint8)
    
    return protanopia_image

# Cargar la imagen
image_path = 'images/image6.jpg.webp'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# En caso de que no exista, dara un error.
if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir BGR a RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
protanopia_result = apply_protanopia_filter(image_rgb)

# Mostrar imágenes usando Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
images = [image_rgb, protanopia_result]
titles = ["Imagen Original", "Filtro Protanopia"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()