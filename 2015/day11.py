from aoc_utils import data_import

raw_data = data_import.get_input()
letters = [chr(i) for i in range(97,123)]
pairs = [l+l for l in letters]

def increment_letter(ord_num):
    if ord_num != 122:
        return ord_num + 1, False
    else:
        return 97, True


def increment_password(password):
    carry = True # Set to true for first loop so first number is always incremented
    ord_pw = [ord(l) for l in list(password)]
    for i in range(1, len(password)+1):
        if carry:
            ord_pw[-i], carry = increment_letter(ord_pw[-i])
        else:
            return "".join([chr(num) for num in ord_pw])

    return "".join([chr(num) for num in ord_pw])


def rule_one(password):
    for i in range(len(password)-2):
        i_ord = ord(password[i])
        j_ord = ord(password[i+1])
        k_ord = ord(password[i+2])
        if i_ord == (j_ord -1) and j_ord == (k_ord -1):
            return True
    return False

def rule_two(password):
    return any(letter not in password for letter in ["i", "o", "l"])


def rule_three(password):
    password_pairs = []
    for i in range(len(password)-1):
        j = i + 1
        if password[i] == password[j]:
            password_pairs.append(password[i]+password[j])

    total_count = sum(pair in password_pairs for pair in pairs)
    if total_count >= 2:
        return True
    else:
        return False


def main_p1(password):
    while not (rule_one(password) and rule_two(password) and rule_three(password)):
        password = increment_password(password)
    return password


def main_p2(password):
    pw1 = main_p1(password)
    print(pw1)
    print(main_p1(increment_password(pw1)))

if __name__ == "__main__":
    # main_p1(raw_data)
    main_p2(raw_data)
    # test_str = "abcdffaa"
    # print(rule_one(test_str), rule_two(test_str), rule_three(test_str))
