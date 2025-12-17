class Config:
    BASE_URL = "https://ru.yougile.com"
    API_URL = f"{BASE_URL}/api-v2"

    API_TOKEN = "p5yhnNlsWopGncHtO20ZbzEw5-+9adB+Ai86owI-gwlZ6-qlchzktWvu7jdafVvF"

    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }