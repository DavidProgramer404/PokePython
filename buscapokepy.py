import requests

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        return pokemon
    else:
        return None

def generar_html():
    with open("pokemonesBusca.html", "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>Buscar Pokemon</title>\n")
        f.write("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n")
        f.write("<style>")
        f.write(".pokemon-card {background-color: #f8d030; border-radius: 10px; padding: 20px; margin-bottom: 20px;}")
        f.write("</style>")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<div class='container'>\n")
        f.write("<h1 class='text-center mb-4'>Buscar Pokemon</h1>\n")
        f.write("<div class='input-group mb-3'>\n")
        f.write("<input type='text' class='form-control' placeholder='Ingrese el nombre del Pokemon' id='inputPokemon'>\n")
        f.write("<div class='input-group-append'>\n")
        f.write("<button class='btn btn-primary' type='button' onclick='buscarPokemon()'>Buscar tu Pokemon</button>\n")
        f.write("</div>\n")
        f.write("</div>\n")
        f.write("<div id='pokemonInfo'></div>\n")
        f.write("</div>\n")
        f.write("<script>")
        f.write("function buscarPokemon() {")
        f.write("var nombrePokemon = document.getElementById('inputPokemon').value;")
        f.write("fetch(`https://pokeapi.co/api/v2/pokemon/${nombrePokemon.toLowerCase()}`)")
        f.write(".then(response => response.json())")
        f.write(".then(data => {")
        f.write("if (data.detail) {")
        f.write("document.getElementById('pokemonInfo').innerHTML = '<p>Pokémon no encontrado.</p>';")
        f.write("} else {")
        f.write("var pokemonHTML = '<div class=\"pokemon-card\">';")
        f.write("pokemonHTML += `<h2 class='text-center'>${data.name.toUpperCase()}</h2>`;")
        f.write("pokemonHTML += `<img src='${data.sprites.front_default}' alt='${data.name}' class='mx-auto d-block mb-3'>`;")
        f.write("pokemonHTML += `<p><strong>Tipo:</strong> ${data.types[0].type.name.toUpperCase()}</p>`;")
        f.write("pokemonHTML += `<p><strong>Altura:</strong> ${data.height} dm</p>`;")
        f.write("pokemonHTML += `<p><strong>Peso:</strong> ${data.weight} hectogramos</p>`;")
        f.write("pokemonHTML += '</div>';")
        f.write("document.getElementById('pokemonInfo').innerHTML = pokemonHTML;")
        f.write("}")
        f.write("})")
        f.write(".catch(error => {")
        f.write("console.error('Error:', error);")
        f.write("});")
        f.write("}")
        f.write("</script>")
        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == "__main__":
    generar_html()
