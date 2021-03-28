import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor

def search(session, request):
    with session.get(request) as response:
        data = response.text
        if response.status_code != 200:
            print("FAILURE::{0}".format(url))

        return data

async def make_req_async(reqs):
    with ThreadPoolExecutor(max_workers=len(reqs)) as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(
                    executor,
                    search,
                    *(session, req) # Allows us to pass in multiple arguments to `fetch`
                )
                for req in reqs
            ]
            for response in await asyncio.gather(*tasks):
                pass

def make_request(word):
    return f"http://localhost:8983/solr/MemCore/select?q=image%3A*{word}*%0Ayear%3A*{word}*%0Atitle%3A*{word}*%0Acategory%3A*{word}*%0Acontent%3A*{word}*%0Aurl%3A*{word}*%0Astatus%3A*{word}*%0Aid%3A*{word}*";

def get_req_to_search():
    with open('random_words.txt', 'r') as reader:
        all_words = reader.readlines()
        return [make_request(word) for word in all_words]

def main():
    loop = asyncio.get_event_loop()
    requests = get_req_to_search()
    future = asyncio.ensure_future(make_req_async(requests))
    loop.run_until_complete(future)
    print('--------DONE--------')
main()