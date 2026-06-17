---
tags:
  - quic
  - quic-go
---
# Quic-go 101

- This module is about using QUIC (protocol) in Go language through the **quic-go** library. We’ll begin with easy steps to install everything and build a simple “Hello World” QUIC client and server. 
- Gradually, we’ll explore more advanced topics like handling multiple streams, connection migration

---
## What is Quic-go


✅ QUIC is a protocol- (Click for more details: [QUIC protocol](../../../programming/media-streaming/protocols/quic.md))

✅ quic-go is a Go library that implements that protocol, which:

- is open-source 
- runs on Linux, macOS, and Windows.
- enables building QUIC clients and servers, and can be used as a foundation for HTTP/3 servers.

### What is an HTTP/3 

- HTTP/3 is the latest version of the HTTP protocol used by web browsers to communicate with servers.
- Unlike older versions (HTTP/1.1, HTTP/2), HTTP/3 runs on top of the QUIC protocol instead of TCP.
- This means HTTP/3 servers use QUIC’s features like multiplexing — allowing many requests and responses to happen simultaneously over a single connection without blocking each other.

---
## Relevant links

[QUIC protocol](../../../programming/media-streaming/protocols/quic.md)

[Connection Migration](https://quic-go.net/docs/quic/connection-migration/)

[Multipath](https://quic-go.net/docs/quic/multipath/)

[github](https://github.com/quic-go/quic-go/tree/v0.54.0)
