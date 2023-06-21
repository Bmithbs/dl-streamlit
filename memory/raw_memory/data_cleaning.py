import re


def processing_string(input:str):
    # 去除数字和括号
    output_string = re.sub(r'\d+|\(|\)', '', input)
    # 替换字符串
    output_string = output_string.replace('Thoureality', 'Forest')
    output_string = output_string.replace(' -- :::', ':')
    return output_string


if __name__ == '__main__':
    input_path = 'lsc1.txt'
    output_path = 'lsc.txt'
    with open(input_path, 'r') as f:
        content = f.read()
        content = processing_string(content)
    with open(output_path, 'w+') as f:
        f.write(content)
        