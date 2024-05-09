import asyncio
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def update_status():

    while True:
        # set sleep time before next task run

        await asyncio.sleep(3)

        # your task code goes here
        # e.g: await some_remote_api_call()

        print('task is running')


async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(update_status())

app = Starlette(debug=True,
                routes=[
                    Route('/', homepage),
                ],
                on_startup=[startup_event],)
