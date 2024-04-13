import asyncio

async def client_handler(reader, writer):
	request = await reader.read(1024)
	#print(f"Данные - {request.decode}")
	writer.close()

async def start_server():
	server = await asyncio.start_server(client_handler, 'localhost', 9090)
	print("Сервер запущен. Ожидание подключений...")
	async with server:
		await server.serve_forever()

asyncio.run(start_server())
