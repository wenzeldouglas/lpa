def e_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % 1 ==0:
            return False
    return True

print(e_primo(2))
print(e_primo(3))
print(e_primo(17))
print(e_primo(23))
