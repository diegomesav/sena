//alert('funciona')

let pokemons = document.getElementById('pokelist');
let URL = 'https://pokeapi.co/api/v2/pokemon/';
async function fetchPokemons() {
    for (let i = 0; i <= 5; i++) {
        const pokemonId = i + 1;
        try {
            const response = await fetch(URL + pokemonId);
            const data = await response.json();
            console.log(data)
            pokedex(data);
        } catch (error) {
            console.log('Error al traer datos pokemon: ', error);
        }
    }
}
function pokedex(data) {
    const div = document.createElement('div')
    div.classList.add('pokemon')
    div.innerHTML = `
    <p class="pokemon-id-back">#${data.id}</p>
    <div class="pokemon-image">
    <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${data.id}.png">
    </div>
    <p class="pokemon-name">${data}</p>
`;
    pokemons.append(div)
}

fetchPokemons()