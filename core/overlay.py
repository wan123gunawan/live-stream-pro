import random

def get_overlay_position():
    positions = [
        "10:10",
        "W-w-10:10",
        "10:H-h-10",
        "W-w-10:H-h-10"
    ]
    return random.choice(positions)
