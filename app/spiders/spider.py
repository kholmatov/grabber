import logging
import validators
from http import HTTPStatus
from aiohttp import ClientSession

logger = logging.getLogger(__name__)


class Spider:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) "
                      "Gecko/20100101 Firefox/70.0",
    }

    async def make_request(self, url: str, allow_url: str) -> dict:
        status = 400
        try:
            if not self.validation(url, allow_url):
                raise Exception(f'Invalid url: {url}')
            async with ClientSession() as session:
                async with session.get(url, headers=self.headers) as resp:
                    if resp.status != HTTPStatus.OK:
                        status = resp.status
                        raise Exception(f'Response code: {resp.status}')
                    return (await resp.read(), resp.status)
        except Exception as e:
            logger.error("Data from %s is not received. %s", url, e)
            return (False, status)

    def validation(self, url: str, allow_url: str) -> bool:
        return True if validators.url(url) and allow_url in url else False
