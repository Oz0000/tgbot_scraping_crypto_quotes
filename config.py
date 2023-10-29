import requests
from bs4 import BeautifulSoup


def price(of_what, currency):
    headers = {
        'authority': 'www.google.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        # 'cookie': 'SID=bggsjshWf78rRSpSLfo1tU6Sd1bSJI3ark1d3W22LBpgtPzwTbKGtAPGwo95yrsO8-vkoA.; __Secure-1PSID=bggsjshWf78rRSpSLfo1tU6Sd1bSJI3ark1d3W22LBpgtPzwkUYpb6OfGZedR4LRd8ncCg.; __Secure-3PSID=bggsjshWf78rRSpSLfo1tU6Sd1bSJI3ark1d3W22LBpgtPzwU8Jg-sRAg563LBvd8VTx2Q.; HSID=AX3e1XL3IjKZwKvrm; SSID=AO3JrQeTAG_9TBIuX; APISID=TMLID-gphXBkucli/AxcH75g_PyFgEg3Xo; SAPISID=JBEC0fBOMScln7Zs/A3jp9DGkiLzPTfWuK; __Secure-1PAPISID=JBEC0fBOMScln7Zs/A3jp9DGkiLzPTfWuK; __Secure-3PAPISID=JBEC0fBOMScln7Zs/A3jp9DGkiLzPTfWuK; SEARCH_SAMESITE=CgQIupkB; AEC=Ackid1QHHhbGoHGGPB8Gfy8x7sShbRGk3oOQJ1SsJEv2K_Lok9AVpcu3iMQ; OGPC=19022552-2:; OGP=-19022552:; NID=511=KLnzAm5UtCiuvNsKpZhTttZKPHZ--lZHOsqHur8c-cNwtmwxxhkKB9loq7h6Q526bQgez-ccGxvZkZTZytn-l7807uMDD1UvNVQPuO5nU4Mpd4Ez_rTe0tnrN_QCcEVNOabUiAT9FwHr9FdTpjNsu3DKufyWwc3Qgz8jgxhW4qkgqIKUR0sWfYF0n52Uhuo9CGCXoJzijmP0Lc5L3mlWLu1w3lv8bXtZnkKloIBCfbNL7s5ziszUn-1K3EvQ8QhEgybpOUgYKT6JgO7gwsc; DV=MztSadU5U5dasL45xLkJ8-RV0wlft5hw4P5MyRCtAwAAAIAGwtOLQBGLuwAAAICIXxvmwpdnMwAAABzujBTNWAdZDgAAAA; __Secure-1PSIDTS=sidts-CjEBNiGH7h4o-ulCgyXpUy0pgmc4DPAn-hUlbvADyd46POGXumsAgT2bvy_xaYN3aZcwEAA; __Secure-3PSIDTS=sidts-CjEBNiGH7h4o-ulCgyXpUy0pgmc4DPAn-hUlbvADyd46POGXumsAgT2bvy_xaYN3aZcwEAA; 1P_JAR=2023-10-28-11; SIDCC=ACA-OxNHMv0Pj0_o9CiyPdtrJeI0p_mSV9oUHcZjQUOfy73m2L2gjwZ45chXDhyC3f96V-H9Ww; __Secure-1PSIDCC=ACA-OxM9KAwqN6NwC5d35nEMcjZMHObmzLk7Gq_ltHSJOijtERhL7224Z4A8k2ILsDxjcGkGSA; __Secure-3PSIDCC=ACA-OxNNdphBnCrjiXQ_R9OKmF5u0k5JUfG7u6dKmzqe3d6dBZdnj3ne2lMHeSIM6a23fF5Cla8',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"117.0.5938.149"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5938.149", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.149"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"5.10.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-client-data': 'CIe2yQEIo7bJAQipncoBCPDoygEIlqHLAQia/swBCIegzQEI3L3NAQi5ys0BCKjYzQEI4trNAQjm2s0BCPnA1BUY9MnNAQ==',
    }

    response = requests.get(url=f'https://www.google.com/search?q=price+of+{of_what}+{currency}', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    answer = []
    try:
        price1 = bs.find('div', class_='GyAeWb').find('div', id='search').find('div', class_='v7W49e').find('div', class_='ULSxyf').find('div', class_='MjjYud').find('div', class_='wDYxhc NFQFxe').find('div', class_='obcontainer').find('div', lang='ru-BY').find('div', class_='Ww4FFb vt6azd').find('div', class_='bk7x').find('span', class_='pclqee')
        for x1 in price1:
            answer.append(x1.text)
    except AttributeError:
        pass

    try:
        price2 = bs.find('div', class_='GyAeWb').find('div', id='search').find('div', class_='v7W49e').find('div', class_='ULSxyf').find('div', class_='MjjYud').find_all('b')

        for x2 in price2:
            upk = ' '
            for c in x2.text:
                if c.isdigit() or c in ['.', ',']:
                    upk += c
            answer.append(upk)
    except AttributeError:
        pass

    st_answer = f'{str(max(answer))} {currency}'
    return st_answer

