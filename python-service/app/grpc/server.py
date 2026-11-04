import grpc
from app.grpc import health_pb2, health_pb2_grpc
from app.grpc import board_pb2_grpc
from app.grpc.services.board import BoardServicer

class HealthServicer(health_pb2_grpc.HealthServicer):
    async def Check(self, request, context):
        return health_pb2.HealthCheckResponse(status="SERVING")

async def start_grpc_server(port: int) -> grpc.aio.Server:
    server = grpc.aio.server()

    board_pb2_grpc.add_BoardServiceServicer_to_server(BoardServicer(), server)
    
    health_pb2_grpc.add_HealthServicer_to_server(HealthServicer(), server)

    server.add_insecure_port(f"[::]:{port}")
    await server.start()
    return server