# Akwam Content Scraper API

This FastAPI-based web application provides an API for searching, retrieving detailed content information, download URLs, and episode lists from the Akwam website. It offers asynchronous endpoints to interact with the site’s data and return results in JSON format.

## Features

- **Search Content**: Search for movies or series on Akwam.
- **Retrieve Content Information**: Get detailed information about specific content such as title, poster, and metadata.
- **Get Download URLs**: Retrieve a list of direct download links, including file sizes, for specific content.
- **List Episodes**: Fetch a list of episodes for a specific season of a series, including episode title, thumbnail, and URL.

## Requirements

- Python 3.7+
- Required Python packages:
  - `fastapi`
  - `uvicorn`
  - `aiohttp`
  - `beautifulsoup4`
  - `lxml`

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## How to Run the API

1. Save the code to a file named `main.py`.

2. Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

3. The API will be accessible at `http://127.0.0.1:8000`.

4. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

### Root Endpoint

- **GET /**  
  Returns a welcome message to check if the API is running.
  
  Example:

  ```bash
  curl http://127.0.0.1:8000/
  ```

  **Response**:
  ```json
  {
      "message": "Welcome to the Akwam Content Scraper API"
  }
  ```

### 1. Search for Content

- **GET /search/**  
  Search for movies or series on Akwam based on a query.

  **Parameters**:
  - `query` (required): The name of the content.
  - `search_type` (optional): The type of content to search for (either `movie` or `series`). Defaults to `movie`.
  - `page` (optional): The page number of search results. Defaults to 1.

  **Example**:
  ```bash
  curl "http://127.0.0.1:8000/search/?query=batman&search_type=movie&page=1"
  ```

  **Response**:
  ```json
  [
    {
      "title": "Batman",
      "url": "/movie/batman"
    },
    {
      "title": "Batman Returns",
      "url": "/movie/batman-returns"
    }
  ]
  ```

### 2. Get Content Information

- **GET /info/**  
  Get detailed information about specific content from Akwam.

  **Parameters**:
  - `url` (required): The URL of the content from Akwam.

  **Example**:
  ```bash
  curl "http://127.0.0.1:8000/info/?url=https://ak.sv/movie/batman"
  ```

  **Response**:
  ```json
  {
    "poster": "https://ak.sv/images/poster.jpg",
    "title": "Batman",
    "remains_info": ["Year: 1989", "Genre: Action", "Duration: 126 mins"]
  }
  ```

### 3. Get Content Download URLs

- **GET /content_urls/**  
  Fetch direct download links for a specific content from Akwam.

  **Parameters**:
  - `url` (required): The content URL from Akwam.

  **Example**:
  ```bash
  curl "http://127.0.0.1:8000/content_urls/?url=https://ak.sv/movie/batman"
  ```

  **Response**:
  ```json
  [
    {
      "url": "https://ak.sv/download/batman-1080p.mp4",
      "size": "1.4 GB"
    },
    {
      "url": "https://ak.sv/download/batman-720p.mp4",
      "size": "850 MB"
    }
  ]
  ```

### 4. Get Episodes for a Season

- **GET /episodes/**  
  Retrieve a list of episodes for a specific season of a series.

  **Parameters**:
  - `url` (required): The URL of the season from Akwam.

  **Example**:
  ```bash
  curl "http://127.0.0.1:8000/episodes/?url=https://ak.sv/series/season-1"
  ```

  **Response**:
  ```json
  [
    {
      "title": "Episode 1",
      "url": "/episode/1",
      "thumbnail": "https://ak.sv/images/ep1-thumb.jpg"
    },
    {
      "title": "Episode 2",
      "url": "/episode/2",
      "thumbnail": "https://ak.sv/images/ep2-thumb.jpg"
    }
  ]
  ```

## Conclusion

This API provides access to various content-related features on Akwam, including searching for media, retrieving detailed content information, downloading content URLs, and getting episode lists. It is built using FastAPI and offers asynchronous handling of requests for better performance.