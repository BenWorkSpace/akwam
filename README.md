# Content Scraper for Akwam

This repository contains an asynchronous Python scraper designed to retrieve content information, search for media, and fetch download URLs from the Akwam website. The tool uses `aiohttp` for making asynchronous HTTP requests and `BeautifulSoup` for parsing HTML content.

## Requirements

- Python 3.7+
- `aiohttp` for handling asynchronous HTTP requests
- `beautifulsoup4` for parsing HTML
- `lxml` for HTML parsing

### Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Features

1. **Search for Media**
   - You can search for movies or series by providing a query and search type.
   
2. **Fetch Media Information**
   - Retrieve detailed information about specific media content, such as title, poster, and additional metadata.
   
3. **Get Content Download URLs**
   - Extract a list of direct download links, including file sizes, from the content page.

4. **Retrieve Episodes of a Series**
   - Fetch a list of episodes for a specific season of a series, including their titles, URLs, and thumbnails.

## Usage

### 1. Search for Content

```python
results = await search("movie_name", search_type="movie", page=1)
```

- `query`: The name of the content you're searching for.
- `search_type`: The type of content to search for (either `movie` or `series`).
- `page`: Optional, the page number of search results.

**Returns**: A dictionary with titles and URLs of search results.

### 2. Get Content Information

```python
info = await get_info("https://ak.sv/some-content-url")
```

- `url`: The content URL from Akwam.

**Returns**: A dictionary containing the media's title, poster URL, and additional information.

### 3. Get Content Download URLs

```python
urls = await get_content_urls("https://ak.sv/some-content-url")
```

- `url`: The content URL from Akwam.

**Returns**: A list of dictionaries containing the download URLs and file sizes.

### 4. Get Season Episodes

```python
episodes = await get_episodes("https://ak.sv/season-url")
```

- `url`: The season URL from Akwam.

**Returns**: A list of episodes, each containing the episode title, URL, and thumbnail.

## Error Handling

The functions handle network errors and unexpected status codes gracefully, returning a dictionary with the error message and status code when applicable.

## License

This project is licensed under the MIT License.
