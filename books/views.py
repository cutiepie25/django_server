from django.http import HttpResponse

# Create your views here.
def find_all(request):
    libros = [
        "Cien años de soledad",
        "El principito",
        "1984",
        "Don Quijote de la Mancha"
    ]

    lista = "<ul>"

    for libro in libros:
        lista += f"<li>{libro}</li>"

    lista += "</ul>"

    return HttpResponse(f"""
        <h1>Lista de libros</h1>
        {lista}
    """)