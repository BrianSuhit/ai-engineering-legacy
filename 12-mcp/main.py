"""
This script demonstrates the basic workflow of creating an MCP (Machine-to-Machine Communication Protocol) server.
"""
from mcp.server.fastmcp import FastMCP

# 1. Create the MCP Server
mcp = FastMCP("Basic")

# 2. Define the TOOL
# The "Hello World" of MCPs, just returns text.
@mcp.tool()
def greet(name: str = "User") -> str:
    """
    Greets the user. It is the simplest possible function.
    """
    return f"Hello, {name}! This is your first MCP."

# 3. The server starts listening (Run)
if __name__ == "__main__":
    mcp.run()
    
    # run mcp: npx @modelcontextprotocol/inspector python main.py