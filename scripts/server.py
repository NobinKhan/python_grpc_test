import asyncio
import logging
from server.grpc_server import serve
from granian import Granian, constants

def rest_serve():
    Granian(
        target="server.rest_server:app", 
        address="0.0.0.0",
        port=8000,
        interface=constants.Interfaces.ASGI,
        reload=True
    ).serve()


def grpc_serve():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())