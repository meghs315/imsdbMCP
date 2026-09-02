# This is a tool for the agent to use to turn the raw IMSDb script text into a table 
# divided by scenes. Each row will contain the move title, scene number, scene summary 
# the full scene text. The agent will then use this table to recap up to a scene.

import re

def parse_script(text, movie_title):
    """
    Parses raw IMSDb script text into a list of scene dicts.
    Returns: list of {"movie_title": ..., "scene_number": ..., "scene_text": ...}
    """
    scenes = []
    scene_count = 1
    accumulator = []

    lines = text.splitlines()

    for line in lines:
        if is_header(line, scene_count):
            # save the scene that just finished (if there's anything accumulated)
            if accumulator:
                scenes.append({
                    "movie_title": movie_title,
                    "scene_number": scene_count,
                    "scene_text": "\n".join(accumulator)
                })
                scene_count += 1
                accumulator = []
            # if accumulator is empty, this is the very first header — nothing to save yet
        else:
            accumulator.append(line)

    # catch the final scene, which never triggers a save inside the loop
    if accumulator:
        scenes.append({
            "movie_title": movie_title,
            "scene_number": scene_count,
            "scene_text": "\n".join(accumulator)
        })

    return scenes

def is_header(line, scene_count):
    pattern = r'^(\d+)\s+(INT|EXT|INT/EXT|EXT/INT)\.?\s*.*\s+(\d+)$'
    match = re.match(pattern, line)  # one call does both the check AND gives you the object
    if match:
        if match.group(1) == match.group(3) and match.group(1) == str(scene_count):
            return True
    return False