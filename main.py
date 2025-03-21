import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para aplicar el filtro de Deuteranopia (dificultad para distinguir verdes)
def apply_deuteranopia_filter(image):
    matrix = np.array([[0.43, 0.72, -0.15],
                       [0.34, 0.57, 0.09],
                       [-0.02, 0.03, 1.00]])
    return apply_color_filter(image, matrix)

# Función para aplicar el filtro de Protanopia (dificultad para distinguir rojos)
def apply_protanopia_filter(image):
    matrix = np.array([[0.152, 1.053, -0.205],
                       [0.115, 0.786, 0.099],
                       [0.000, 0.000, 1.000]])
    return apply_color_filter(image, matrix)

# Función para aplicar el filtro de Tritanopia (dificultad para distinguir azules)
def apply_tritanopia_filter(image):
    matrix = np.array([[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [-0.395, 0.801, 0.0]])
    return apply_color_filter(image, matrix)

# Función para aplicar el filtro de Acromatopsia (visión en escala de grises)
def apply_acromatopsia_filter(image):
    # Esta matriz convierte todos los colores a tonos grises (sin color)
    matrix = np.array([[0.299, 0.587, 0.114],
                       [0.299, 0.587, 0.114],
                       [0.299, 0.587, 0.114]])
    return apply_color_filter(image, matrix)

# Función genérica para aplicar una matriz de transformación de color
def apply_color_filter(image, matrix):
    # Convertimos de BGR (formato de OpenCV) a RGB (formato visual)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Multiplicación matricial para aplicar el filtro de daltonismo
    filtered = rgb_image @ matrix.T
    # Limitar valores entre 0 y 255, y convertir a formato de imagen
    filtered = np.clip(filtered, 0, 255).astype(np.uint8)
    return filtered

# Ruta de la imagen a cargar
image_path = "images/image6.jpg.webp"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Validación por si no se encuentra o carga mal
if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir la imagen original a RGB para mostrar
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Aplicar todos los filtros a la imagen original
deuteranopia_img = apply_deuteranopia_filter(image)
protanopia_img = apply_protanopia_filter(image)
tritanopia_img = apply_tritanopia_filter(image)
acromatopsia_img = apply_acromatopsia_filter(image)

# Crear una figura con 2 filas y 3 columnas para mostrar las imágenes
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

# Lista de imágenes y títulos correspondientes
images = [original_rgb, deuteranopia_img, protanopia_img, tritanopia_img, acromatopsia_img]
titles = ["Original", "Deuteranopia", "Protanopia", "Tritanopia", "Acromatopsia"]

# Mostrar cada imagen con su respectivo título
for i in range(6):
    if i < len(images):
        axes[i].imshow(images[i])       # Mostrar imagen
        axes[i].set_title(titles[i])    # Asignar título
    else:
        axes[i].axis("off")             # Si no hay imagen, se deja el eje vacío
    axes[i].axis("off")                 # Ocultar los ejes

# Ajustar el diseño para que no se encimen las imágenes o títulos
plt.tight_layout()

# Mostrar el resultado en pantalla
plt.show()
