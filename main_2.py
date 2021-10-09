def all_div_10(lst):
    """
    Determina toate numerele divizibile cu 10 dintr-o lista.
    :param lst: nr. intregi
    :return: True daca toate elementele sunt divizibile cu 10, False in caz contrar
    """
    for x in lst:
        if x % 10 != 0:
            return False
    return True


def test_all_div_10():
    assert all_div_10([79, 81, 41, 91, 11, 17, 10, 100, 88, 66]) is False
    assert all_div_10([10, 20, 30]) is True
    assert all_div_10([]) is True


def get_longest_div_10(lst):
    """
    Determina cea mai lunga subsecventa cu toate numerele divizibile cu 10.
    :param lst: nr. intregi
    :return: cea mai lunga subsecventa cu toate numerele divizibile cu 10
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_div_10(lst[i:j+1]) is True and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max


def test_get_longest_div_10():
    assert get_longest_div_10([79, 81, 41, 91, 11, 17, 10, 100, 88, 66]) == [10, 100]
    assert get_longest_div_10([79, 81, 10, 41, 10, 20, 30, 40, 88, 66]) == [10, 20, 30, 40]
    assert get_longest_div_10([]) == []
    assert get_longest_div_10([79, 81, 41, 91, 11, 17, 88, 66]) == []


def read_list():
    lst = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        lst.append(int(input("lst["+str(i)+"]= ")))
    return lst


def print_menu():
    print("1. Citire lista")
    print("2. Cea mai mare subsecventa de elemente divizibile cu 10")
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
            print(get_longest_div_10(lst))
        elif optiune == "3":
            should_run = False
        else:
            print("Optiune gresita!")


if __name__ == "__main__":
    test_all_div_10()
    test_get_longest_div_10()
    main()
