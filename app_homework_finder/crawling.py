# find.py
import requests
from bs4 import BeautifulSoup as bs
import time
class user_data:
    def __init__(self):
        self.name=''
        self.url=''

def crawling(user_name, user_password,user_univ,user_homework):
    start = time.time()
    """
    #결과물을 json 으로 받아보고싶을때
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    """
    LOGIN_INFO = {'username': str(user_name), 'password': str(user_password)}
    data = []
    # Session 생성, with 구문 안에서 유지

    with requests.session() as s:

        URL = 'https://class.likelion.org/accounts/login/?next=/board/notices/'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        headers = {
            'User-Agent':
            user_agent,
            'Referer':
            'https://class.likelion.org/accounts/login/?next=/assignments/'+str(user_homework)+'/submissions'
        }

        first_page = s.get(URL)
        html = first_page.text
        soup = bs(html, 'html.parser')
        csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'
                                })  
        # input태그 중에서 name이 csrfmiddleware인 것을 찾습니다.
        #print(csrf['value']) # 위에서 찾은 태그의 value를 가져옵니다.

        # 이제 LOGIN_INFO에 csrf값을 넣어줍시다.
        # (p.s.)Python3에서 두 dict를 합치는 방법은 {**dict1, **dict2} 으로 dict들을 unpacking하는 것입니다.
        LOGIN_INFO = {**LOGIN_INFO, **{'csrfmiddlewaretoken': csrf['value']}}
        #print(LOGIN_INFO)

        #Login
        res = s.post(
            URL,
            headers=headers,
            data=LOGIN_INFO,
        )
        print(res.status_code) 
        if res.status_code != 200:
            return 0

        start_page_num = 1
        end_page_num = 1000 
        #end_page_num = 3
        for cur_page_num in range(start_page_num, end_page_num):
            boardnum = 'https://class.likelion.org/assignments/'+str(user_homework)+'/submissions?page=' + str(
                cur_page_num)
            #boardnum = 'https://class.likelion.org/board/notices/'
            post_one = s.get(boardnum)
            #print(post_one.text)
            soup = bs(post_one.text, 'html.parser')  # Soup으로 만들어 줍시다.
            #print(soup)
            tot = soup.select(
                    'body > div.page-container > div.page-content-wrapper.PageContainer > div > div > div.row.w-100 > div > div > a'
                )
            if len(tot) != 9:
                for q in range(len(tot)):
                    adrs2 = tot[q]['href']
                    ret = 'https://class.likelion.org' + adrs2

                    name_and_univ = soup.select('body > div.page-container > div.page-content-wrapper.PageContainer > div > div > div.row.w-100 > div > div > a > div > div.d-flex.align-items-center')[q].text
                    user_info = name_and_univ.split('\n')
                    name = user_info[1]
                    univ = user_info[3]
                    if univ == str(user_univ):
                        tmp_data = user_data()
                        tmp_data.name = name
                        tmp_data.url = ret
                        data.append(tmp_data)
                break
            for i in range(9):
                """
                adrs = soup.select(
                    'body > div.page-container > div.page-content-wrapper.PageContainer > div > div > div.row > div> div > a'
                )[i]['href']
                """
                
                adrs2 = tot[i]['href']
                ret = 'https://class.likelion.org' + adrs2

                name_and_univ = soup.select('body > div.page-container > div.page-content-wrapper.PageContainer > div > div > div.row.w-100 > div > div > a > div > div.d-flex.align-items-center')[i].text
                user_info = name_and_univ.split('\n')
                name = user_info[1]
                univ = user_info[3]
                if univ == str(user_univ):
                    tmp_data = user_data()
                    tmp_data.name = name
                    tmp_data.url = ret
                    data.append(tmp_data)
                
        """
        for ele in reversed(data):
            print(ele.name,ele.url)
        print("total submit : ", len(data))
        print("end_page : ", cur_page_num)
        print("total elapsed time : " , time.time() - start , "(sec)")
        """

        """
        data = {}
        for title in my_titles:
            data[title.text] = title.get('href')

        with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
            json.dump(data, json_file)
        """
    return data
