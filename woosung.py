import streamlit as st
import requests
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="상록우성 320,322,325동 아파트 매물", layout="wide")
st.title("상록우성 320,322,325동 아파트 매물")
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
    'SRT30': '1738555142',
    'nid_inf': '72420803',
    'NID_AUT': '16/bv5OXlkXuiYowV0TeTt4b2bZFiJGVLUUjV292ce1JnlkIVuxCYm76JmtT3bc7',
    'NID_JKL': 'ZWcc4pC+dyLPB9u9tSmmWt+nC26NKSj/qcNb0kKCqCg=',
    'NID_SES': 'AAABkA8py4OWA1et+vUaDn2oDYr2BycAaO4PexjU/btQNghxYpydv5LHi+XYKkYF/0l7cp+Kpyft356yT/FLZeVBwZPCmhQ1hPGphgOftL1WDLIu/ZopZ04QKr2wUh6akNY9Pj6N/DF/XiVWAQdcD8bu8u9slEVNUK2j2NJcnW62aQr8tweuhmH57shmNiMHl8pk0+rofFH8i5XsVN9rqJ0S8R2TIHSKwoI0MdKmDemXC6PFMfRIu8/yCC1/krthRJagLb52+3Zr01sx93OKL70HOHVvtiEMSvn0CSGhEr3td+mfVsUsV+UI0g20s2YUB1DHecGd9Kd2/6wRjpQcCf5JLxebVLmiDnSf4o/A70EC/mkMpwKJm5txp0+bfCbx9fmMlYGWHzvh8cLBKxW4iydQwBghNtnZ4vHqu+rgwh49nxPwXoapl2c/a+RyEz3zjuuGmpC6H47L55ybmi9wCy647XLoHfyNuPJ4Fi78Z/Cwhm87SpeXq7J6hRDeCg0pS9ZPE8msNQPU8Ejnk3YE/HUKjro=',
    'REALESTATE': 'Mon%20Feb%2003%202025%2014%3A35%3A14%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'YHTcLisI84_PljD9o9k1THDi7Fwy1UU3Am6WZGy9Qcc=',
}
headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzg1NjA5MTQsImV4cCI6MTczODU3MTcxNH0.wbM6HqwjqUAf_5a9Z1sMCFvtD85JNaP-A4lI2zLyJaU',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/2645?ms=37.364204,127.112097,17&a=PRE:APT&b=A1&e=RETAIL&h=66&i=132',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

# Function to get data from the API for pages 1 to 10
@st.cache_data
def fetch_all_data():
    all_articles = []
    for page in range(1, 11):
        try:
            url = f'https://new.land.naver.com/api/articles/complex/2645?realEstateType=PRE%3AAPT&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&complexNo=2645&buildingNos=663947%3A1400508%3A1086427%3A866578&areaNos=2&type=list&order=rank'
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

# Fetch data for all pages
data = fetch_all_data()

if data:
    df = pd.DataFrame(data)
    # 필요한 컬럼만 선택
    df_display = df[["articleNo", "articleName", "tradeTypeName", "buildingName", "floorInfo",
                     "dealOrWarrantPrc", "areaName", "direction", "articleConfirmYmd", "articleFeatureDesc",
                     "sameAddrMaxPrc", "sameAddrMinPrc", "realtorName", "tagList"]]
    
    # "buildingName", "floorInfo", "dealOrWarrantPrc" 3개 컬럼이 동일한 행은 중복 제거
    df_display = df_display.drop_duplicates(subset=["buildingName", "floorInfo", "dealOrWarrantPrc"])

    # "매물보기" 링크 생성: articleNo를 URL 파라미터에 추가
    df_display["매물보기"] = df_display["articleNo"].apply(
        lambda x: f'<a href="https://new.land.naver.com/complexes/2645?ms=37.364204,127.112097,17&a=PRE:APT&b=A1&e=RETAIL&h=66&i=132&articleNo={x}" target="_blank">매물보기</a>'
    )
    
    # HTML 테이블 생성 (escape=False로 HTML 태그 유지)
    html_table = df_display.to_html(escape=False, index=False)
    
    st.write("### Real Estate Listings - Pages 1 to 10")
    st.markdown(html_table, unsafe_allow_html=True)
else:
    st.write("No data available.")
