# 🧠 Bussatthi Backend – FastAPI Powered Real-Time Bus Tracking Server

The **Bussatthi Backend** is the core of the **Bussatthi ecosystem**, powering both the **Passenger App** and the **Driver App**.  
Built with **Python (FastAPI)** and **AWS RDS (MySQL)**, it manages **real-time bus tracking**, **user authentication**, and **live location synchronization** between drivers and passengers — ensuring no one ever misses a bus again. 🚍⚡


## 🎥 Working Demo

📺 **Watch the full demo video here:**  
👉 [Passenger App Video](https://drive.google.com/file/d/1S1yZbXOTsgJozRmgPgEwN81wn5ncznyr/view?usp=drive_link) 
👉 [Driver App Video](https://drive.google.com/file/d/1J7KAkLiCvW3hzq1BGVQNuUnS0GiTBYcT/view?usp=drive_link) 

## 🔗 Related Repositories

- 📱 **Passenger App:** [Bussatthi App](https://github.com/karan3613/BusSaathiApp)  
- 🚍 **Driver App:** [Bussatthi Driver App](https://github.com/karan3613/BusSaathi-DriverApp)

## 🚀 Overview

This backend acts as the communication bridge between:
- 🚌 **Driver App** → Sends bus location every 3 seconds.  
- 📱 **Passenger App** → Fetches nearby and available buses in real-time.  
- 💾 **Database (AWS RDS MySQL)** → Stores driver, bus, and user data.

With efficient API design, secure authentication, and optimized queries, Bussatthi delivers **high-speed performance** and **reliable live tracking** for thousands of users simultaneously.

## 🧩 Key Features

- ⚡ **FastAPI Framework** – High-performance Python backend with async capabilities.  
- 🗺️ **Real-Time Location Handling** – Receives driver locations every 3 seconds.  
- 🧭 **Nearby Bus Finder** – Fetches buses close to a user’s source & destination.  
- 🔐 **JWT Authentication** – Secure login for drivers and passengers.  
- 🧑‍💼 **Profile Management** – Handles driver, conductor, and bus details.  
- 🗃️ **AWS RDS (MySQL)** – Reliable cloud database for scalable data storage.  
- 🌐 **RESTful APIs** – Clean endpoints for fast integration with mobile apps.  
- 🧠 **Optimized Architecture** – Ensures low-latency updates and fault tolerance.


## 🛠️ Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Backend Framework** | FastAPI (Python 3.10+) |
| **Database** | AWS RDS (MySQL) |
| **Authentication** | JWT (PyJWT) |
| **ORM / DB Management** | SQLAlchemy + Alembic |
| **Hosting / Deployment** | AWS EC2 / AWS Lambda *(configurable)* |
| **Environment Management** | python-dotenv |
| **Testing** | Pytest |


## 📂 Project Structure

