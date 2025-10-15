# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    kek, lol, miau = map(int, input().split())
    z = kek*kek
    v = lol*lol
    r = miau*miau
    print(z == v + r or v == z + r or r == z + v)

   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()