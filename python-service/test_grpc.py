import asyncio
import grpc
from app.grpc import board_pb2, board_pb2_grpc


async def main():
    # Подключаемся к нашему gRPC серверу
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = board_pb2_grpc.BoardServiceStub(channel)

        print("Отправляем запрос на создание доски...")

        # Формируем запрос (title="Моя первая доска", owner_id=1)
        request = board_pb2.CreateBoardRequest(title="Моя первая доска", owner_id=1)

        # Вызываем метод на сервере
        response = await stub.CreateBoard(request)

        print(f"✅ Успех! База данных вернула ID доски: {response.id}")
        print(f"Название: {response.title}")
        print(f"Владелец (ID): {response.owner_id}")


if __name__ == '__main__':
    asyncio.run(main())