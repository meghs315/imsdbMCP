from fastmcp import FastMCP
import requests
import uvicorn
import starlette

mcp = FastMCP("Movie Summarization MCP")

def get_movie_script(movie_title):
    return "hello world"
