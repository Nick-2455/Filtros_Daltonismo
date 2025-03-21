import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_deuteranopia_filter(image):
    deuteranopia_matrix = np.array([[0.43, 0.72, -0.15],
                                    [0.34, 0.57, 0.09],
                                    [-0.02, 0.03, 1.00]])
    
    corrected_image = cv2.transform(image, deuteranopia_matrix)
    corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)
    return corrected_image

def apply_tritanopia_filter(image):
    tritanopia_matrix = np.array([[1.0, 0.0, 0.0],
                                  [0.0, 1.0, 0.0],
                                  [-0.395, 0.801, 0.0]])  

    corrected_image = cv2.transform(image, tritanopia_matrix)
    corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)
    return corrected_image

# Cargar imagen
image = cv2.imread("images/paisaje.jpg", cv2.IMREAD_COLOR)

if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar filtros
deuteranopia_result = apply_deuteranopia_filter(image)
tritanopia_result = apply_tritanopia_filter(image)

# Mostrar imágenes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

images = [
    cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(deuteranopia_result, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(tritanopia_result, cv2.COLOR_BGR2RGB)
]

titles = ["Imagen Original", "Filtro Deuteranopia", "Filtro Tritanopia"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
