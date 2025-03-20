# Define the gate positions
rave_mandala_gate_positions = {
    1: {"left": 578, "top": 165},
    2: {"left": 198, "top": 602},
    3: {"left": 142, "top": 539},
    4: {"left": 627, "top": 553},
    5: {"left": 627, "top": 552},
    6: {"left": 679, "top": 392},
    7: {"left": 606, "top": 572},
    8: {"left": 244, "top": 637},
    9: {"left": 479, "top": 106},
    10: {"left": 367, "top": 92},
    11: {"left": 395, "top": 92},
    12: {"left": 381, "top": 674},
    13: {"left": 168, "top": 192},
    14: {"left": 532, "top": 130},
    15: {"left": 410, "top": 674},
    16: {"left": 296, "top": 662},
    17: {"left": 101, "top": 433},
    18: {"left": 675, "top": 334},
    19: {"left": 175, "top": 188},
    20: {"left": 270, "top": 649},
    21: {"left": 107, "top": 462},
    22: {"left": 99, "top": 348},
    23: {"left": 219, "top": 622},
    24: {"left": 178, "top": 583},
    25: {"left": 97, "top": 405},
    26: {"left": 424, "top": 95},
    27: {"left": 158, "top": 563},
    28: {"left": 618, "top": 203},
    29: {"left": 640, "top": 527},
    30: {"left": 135, "top": 241},
    31: {"left": 566, "top": 613},
    32: {"left": 648, "top": 253},
    33: {"left": 590, "top": 595},
    34: {"left": 506, "top": 118},
    35: {"left": 324, "top": 668},
    36: {"left": 96, "top": 377},
    37: {"left": 111, "top": 292},
    38: {"left": 311, "top": 103},
    39: {"left": 465, "top": 661},
    40: {"left": 663, "top": 475},
    41: {"left": 209, "top": 155},
    42: {"left": 128, "top": 514},
    43: {"left": 556, "top": 145},
    44: {"left": 601, "top": 183},
    45: {"left": 352, "top": 673},
    46: {"left": 679, "top": 362},
    47: {"left": 677, "top": 420},
    48: {"left": 668, "top": 307},
    49: {"left": 150, "top": 216},
    50: {"left": 631, "top": 231},
    51: {"left": 116, "top": 488},
    52: {"left": 437, "top": 670},
    53: {"left": 492, "top": 653},
    54: {"left": 285, "top": 114},
    55: {"left": 120, "top": 266},
    56: {"left": 543, "top": 630},
    57: {"left": 658, "top": 279},
    58: {"left": 338, "top": 96},
    59: {"left": 653, "top": 502},
    60: {"left": 232, "top": 139},
    61: {"left": 257, "top": 125},
    62: {"left": 518, "top": 643},
    63: {"left": 103, "top": 320},
    64: {"left": 667, "top": 447},
}

# Define planet mappings
planet_mappings = {
    "sun": "Sun",
    "earth": "Earth",
    "north-node": "NorthNode",
    "south-node": "SouthNode",
    "moon": "Moon",
    "mercury": "Mercury",
    "venus": "Venus",
    "mars": "Mars",
    "jupiter": "Jupiter",
    "saturn": "Saturn",
    "uranus": "Uranus",
    "neptune": "Neptune",
    "pluto": "Pluto",
}

# Placeholder for design and personality activations
design_activations = {
    "Sun": {"g": 1},  # Example data
    "NorthNode": {"g": 2},  # Example data
    # Add other planets as needed
}

personality_activations = {
    "Sun": {"g": 1},  # Example data
    "NorthNode": {"g": 2},  # Example data
    # Add other planets as needed
}

# Helper function to get the opposite gate
def opposite_gate(gate):
    # Placeholder logic for opposite gate calculation
    return gate  # Replace with actual logic

# Track gate counts
gate_count = {}

# List of bottom gates
bottom_gates = [25, 17, 21, 51, 42, 3, 27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56, 31, 33, 7, 4, 29, 59, 40, 64, 47, 6]

# Process each planet
for planet in planet_mappings.keys():
    planet_key = planet_mappings[planet]

    # Get design and personality gates
    if planet_key == "Earth":
        design_gate = opposite_gate(design_activations["Sun"]["g"])
        personality_gate = opposite_gate(personality_activations["Sun"]["g"])
    elif planet_key == "SouthNode":
        design_gate = opposite_gate(design_activations["NorthNode"]["g"])
        personality_gate = opposite_gate(personality_activations["NorthNode"]["g"])
    else:
        design_gate = design_activations[planet_key]["g"]
        personality_gate = personality_activations[planet_key]["g"]

    # Calculate offsets
    design_gate_offset = gate_count.get(design_gate, 0) * 28
    personality_gate_offset = gate_count.get(personality_gate, 0) * 28

    # Update gate counts
    gate_count[design_gate] = gate_count.get(design_gate, 0) + 1
    gate_count[personality_gate] = gate_count.get(personality_gate, 0) + 1

    # Adjust offsets for bottom gates
    design_gate_top_offset = -design_gate_offset if design_gate in bottom_gates else design_gate_offset
    personality_gate_top_offset = -personality_gate_offset if personality_gate in bottom_gates else personality_gate_offset

    # Get positions
    design_gate_position = rave_mandala_gate_positions[design_gate]
    personality_gate_position = rave_mandala_gate_positions[personality_gate]

    # Render logic (placeholder)
    print(f"Planet: {planet_key}")
    print(f"Design Gate: {design_gate}, Position: {design_gate_position}, Offset: {design_gate_top_offset}")
    print(f"Personality Gate: {personality_gate}, Position: {personality_gate_position}, Offset: {personality_gate_top_offset}")
    print("-" * 40)