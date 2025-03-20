import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey!"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet", logger=True, engineio_logger=True)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    # print("✅ A user connected!")
    pass

@socketio.on("disconnect")
def handle_disconnect():
    # print("❌ A user disconnected!")
    pass

@socketio.on("message")
def handle_message(msg):
    # print(f"🔹 Received Encrypted Message: {msg}")
    message_to_send = str(msg)
    # print(f"📩 Emitting Encrytped Message to Clients: {message_to_send}")  # Debugging print
    socketio.emit("message", message_to_send, namespace="/")


    

if __name__ == "__main__":
    # print("🚀 Flask WebSocket Server is Starting...")
    port = int(os.environ.get("PORT", 5001))
    socketio.run(app, host = "0.0.0.0", port = 5001, debug = True)

