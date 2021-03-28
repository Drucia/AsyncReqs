import asyncio
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor

async def get_data_asynchronous():
    csvs_to_fetch = [
        "ford_escort.csv",
        "cities.csv",
        "hw_25000.csv",
        "mlb_teams_2012.csv",
        "nile.csv",
        "homes.csv",
        "hooke.csv",
        "lead_shot.csv",
        "news_decline.csv",
        "snakes_count_10000.csv",
        "trees.csv",
        "zillow.csv"
    ]
    print("{0:<30} {1:>20}".format("File", "Completed at"))
    
    # Note: max_workers is set to 10 simply for this example,
    # you'll have to tweak with this number for your own projects
    # as you see fit
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            # Set any session parameters here before calling `fetch`

            # Initialize the event loop        
            loop = asyncio.get_event_loop()
            
            # Set the START_TIME for the `fetch` function
            START_TIME = default_timer()
            
            # Use list comprehension to create a list of
            # tasks to complete. The executor will run the `fetch`
            # function for each csv in the csvs_to_fetch list
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    *(session, csv) # Allows us to pass in multiple arguments to `fetch`
                )
                for csv in csvs_to_fetch
            ]
            
            # Initializes the tasks to run and awaits their results
            for response in await asyncio.gather(*tasks):
                pass