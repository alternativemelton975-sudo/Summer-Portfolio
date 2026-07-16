import json
import random
from pathlib import Path
from datetime import datetime


class Character:
    """Represents a hero character with stats and progression."""
    
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
        self.level = 1
        self.experience = 0
        self.stats = {
            "strength": random.randint(5, 20),
            "intelligence": random.randint(5, 20),
            "agility": random.randint(5, 20),
            "endurance": random.randint(5, 20),
        }
        self.created_date = datetime.now().isoformat()
    
    def describe_character(self) -> str:
        return f"{self.name} wields {self.power} with royal confidence."
    
    def get_full_profile(self) -> str:
        """Get detailed character profile."""
        total_stats = sum(self.stats.values())
        profile = f"\n{'='*50}\n"
        profile += f"⚔️  {self.name.upper()}\n"
        profile += f"{'='*50}\n"
        profile += f"Level: {self.level} | Experience: {self.experience}\n"
        profile += f"Primary Power: {self.power}\n"
        profile += f"\nSTATS:\n"
        for stat, value in self.stats.items():
            profile += f"  {stat.title()}: {value}\n"
        profile += f"\nTotal Power: {total_stats}\n"
        profile += f"{'='*50}\n"
        return profile
    
    def gain_experience(self, amount: int):
        """Gain experience and level up."""
        self.experience += amount
        levels_gained = self.experience // 100
        if levels_gained > 0:
            self.level += levels_gained
            self.experience = self.experience % 100
            # Increase stats on level up
            for stat in self.stats:
                self.stats[stat] += random.randint(1, 3)
            return f"🎉 {self.name} leveled up! Now Level {self.level}!"
        return None
    
    def to_dict(self) -> dict:
        """Convert character to dictionary for JSON storage."""
        return {
            "name": self.name,
            "power": self.power,
            "level": self.level,
            "experience": self.experience,
            "stats": self.stats,
            "created_date": self.created_date
        }


def describe_character(name, power):
    """Simple description function for backward compatibility."""
    return f"{name} wields {power} with royal confidence."


def create_team(character_list: list[Character]) -> dict:
    """Create a team of characters."""
    total_power = sum(sum(char.stats.values()) for char in character_list)
    team_level = sum(char.level for char in character_list)
    
    return {
        "members": [char.name for char in character_list],
        "count": len(character_list),
        "total_power": total_power,
        "average_level": team_level / len(character_list),
        "characters": character_list
    }


def display_team(team: dict):
    """Display team information."""
    print(f"\n🏰 TEAM ROSTER 🏰\n{'='*50}")
    print(f"Members: {', '.join(team['members'])}")
    print(f"Team Size: {team['count']}")
    print(f"Total Power: {team['total_power']}")
    print(f"Average Level: {team['average_level']:.1f}")
    print(f"{'='*50}\n")


def save_character(character: Character, filename: str = None):
    """Save character to JSON file."""
    if filename is None:
        filename = f"{character.name.replace(' ', '_')}.json"
    
    with open(filename, 'w') as f:
        json.dump(character.to_dict(), f, indent=2)
    print(f"✅ Character saved to {filename}")


def load_character(filename: str) -> Character:
    """Load character from JSON file."""
    if not Path(filename).exists():
        print(f"❌ File not found: {filename}")
        return None
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    char = Character(data["name"], data["power"])
    char.level = data["level"]
    char.experience = data["experience"]
    char.stats = data["stats"]
    char.created_date = data["created_date"]
    
    return char


def battle_simulation(character1: Character, character2: Character) -> str:
    """Simulate a battle between two characters."""
    char1_power = sum(character1.stats.values()) + (character1.level * 10)
    char2_power = sum(character2.stats.values()) + (character2.level * 10)
    
    winner = character1 if char1_power > char2_power else character2
    experience_gain = 50 + (winner.level * 10)
    winner.gain_experience(experience_gain)
    
    result = f"\n⚔️ BATTLE RESULTS ⚔️\n"
    result += f"{character1.name} ({char1_power} power) vs {character2.name} ({char2_power} power)\n"
    result += f"🏆 Winner: {winner.name}!\n"
    result += f"Experience gained: +{experience_gain}\n"
    if winner.gain_experience(0):  # Check if leveled up
        result += winner.gain_experience(0)
    
    return result


if __name__ == "__main__":
    print("=== KINGMYER CHARACTER BUILDER ===\n")
    print("1. Create new character")
    print("2. View character profile")
    print("3. Battle simulator")
    print("4. Manage team")
    choice = input("\nChoose option (1-4): ").strip() or "1"
    
    if choice == "2":
        hero_name = input("Character name: ").strip() or "KingMyer"
        hero_power = input("Character power: ").strip() or "lightning"
        hero = Character(hero_name, hero_power)
        print(hero.get_full_profile())
    elif choice == "3":
        char1 = Character(input("First character name: ").strip() or "Hero1", "fire")
        char2 = Character(input("Second character name: ").strip() or "Hero2", "ice")
        print(battle_simulation(char1, char2))
    elif choice == "4":
        team = create_team([
            Character("KingMyer", "lightning"),
            Character("Inferno", "fire"),
            Character("Frostbyte", "ice")
        ])
        display_team(team)
    else:
        hero_name = input("Enter a hero name: ").strip() or "KingMyer"
        hero_power = input("Enter a power: ").strip() or "lightning"
        hero = Character(hero_name, hero_power)
        print(hero.get_full_profile())
