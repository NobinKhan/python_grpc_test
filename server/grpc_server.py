import logging
from grpc.aio import server as Server, ServicerContext
from protobuf.gen.helloworld_pb2 import (
    HelloRequest,
    HelloReply,
    GetAgeRequest,
    GetAgeReply,
)
from protobuf.gen.helloworld_pb2_grpc import (
    GreeterServicer,
    add_GreeterServicer_to_server,
)


class Greeter(GreeterServicer):
    async def SayHello(
        self, request: HelloRequest, context: ServicerContext
    ) -> HelloReply:
        print(request.name, " Sent a Request With SayHello!")
        return HelloReply(message="Hello, %s!" % request.name)

    async def GetAge(
        self, request: GetAgeRequest, context: ServicerContext
    ) -> GetAgeReply:
        return GetAgeReply(message=f"Your Age Maybe {request.age}!")


async def serve() -> None:
    server = Server()
    add_GreeterServicer_to_server(Greeter(), server)

    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)

    logging.info("Starting server on %s", listen_addr)
    await server.start()
    logging.info("Server Successfully started at port 50051")
    await server.wait_for_termination()

