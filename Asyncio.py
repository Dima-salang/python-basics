import asyncio


# asyncio is a python library to run write concurrent code using async/await syntax

# will return a co-routine object
async def foo():
    print("hello!")
    # creates a task to run concurrent code while a function is sleeping
    task = asyncio.create_task(main())
    await asyncio.sleep(1)
    print("finished")


async def main():
    print("hello2you!")
    await asyncio.sleep(2)


# // Here, the program switches between the execution of functions as they sleep.
async def fetch():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data' : 1}


async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def tasks():
    task1 = asyncio.create_task(fetch())
    task2 = asyncio.create_task(print_num())
    value = await task1  # needs to finish task1 first
    print(value)
    await task2  # finish task2

# create an event loop
asyncio.run(foo())
asyncio.run(tasks())
