import asyncio

host = "localhost"

async def scan_port(port):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"\nПорт {port} открыт")
        writer.close()
    except:
        pass

async def main():
    tasks = [scan_port(port) for port in range(1, 10000)]
    await asyncio.gather(*tasks)

asyncio.run(main())