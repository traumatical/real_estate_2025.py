import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components

# Streamlit page setup
st.set_page_config(page_title="매물", layout="wide")
st.markdown("This page fetches and displays real estate listings from pages 1 to 10 using the Naver Real Estate API.")

# Define the cookies and headers as provided
cookies = {
    'NNB': 'NQEXHGD2XU2GM',
    'ASID': 'c05e26390000018fcc25a48000000055',
    '_fwb': '131eAsIpFO373ytQwpbOSZE.1725426689256',
    'wcs_bt': '4f99b5681ce60:1732856781',
    'nstore_session': 'u3T3vjoEohJRn3IPXMPnBOT0',
    'nstore_pagesession': 'i2ZBXdqqBM3vjwsLd78-421275',
    'NAC': 'spW0BQghgTym',
    '_ga': 'GA1.1.538653697.1737098822',
    '_gcl_au': '1.1.283869221.1737098822',
    'naverfinancial_CID': 'b7aaf02b187c4281dcc59d6adedd1ff9',
    '_fbp': 'fb.1.1737098822146.642750228776791210',
    '_tt_enable_cookie': '1',
    '_ttp': 'omIBxgLIu0Nujo4hgOBhfN9dWCY.tt.1',
    '_ga_Q7G1QTKPGB': 'GS1.1.1737098821.1.1.1737098970.0.0.0',
    'recent_card_list': '10108',
    '_fwb': '236ImmkFa7R6pqDLu5TYI8N.1738395390547',
    'NACT': '1',
    'SRT30': '1738630427',
    'SRT5': '1738630427',
    'REALESTATE': 'Tue%20Feb%2004%202025%2009%3A55%3A50%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'ocNn2u1qtaMDGvPDh5asxMXQEMXxt6dXKb-3Ab5Dv0M=',
}
headers = {
 'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzg2MzA1NTAsImV4cCI6MTczODY0MTM1MH0.SbEVYjPglNUotHGDTGFqa41Kukj1niYtfayn-UnXPj8',
    # 'cookie': 'NNB=NQEXHGD2XU2GM; ASID=c05e26390000018fcc25a48000000055; _fwb=131eAsIpFO373ytQwpbOSZE.1725426689256; wcs_bt=4f99b5681ce60:1732856781; nstore_session=u3T3vjoEohJRn3IPXMPnBOT0; nstore_pagesession=i2ZBXdqqBM3vjwsLd78-421275; NAC=spW0BQghgTym; _ga=GA1.1.538653697.1737098822; _gcl_au=1.1.283869221.1737098822; naverfinancial_CID=b7aaf02b187c4281dcc59d6adedd1ff9; _fbp=fb.1.1737098822146.642750228776791210; _tt_enable_cookie=1; _ttp=omIBxgLIu0Nujo4hgOBhfN9dWCY.tt.1; _ga_Q7G1QTKPGB=GS1.1.1737098821.1.1.1737098970.0.0.0; recent_card_list=10108; _fwb=236ImmkFa7R6pqDLu5TYI8N.1738395390547; NACT=1; SRT30=1738630427; SRT5=1738630427; REALESTATE=Tue%20Feb%2004%202025%2009%3A55%3A50%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=ocNn2u1qtaMDGvPDh5asxMXQEMXxt6dXKb-3Ab5Dv0M=',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/2645?ms=37.3642744,127.1106445,19&a=PRE:APT&b=A1&e=RETAIL&h=66&i=132',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

@st.cache_data
def fetch_all_data():
    all_articles = []
    for page in range(1, 11):
        try:
            url = f'https://new.land.naver.com/api/articles/complex/2645?realEstateType=PRE%3AAPT&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=2&complexNo=2645&buildingNos=&areaNos=1%3A7%3A2%3A3%3A4&type=list&order=rank'
            response = requests.get(url, cookies=cookies, headers=headers)
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articleList", [])
                all_articles.extend(articles)
            else:
                st.warning(f"Failed to retrieve data for page {page}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
        except ValueError:
            st.error(f"Non-JSON response for page {page}.")
    return all_articles

data = fetch_all_data()

if data:
    df = pd.DataFrame(data)
    # 필요한 컬럼만 선택
    df_display = df[["articleConfirmYmd", "articleNo", "articleName", "tradeTypeName", "buildingName", "floorInfo",
                     "dealOrWarrantPrc", "areaName", "direction", "articleFeatureDesc",
                     "sameAddrMaxPrc", "sameAddrMinPrc", "realtorName", "tagList"]]
    
    # 중복 제거: "buildingName", "floorInfo", "dealOrWarrantPrc" 동일한 행 제거
    df_display = df_display.drop_duplicates(subset=["buildingName", "floorInfo", "dealOrWarrantPrc"])
    
    # 기본 정렬: 매물날짜 기준 내림차순 (최신 날짜가 가장 위)
    df_display = df_display.sort_values(by="articleConfirmYmd", ascending=False)
    
    # "매물보기" 링크 생성 (인라인 스타일: 한 줄, 폰트 크기 13px)
    df_display["매물보기"] = df_display["articleNo"].apply(
        lambda x: f'<a href="https://new.land.naver.com/complexes/2645?ms=37.364204,127.112097,17&a=PRE:APT&b=A1&e=RETAIL&h=66&i=132&articleNo={x}" target="_blank" style="white-space: nowrap; font-size: 13px;">매물보기</a>'
    )
    
    # 컬럼명 한글로 변경
    rename_dict = {
        "articleConfirmYmd": "매물날짜",
        "articleNo": "매물번호",
        "articleName": "아파트명",
        "tradeTypeName": "거래분류",
        "buildingName": "동수",
        "floorInfo": "층수",
        "dealOrWarrantPrc": "매매가격",
        "areaName": "평수",
        "direction": "방향",
        "articleFeatureDesc": "특징",
        "sameAddrMaxPrc": "매매변동가격(max)",
        "sameAddrMinPrc": "매매변동가격(min)",
        "realtorName": "중개소",
        "tagList": "태그"
    }
    df_display = df_display.rename(columns=rename_dict)
    
    # 불필요한 컬럼 삭제: 매물번호, 아파트명, 거래분류, 평수
    df_display = df_display.drop(columns=["매물번호", "아파트명", "거래분류", "평수"])
    
    # DataFrame을 HTML 테이블로 변환
    html_table = df_display.to_html(escape=False, index=False)
    
    # CSS 스타일:
    # - 전체 테이블 너비 100%
    # - 굴림체, 데이터 셀 글씨 크기 13px, 헤더 글씨 크기는 13pt로 설정
    # - 배경은 검은색, 글씨는 흰색, 셀 패딩 2px, 모든 셀에 white-space: nowrap; 적용
    # - 매물날짜(1번째), 동수(3번째), 층수(4번째), 매매가격(5번째)는 굵게 처리
    table_style = """
    <style>
        table {
            width: 100%;
        }
        table, th, td {
            font-family: '굴림체', Gulim, sans-serif;
            font-size: 13px;
            padding: 2px;
            background-color: white;
            color: black;
            border: 1px solid black;
            white-space: nowrap;
        }
        th {
            text-align: center;
            font-size: 13pt;
        }
        /* 매물날짜(1번째), 동수(3번째), 층수(4번째), 매매가격(5번째) 열 굵게 처리 */
        th:nth-child(1), th:nth-child(3), th:nth-child(4), th:nth-child(5),
        td:nth-child(1), td:nth-child(3), td:nth-child(4), td:nth-child(5) {
            font-weight: bold;
        }
        a {
            color: #00bfff;
            text-decoration: none;
        }
    </style>
    """
    
    components.html(table_style + html_table, height=800, scrolling=True)
else:
    st.write("No data available.")
