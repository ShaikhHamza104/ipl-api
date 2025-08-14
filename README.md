
<div align="center">

# 🏏 IPL API – FastAPI Service for Cricket Data

![IPL Logo](https://upload.wikimedia.org/wikipedia/en/4/41/Indian_Premier_League_Logo.png)

📡 **Live API**: [ipl-api-y5az.onrender.com](https://ipl-api-y5az.onrender.com)  
📄 **API Docs**: [ipl-api-y5az.onrender.com/docs](https://ipl-api-y5az.onrender.com/docs)  

Serve **Indian Premier League** (IPL) match data through a simple and fast REST API, powered by **FastAPI** & **Pandas**.

</div>

---

## 📋 Overview

This project provides:
- 🚀 **FastAPI service** serving IPL match and delivery data from CSV files  
- 📊 **Jupyter Notebook** for quick data cleaning and EDA (`data-cleaning.ipynb`)  
- 📂 **Cleaned datasets** ready for dashboards or apps  

Perfect for:
- Building cricket dashboards 🖥️  
- Running quick data analysis 📈  
- Powering a cricket stats frontend ⚡  

---

## 📂 Project Structure

| File / Folder      | Description |
|--------------------|-------------|
| `ipl_clean.csv`    | Cleaned IPL dataset used by the API |
| `matches.csv`      | Match data |
| `requirements.txt` | Python dependencies |
| `main.py`          | FastAPI application |
| `README.md`        | Project documentation |
| `LICENSE`          | MIT License |

---

## ⚡ Quickstart

1️⃣ **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the API**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4️⃣ **Open API Docs**
```bash
http://localhost:8000/docs
```

---

## 🌐 Live Deployment

- **Base URL:** [https://ipl-api-y5az.onrender.com](https://ipl-api-y5az.onrender.com)  
- **Docs:** [https://ipl-api-y5az.onrender.com/docs](https://ipl-api-y5az.onrender.com/docs)

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Service status |
| `GET` | `/api/matches/id/{match_id}` | Match by ID |
| `GET` | `/api/matches/{year}?limit=5` | Matches by season |
| `GET` | `/api/allteams` | List of unique teams |
| `GET` | `/api/matches/venue/{venue_name}` | Matches at a specific venue |

---

## 📌 Example Requests

```bash
curl https://ipl-api-y5az.onrender.com/
curl https://ipl-api-y5az.onrender.com/api/matches/id/1
curl "https://ipl-api-y5az.onrender.com/api/matches/2016?limit=5"
curl https://ipl-api-y5az.onrender.com/api/allteams
curl "https://ipl-api-y5az.onrender.com/api/matches/venue/eden%20gardens"
```

---

## 🗒️ Notes on Data

- API expects `ipl_clean.csv` in the root directory  
- All team and venue names are normalized to lowercase for filtering consistency  

---

## 🛠 Development

- Python **3.10+** recommended  
- Stack: **FastAPI**, **Uvicorn**, **Pandas**  
- Install and run:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🤝 Contributing

Contributions are welcome!  
Please check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

<div align="center">

⚡ Built with ❤️ by Hamza Shaikh

</div>
