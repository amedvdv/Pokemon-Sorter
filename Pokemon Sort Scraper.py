import requests
import json

# Function to get Pokémon data
def get_pokemon_data():
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    species_url = "https://pokeapi.co/api/v2/pokemon-species/"
    
    pokemon_list = []
    
    for i in range(1, 1025):  # Adjust for latest Pokémon count
        print(f"Fetching data for Pokémon #{i}...")
        
        # Get basic Pokémon info
        response = requests.get(f"{base_url}{i}")
        if response.status_code != 200:
            print(f"Skipping {i}, data not found.")
            continue
        
        data = response.json()
        name = data["name"].capitalize()
        types = [t["type"]["name"].capitalize() for t in data["types"]]
        hp = next((stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp"), 0)
        
        # Get weaknesses (by checking type effectiveness)
        type_data = [requests.get(t["type"]["url"]).json() for t in data["types"]]
        weaknesses = list(set(
            w["name"].capitalize() for t in type_data for w in t["damage_relations"]["double_damage_from"]
        ))

        # Get moves with damage
        moves = {}
        for move in data["moves"][:4]:  # Limit to first 4 moves for readability
            move_data = requests.get(move["move"]["url"]).json()
            power = move_data.get("power", "N/A")  # Some moves don't have power
            moves[move["move"]["name"].capitalize()] = power
        
        # Get Evolution data
        evo_response = requests.get(f"{species_url}{i}")
        if evo_response.status_code == 200:
            evo_data = evo_response.json()
            evo_chain_url = evo_data["evolution_chain"]["url"]
            evo_chain_response = requests.get(evo_chain_url).json()
            
            # Extract evolution chain
            def get_evo_chain(chain):
                evo_chain = []
                while chain:
                    evo_chain.append(chain["species"]["name"].capitalize())
                    chain = chain["evolves_to"][0] if chain["evolves_to"] else None
                return evo_chain

            evolutions = " → ".join(get_evo_chain(evo_chain_response["chain"]))
        else:
            evolutions = "No evolution"

        # Save Pokémon data
        pokemon_list.append({
            "name": name,
            "type": types,
            "weaknesses": weaknesses,
            "hp": hp,
            "moves": moves,
            "evolutions": evolutions
        })

    return pokemon_list

# Generate and save JSON file
pokemon_data = get_pokemon_data()

with open("pokemon_data.json", "w", encoding="utf-8") as f:
    json.dump({"pokemon": pokemon_data}, f, indent=4)

print("✅ Pokémon data successfully saved to 'pokemon_data.json'!")
