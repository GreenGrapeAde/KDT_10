## 28.3 연습문제: 단어 단위 N-gram 만들기
n = int(input())
text = input()
words = text.split()

if len(words) < n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)

## 28.4 심사문제: 파일에서 회문인 단어 출력하기
with open('./words.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        line = line.strip('\n')
        if line == line[::-1]:
            print(line)

## 34.6 심사문제: 게임 캐릭터 클래스 만들기
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print(f'티버: 피해량 {self.ability_power * 0.65 + 400}')

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()