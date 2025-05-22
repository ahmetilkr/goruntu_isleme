from pymavlink import mavutil

# PX4'e bağlan
master = mavutil.mavlink_connection("udp:127.0.0.1:14550")
print("Bağlantı bekleniyor...")
master.wait_heartbeat()
print("✅ MAVLink bağlantısı başarılı!")

# Test mesajı al
msg = master.recv_match(blocking=True)
print(msg)
