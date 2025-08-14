# Contributing to IPL API

Thanks for your interest in contributing! This guide explains how to propose changes and get them merged.

## Code of Conduct

Be respectful and inclusive. Harassment and disrespectful behavior aren’t tolerated.

## Getting Started

1. Fork the repository and clone your fork
2. Create a feature branch from `main`
3. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
4. Ensure `ipl_clean.csv` is present in the repo root if you plan to run the API

## Development Workflow

- Keep changes focused and incremental
- Prefer small PRs with clear scope
- Add/adjust docs when behavior changes

## Commit Style

- Use concise, descriptive messages
- Examples:
  - `docs: expand README with setup steps`
  - `feat(api): add /api/matches/venue endpoint`
  - `fix: handle NaN in /api/matches response`

## Testing the API

Run locally with:
```bash
uvicorn main:app --reload
```
Open docs at:
```bash
$BROWSER http://localhost:8000/docs
```

## Pull Requests

- Rebase on latest `main`
- Ensure the app starts and endpoints work
- Link related issues if any
- Provide a brief, helpful description

## Issues

- Use issues for bugs and feature requests
- Include reproduction steps and environment details

## License

By contributing, you agree your contributions are licensed under the repo’s existing license.
