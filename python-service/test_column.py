import asyncio
import grpc
from app.grpc import column_pb2, column_pb2_grpc


async def main():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = column_pb2_grpc.ColumnServiceStub(channel)

        print("Отправляем запрос на создание колонки...")
        # Привязываем к доске с ID=1
        request = column_pb2.CreateColumnRequest(title="To Do", board_id=1, position=1)

        response = await stub.CreateColumn(request)

        print(f"✅ Успех! Колонка создана с ID: {response.id}")
        print(f"Название: {response.title}, Доска: {response.board_id}")


if __name__ == '__main__':
    asyncio.run(main())