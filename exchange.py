def exchange(money : int, c : list) -> int:
    revers_c = sorted(c, reverse=True)
    result = 0
    for i in range(0, len(c)):
        i_k = money // c[i]
        if i_k > 0:
            result += i_k
        money = money - c[i] * i_k

    return result

print(exchange(money=int(input()), c=list(map(int, input().split()))))
