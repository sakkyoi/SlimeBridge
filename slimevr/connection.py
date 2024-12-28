import socket
import asyncio


class Connection:
    # https://github.com/SlimeVR/SlimeVR-Sender-Example/blob/1df342a0fcb18bd84c4103a10453d41ec9dfdcdc/src/main/kotlin/PacketBuilder.kt#L16-L19
    HEARTBEAT_PACKET = b'\x00' * 28

    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        self.sock.bind((ip, port))  # Bind to the server address

        # Start the heartbeat task
        self.heartbeat_task = asyncio.create_task(self.heartbeat())

    async def heartbeat(self):
        """
        https://github.com/SlimeVR/SlimeVR-Sender-Example/blob/1df342a0fcb18bd84c4103a10453d41ec9dfdcdc/src/main/kotlin/UDPHandler.kt#L25-L35
        """
        while True:
            self.sock.send(Connection.HEARTBEAT_PACKET)
            await asyncio.sleep(0.8)
