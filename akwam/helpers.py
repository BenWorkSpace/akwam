from user_agent import generate_user_agent
from typing import Any, Dict
import asyncio
import aiohttp
import json
import urllib.parse

# THIS DOMAIN CAN BE CHANGE IN THE FUTURE
domain = "https://ak.sv"


async def get(url: str, is_json: bool = False, **kwargs) -> Dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        try:
            response: aiohttp.ClientResponse = await asyncio.create_task(
                session.get(url, **kwargs)
            )
        except Exception as e:
            return {
                "ok": False,
                "status": None,
                "response": "",
                "error": str(e),
            }
        data: Dict = {}
        data["status"] = response.status
        data["response"] = await response.json() if is_json else await response.text()
        if response.status == 200:
            data["ok"] = True
        else:
            data["ok"] = False
    return data


def simple_headers():
    return {"User-Agent": generate_user_agent()}


def write(data: Any, fp: str, is_json: bool = True) -> None:
    with open(fp, "w", encoding="utf-8") as file:
        if is_json:
            json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            file.write(data)


# def decode(url: str) -> str:
#     return urllib.parse.unquote(url)
