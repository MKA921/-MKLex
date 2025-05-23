## How to Run

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # (macOS/Linux)
   # or
   venv\Scripts\activate  # (Windows)
   ```

2. Run the main script:

   ```bash
   python src/main.py
   ```

3. Run tests with pytest:

   ```bash
   pytest tests/
   ```
   ## Committing and Pushing Changes

```bash
git add .
git commit -m "Setup project environment, add main script and test, update README"
git push origin main
```