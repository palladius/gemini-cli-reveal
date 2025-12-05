update:
    @echo "Site is now client-side rendered. No build step needed."

serve:
    python3 -m http.server 8010

run: update serve

# Configure GitHub Pages to deploy from 'main' branch root
init-repo:
    @echo "Configuring GitHub Pages to serve from main branch..."
    # Try PUT (update) first, then POST (create) if it fails
    gh api repos/:owner/:repo/pages -X PUT -F "source[branch]=main" -F "source[path]=/" || \
    gh api repos/:owner/:repo/pages -X POST -F "source[branch]=main" -F "source[path]=/"
    @echo "GitHub Pages configured!"

open:
    open https://palladius.github.io/gemini-cli-reveal/
