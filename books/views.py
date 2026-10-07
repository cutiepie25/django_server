from django.http import HttpResponse

# Create your views here.
def find_all(request):
    libros = [
        "Cien años de soledad",
        "El principito",
        "1984",
        "Don Quijote de la Mancha",
        "El amor en los tiempos del cólera",
        "Crónica de una muerte anunciada",
        "La casa de los espíritus",
        "Pedro Páramo",
        "Rayuela",
        "Ficciones",
        "El Aleph",
        "La sombra del viento",
        "La ciudad y los perros",
        "La fiesta del Chivo",
        "Los detectives salvajes",
        "El túnel",
        "Sobre héroes y tumbas",
        "Maria",
        "La vorágine",
        "Fahrenheit 451",
        "Un mundo feliz",
        "Rebelión en la granja",
        "El Gran Gatsby",
        "Matar a un ruiseñor",
        "Orgullo y prejuicio",
        "Jane Eyre",
        "Cumbres borrascosas",
        "Frankenstein",
        "Drácula",
        "El retrato de Dorian Gray",
        "Moby Dick",
        "Las aventuras de Tom Sawyer",
        "El guardián entre el centeno",
        "Las uvas de la ira",
        "De ratones y hombres",
        "El viejo y el mar",
        "Crimen y castigo",
        "Los hermanos Karamázov",
        "Guerra y paz",
        "Anna Karénina",
        "El maestro y Margarita",
        "Los miserables",
        "El conde de Montecristo",
        "Los tres mosqueteros",
        "Madame Bovary",
        "El extranjero",
        "La peste",
        "La metamorfosis",
        "El proceso",
        "El perfume",
        "El nombre de la rosa",
        "La divina comedia",
        "Ulises",
        "Hamlet",
        "Romeo y Julieta",
        "El hobbit",
        "El señor de los anillos",
        "Harry Potter y la piedra filosofal",
        "Las crónicas de Narnia",
        "Dune",
        "Fundación",
        "Neuromante",
        "Ender el estratega",
        "El código Da Vinci",
        "Ensayo sobre la ceguera",
        "El alquimista",
        "Lazarillo de Tormes",
        "La Celestina",
        "Platero y yo",
        "La casa de Bernarda Alba",
        "Don Juan Tenorio",
        "Veinte poemas de amor y una canción desesperada",
        "El laberinto de la soledad",
        "Las venas abiertas de América Latina",
        "Sapiens: De animales a dioses",
        "Breve historia del tiempo",
    ]

    lista = "<ul>"

    for libro in libros:
        lista += f"<li>{libro}</li>"

    lista += "</ul>"

    return HttpResponse(f"""
        <h1>Lista de libros</h1>
        {lista}
    """)