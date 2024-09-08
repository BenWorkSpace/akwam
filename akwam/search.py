from bs4 import BeautifulSoup as bs4, ResultSet, Tag
from typing import Dict, Any
from .helpers import get, domain


async def search(
    query: str, search_type: str = "movie", page: int = 1
) -> Dict[str, str]:
    """search in akwam

    Args:
        query (str): content name
        search_type (str, optional): movie Or series. Defaults to "movie".
        page (int, optional): if results appears in more than one page. Defaults to 1.

    Returns:
        Dict[str, str]: dictionery of results, empty if no results
    """    
    if search_type != "public":
        params = {"q": query, "section": search_type, "page": page}
    else:
        params = {"q": query, "page": page}
    response: Dict[str, Any] = await get(f"{domain}/search", params=params)
    if response["ok"]:
        soup = bs4(response["response"], "lxml")
        anchores: ResultSet[Tag] = soup.find_all("a", href=True)
        result = [
            {"title": a.find("img").get("alt"), "url": a.get("href", "")}
            for a in anchores
            if f"/{search_type}/" in a.get("href", "") and a.find("img")
        ]
    else:
        result = {}
    return result
