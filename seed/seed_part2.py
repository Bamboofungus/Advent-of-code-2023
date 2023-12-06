from collections import namedtuple

PlantMap = namedtuple('PlantMap', ['dest_start', 'source_start', 'range'])
SeedRange = namedtuple('SeedRange', ['start', 'end'])

def seed(file_path) -> int:
    with open(file_path, 'r') as file:
        seeds, codebook = serialize_seed(file)

    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append(SeedRange(seeds[i], seeds[i] + seeds[i+1]))
    print(seed_ranges)
    return min(map(lambda s: transform_seed_to_location(s, codebook), seed_ranges))

def transform_seed_to_location(initial_range, codebook) -> int:
    def compute_encoded_seeds(codemap, intersect):
        return codemap.dest_start + intersect - codemap.source_start
    seed_ranges = [initial_range]
    i = 0
    for code_section in codebook:
        temp = []
        for seed_range in seed_ranges:
            seed_range_updated = False
            for codemap in code_section:
                map_end = codemap.source_start + codemap.range
                intersect = [
                    max(seed_range.start, codemap.source_start), 
                    min(seed_range.end, map_end)
                ]
                # check intersect found is valid
                if intersect[0] > intersect[1]:
                    continue
                seed_range_updated = True
                # Intersect within seed range
                if seed_range.start < intersect[0] and seed_range.end > intersect[1]: 
                    entire_range = [min(codemap.source_start, seed_range.start), max(map_end, seed_range.end)]
                    input_ranges = [                        
                        SeedRange(entire_range[0], intersect[0]),
                        SeedRange(compute_encoded_seeds(codemap, intersect[0]), compute_encoded_seeds(codemap, intersect[1])),
                        SeedRange(intersect[1], entire_range[1]),
                    ]
                    temp.extend(input_ranges)
                    break
                # Seed range contained in map
                elif intersect[0] == seed_range.start and intersect[1] == seed_range.end:
                    temp.append(
                        SeedRange(compute_encoded_seeds(codemap, intersect[0]), compute_encoded_seeds(codemap, intersect[1]))
                    )
                    break
                # Seed range bisected
                elif intersect[0] > seed_range.start:
                    temp.extend([
                        SeedRange(seed_range.start, intersect[0]), 
                        SeedRange(compute_encoded_seeds(codemap, intersect[0]), compute_encoded_seeds(codemap, seed_range.end))
                    ])
                    break
                elif intersect[1] < seed_range.end:
                    temp.extend([
                        SeedRange(compute_encoded_seeds(codemap, intersect[1]), compute_encoded_seeds(codemap, seed_range.start)), 
                        SeedRange(seed_range.start, intersect[1])
                    ])
                    break

            if not seed_range_updated:
                temp.append(seed_range)
        seed_ranges = temp[:]
        i += 1
        print(seed_ranges)
        print(i)
    return min(map(lambda s: s.start, seed_ranges))

def serialize_seed(file):
    raw = file.read()
    split_sections = raw.split("\n\n")
    seeds = list(map(int, split_sections.pop(0).split(":")[1].strip().split(" ")))
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