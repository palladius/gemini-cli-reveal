update:
    @echo "Site is now client-side rendered. No build step needed."

serve:
    python3 -m http.server 8010

run: update serve
