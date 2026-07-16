from pathlib import Path


def reverse_text(text: str) -> str:
    """Reverse text character by character."""
    return text[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words."""
    return ' '.join(text.split()[::-1])


def reverse_lines(text: str) -> str:
    """Reverse the order of lines."""
    return '\n'.join(text.split('\n')[::-1])


def check_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring spaces and case)."""
    cleaned = text.replace(' ', '').lower()
    return cleaned == cleaned[::-1]


def get_text_statistics(text: str) -> dict:
    """Get statistics about text."""
    words = text.split()
    return {
        "total_characters": len(text),
        "characters_no_spaces": len(text.replace(' ', '')),
        "total_words": len(words),
        "total_lines": len(text.split('\n')),
        "average_word_length": sum(len(w) for w in words) / len(words) if words else 0,
        "unique_words": len(set(word.lower() for word in words))
    }


def get_character_codes(text: str) -> str:
    """Get ASCII/Unicode codes for each character."""
    codes = [f"{char}:{ord(char)}" for char in text]
    return " | ".join(codes)


def reverse_alternating(text: str) -> str:
    """Reverse every other character."""
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char)
        else:
            result.append(char)
    # Reverse odd-indexed characters
    chars = list(text)
    for i in range(1, len(chars), 2):
        chars[i] = chars[i]
    # Actually reverse them
    odd_chars = [chars[i] for i in range(1, len(chars), 2)]
    result = []
    odd_idx = len(odd_chars) - 1
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char)
        else:
            result.append(odd_chars[odd_idx])
            odd_idx -= 1
    return ''.join(result)


def process_file(input_file: str, operation: str = "reverse", output_file: str = None):
    """Process text file with various operations."""
    file_path = Path(input_file)
    
    if not file_path.exists():
        return "❌ File not found"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if operation == "reverse":
        result = reverse_text(content)
    elif operation == "reverse_words":
        result = reverse_words(content)
    elif operation == "reverse_lines":
        result = reverse_lines(content)
    else:
        return "❌ Unknown operation"
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        return f"✅ Processed and saved to {output_file}"
    
    return result


def display_text_analysis(text: str):
    """Display comprehensive text analysis."""
    stats = get_text_statistics(text)
    
    print("\n" + "="*50)
    print("📊 TEXT ANALYSIS")
    print("="*50)
    print(f"Total Characters: {stats['total_characters']}")
    print(f"Characters (no spaces): {stats['characters_no_spaces']}")
    print(f"Total Words: {stats['total_words']}")
    print(f"Total Lines: {stats['total_lines']}")
    print(f"Average Word Length: {stats['average_word_length']:.2f}")
    print(f"Unique Words: {stats['unique_words']}")
    
    if check_palindrome(text):
        print(f"✅ This is a palindrome!")
    else:
        print(f"❌ Not a palindrome")
    
    print("="*50 + "\n")


if __name__ == "__main__":
    print("=== WORLD OF REVERSED SCRIPTS ===\n")
    print("1. Reverse text")
    print("2. Reverse words")
    print("3. Reverse lines")
    print("4. Text analysis")
    print("5. Palindrome check")
    print("6. Show character codes")
    choice = input("\nChoose option (1-6): ").strip() or "1"
    
    if choice == "4":
        sample = input("Enter text to analyze: ").strip()
        display_text_analysis(sample)
    elif choice == "5":
        sample = input("Enter text to check: ").strip()
        is_palindrome = check_palindrome(sample)
        print(f"\nPalindrome: {'✅ YES' if is_palindrome else '❌ NO'}")
    elif choice == "6":
        sample = input("Enter text: ").strip()
        print(f"\nCharacter Codes:\n{get_character_codes(sample)}")
    elif choice == "3":
        sample = input("Enter text: ").strip()
        print(f"\nReversed:\n{reverse_lines(sample)}")
    elif choice == "2":
        sample = input("Enter text: ").strip()
        print(f"\nReversed:\n{reverse_words(sample)}")
    else:
        sample = input("Enter text to reverse: ").strip()
        print(f"\nReversed: {reverse_text(sample)}")
