from pathlib import Path
import json
from datetime import datetime


SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.tiff']


def image_to_caption(path: str, style: str = "simple") -> str:
    """Convert image to caption in different styles."""
    image_path = Path(path)
    if not image_path.exists():
        return "❌ Image file not found."
    
    captions = {
        "simple": f"The image '{image_path.name}' was detected successfully.",
        "poetic": f"A visual masterpiece: {image_path.stem}, captured in {image_path.suffix[1:].upper()}.",
        "technical": f"File: {image_path.name} | Format: {image_path.suffix.upper()} | Path: {image_path.resolve()}",
        "playful": f"📸 Found a {image_path.suffix.upper()} treasure named '{image_path.stem}'!"
    }
    
    return captions.get(style, captions["simple"])


def get_image_details(path: str) -> dict:
    """Get detailed information about an image."""
    image_path = Path(path)
    
    if not image_path.exists():
        return {"error": "File not found"}
    
    if image_path.suffix.lower() not in SUPPORTED_FORMATS:
        return {"error": f"Unsupported format: {image_path.suffix}"}
    
    stats = image_path.stat()
    
    return {
        "filename": image_path.name,
        "format": image_path.suffix[1:].upper(),
        "size_bytes": stats.st_size,
        "size_mb": round(stats.st_size / (1024*1024), 2),
        "created": datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M"),
        "modified": datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M"),
    }


def batch_process_images(directory: str) -> list:
    """Process all images in a directory."""
    dir_path = Path(directory)
    
    if not dir_path.exists() or not dir_path.is_dir():
        return []
    
    images = []
    for ext in SUPPORTED_FORMATS:
        images.extend(dir_path.glob(f"*{ext}"))
        images.extend(dir_path.glob(f"*{ext.upper()}"))
    
    return sorted(list(set(images)))


def generate_image_report(directory: str, output_file: str = "image_report.json") -> str:
    """Generate a report of all images in a directory."""
    images = batch_process_images(directory)
    
    if not images:
        return f"❌ No images found in {directory}"
    
    report = {
        "directory": str(directory),
        "scan_date": datetime.now().isoformat(),
        "total_images": len(images),
        "images": [get_image_details(str(img)) for img in images]
    }
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    return f"✅ Report generated: {output_file} ({len(images)} images found)"


def list_supported_formats() -> str:
    """List all supported image formats."""
    return f"Supported formats: {', '.join([fmt.upper() for fmt in SUPPORTED_FORMATS])}"


if __name__ == "__main__":
    print("=== IMAGE ANALYZER ===\n")
    print("1. Analyze single image")
    print("2. Get detailed info")
    print("3. Batch process directory")
    print("4. Supported formats")
    choice = input("\nChoose option (1-4): ").strip() or "1"
    
    if choice == "2":
        image_path = input("Enter image path: ").strip()
        details = get_image_details(image_path)
        if "error" in details:
            print(f"❌ {details['error']}")
        else:
            print("\n" + "="*40)
            for key, value in details.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("="*40)
    elif choice == "3":
        directory = input("Enter directory path: ").strip() or "."
        print(generate_image_report(directory))
    elif choice == "4":
        print(list_supported_formats())
    else:
        image_path = input("Enter image path: ").strip()
        style = input("Caption style (simple/poetic/technical/playful) [default: simple]: ").strip() or "simple"
        print(f"\n{image_to_caption(image_path, style)}")
