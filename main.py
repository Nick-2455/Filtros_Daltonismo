import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_colorblind_filter(image):
    colorblind_matrix = np.array([[0.43, 0.72, -0.15],
                                   [0.34, 0.57, 0.09],
                                   [-0.02, 0.03, 1.00]])
    
    corrected_image = cv2.transform(image, colorblind_matrix)
    corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)
    return corrected_image

image = cv2.imread('images/image6.jpg.webp', cv2.IMREAD_COLOR)

if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

colorblind_result = apply_colorblind_filter(image)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cv2.cvtColor(colorblind_result, cv2.COLOR_BGR2RGB)]
titles = ["Imagen Original", "Filtro Deuteranopía"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
exit()
