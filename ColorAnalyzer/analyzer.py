from PIL import image
from collections import Counter

def analyze_colors(image_path, resize_to=100):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((resize_to, resize_to))
    
    pixels = list(img.getdata())
    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in pixels]
    
    total_pixels = len(hex_colors)
    color_counts = Counter(hex_colors)
    
    percentages = [
        {"hex": color, "percent": round((count / total_pixels) * 100, 2)}
        for color, count in color_counts.most_common()
    ]
    return percentages