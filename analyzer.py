import random

def get_prediction():
    colors = ['🟢 GREEN', '🔴 RED', '⚫ VIOLET']
    prediction = random.choice(colors)
    confidence = random.randint(70, 95)  # Later replace with logic
    return {
        "color": prediction,
        "confidence": confidence
    }
