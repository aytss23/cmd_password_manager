import random
def password_generator(password_length=16):
    generated_password = []
    for i in range(password_length):
        generated_password.append(chr(random.randint(33,126)))
    print(''.join(generated_password))
    return ''.join(generated_password)
def logger(log_data=0):
    if log_data == 0:
        with open('log.txt','r+') as log_file:
            print(log_file.read())
    elif log_data == 1:
        with open('log.txt','w+') as log_file:
            log_file.close()
    else:
        with open('log.txt','a+') as log_file:
            for data in log_data:
                log_file.write(data)
                log_file.write('\t')
            log_file.write('\n')
def get_command():
    keyboard_input = str(input("password-manager@::"))
    keyboard_input = keyboard_input.split(" ")
    match(keyboard_input[0]):
        case 'create':
            keyboard_input[2] = password_generator(int(keyboard_input[2]))
            logger([keyboard_input[1],keyboard_input[2]])
        case 'append':
            logger([keyboard_input[1],keyboard_input[2]])
        case 'list':
            logger(0)
        case 'truncate':
            logger(1)
        case 'exit':
            exit()
        case _:
            get_command()
    get_command()
def main():
    get_command()
main()