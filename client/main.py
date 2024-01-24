"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging
import grpc
from protobuf.gen import helloworld_pb2
from protobuf.gen import helloworld_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = await stub.SayHello(helloworld_pb2.HelloRequest(name="nobin"))
        print("Greeter client received: " + response.message)

        response = await stub.GetAge(helloworld_pb2.GetAgeRequest(age="50"))
        print(response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())