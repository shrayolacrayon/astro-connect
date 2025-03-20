bodygraph_data = {
    "centers": {
        "head": {"name": "Head", "color": "#FF5733"},
        "ajna": {"name": "Ajna", "color": "#33FF57"},
        "throat": {"name": "Throat", "color": "#3357FF"},
        "g": {"name": "G", "color": "#FF33A1"},
        "sacral": {"name": "Sacral", "color": "#A133FF"},
        "root": {"name": "Root", "color": "#33FFF5"},
        "spleen": {"name": "Spleen", "color": "#F5FF33"},
        "heart": {"name": "Heart", "color": "#FF3333"},
        "solar": {"name": "Solar Plexus", "color": "#33FF33"}
    },
    "channels": {
        "1-8": {"name": "Inspiration", "centers": ["head", "throat"]},
        "2-14": {"name": "The Beat", "centers": ["g", "sacral"]},
        "3-60": {"name": "Mutation", "centers": ["root", "sacral"]},
        "4-63": {"name": "Logic", "centers": ["head", "ajna"]},
        "5-15": {"name": "Rhythm", "centers": ["g", "throat"]},
        "6-59": {"name": "Reproduction", "centers": ["sacral", "spleen"]},
        "7-31": {"name": "The Alpha", "centers": ["throat", "g"]},
        "9-52": {"name": "Concentration", "centers": ["root", "spleen"]},
        "10-20": {"name": "Awakening", "centers": ["g", "throat"]},
        "11-56": {"name": "Curiosity", "centers": ["ajna", "throat"]},
        "12-22": {"name": "Openness", "centers": ["throat", "solar"]},
        "13-33": {"name": "The Prodigal", "centers": ["g", "throat"]},
        "16-48": {"name": "The Wavelength", "centers": ["throat", "spleen"]},
        "17-62": {"name": "Acceptance", "centers": ["ajna", "throat"]},
        "18-58": {"name": "Judgment", "centers": ["root", "spleen"]},
        "19-49": {"name": "Synthesis", "centers": ["root", "spleen"]},
        "20-34": {"name": "Charisma", "centers": ["throat", "sacral"]},
        "21-45": {"name": "The Money Line", "centers": ["throat", "root"]},
        "23-43": {"name": "Structuring", "centers": ["throat", "ajna"]},
        "24-61": {"name": "Awareness", "centers": ["head", "ajna"]},
        "25-51": {"name": "Initiation", "centers": ["heart", "root"]},
        "26-44": {"name": "Surrender", "centers": ["spleen", "heart"]},
        "27-50": {"name": "Preservation", "centers": ["spleen", "sacral"]},
        "28-38": {"name": "Struggle", "centers": ["root", "spleen"]},
        "29-46": {"name": "Discovery", "centers": ["sacral", "spleen"]},
        "30-41": {"name": "Recognition", "centers": ["root", "spleen"]},
        "32-54": {"name": "Transformation", "centers": ["root", "sacral"]},
        "35-36": {"name": "Transitoriness", "centers": ["spleen", "solar"]},
        "37-40": {"name": "Community", "centers": ["root", "heart"]},
        "39-55": {"name": "Emotion", "centers": ["root", "solar"]},
        "42-53": {"name": "Maturation", "centers": ["root", "sacral"]},
        "47-64": {"name": "Abstraction", "centers": ["head", "ajna"]}
    }
}

# To use this data in Python, you can simply access it like a dictionary.
# For example:
# print(bodygraph_data["centers"]["head"]["name"])  # Output: Head
# print(bodygraph_data["channels"]["1-8"]["name"])  # Output: Inspiration