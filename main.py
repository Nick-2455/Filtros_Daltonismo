import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_convolution(image, kernel):
    """
    Aplica una operación de convolución a una imagen usando un kernel dado.
    :param image: Matriz 2D representando la imagen de entrada.
    :param kernel: Matriz 2D representando el filtro a aplicar.
    :return: Matriz 2D representando la imagen filtrada.
    """
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    result = np.zeros((image_height, image_width))

    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i+kernel_height, j:j+kernel_width]
            result[i, j] = np.sum(region * kernel)

    return result

# Cargar imagen en color
image = cv2.imread('images/image.jpg', cv2.IMREAD_COLOR)

# Verificar que la imagen se cargó correctamente
if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Definir los kernels
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
gaussian_kernel = (1/256) * np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])
high_boost_kernel = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]])

# Aplicar los filtros
laplacian_result = apply_convolution(gray_image, laplacian_kernel)
gaussian_result = apply_convolution(gray_image, gaussian_kernel)
high_boost_result = apply_convolution(gray_image, high_boost_kernel)

# Normalizar resultados
laplacian_result = cv2.normalize(laplacian_result, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
gaussian_result = np.clip(gaussian_result, 0, 255).astype(np.uint8)
high_boost_result = np.clip(high_boost_result, 0, 255).astype(np.uint8)

# Configurar la visualización con Matplotlib
fig, axes = plt.subplots(1, 4, figsize=(12, 4))
images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB), laplacian_result, gaussian_result, high_boost_result]
titles = ["Imagen Original", "Filtro Laplaciano", "Filtro Gaussiano", "Filtro High Boost"]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
exit()
