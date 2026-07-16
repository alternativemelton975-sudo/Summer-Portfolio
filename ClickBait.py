import random


def clickbait_headline(topic: str) -> str:
    templates = [
        f"You won't believe what happens when {topic} goes wrong!",
        f"{topic}: Doctors hate this one simple trick!",
        f"This {topic} hack will blow your mind!",
        f"{topic} destroyed in seconds (number 7 will shock you!)",
        f"Celebrities are FURIOUS over this {topic} secret!",
        f"Top 10 {topic} moments that changed everything!",
    ]
    return random.choice(templates)


def generate_multiple_headlines(topic: str, count: int = 5) -> list:
    """Generate multiple random clickbait headlines."""
    return [clickbait_headline(topic) for _ in range(count)]


def rate_clickbait_level(headline: str) -> str:
    """Rate the clickbait intensity."""
    intensity_words = ["destroy", "furious", "shock", "won't believe", "hate", "secret"]
    count = sum(headline.lower().count(word) for word in intensity_words)
    
    if count >= 3:
        return "🔥 MAXIMUM CLICKBAIT"
    elif count >= 2:
        return "⚡ HIGH CLICKBAIT"
    else:
        return "📰 MODERATE CLICKBAIT"


def save_headlines(topic: str, filename: str = "headlines.txt"):
    """Save generated headlines to file."""
    headlines = generate_multiple_headlines(topic, 10)
    with open(filename, 'w') as f:
        f.write(f"Clickbait Headlines for '{topic}':\n")
        f.write("=" * 50 + "\n")
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")
            f.write(f"   {rate_clickbait_level(headline)}\n\n")
    print(f"✅ Headlines saved to {filename}")


if __name__ == "__main__":
    print("=== CLICKBAIT GENERATOR ===\n")
    topic = input("Enter a topic: ").strip() or "the internet"
    
    print("\n1. Single headline")
    print("2. Multiple headlines")
    print("3. Save to file")
    choice = input("\nChoose option (1-3): ").strip() or "1"
    
    if choice == "2":
        count = int(input("How many headlines? (default 5): ").strip() or "5")
        for headline in generate_multiple_headlines(topic, count):
            print(f"• {headline}")
            print(f"  {rate_clickbait_level(headline)}\n")
    elif choice == "3":
        save_headlines(topic)
    else:
        headline = clickbait_headline(topic)
        print(f"\n{headline}")
        print(f"{rate_clickbait_level(headline)}")
