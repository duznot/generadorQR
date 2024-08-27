# Generador de Códigos QR con Interfaz Gráfica

Este proyecto es un simple generador de códigos QR desarrollado en Python, que permite a los usuarios ingresar texto o un enlace a través de una interfaz gráfica de usuario (GUI) y generar un código QR. El código QR se guarda automáticamente en dos formatos de imagen: `.png` y `.jpg` con fondo blanco.

## Características

- **Interfaz Gráfica Amigable**: Utiliza `tkinter` para proporcionar una GUI simple y fácil de usar.
- **Generación de QR**: Genera códigos QR a partir del texto o enlace que se ingrese.
- **Soporte de Múltiples Formatos**: Guarda el código QR en formato `.png` y `.jpg`.
- **Fondo Blanco**: El archivo `.jpg` se genera con un fondo blanco, ideal para usos donde se requiere este tipo de formato.
- **Fácil de Usar**: Con solo unos pocos clics, puedes generar y guardar tu código QR.

## Requisitos

- Python 3.x
- Librerías:
  - `qrcode`
  - `Pillow` (para manejar las imágenes)

## Instalación

Primero, asegúrate de tener Python instalado en tu máquina. Luego, instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install qrcode[pil] pillow

