import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_deuteranopia_filter(image):
    matrix = np.array([[0.43, 0.72, -0.15],
                       [0.34, 0.57, 0.09],
                       [-0.02, 0.03, 1.00]])
    return apply_color_filter(image, matrix)

def apply_protanopia_filter(image):
    matrix = np.array([[0.152, 1.053, -0.205],
                       [0.115, 0.786, 0.099],
                       [0.000, 0.000, 1.000]])
    return apply_color_filter(image, matrix)

def apply_tritanopia_filter(image):
    matrix = np.array([[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [-0.395, 0.801, 0.0]])
    return apply_color_filter(image, matrix)

def apply_acromatopsia_filter(image):
    # Convierte a escala de grises imitando la ausencia total de percepción de color
    matrix = np.array([[0.299, 0.587, 0.114],
                       [0.299, 0.587, 0.114],
                       [0.299, 0.587, 0.114]])
    return apply_color_filter(image, matrix)

def apply_color_filter(image, matrix):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = rgb_image @ matrix.T
    filtered = np.clip(filtered, 0, 255).astype(np.uint8)
    return filtered

# Cargar imagen

# image_path = 'images/paisaje.jpg'
image_path = 'images/image6.jpg.webp'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar todos los filtros
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
deuteranopia_img = apply_deuteranopia_filter(image)
protanopia_img = apply_protanopia_filter(image)
tritanopia_img = apply_tritanopia_filter(image)
acromatopsia_img = apply_acromatopsia_filter(image)

# Mostrar las imágenes
fig, axes = plt.subplots(1, 5, figsize=(22, 5))
images = [original_rgb, deuteranopia_img, protanopia_img, tritanopia_img, acromatopsia_img]
titles = ["Original", "Deuteranopia", "Protanopia", "Tritanopia", "Acromatopsia"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
