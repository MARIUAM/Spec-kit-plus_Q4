import re
from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent

mcp = FastMCP(name="MyFirstMCPServer")

@mcp.tool
def greet(name:str) -> str:
    """Returns a friendly greeting"""
    return f"Hello {name}! Its a pleasure to connect from your first MCP Server."    

@mcp.tool
def calculate_readability(text: str) -> float:
    """Calculates the Flesch-Kincaid grade level for the given text."""
    # This is a simplified implementation for demonstration purposes.
    words = len(text.split())
    sentences = len(re.split(r'[.!?]+', text))
    syllables = sum(1 for word in text.split() for c in word.lower() if c in 'aeiou')
    
    # Avoid division by zero
    if words == 0 or sentences == 0:
        return 0.0
        
    # Flesch-Kincaid Grade Level formula
    score = (0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59
    return round(score, 2)

@mcp.tool
def check_for_weasel_words(text: str) -> list[str]:
    """Identifies and returns a list of ambiguous 'weasel words' from the text."""
    weasel_words = ["It seems that this method might be better than others.y"]
    # Use regex to find all occurrences of any weasel word, ignoring case and matching whole words
    pattern = r'\b(' + '|'.join(weasel_words) + r')\b'
    found_words = re.findall(pattern, text, re.IGNORECASE)
    return list(set(found_words)) # Return unique words found      

@mcp.prompt
def tech_edit(text_to_review: str) -> PromptMessage:
    """Acts as a senior technical editor to review the provided text."""
    prompt_text = f"""
    You are an expert technical editor. Your goal is to provide a comprehensive and helpful review of 
    the following text.
    
    Please perform the following steps in order:
    1. First, call the `calculate_readability` tool on the text to determine its Flesch-Kincaid grade level.
    2. Next, call the `check_for_weasel_words` tool to find any ambiguous "weasel words".
    3. After using the tools, perform your own analysis of the text for overall clarity, tone, and style.
    Specifically look for passive voice and overly complex sentences.
    4. Finally, synthesize all of your findings (from the tool outputs and your own analysis) into a 
    single, well-structured markdown report with three sections:
        - ### Readability Score
          State the score returned by the tool and briefly explain what it means (e.g., "suitable for a
          general audience").
        - ### Weasel Words
          List any words found by the tool. For each word, explain why it's ambiguous and suggest a more
          specific alternative.
        - ### General Feedback
          Provide your analysis on tone, clarity, and style. Include specific examples from the text and
          offer concrete suggestions for improvement.
    
    Your final output should be ONLY the markdown report.
    
    Here is the text to review:
    ---
    {text_to_review}
    ---
    """
    return PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))

if __name__ == "__main__":
    mcp.run(transport="http",port="8080")


# from fastmcp import FastMCP

# # MCP server banate hain
# mcp = FastMCP("my-server")

# # simple tool define karte hain
# @mcp.tool()
# def say_hello(name: str) -> str:
#     """Return a greeting message."""
#     return f"Hello, {name}! 👋"
# @tool
# def check_syntax_errors(code: str) -> dict:
#     """
#     Checks Python code for syntax errors.
#     """
#     try:
#         compile(code, "<string>", "exec")
#         return {"result": "No syntax errors found!"}
#     except SyntaxError as e:
#         return {"result": f"Syntax Error: {e}"}

        
# # Server ko run karne ka command
# if __name__ == "__main__":
#     mcp.run()


# from fastapi import FastAPI
# from fastmcp import FastMCP

# # Create FastAPI app
# app =  FastAPI()

# # Create MCP server instance
# mcp = FastMCP(name="MyFirstMCPServer")

# # Add MCP tool
# @mcp.tool
# def greet(name: str) -> str:
#     """Returns a friendly greeting"""
#     return f"Hello {name}! It's a pleasure to connect from your first MCP Server."

# # Add a home route for browser access
# @app.get("/")
# def home():
#     return {"message": "Hello from MyFirstMCPServer 👋"}

# if __name__ == "__main__":
#     # Run both MCP and FastAPI together
#     import uvicorn
#     from threading import Thread

#     # Run MCP in a background thread
#     def run_mcp():
#         mcp.run(transport="http", port=8081)

#     Thread(target=run_mcp).start()

#     # Run FastAPI app
#     uvicorn.run(app, host="127.0.0.1", port=8080)
