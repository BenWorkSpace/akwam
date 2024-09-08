from bs4 import BeautifulSoup as bs4, ResultSet, Tag
from typing import Dict, List
from .helpers import get
import asyncio


async def get_content_urls(url: str) -> List[Dict[str, str]]:
    """get content direct download urls

    Args:
        url (str): content url

    Returns:
        List[Dict[str, str]]: list of dictionaries of content urls (size, url)
    """    
    response = await get(url)
    if response["ok"]:
        soup = bs4(response["response"], "lxml")
        qualities = []
        quality_tags: ResultSet[Tag] = soup.find_all("a", {"class": "link-download"})
        urls = await asyncio.gather(
            *[
                get_direct_url(tag.get("href", "").replace("http://", "https://"))
                for tag in quality_tags
            ]
        )
        size_tags: ResultSet[Tag] = soup.find_all("span", class_="font-size-14 mr-auto")
        for url, size in zip(urls, size_tags):
            qualities.append({"url": url, "size": size.text.strip()})
        return qualities
    return []


async def get_direct_url(shortened_url: str) -> str:
    initial_response = await get(shortened_url)
    if initial_response["ok"]:
        soup = bs4(initial_response["response"], "lxml")
        download_page_link = soup.find("a", {"class": "download-link"})["href"]
        download_page_response = await get(download_page_link)
        if download_page_response["ok"]:
            soup = bs4(download_page_response["response"], "lxml")
            btn_loader = soup.find("div", {"class": "btn-loader"})
            direct_download_link = btn_loader.find("a").get("href", "")
            return direct_download_link
    return ""
