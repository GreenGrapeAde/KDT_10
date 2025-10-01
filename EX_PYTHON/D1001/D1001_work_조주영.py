# ------------------------------------------------------------
# 자판기 프로그램
# - 상품 목록 / 구매
# - 거스름돈 반환
# - 마지막 거래 취소(UNDO)
# - 거래기록을 example.txt에 저장
# ------------------------------------------------------------

items = {
    "A1": ["콜라", 1200, 5],
    "A2": ["사이다", 1100, 5],
    "B1": ["물", 700, 5],
    "B2": ["커피", 1500, 5],
    "C1": ["초코바", 900, 5],
}
balance = 5000
last_txn = None
COINS = [1000, 500, 100, 50, 10]
LOG_FILE = "./example.txt"

# ------------------------------------------------------------
# 함수기능 : 메뉴 출력
# 함수이름 : printMenu
# 매개변수 : 없음
# 결과반환 : 없음
# ------------------------------------------------------------
def printMenu():
    print("-" * 26)
    print("자판기 메뉴")
    print("1. 상품 목록 / 구매")
    print("2. 거스름돈 반환")
    print("3. 거래 내역 조회")
    print("X. 종료")
    print("-" * 26)

# ------------------------------------------------------------
# 함수기능 : 거래기록 한 줄을 example.txt에 저장
# 함수이름 : writeLog
# 매개변수 : line(문자열)
# 결과반환 : 없음
# ------------------------------------------------------------
def writeLog(line):
    try:
        f = open(LOG_FILE, "a", encoding="utf-8")
        f.write(line + "\n")
        f.close()
    except:
        print("거래기록 저장 중 오류가 발생했습니다.")

# ------------------------------------------------------------
# 함수기능 : 상품 목록 화면 출력
# 함수이름 : showItems
# 매개변수 : 없음
# 결과반환 : 없음
# ------------------------------------------------------------
def showItems():
    print("코드  이름    가격   재고")
    for code in items:
        name = items[code][0]
        price = items[code][1]
        stock = items[code][2]
        print(code, name, str(price) + "원", str(stock) + "개")

# ------------------------------------------------------------
# 함수기능 : 상품 구매(재고/잔액 체크 & 거래기록 저장)
# 함수이름 : buy
# 매개변수 : 없음
# 결과반환 : 없음
# ------------------------------------------------------------
def buy():
    global balance, last_txn
    showItems()
    code = input("구매할 코드 입력(예: A1): ").strip().upper()

    if code not in items:
        print("존재하지 않는 코드입니다.")
        return

    name = items[code][0]
    price = items[code][1]
    stock = items[code][2]

    if stock <= 0:
        print("품절입니다.")
        return

    if balance < price:
        print("잔액 부족! 필요", price, "원, 현재", balance, "원")
        return

    # 결제 처리
    items[code][2] = items[code][2] - 1
    balance = balance - price
    print(name, "구매 완료! 잔액:", balance, "원")

    # 거래기록 저장
    writeLog("BUY " + code + " " + name + " -" + str(price) +
             " => balance " + str(balance) + " (stock " + str(items[code][2]) + ")")

    # undo
    last_txn = {"type": "buy", "code": code, "name": name, "price": price}

# ------------------------------------------------------------
# 함수기능 : 최소 개수의 동전으로 거스름돈 계산
# 함수이름 : makeChange
# 매개변수 : amount(정수)
# 결과반환 : 리스트(튜플(동전, 개수))
# ------------------------------------------------------------
def makeChange(amount):
    result = []
    remain = amount
    for c in COINS:
        cnt = remain // c
        if cnt > 0:
            result.append((c, cnt))
            remain = remain - (c * cnt)
    return result

# ------------------------------------------------------------
# 함수기능 : 잔액 전액 반환(거래기록 저장)
# 함수이름 : refund
# 매개변수 : 없음
# 결과반환 : 없음
# ------------------------------------------------------------
def refund():
    global balance, last_txn
    if balance <= 0:
        print("반환할 잔액이 없습니다.")
        return

    change = makeChange(balance)
    text_list = []
    for coin, cnt in change:
        text_list.append(str(coin) + "원x" + str(cnt))
    text = ", ".join(text_list)

    refunded = balance
    balance = 0
    print("거스름돈:", refunded, "원 ->", text)

    # 거래기록 저장
    writeLog("REFUND " + str(refunded) + " => balance " + str(balance) +
             " (change: " + text + ")")

    # undo
    last_txn = {"type": "refund", "amount": refunded, "coins": change}

# ------------------------------------------------------------
# 함수기능 : 거래 기록 조회
# 함수이름 : printFile
# 매개변수 : 없음
# 결과반환 : 없음
# ------------------------------------------------------------
def printFile():
    with open(LOG_FILE, mode='r', encoding='utf-8') as f:
        print(f.read())


## 메인 함수
print("== 자판기 프로그램 시작 ==")


while True:
    print("\n현재 잔액:", balance, "원")
    printMenu()
    cmd = input("선택: ").strip().lower()

    if cmd == "1":
        buy()
    elif cmd == "2":
        refund()
    elif cmd == "3":
        printFile()
    elif cmd in ["x", "X"]:
        print("프로그램 종료")
        writeLog("=== END (balance " + str(balance) + ") ===")
        break
    else:
        print("존재하지 않는 항목입니다.")
