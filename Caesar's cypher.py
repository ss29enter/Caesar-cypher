# alphabet & vars
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
name = input('Your username: ')

# funtions
def say_hello():
    print(f'Hi, {name} =)', 'I can code or decode text based on the Caesar cipher.',sep='\n')

def ask_to_repeat():
    answer = input('Do you wanna repeat? [yes/no]: ').lower()
    if answer in ['y','yes']: return 'yes'
    elif answer in ['n','no','nope']: return 'no'
    else:
        print('Try again!')
        ask_to_repeat()

def say_bye():
    print(f'Bye {name} !', 'Reach out anytime =)',sep='\n')

def determine_operation():
    option = input('Do you wanna coding or decoding text? [cod/decod]: ').lower()
    if option in ['c','cod','coding']: return 'cod'
    elif option in ['d','decod','decoding']: return 'decod'
    else: 
        print('Try again!')
        determine_operation()

def determine_lang():
    lang = input('Enter the language [rus/eng]: ').lower()
    if lang in ['r','rus','russian']: return 'rus'
    elif lang in ['e','eng','english']: return 'eng'
    else:
        print('Try again!') 
        determine_lang()

def enter_step():
    step = input('Enter a step: ')
    if not step.isdigit():
        print('Try again!')
        enter_step
    return int(step)

def enter_text():
    return input('Enter your message: ')

def coding(text,language,step):
    res, curr = [],''

    if language == 'rus':
        dict_lower = rus_lower_alphabet
        dict_upper = rus_upper_alphabet
    if language == 'eng':
        dict_lower = eng_lower_alphabet
        dict_upper = eng_upper_alphabet

    for i in range(len(text)):
        if text[i] in dict_lower:
            curr = dict_lower
        elif text[i] in dict_upper:
            curr = dict_upper
        else: res.append(text[i])

        if text[i] in curr:
            for j in range(len(curr)):
                if 0<= j + step < len(curr) and text[i] == curr[j]:
                    res.append(curr[j+step])
                elif j + step > len(curr) and text[i] == curr[j]:
                    res.append(curr[(j+step)%len(curr)])
    
    return ''.join(res)

def decoding(text,language,step):
    res, curr = [],''

    if language == 'rus':
        dict_lower = rus_lower_alphabet
        dict_upper = rus_upper_alphabet
    if language == 'eng':
        dict_lower = eng_lower_alphabet
        dict_upper = eng_upper_alphabet

    for i in range(len(text)):
        if text[i] in dict_lower:
            curr = dict_lower
        elif text[i] in dict_upper:
            curr = dict_upper
        else: res.append(text[i])

        if text[i] in curr:
            for j in range(len(curr)):
                if 0<= j - step < len(curr) and text[i] == curr[j]:
                    res.append(curr[j-step])
                elif j - step < 0 and text[i] == curr[j]:
                    res.append(curr[(j-step)%len(curr)])
    
    return ''.join(res)

# main  
def action():
    act = determine_operation()
    lang = determine_lang()
    step = enter_step()
    text = enter_text()
    if act == 'cod':
        print(f'> Your coded message: {coding(text,lang,step)}')
    elif act == 'decod':
        print(f'> Your decoded message: {decoding(text,lang,step)}')
    print()

    repeat = ask_to_repeat()
    if repeat == 'no':
        return say_bye()
    return action()

def main():
    say_hello()
    print()
    action()

# run
if __name__ == '__main__':
   main()