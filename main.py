import cv2
import numpy as np

def apply_convolution(image, kernel):
    """
    Aplica una operación de convolución a una imagen usando un kernel dado.
    :param image: Matriz 2D representando la imagen de entrada.
    :param kernel: Matriz 2D representando el filtro a aplicar.
    :return: Matriz 2D representando la imagen filtrada.
    """
    # Obtiene las dimensiones de la imagen y el kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # Calcula los márgenes para el padding
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    
    # Aplica padding a la imagen para mantener el tamaño original
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    
    # Inicializa la matriz resultante
    result = np.zeros((image_height, image_width))
    
    # Itera sobre la imagen aplicando la convolución
    for i in range(image_height):
        for j in range(image_width):
            # Extrae la región de interés de la imagen
            region = padded_image[i:i+kernel_height, j:j+kernel_width]
            
            # Aplica la multiplicación elemento a elemento y suma los valores
            result[i, j] = np.sum(region * kernel)
    
    return result

# Cargar la imagen en color
image = cv2.imread('images/image.jpg', cv2.IMREAD_COLOR)

# Verificar que la imagen se haya cargado correctamente
if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir a float32 para precisión en cálculos
image = image.astype(np.float32)

# Convertir la imagen a escala de grises para aplicar convolución
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Definir los kernels
laplacian_kernel = np.array([[0, -1, 0],
                              [-1, 4, -1],
                              [0, -1, 0]])

gaussian_kernel = (1/16) * np.array([[1, 2, 1],
                                     [2, 4, 2],
                                     [1, 2, 1]])

high_boost_kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])

# Aplicar los filtros
laplacian_result = apply_convolution(gray_image, laplacian_kernel)
gaussian_result = apply_convolution(gray_image, gaussian_kernel)
high_boost_result = apply_convolution(gray_image, high_boost_kernel)

# Normalizar las imágenes resultantes para visualizarlas correctamente
laplacian_result = np.clip(laplacian_result, 0, 255).astype(np.uint8)
gaussian_result = np.clip(gaussian_result, 0, 255).astype(np.uint8)
high_boost_result = np.clip(high_boost_result, 0, 255).astype(np.uint8)

# Mostrar la imagen original y las filtradas
cv2.imshow('Imagen Original', image.astype(np.uint8))
cv2.imshow('Filtro Laplaciano (Bordes)', laplacian_result)
cv2.imshow('Filtro Gaussiano (Suavizado)', gaussian_result)
cv2.imshow('Filtro High Boost (Realce)', high_boost_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
