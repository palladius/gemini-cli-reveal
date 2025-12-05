update:
    uv run scripts/generate_slides.py

serve:
    python3 -m http.server 8010


run: update serve
