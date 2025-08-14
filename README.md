<div align="center">

# 🏏 IPL API

Serve Indian Premier League (IPL) data via a simple FastAPI service and explore it with a handy notebook.

</div>

## Overview

This repository contains:

- A FastAPI service that exposes IPL match data from CSV files.
- A Jupyter Notebook for data cleaning and quick exploration (`data-cleaning.ipynb`).
- CSV datasets (matches, deliveries, merged/cleaned).

Use it to build dashboards, perform EDA, or power a frontend app.

## Project Structure

- `data-cleaning.ipynb` – cleaning and quick queries over the dataset
- `ipl_clean.csv` – cleaned IPL data (source for the API)
- `matches.csv`, `deliveries.csv`, `merged_data.csv` – raw data
- `README.md` – you are here
- `requirements.txt` – Python dependencies
- `LICENSE` – repository license

## Quickstart

1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Run the API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4) Open the docs

```bash
$BROWSER http://localhost:8000/docs
```

## API Endpoints

The following endpoints are commonly available in this project setup. Your local `main.py` may include a subset or additional routes.

- `GET /` – service status
- `GET /api/matches` – all matches summary (NaN-safe serialization)
- `GET /api/matches/{limit}` – first N unique matches
- `GET /api/matches/{match_id}` – deliveries/details for a specific match
- `GET /api/season/{year}/{limit}` – matches for a season
- `GET /api/matches/team/{team_name}/{limit}` – matches involving a team
- `GET /api/matches/venue/{venue_name}/{limit}` – matches at a venue

Example requests:

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/matches/10
curl http://localhost:8000/api/season/2016/5
curl "http://localhost:8000/api/matches/team/royal%20challengers%20bangalore/5"
```

## Notes on Data

- The API expects `ipl_clean.csv` in the project root; ensure the file exists before starting the server.
- To avoid JSON serialization errors, NaN values are converted to `null` (or safe defaults) before responses are returned.
- Some endpoints normalize strings (e.g., team names) to lowercase for consistent filtering.

## Notebook

Open `data-cleaning.ipynb` to inspect, clean, or extend the dataset. You can add new features (e.g., team name standardization, imputation, or venue-level summaries) and export a refreshed `ipl_clean.csv` for the API to consume.

## Development

- Python >= 3.10 recommended
- FastAPI + Uvicorn runtime
- Pandas/Numpy for data ops

Suggested commands:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, including branching, commit style, and how to open a Pull Request.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
