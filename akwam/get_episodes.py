from typing import Dict, List
from bs4 import BeautifulSoup as bs4, ResultSet, Tag
from .helpers import get


async def get_episodes(url: str) -> List[Dict[str, str]]:
    """get season episodes

    Args:
        url (str): season url

    Returns:
        List[Dict[str, str]]: list of dictionaries of episodes (title, url)
    """    
    response = await get(url)
    if response["ok"]:
        soup = bs4(response["response"], "lxml")
        anchores: ResultSet[Tag] = soup.find_all("a", href=True)
        episodes = [
            {
                "title": a.find("img").get("alt"),
                "url": a["href"],
                "thumbnail": a.find("img").get("src"),
            }
            for a in anchores
            if f"/episode/" in a["href"] and a.find("img")
        ]
        return episodes
    return []
