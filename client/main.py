"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging
from datetime import datetime
import grpc
from protobuf import helloworld_pb2
from protobuf import helloworld_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        count = 0
        start = datetime.now()
        while count < 100001:
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = await stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
            count += 1
        end = datetime.now()
        print(f"Greeter client {(end-start).seconds} received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())