from bs4 import BeautifulSoup as bs4, ResultSet, Tag
from typing import Dict, Any
from .helpers import get


async def get_info(url: str) -> Dict[str, Any]:
    """get content info using its url

    Args:
        url (str): content url

    Returns:
        Dict[str, Any]: dictionry with content info
    """    
    response: Dict[str, Any] = await get(url)
    if response["ok"]:
        soup: bs4 = bs4(response["response"], "lxml")
        main_container: Tag = soup.find_all("div", {"class": "container"})[3]
        poster: str = main_container.find("a").get("href", "")
        info_container: Tag = main_container.find("div").find_all("div")[1]
        title: str = info_container.find("h1", {"class": "entry-title"}).get_text()
        info_container_divs: ResultSet[Tag] = info_container.find_all("div")
        another_info: list = [
            div.get_text(" ", strip=True) for div in info_container_divs
        ]
        return {"poster": poster, "title": title, "another_info": another_info}
    else:
        return {}
