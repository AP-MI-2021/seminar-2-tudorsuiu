def is_prime(x):
    """
    Determina daca numarul este prim.
    :param x: nr. intreg
    :return: True daca x este prim, False in caz contrar
    """
    if x < 2:
        return False
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


def get_primes(lst):
    """
    Determina si returneaza numerele prime din lista.
    :param lst: nr. intregi
    :return: numerele prime din lista
    """
    result = []
    for x in lst:
        if is_prime(x):
            result.append(x)
    return result


def test_get_primes():
    assert get_primes([]) == []
    assert get_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [2, 3, 5, 7, 11, 13]
    assert get_primes([21, 23, 69, 823, 3, 1093, 22, 534]) == [23, 823, 3, 1093]


def read_list():
    lst = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        lst.append(int(input("lst["+str(i)+"]= ")))
    return lst


def print_menu():
    print("1. Citire lista")
    print("2. Afisare numere prime")
    print("3. Iesire")


def main():
    should_run = True
    lst = []
    while should_run:
        print_menu()
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            lst = read_list()
        elif optiune == "2":
            print(get_primes(lst))
        elif optiune == "3":
            should_run = False
        else:
            print("Optiune gresita!")


if __name__ == "__main__":
    test_is_prime()
    test_get_primes()
    main()
