from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
from akwam import search, get_info, get_content_urls, get_episodes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Akwam Content Scraper API"}


@app.get("/search/")
async def api_search(
    query: str = Query(..., description="The name of the content you're searching for"),
    search_type: str = Query(
        "movie",
        regex="^(movie|series)$",
        description='The type of content (movie or series). Defaults to "movie"',
    ),
    page: int = Query(
        1, description="The page number of search results. Defaults to 1."
    ),
):
    """
    Search for content on Akwam.

    Args:
        query (str): The name of the content you're searching for.
        search_type (str, optional): The type of content (movie, series, or public). Defaults to "movie".
        page (int, optional): The page number of search results. Defaults to 1.

    Returns:
        List[Dict[str, str]]: A list of search results (title and URL).
    """
    return await search(query=query, search_type=search_type, page=page)


@app.get("/info/")
async def api_get_info(
    url: str = Query(..., description=" The content URL from Akwam")
) -> Dict[str, Any]:
    """
    Get detailed information about specific content from Akwam.

    Args:
        url (str): The content URL from Akwam.

    Returns:
        Dict[str, Any]: A dictionary containing content information.
    """
    return await get_info(url)


@app.get("/content_urls/")
async def api_get_content_urls(
    url: str = Query(..., description=" The content URL from Akwam")
) -> List[Dict[str, str]]:
    """
    Get direct download URLs for a specific content.

    Args:
        url (str): The content URL from Akwam.

    Returns:
        List[Dict[str, str]]: A list of download URLs and file sizes.
    """
    return await get_content_urls(url)


@app.get("/episodes/")
async def api_get_episodes(
    url: str = Query(..., description=" The season URL from Akwam")
) -> List[Dict[str, str]]:
    """
    Get a list of episodes for a specific season from Akwam.

    Args:
        url (str): The season URL from Akwam.

    Returns:
        List[Dict[str, str]]: A list of episodes with their titles, URLs, and thumbnails.
    """
    return await get_episodes(url)
