import re


def standard(pattern: str, text: str):
    values = re.findall(pattern, text)
    return sum(int(value[0]) * int(value[1]) for value in values)

pattern = r'mul[(](\d{1,3})[,](\d{1,3})[)]'

test_str = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

def import_txt(data_loc: str) -> str:
    with open(data_loc, 'r', encoding='utf-8') as txt_file:
        return txt_file.read()

if __name__ == '__main__':
    data_loc = r'day_3.txt'
    imported_txt = import_txt(data_loc)
    print(standard(pattern, imported_txt))