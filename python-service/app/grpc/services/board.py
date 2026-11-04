import grpc
from app.grpc import board_pb2, board_pb2_grpc
from app.db.session import AsyncSessionLocal
from app.models.board import Board

class BoardServicer(board_pb2_grpc.BoardServiceServicer):

    async def CreateBoard(self, request, context):
        # 1. Открываем сессию с базой данных (как бы "берем трубку")
        async with AsyncSessionLocal() as session:
            # 2. Создаем объект модели SQLAlchemy (пока просто в памяти Python)
            new_board = Board(
                title=request.title,
                owner_id=request.owner_id
            )

            # 3. Добавляем объект в сессию (говорим базе: "запомни это")
            session.add(new_board)

            # 4. Сохраняем изменения в базу (физически отправляем INSERT)
            await session.commit()

            # 5. Обновляем объект, чтобы получить ID, который выдала база
            await session.refresh(new_board)

            # 6. Возвращаем ответ по нашему gRPC-контракту
            return board_pb2.BoardResponse(
                id=new_board.id,
                title=new_board.title,
                owner_id=new_board.owner_id
            )