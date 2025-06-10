# Cloudflare Demo Flask App

This Flask app demonstrates Cloudflare Advanced Application Security:
- Web Application Firewall (WAF)
- API Shield
- Bot Management
- Zero Trust Access

## Routes
- `/` – Public homepage
- `/admin` – Should be protected by Cloudflare Zero Trust
- `/api/data` – Used for API Shield + WAF testing
- `/login` – Target for bot protection and brute force

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```