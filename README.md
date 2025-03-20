Secure Messaging App

📌 Overview
The **Secure Messaging App** is a **real-time, end-to-end encrypted chat application** that allows users to send secure messages via **WebSockets**. Messages are **encrypted before sending** and **decrypted on reception**, ensuring privacy.  

---

## **🛠 Features**
✅ **End-to-End Encryption (AES Encryption)** – Messages are encrypted client-side before transmission.  
✅ **Real-Time Messaging** – Powered by **Flask-SocketIO & WebSockets** for fast, instant chat.  
✅ **Secure Communication** – The server **never sees plain-text messages** due to encryption.  
✅ **Multi-User Support** – Open multiple tabs to chat in real-time.  

---

## **🔧 Technologies Used**
- **Frontend:** HTML, JavaScript (CryptoJS for AES encryption)
- **Backend:** Flask, Flask-SocketIO
- **Real-Time:** WebSockets via Flask-SocketIO
- **Deployment:** Render
- **Encryption:** AES (Advanced Encryption Standard)

---

## **🚀 Installation & Running Locally**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/MikeAndersn/secure-messaging-app.git
cd secure-messaging-app
