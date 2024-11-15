install libs

```bash
uv sync
```

setting api key
```bash
echo "xxx" > .OPEN_AI_API_KEY
```

```bash
$ uv run python3 main.py
SELECT "Name"
FROM "Artist"
WHERE "Name" LIKE 'A%'
ORDER BY "Name"
LIMIT 5;

# or
$ source .venv/bin/activate
$ python3 main.py
```
