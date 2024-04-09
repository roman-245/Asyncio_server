import asyncio  # Импортируем модуль asyncio для асинхронного программирования

async def handle_echo(reader, writer):
    """
    Эта асинхронная функция обрабатывает входящие соединения.
    Она читает данные, полученные от клиента, и отправляет их обратно.
    """
    data = await reader.read(1000)  # Читаем максимум 100 байт данных от клиента
    message = data.decode()  # Декодируем байтовые данные в строку
    addr = writer.get_extra_info('peername')  # Получаем адрес клиента
    print(f"Received {message!r} from {addr!r}")  # Выводим полученное сообщение и адрес клиента

    writer.write(data)  # Отправляем полученные данные обратно клиенту
    await writer.drain()  # Ожидаем, пока буфер отправки опустеет
    print(f"Sent {message!r} to {addr!r}")  # Выводим, что данные были отправлены обратно

    writer.close()  # Закрываем соединение с клиентом


async def main():
    """
    Главная функция, создающая и запускающая сервер.
    """
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 9090)
    # Создаем сервер, привязываем его к локальному хосту на порту 9090
    # и регистрируем обработчик handle_echo для входящих соединений

    addr = server.sockets[0].getsockname()  # Получаем адрес сервера
    print(f'Serving on {addr}')  # Выводим адрес сервера

    async with server:
        # Запускаем сервер в контекстном менеджере
        await server.serve_forever()  # Ожидаем бесконечно входящие соединения

# Запускаем главную функцию в асинхронной петле
asyncio.run(main())