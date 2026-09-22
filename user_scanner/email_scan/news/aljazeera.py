import httpx
import json
import base64
from user_scanner.core.result import Result


async def _check(email: str) -> Result:
    show_url = "https://aljazeera.com"
    url = "https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri"

    params = {
        'key': base64.b64decode(b"QUl6YVN5RFd6OVRadlBzY043cUZkRzZ6MWJ2TGg5OGVYVkJTVVBN").decode("ascii")
    }

    payload = {
        "identifier": email,
        "continueUri": "https://www.aljazeera.com/account/sign-up"
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
        'Content-Type': "application/json",
        'Origin': "https://www.aljazeera.com",
        'Referer': "https://www.aljazeera.com/",
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(url, params=params, content=json.dumps(payload), headers=headers)
            data = response.json()

            is_registered = data.get("registered")

            if is_registered is True:
                return Result.taken(url=show_url)

            if is_registered is False:
                return Result.available(url=show_url)

            return Result.error("Unexpected response body, report it on github")

    except httpx.ConnectTimeout:
        return Result.error("Connection timed out while reaching Al Jazeera Auth")
    except httpx.ReadTimeout:
        return Result.error("Server took too long to respond (Read Timeout)")
    except Exception as e:
        return Result.error(e)


async def validate_aljazeera(email: str) -> Result:
    return await _check(email)
