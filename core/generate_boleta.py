<<<<<<< HEAD
from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.pdfgen import canvas # type: ignore
=======
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
>>>>>>> 20240184a39f3dd54aaedf7da6908bf5f7d8fab5
import io
from django.http import FileResponse

def generate_boleta_pdf(datos):
    # Crear un archivo PDF en memoria
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar contenido al PDF usando los datos proporcionados
    p.drawString(100, 750, "Boleta de Compra")
    p.drawString(100, 735, "----------------")
    p.drawString(100, 720, f"Nombre: {datos.get('nombre')}")
    p.drawString(100, 705, f"Producto: {datos.get('producto')}")
    p.drawString(100, 690, f"Cantidad: {datos.get('cantidad')}")
    p.drawString(100, 675, f"Precio: {datos.get('precio')}")
    p.drawString(100, 660, f"Total: {datos.get('total')}")

    # Finalizar el PDF
    p.showPage()
    p.save()

    # Mover el buffer al inicio para crear una respuesta de archivo
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='boleta.pdf')
