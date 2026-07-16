import random
from enum import Enum


class DragonColor(Enum):
    RED = "🔴 Red"
    BLUE = "🔵 Blue"
    GREEN = "💚 Green"
    GOLD = "💛 Gold"
    BLACK = "⚫ Black"
    SILVER = "⚪ Silver"


class DragonSize(Enum):
    SMALL = "Small (30ft)"
    MEDIUM = "Medium (50ft)"
    LARGE = "Large (80ft)"
    COLOSSAL = "Colossal (150ft+)"


def dragon_story(location: str) -> str:
    templates = [
        f"A dragon rises over {location}, bringing wonder and flame.",
        f"The skies darken as an ancient dragon awakens above {location}.",
        f"From the depths emerges a mighty dragon, casting shadow upon {location}.",
        f"Legend speaks of a dragon that dwells near {location}, and today it takes flight.",
    ]
    return random.choice(templates)


def create_dragon_profile(name: str, location: str, color: DragonColor, size: DragonSize) -> dict:
    """Create a complete dragon profile."""
    return {
        "name": name,
        "location": location,
        "color": color.value,
        "size": size.value,
        "power_level": random.randint(1, 100),
        "age": random.randint(50, 5000),
        "special_ability": random.choice([
            "Frost breath", "Fire breath", "Lightning strike", 
            "Mind control", "Time manipulation"
        ])
    }


def display_dragon_profile(dragon: dict):
    """Display dragon profile in a formatted way."""
    print("\n" + "="*50)
    print(f"🐉 {dragon['name'].upper()}")
    print("="*50)
    print(f"Location:        {dragon['location']}")
    print(f"Color:           {dragon['color']}")
    print(f"Size:            {dragon['size']}")
    print(f"Age:             {dragon['age']} years")
    print(f"Power Level:     {dragon['power_level']}/100")
    print(f"Special Ability: {dragon['special_ability']}")
    print("="*50 + "\n")


def dragon_battle_stats(dragon1: dict, dragon2: dict) -> str:
    """Compare two dragons in a hypothetical battle."""
    winner = dragon1 if dragon1['power_level'] > dragon2['power_level'] else dragon2
    loser = dragon2 if winner == dragon1 else dragon1
    
    return f"\n⚔️ BATTLE PREVIEW:\n{winner['name']} (Power: {winner['power_level']}) would likely defeat {loser['name']} (Power: {loser['power_level']})"


def generate_dragon_lore(dragon: dict) -> str:
    """Generate a story about the dragon."""
    abilities_desc = {
        "Frost breath": "freezes anything in its path",
        "Fire breath": "consumes everything with eternal flames",
        "Lightning strike": "commands the very storms themselves",
        "Mind control": "bends the will of those who gaze upon it",
        "Time manipulation": "moves between moments as it pleases"
    }
    
    ability_desc = abilities_desc.get(dragon['special_ability'], "possesses ancient magic")
    
    return f"\n📖 LORE:\n{dragon['name']}, a {dragon['age']}-year-old {dragon['color'].split()[-1].lower()} dragon, dwells near {dragon['location']}. This magnificent creature {ability_desc}. Beware its power!"


if __name__ == "__main__":
    print("=== DRAGONS ON EARTH ===\n")
    location = input("Enter a place: ").strip() or "the mountain"
    
    print("\n1. Simple story")
    print("2. Create dragon profile")
    print("3. Battle two dragons")
    choice = input("\nChoose option (1-3): ").strip() or "1"
    
    if choice == "2":
        dragon_name = input("Dragon name: ").strip() or "Inferno"
        color = random.choice(list(DragonColor))
        size = random.choice(list(DragonSize))
        dragon = create_dragon_profile(dragon_name, location, color, size)
        display_dragon_profile(dragon)
        print(generate_dragon_lore(dragon))
    elif choice == "3":
        dragon1 = create_dragon_profile("Inferno", location, random.choice(list(DragonColor)), random.choice(list(DragonSize)))
        dragon2 = create_dragon_profile("Icewing", location, random.choice(list(DragonColor)), random.choice(list(DragonSize)))
        display_dragon_profile(dragon1)
        display_dragon_profile(dragon2)
        print(dragon_battle_stats(dragon1, dragon2))
    else:
        story = dragon_story(location)
        print(f"\n{story}")
