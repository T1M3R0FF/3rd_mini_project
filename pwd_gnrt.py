import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


num = input('Укажите количество паролей для генерации \n').strip()
length = input('Укажите длину пароля \n').strip()
dig = input('Включать ли цифры? (да/нет)\n').strip()
if dig == 'да':
    chars += digits
lwr = input('Включать ли строчные буквы? (да/нет)\n').strip()
if lwr == 'да':
    chars += lowercase_letters
uppr = input('Включать ли прописные буквы (да/нет)\n').strip()
if uppr == 'да':
    chars += uppercase_letters
sym = input('Включать ли символы?(!#$%&*+-=?@^_) (да/нет)\n').strip()
if sym == 'да':
    chars += punctuation
remove_badsymbols = input('Исключить символы il1Lo0O? (да/нет)\n').strip()
if remove_badsymbols == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)


for _ in range(int(num)):
    generate_password(int(length), chars)
