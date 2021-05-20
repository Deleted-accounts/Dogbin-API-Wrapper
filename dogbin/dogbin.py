import re
import aiohttp
import asyncio
import os
import requests


class Dogbin:

    async def Async_paste(self, text: str):
        async with aiohttp.ClientSession() as session:
            async with session.post("https://del.dog/documents", json={"content": text}, timeout=3) as response:
                r = await response.json()
                pasted = f"https://del.dog/{r['key']}"
        return pasted

    async def Async_getpaste(self, url: str, save_to_file: bool = False):
        sub = re.compile(r'(https://del.dog/(raw/)?)?')
        key = re.sub(sub, '', url)
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://del.dog/raw/{key}') as resp:
                text = await resp.text()
            if save_to_file:
                with open(key + '.txt', 'w') as file:
                    file.write(text)
        return text

    def paste(self, text: str):
        get = requests.post("https://del.dog/documents", json={"content": text})
        r = get.json()
        pasted = f"https://del.dog/{r['key']}"
        return pasted

    def get_paste(self, url: str, save_to_file: bool = False):
        sub = re.compile(r'(https://del.dog/(raw/)?)?')
        key = re.sub(sub, '', url)
        get = requests.get(f'https://del.dog/raw/{key}')
        text = get.text
        if save_to_file:
            with open(key + '.txt', 'w') as file:
                file.write(text)
        return text


if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

