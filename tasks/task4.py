# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    z, o, v = map(int, input().split())
    rezultat = (z + o > v) and (z + v > o) and (o + v > z)
    print(rezultat)
    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()