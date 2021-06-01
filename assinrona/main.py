import asyncio

async def flash_correr():
    print('O flash começou a correr')

    await asyncio.sleep(3)
    print('O flash chegou !')

async  def superman_correr():
    print('O superman começou a correr')

    await asyncio.sleep(4)
    print('O superman chegou !')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.gather(superman_correr(),flash_correr()))

async def ola_mundo():
   print('Olá ...')
   await asyncio.sleep(1)
   print('... Mundo!')

asyncio.run(ola_mundo())

