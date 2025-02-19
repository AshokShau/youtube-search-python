import os

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2.0
        self.transport = httpx.HTTPTransport()

        http_proxy = os.environ.get("HTTP_PROXY")
        if http_proxy:
            self.transport = httpx.Proxy(http_proxy)

        https_proxy = os.environ.get("HTTPS_PROXY")
        if https_proxy:
            self.transport = httpx.Proxy(https_proxy)
        self.client = httpx.Client(transport=self.transport, timeout=self.timeout)

    def syncPostRequest(self) -> httpx.Response:
        return self.client.post(
            self.url,
            headers={"User-Agent": userAgent},
            json=self.data
        )

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data
            )
            return response

    def syncGetRequest(self) -> httpx.Response:
        cookies = {'CONSENT': 'YES+1'}
        return self.client.get(
            self.url,
            headers={"User-Agent": userAgent},
            cookies=cookies
        )

    async def asyncGetRequest(self) -> httpx.Response:
        cookies = {'CONSENT': 'YES+1'}
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                self.url,
                headers={"User-Agent": userAgent},
                cookies=cookies
            )
            return response

    def __del__(self):
        # Close the client when the instance is destroyed
        self.client.close()
