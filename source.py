import socket
from hashlib import sha256
from Crypto.Util.number import bytes_to_long
from ecdsa import SigningKey, SECP256k1

def brute_force_signature(msg, confidence):
    G = SECP256k1.generator
    q = G.order()

    for d in range(1, q):
        privkey = SigningKey.from_secret_exponent(d, curve=SECP256k1)
        pubkey = privkey.get_verifying_key()

        confidence_convert = int((confidence / 100) * 256)
        hash_msg = sha256(msg.encode()).digest()
        nonce_input = bytes_to_long(privkey.to_string()) + bytes_to_long(hash_msg)
        nonce = int.from_bytes(sha256(bytes(nonce_input)).digest(), 'big') % (1 << confidence_convert)
        signature = privkey.sign(bytes_to_long(hash_msg), nonce)

        if pubkey.verify(signature, hash_msg):
            return {"pubkey": pubkey.to_string().hex(), "r": hex(signature.r), "s": hex(signature.s)}

    return None

# Thông tin máy chủ
host = "14.225.211.39"
port = 13375

# Kết nối tới máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Nhận dữ liệu từ máy chủ
data = client_socket.recv(1024).decode()
print(data)

# Tìm public key và signature đúng
msg = "Student: h114mx001, GPA: 4.0"
confidence = 100

result = brute_force_signature(msg, confidence)
if result:
    # Gửi public key và signature đúng tới máy chủ
    client_socket.send(result["pubkey"].encode() + b"\n")
    client_socket.send(result["r"].encode() + b"\n")
    client_socket.send(result["s"].encode() + b"\n")

    # Nhận kết quả từ máy chủ
    response = client_socket.recv(1024).decode()
    print(response)
else:
    print("Không tìm thấy public key và signature đúng.")

# Đóng kết nối
client_socket.close()