materials = [r"\stainless", r"\brass"]

variants = [
    r"\slotted\panhead",
    r"\phillips\panhead",
    r"\pozidrive\panhead",
    r"\slotted\countersunk",
    r"\phillips\countersunk",
    r"\pozidrive\countersunk",
    r"\allen\countersunk",
    r"\allen\socket",
    r"\hexhead",
]

sizes = ["M1.0", "M1.2", "M1.4", "M1.6", "M2.0", "M2.5", "M3", "M4", "M6", "M8"]

lengths = [4, 6, 8, 10, 12, 16, 20, 25, 30]

TOTAL_PER_PAGE = 84
TOTAL_PER_LINE = 4

i = 0
for material in materials:
    for variant in variants:
        for size in sizes:
            for length in lengths:
                i += 1
                size_desc = f"{size} x {length}"
                print("\\screw{" + material + "}{" + variant + "}{" + size_desc + "}")
                print()
        skip_for_col = (TOTAL_PER_LINE - (i % TOTAL_PER_LINE)) % TOTAL_PER_LINE
        if skip_for_col:
            for j in range(skip_for_col):
                print(f"BLANK {i}")
                print()
                i += 1

    skip_for_page = (TOTAL_PER_PAGE - (i % TOTAL_PER_PAGE)) % TOTAL_PER_PAGE
    if skip_for_page:
        for j in range(skip_for_page):
            print(f"BLANK {i}")
            print()
            i += 1
