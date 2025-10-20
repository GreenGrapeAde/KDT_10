import pandas as pd

## 문제 1] 아래 데이터를 시리즈 객체로 저장해 주세요.
jumsu = [100, 200, 300]

dataSR1 = pd.Series(jumsu, name='점수')                          ## 인덱스 지정
print(dataSR1)

## 문제 2] 아래 데이터를 시리즈 객체로 저장해 주세요.
idx = ['철수', '영희', '아름']
dataSR2 = pd.Series(jumsu, index=idx, name="점수")
print(dataSR2)

## 문제 3] 아래 데이터를 시리즈 객체로 저장해 주세요. 저장 후 인덱스 속성과 형태 속성을 출력해 주세요.
price = [73000, 356000, 367000, 68600, 34150]
index = ["삼성전자", "셀트리온", "카카오", "삼성전자우", "현대바이오"]
dataSR3 = pd.Series(price, index=index, name="종가")

print(dataSR3)
print(f"\n[인덱스]: {dataSR3.index}")
print(f"[형태]: {dataSR3.shape}")

## 문제 4] 아래 파일을 읽어서 DataFrame으로 저장하는 함수를 적어주세요.
def to_dataframe(xlsx, csv, json):
    df1 = pd.read_excel(xlsx)
    df2 = pd.read_csv(csv)
    df3 = pd.read_json(json)

## 문제 5] 아래 파일을 읽어서 DataFrame으로 저장해 주세요.
DATA_FILE = r".\EX_PANDAS\D1020\member.json"

member = pd.read_json(DATA_FILE)
print(member)

## 문제 6] 아래 데이터를 저장 후 조건을 만족하는 코드를 작성하세요.
data = [["2차전지(생산)", "SK이노베이션", 10.19, 1.29], 
        ["해운", "팬오션", 21.23, 0.95], 
        ["시스템반도체", "티엘아이", 35.97, 1.12], 
        ["해운", "HMM", 21.52, 3.20], 
        ["시스템반도체", "아이에이", 37.32, 3.55], 
        ["2차전지(생산)", "LG화학", 83.06, 3.75]]

columns = ["테마", "종목명", "PER", "PBR"]

## 1) DataFrame으로 저장
dataDF6 = pd.DataFrame(data, columns=columns)

## 2) 행인덱스를 SK, PO, TL, HMM, IA, LG로 설정
rows = ['SK', 'PO', 'TL', 'HMM', 'IA', 'LG']
dataDF6 = pd.DataFrame(data, index=rows, columns=columns)

## 3) 데이터 전체 출력
print(dataDF6)

## 4) 행 인덱스 속성만 출력
print(dataDF6.index)

## 5) 형태 및 차원 정보 출력
print(f"형태: {dataDF6.shape}, 차원: {dataDF6.ndim}")

## 6) 컬럼 속성 출력
print(f"컬럼 속성: {dataDF6.columns}")

## 7) 실제 메모리에 저장된 데이터만 출력
print(f"데이터: \n{dataDF6.values}")