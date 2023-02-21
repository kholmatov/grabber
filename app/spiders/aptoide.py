from .spider import Spider
from bs4 import BeautifulSoup
from collections import defaultdict


class Aptoide:

    async def get_info(self, soup: BeautifulSoup) -> dict:
        data = defaultdict(str)
        class_info = "app-informations__DetailsItem-sc-1wisk8p-14 eNBArA"
        for row in soup.find_all('div', class_=class_info):
            spans = row.find_all('span')
            if len(spans) > 1:
                if 'Downloads' in spans[1].text:
                    data['downloads'] = spans[0].text
                elif 'Size' in spans[1].text:
                    data['size'] = spans[0].text
                elif 'Android Version' in spans[1].text:
                    data['version'] = spans[0].text

        class_desc = "details__DescriptionParagraphs-rnz8ql-10 QxOrQ"
        desc = soup.find("div", class_=class_desc)

        if desc:
            data['description'] = desc.text

        return data

    async def get_name(self, soup: BeautifulSoup, item: str) -> str:
        value = soup.find('meta', itemprop=item)
        if value:
            return value['content'].strip()
        return ''

    async def get(self, url: str) -> dict:
        result = {}
        spider = Spider()
        response, status = await spider.make_request(url, 'aptoide.com')
        if response:
            soup = BeautifulSoup(response, 'html.parser')
            result['name'] = await self.get_name(soup, 'name')
            data = await self.get_info(soup)
            result['version'] = data.get('version', '')
            result['downloads'] = data.get('downloads', '')
            result['description'] = data.get('description', '')

        return (result, status)
