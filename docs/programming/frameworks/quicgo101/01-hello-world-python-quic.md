# aioquic (QUIC implementation with Python): Hello, World

## Install Dependencies

Python Virtual Environment and OpenSSL are required to be installed. Following commands are for Ubuntu and Debian-based distributions for any other OS or Linux distribution, please check the concerned documentations.

```console
sudo apt install python3-venv openssl
```

## Create Project Directory

```console
mkdir quic-python
cd quic-python
```

## Create and Activate Python Virtual Environment

```console
python3 -m venv venv
source venv/bin/activate
```

## Create `requirements.txt`

Create file `requirements.txt` with following content:

```plaintext
aioquic==1.2.0
asyncio==4.0.0
attrs==25.3.0
certifi==2025.8.3
cffi==1.17.1
cryptography==45.0.6
pyasn1==0.6.1
pyasn1_modules==0.4.2
pycparser==2.22
pylsqpack==0.3.22
pyOpenSSL==25.1.0
service-identity==24.2.0
typing_extensions==4.14.1
```

## Install Python Dependencies

```console
pip install -r requirements.txt
```

## Generate Self-Signed Certificate for Local Host

```console
openssl req \
  -new \
  -newkey rsa:2048 \
  -days 365 \
  -nodes \
  -x509 \
  -keyout key.pem \
  -out cert.pem \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost"
```

## Create Server

Create server file `server.py` with following content:

```python
import asyncio
from aioquic.asyncio import QuicConnectionProtocol, serve
from aioquic.quic.configuration import QuicConfiguration

# Define server protocol (how to handle messages)
class ServerProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if hasattr(event, "data"):  # If data is received
            print("Server received:", event.data.decode())
            # Echo back to client
            self._quic.send_stream_data(event.stream_id, b"Hello from server!")

# Run the QUIC server
async def main():
    config = QuicConfiguration(is_client=False)
    config.load_cert_chain("cert.pem", "key.pem")  # TLS cert required

    # Listen on localhost:4433
    await serve("localhost", 4433, configuration=config, create_protocol=ServerProtocol)
    await asyncio.get_running_loop().create_future()  # Keep server running

if __name__ == "__main__":
    asyncio.run(main())
```

## Create Client

Create client file `client.py` with following content:

```python
import asyncio
from aioquic.asyncio import connect, QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived

class ClientProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            print("Client received:", event.data.decode())

async def main():
    config = QuicConfiguration(is_client=True)
    config.verify_mode = False  # disable TLS verification for local testing
    config.load_verify_locations("cert.pem")

    # Connect to server
    async with connect(
        "localhost", 4433, configuration=config, create_protocol=ClientProtocol
    ) as client:
        stream_id = client._quic.get_next_available_stream_id()
        client._quic.send_stream_data(stream_id, b"Hello from client!")

        # Keep running for a bit to receive server reply
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
```

## Run Server

```console
python server.py
```

## Run Client

Now open another terminal, go to same directory, activate Python Virtual Environment, and then run following command:

```console
python client.py
```
