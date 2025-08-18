# Quic-go 101- Hello World
# has some bugs: needs fixing

## 1. Prerequisites
Make sure you have Go installed:

(
[go installation](../../languages/golang101/01-gettingstarted.html#1-go-installation))

---
## 2. Create a new Go module

### What is a Go module
- In modern Go (1.17+), creating a Go module is necessary for almost all development, when you're:
	- Importing third-party packages (like quic-go)
	- Building projects with multiple files
	- Using dependency/version tracking

- A Go module is simply a project with a go.mod file at its root. It tells Go:
	- What your module is called
	- What dependencies it uses (and their versions)
	- How to build and fetch those dependencies

**A side note:** This concept is quite common, e.g. if you have worked with dockers, we create a project similar to the one we are discussing here.

### When we do not need a module:
- If you're writing a one-file script with only Go standard library packages
- If you’re just experimenting and not using go get or go build

### Steps to create a module

i. Create a project folder and initialize the module:
	``` bash
	mkdir quic-hello
	cd quic-hello
	go mod init quic-hello  #this creates a file go.mod
	```

ii. type ```ls -al``` and check the contents of the foler. A file is created ```go.mod```.

Contents of the ```go.mod``` file are similar to the following:
	
``` text
module quic-hello

go 1.22.2
```

---
## 3. Install ```quic-go```
Add quic-go as a dependency:

``` bash
go get github.com/quic-go/quic-go@latest
```

=== "Explaination"
	- Go noticed that v0.54.0 requires Go ≥ 1.23:
	- Reqired dependencies were downloaded automatically
	
=== "Output"
	``` bash
	go: downloading github.com/quic-go/quic-go v0.54.0
	go: github.com/quic-go/quic-go@v0.54.0 requires go >= 1.23; switching to go1.24.6
	go: downloading go.uber.org/mock v0.5.0
	go: downloading golang.org/x/net v0.28.0
	go: downloading golang.org/x/sys v0.23.0
	go: downloading golang.org/x/crypto v0.26.0
	go: downloading golang.org/x/tools v0.22.0
	go: downloading golang.org/x/mod v0.18.0
	go: downloading golang.org/x/sync v0.8.0
	go: upgraded go 1.22.2 => 1.23
	go: added toolchain go1.24.6
	go: added github.com/quic-go/quic-go v0.54.0
	go: added go.uber.org/mock v0.5.0
	go: added golang.org/x/crypto v0.26.0
	go: added golang.org/x/mod v0.18.0
	go: added golang.org/x/net v0.28.0
	go: added golang.org/x/sync v0.8.0
	go: added golang.org/x/sys v0.23.0
	go: added golang.org/x/tools v0.22.0
	```
---
### 4. Write a minimal QUIC server (server.go)
Create a file called ```server.go```:

``` go
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"log"

	quic "github.com/quic-go/quic-go"
)

func main() {
	addr := "localhost:4242"

	// QUIC requires TLS 1.3
	tlsConf := &tls.Config{
		Certificates: []tls.Certificate{generateTLSCert()},
		NextProtos:   []string{"quic-hello"},
	}

	listener, err := quic.ListenAddr(addr, tlsConf, nil)
	if err != nil {
		log.Fatal("Failed to start server:", err)
	}
	fmt.Println("QUIC server listening on", addr)

	for {
		conn, err := listener.Accept(context.Background())
		if err != nil {
			log.Println("Accept error:", err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn quic.Connection) {
	defer conn.CloseWithError(0, "server done")

	stream, err := conn.AcceptStream(context.Background())
	if err != nil {
		log.Println("Stream error:", err)
		return
	}

	buf := make([]byte, 1024)
	n, err := stream.Read(buf)
	if err != nil {
		log.Println("Read error:", err)
		return
	}
	message := string(buf[:n])
	fmt.Println("Received from client:", message)

	// Send a response
	_, err = stream.Write([]byte("Hello from QUIC server!"))
	if err != nil {
		log.Println("Write error:", err)
	}
}

func generateTLSCert() tls.Certificate {
	// Self-signed cert (for dev only — do NOT use in production)
	certPEM := []byte(`-----BEGIN CERTIFICATE-----
MIIBjTCCATOgAwIBAgIJAJuoxEVf38vNMAoGCCqGSM49BAMCMBIxEDAOBgNVBAMM
B3F1aWMtY29kZTAeFw0yMzA4MTgxMzEwMTJaFw0yNDA4MTgxMzEwMTJaMBIxEDAO
BgNVBAMMB3F1aWMtY29kZTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABFYu0LF0
vDuX+S7Zj+j81sK7+aTK1ISXlo5ylCG4K1SCqIUzmQOvh76OwXb1VmcKhpI4iS75
j+x87m76JjoL22ko6jUDBOMB0GA1UdDgQWBBQCV30GqOYqscKgxWLCY6HkRyk1nD
AfBgNVHSMEGDAWgBQCV30GqOYqscKgxWLCY6HkRyk1nDAMBgNVHRMEBTADAQH/
MAoGCCqGSM49BAMCA0cAMEQCIH64kdz+qJAfXzUFCw+Or+vnWVrpp0QxiH6p6EyY
zYQiTAiAvHkJ0u5BvRx+7up8WraYXjKacQtkG+TxvCsQSSbsPRGg==
-----END CERTIFICATE-----`)
	keyPEM := []byte(`-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIAjk6pAqfzHYkAeSxOv7Zj/KXHyfTvRTrKCFKmDeQfq5ZoAoGCCqGSM49
AwEHoUQDQgAEVi7QsXS8O5f5Lt2P6PzWwrv5pMrUhJeWjnKUIbgrVIKohTOZA6+H
vo7BdvVWZwqGkjiJLvmP8fO5u+iY6C9tpA==
-----END EC PRIVATE KEY-----`)
	cert, err := tls.X509KeyPair(certPEM, keyPEM)
	if err != nil {
		log.Fatal(err)
	}
	return cert
}
```

## 5. Write a minimal QUIC client (client.go)
Create a file called ```client.go```:

``` go
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"log"

	quic "github.com/quic-go/quic-go"
)

func main() {
	addr := "localhost:4242"

	tlsConf := &tls.Config{
		InsecureSkipVerify: true, // Accept self-signed cert for testing
		NextProtos:         []string{"quic-hello"},
	}

	conn, err := quic.DialAddr(addr, tlsConf, nil)
	if err != nil {
		log.Fatal("Dial error:", err)
	}
	defer conn.CloseWithError(0, "client done")

	stream, err := conn.OpenStreamSync(context.Background())
	if err != nil {
		log.Fatal("Stream open error:", err)
	}

	// Send message
	message := "Hello from QUIC client!"
	_, err = stream.Write([]byte(message))
	if err != nil {
		log.Fatal("Write error:", err)
	}

	// Read response
	buf := make([]byte, 1024)
	n, err := stream.Read(buf)
	if err != nil {
		log.Fatal("Read error:", err)
	}

	fmt.Println("Received from server:", string(buf[:n]))
}
```

## 6. Run server and client (on linux)

### Terminal 1 — Start the Server:
``` bash
cd quic-hello
go run server.go
```

###  Terminal 2 — Start the Client:
``` bash
cd quic-hello
go run client.go
```


