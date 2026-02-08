# EduCreator AI - Slide Generator (offline version)
# Author: Hojiakbar Akramov

def generate_slides(topic: str, level: str = "beginner", slides: int = 6):
    topic = topic.strip()
    if not topic:
        return []

    # Simple "AI-like" templates by level
    level_guidance = {
        "beginner": "Use simple language and basic examples.",
        "intermediate": "Include key concepts, examples, and small comparisons.",
        "advanced": "Include deeper details, trade-offs, and technical terms."
    }
    guidance = level_guidance.get(level.lower(), level_guidance["beginner"])

    # Basic slide structure
    outline = [
        ("Title", [f"{topic}", f"Level: {level.title()}", "Prepared with EduCreator AI"]),
        ("What is it?", [f"Definition of {topic}", "Why it matters", "Where it is used"]),
        ("Key Concepts", ["Main components", "Important terms", "How it works (high-level)"]),
        ("Examples", ["Real-life example 1", "Real-life example 2", "Simple demo idea"]),
        ("Benefits & Challenges", ["Main benefits", "Common challenges", "How to improve results"]),
        ("Summary", ["Key takeaways", "Quick recap", "Next steps to learn more"]),
    ]

    # Adjust number of slides (min 3, max 10)
    slides = max(3, min(10, slides))
    outline = outline[:slides]

    # Add guidance note into speaker notes style
    result = []
    for i, (title, bullets) in enumerate(outline, start=1):
        result.append({
            "slide": i,
            "title": title if title != "Title" else topic,
            "bullets": bullets,
            "notes": guidance
        })
    return result


def print_slides(slides_data):
    print("\n=== EduCreator AI: Slide Outline ===\n")
    for s in slides_data:
        print(f"Slide {s['slide']}: {s['title']}")
        for b in s["bullets"]:
            print(f" - {b}")
        print(f"Notes: {s['notes']}\n")


if __name__ == "__main__":
    print("EduCreator AI - Slide Generator")
    topic = input("Enter topic: ").strip()
    level = input("Level (beginner/intermediate/advanced): ").strip() or "beginner"

    try:
        num_slides = int(input("Number of slides (3-10): ").strip() or "6")
    except ValueError:
        num_slides = 6

    slides_data = generate_slides(topic, level, num_slides)
    if not slides_data:
        print("Please enter a valid topic.")
    else:
        print_slides(slides_data)
