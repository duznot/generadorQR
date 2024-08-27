import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk, ImageDraw

# Función para generar el QR
def generar_qr():
    texto = entry.get()
    if texto.strip() == "":
        messagebox.showerror("Error", "Por favor ingresa texto o enlace.")
        return
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)
    
    # Crear la imagen QR
    img_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar el QR como .png
    img_qr.save("codigo_qr.png")
    
    # Crear una imagen .jpg con fondo blanco
    img_qr_rgb = Image.new("RGB", img_qr.size, "white")
    img_qr_rgb.paste(img_qr, (0, 0))
    img_qr_rgb.save("codigo_qr.jpg")
    
    # Mostrar confirmación
    messagebox.showinfo("Éxito", "QR generado y guardado como codigo_qr.png y codigo_qr.jpg")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de QR")

# Crear el cuadro de entrada de texto
label = tk.Label(ventana, text="Ingresa texto o enlace:")
label.pack(padx=10, pady=5)

entry = tk.Entry(ventana, width=50)
entry.pack(padx=10, pady=5)

# Crear el botón para generar el QR
boton = tk.Button(ventana, text="Generar QR", command=generar_qr)
boton.pack(padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
