# Dogbin-API-Wrapper

## del.dog asynchronous / synchronous unofficial API

### you can to use with this library:

- paste text to [dogbin](https://del.dog/)
- get paste from [dogbin](https://del.dog/)
- save the getting text to file
- working with asynchronous / synchronous


Getting started
===============

``` 
pip install dogbin
```



paste to [dogbin](https://del.dog/)
-----------------

```python3
from dogbin import Dogbin
import asyncio

deldog = Dogbin()

url = deldog.paste("some text...") # sync
print(url)
Aync = asyncio.run(deldog.Async_paste("some text..."))  # async
print(Aync)
```

get paste from [dogbin](https://del.dog/)
-----------------------
```python
from dogbin import Dogbin
import asyncio

deldog = Dogbin()

by_url = deldog.get_paste('https://del.dog/atacopegno')  # sync
by_key = deldog.get_paste('atacopegno', save_to_file=True)  # sync
print(f'getting this paste by url {by_url}\n\ngetting this paste by key {by_key}')

async_url = asyncio.run(deldog.Async_getpaste('https://del.dog/atacopegno', save_to_file=True))  # async
async_key = asyncio.run(deldog.Async_getpaste("atacopegno"))  # async
print(f'getting this paste by url:\t {async_url}\n\ngetting this paste by key:\t {async_key}')
```
