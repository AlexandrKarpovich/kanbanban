import grpc
from sqlalchemy.future import select
from app.grpc import column_pb2, column_pb2_grpc
from app.db.session import AsyncSessionLocal
from app.models.column import Column
from app.models.board import Board  # Импортируем доску для проверки


class ColumnServicer(column_pb2_grpc.ColumnServiceServicer):

    async def CreateColumn(self, request, context):
        async with AsyncSessionLocal() as session:
            # 1. Проверяем, существует ли доска, к которой крепим колонку
            stmt = select(Board).where(Board.id == request.board_id)
            result = await session.execute(stmt)
            board = result.scalar_one_or_none()

            if not board:
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    f"Доска с ID {request.board_id} не найдена"
                )

            # 2. Создаем колонку
            new_column = Column(
                title=request.title,
                board_id=request.board_id,
                position=request.position
            )
            session.add(new_column)
            await session.commit()
            await session.refresh(new_column)

            return column_pb2.ColumnResponse(
                id=new_column.id,
                title=new_column.title,
                board_id=new_column.board_id,
                position=new_column.position
            )