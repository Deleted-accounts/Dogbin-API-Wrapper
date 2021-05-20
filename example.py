from dogbin import Dogbin
import asyncio


deldog = Dogbin()

# paste to de.dog

url = deldog.paste("some text...") # sync
print(url)
Aync = asyncio.run(deldog.Async_paste("some text..."))  # async
print(Aync)


# get paste from del.dog

by_url = deldog.get_paste('https://del.dog/atacopegno')  # sync
#  save the paste in file
by_key = deldog.get_paste('atacopegno', save_to_file=True)  # sync
print(f'getting this paste by url {by_url}\n\ngetting this paste by key {by_key}')
async_url = asyncio.run(deldog.Async_getpaste('https://del.dog/atacopegno', save_to_file=False))  # async
async_key = asyncio.run(deldog.Async_getpaste("atacopegno"))  # async
print(f'getting this paste by url:\t {async_url}\n\ngetting this paste by key:\t {async_key}')
