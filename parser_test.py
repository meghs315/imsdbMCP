from parser import is_header  # or wherever you saved the function

test_cases = [
    # (line, scene_count, expected_result)
    ("1 EXT/INT. NIGHTCLUB- EVENING 1", 1, True),
    ("2 INT. LIVING ROOM - DAY 2", 2, True),
    ("3 EXT. PARK - NIGHT 4", 3, False),
    ("4 OFFICE - DAY 4", 4, False),
    ("hellooo", 3, False)

    # add more here...
]

for line, scene_count, expected in test_cases:
    result = is_header(line, scene_count)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: is_header({line!r}, {scene_count}) = {result} (expected {expected})")