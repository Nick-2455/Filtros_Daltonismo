import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_deuteranopia_filter(image):
    matrix = np.array([[0.43, 0.72, -0.15],
                       [0.34, 0.57, 0.09],
                       [-0.02, 0.03, 1.00]])
    return apply_color_filter(image, matrix)

def apply_tritanopia_filter(image):
    matrix = np.array([[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [-0.395, 0.801, 0.0]])
    return apply_color_filter(image, matrix)

def apply_protanopia_filter(image):
    matrix = np.array([[0.152, 1.053, -0.205],
                       [0.115, 0.786, 0.099],
                       [0.000, 0.000, 1.000]])
    return apply_color_filter(image, matrix)

def apply_color_filter(image, matrix):
    # Convertir de BGR a RGB antes de aplicar el filtro
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Aplicar transformación
    filtered = rgb_image @ matrix.T
    filtered = np.clip(filtered, 0, 255).astype(np.uint8)
    return filtered

# Ruta de la imagen

# image_path = 'images/paisaje.jpg'
image_path = 'images/image6.jpg.webp'

# Cargar la imagen
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar los tres filtros
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
deuteranopia_result = apply_deuteranopia_filter(image)
protanopia_result = apply_protanopia_filter(image)
tritanopia_result = apply_tritanopia_filter(image)

# Mostrar las imágenes
fig, axes = plt.subplots(1, 4, figsize=(18, 5))
images = [original_rgb, deuteranopia_result, protanopia_result, tritanopia_result]
titles = ["Original", "Deuteranopia", "Protanopia", "Tritanopia"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
