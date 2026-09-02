## Internet Movie Script Database - MCP for Movie Catch Up Tool

# Workflow: 
1. User gives movie title + a description of where they are
2. Check cache (SQLite) for that movie title
3. If not cached: scrape IMSDb → parse into scenes (your number-matching + all-caps + INT/EXT logic) → generate one-line summary per scene (LLM, done once) → insert all rows into SQLite
4. If cached (or now freshly cached): LLM matches user's description against the scene_summary column to find the right scene_number
5. Pull scene_text for all scenes 1 through N → LLM synthesizes a spoiler-free "here's what's happened" recap

# Data model (SQLite, one table):

scenes: movie_title (TEXT), scene_number (INTEGER), scene_summary (TEXT), scene_text(TEXT)