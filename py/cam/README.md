# Setup
## Generate HTTPS Certificate (Linux / macOS)

Run the following command to create a self-signed certificate so the camera can be accessed over HTTPS:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

Important note:
When prompted to fill in certificate details, for the field:

```bash
Common Name (CN):
```


enter the IP address of your computer, for example:
`192.168.x.x`
This ensures the certificate matches the address used to access the server.

## Install Dependencies

```bash
pip install flask
```