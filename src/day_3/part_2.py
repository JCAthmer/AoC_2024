import re


def standard(pattern: str, text: str):
    multiply = True
    command_results = list()
    for command in re.findall(pattern, text):
        if command[1] == 'do':
            multiply = True
        elif command[0] == "don't":
            multiply = False
        else:
            command_results.append(multiply*int(command[2])*int(command[3]))

    return sum(command_results)

def import_txt(data_loc: str) -> str:
    with open(data_loc, 'r', encoding='utf-8') as txt_file:
        return txt_file.read()

if __name__ == '__main__':
    data_loc = r'day_3.txt'
    pattern = r"(don't)|(do)|mul[(](\d{1,3})[,](\d{1,3})[)]"
    imported_txt = import_txt(data_loc)
    print(standard(pattern, imported_txt))