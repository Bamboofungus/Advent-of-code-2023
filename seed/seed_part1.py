from collections import namedtuple

PlantMap = namedtuple('PlantMap', ['dest_start', 'source_start', 'range'])

def seed(file_path) -> int:
    with open(file_path, 'r') as file:
        seeds, codebook = serialize_seed(file)
    return min(map(lambda s: transform_seed_to_location(s, codebook), seeds))

def transform_seed_to_location(seed, codebook) -> int:
    location = seed
    for code_section in codebook:
        for map in code_section:
            # assume unique mapping here
            if map.source_start <= location and location < map.source_start + map.range:
                location = map.dest_start + location - map.source_start
                break
    return location

def serialize_seed(file):
    raw = file.read()
    split_sections = raw.split("\n\n")
    seeds = map(int, split_sections.pop(0).split(":")[1].strip().split(" "))
    codebook = []
    for section in split_sections:
        section_lines = section.rstrip().split("\n")[1:]
        code_section = []
        for line in section_lines:
            dest_start, source_start, code_range = line.split(" ")
            code_section.append(PlantMap(int(dest_start), int(source_start), int(code_range)))
        codebook.append(code_section)
    assert(len(codebook) == 7)
    return seeds, codebook


if __name__ == "__main__":
    res = seed("seed.txt")
    print(res)