from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional

from utils.websearch import web_search

mcp = FastMCP("call-googlesearch-server")

description_prompt = """
targetが入力されるため、その内容をgoogleで検索する。
"""
@mcp.tool(
    name="call-googlesearch-server",
    description = description_prompt, 
    tags={"catalog", "search"},      
)
def search_result(
    target: str = Field(description="検索する対象の文字が入力される。")
    ) -> str:
    result = web_search(target)
    return result


if __name__ == "__main__":
    mcp.run()