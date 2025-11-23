import json
import random
from fastmcp import FastMCP

mcp = FastMCP("remote-math-tools")

@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100):
    """Generate a random integer between min_val and max_val."""
    return {"number": random.randint(min_val, max_val)}

@mcp.tool()
def add_numbers(a: float, b: float):
    """Add two numbers and return the sum."""
    return {"result": a + b}

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port = 8000)
