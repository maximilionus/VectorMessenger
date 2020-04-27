import asyncio
async def my_coro(delay):  
	loop = asyncio.get_running_loop()
	end_time = loop.time() + delay
	while True:
		print("Blocking...")
		await asyncio.sleep(1)
		if loop.time() > end_time:
			print("Done.")
			break
async def main():  
	my_coro(3.0)
	print('that was idioTOC')
asyncio.run(main())  