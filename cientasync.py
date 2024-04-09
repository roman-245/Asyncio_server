import asyncio  # Импортируем модуль asyncio для асинхронного программирования

async def tcp_echo_client():
    """
    Асинхронная функция, которая подключается к TCP-серверу,
    отправляет сообщение и печатает ответ сервера.
    """
    reader, writer = await asyncio.open_connection('127.0.0.1', 9090)
    # Устанавливаем соединение с сервером на локальном хосте (127.0.0.1) по порту 9090
    # reader - объект для чтения данных из сокета
    # writer - объект для записи данных в сокет
    message = input("Введите сообщение: ")
    print(f'Send: {message!r}')  # Выводим отправляемое сообщение
    writer.write(message.encode())  # Кодируем сообщение в байты и отправляем его
    await writer.drain()  # Ожидаем, пока буфер отправки опустеет

    data = await reader.read(1000)  # Читаем максимум 100 байт данных из сокета
    print(f'Received: {data.decode()!r}')  # Декодируем полученные байты и выводим

    writer.close()  # Закрываем соединение

# Запускаем асинхронную функцию tcp_echo_client с аргументом 'Hello World!'
asyncio.run(tcp_echo_client())