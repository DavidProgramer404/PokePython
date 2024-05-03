import requests

def obtener_todos_pokemones():
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"  # Hay un total de 1118 Pokémon  Ingresa el total que gustes 
    response = requests.get(url)
    data = response.json()
    pokemones = data['results']
    return pokemones

def obtener_detalle_pokemon(url):
    response = requests.get(url)
    detalle = response.json()
    return detalle

def generar_html():
    pokemones = obtener_todos_pokemones()
    with open("pokemonespy.html", "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>Pokemon</title>\n")
        f.write("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n")
        f.write("<style>")
        f.write(".pokemon-card {background-color: #f8d030; border-radius: 10px; padding: 20px; margin-bottom: 20px;}")
        f.write("</style>")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<div class='container'>\n")
        f.write("<h1 class='text-center mb-4'>Listado de Pokemon</h1>\n")
        f.write("<div class='row'>\n")

        for pokemon in pokemones:
            nombre = pokemon['name'].capitalize()
            detalle = obtener_detalle_pokemon(pokemon['url'])
            imagen = detalle['sprites']['front_default']
            tipo = detalle['types'][0]['type']['name'].capitalize()
            altura = detalle['height']
            peso = detalle['weight']

            f.write("<div class='col-md-3'>\n")
            f.write("<div class='pokemon-card'>\n")
            f.write(f"<h2 class='text-center'>{nombre}</h2>\n")
            f.write(f"<img src='{imagen}' alt='{nombre}' class='mx-auto d-block mb-3'>\n")
            f.write(f"<p><strong>Tipo:</strong> {tipo}</p>\n")
            f.write(f"<p><strong>Altura:</strong> {altura} dm</p>\n")
            f.write(f"<p><strong>Peso:</strong> {peso} hectogramos</p>\n")
            f.write("</div>\n")
            f.write("</div>\n")

        f.write("</div>\n")
        f.write("</div>\n")
        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == "__main__":
    generar_html()
