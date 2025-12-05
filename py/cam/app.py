from flask import Flask, request, send_from_directory
import os, base64, socket
from datetime import datetime

app = Flask(__name__)
os.makedirs("captures", exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload():
    os.makedirs("captures", exist_ok=True)
    
    data = request.json["image"]
    header, encoded = data.split(",", 1)
    img = base64.b64decode(encoded)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    filepath = os.path.join("captures", filename)

    with open(filepath, "wb") as f:
        f.write(img)

    return {"status": "ok", "filename": filename}

def get_local_ip():
    """Mendapatkan IP address lokal"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == "__main__":
    local_ip = get_local_ip()
    print("\n" + "="*60)
    print("🚀 SERVER BERJALAN!")
    print("="*60)
    print(f"📱 Akses dari perangkat ini:")
    print(f"   http://localhost:8080")
    print(f"   http://127.0.0.1:8080")
    print(f"\n📱 Akses dari perangkat lain (HP/laptop teman):")
    print(f"   http://{local_ip}:8080")
    print("="*60)
    print("⚠️  PENTING: Perangkat lain harus dalam SATU WIFI/jaringan")
    print("="*60 + "\n")
    
    app.run(
        host="0.0.0.0", 
        port=8080,
        debug=False  
    )