name = input('Your username: ')

def determine_operation():
    option = input('Do you want to encode or decode text? [cod/decod]: ').lower()
    if option in ['c','cod','coding']: return 'cod'
    elif option in ['d','decod','decoding']: return 'decod'
    else: 
        print('Try again!')
        return determine_operation()

def determine_lang():
    lang = input('Enter the language [rus/eng]: ').lower()
    if lang in ['r','rus','russian']: return 'rus'
    elif lang in ['e','eng','english']: return 'eng'
    else:
        print('Try again!') 
        return determine_lang()

def enter_step():
    step = input('Enter a step: ')
    if not step.isdigit():
        print('Try again!')
        return enter_step()
    return int(step)

def enter_text():
    return input('Enter your message: ')

def say_hello():
    print(f'Hi, {name} =)', 'I can code or decode text based on the Caesar cipher.',sep='\n')

def ask_to_repeat():
    answer = input('Do you want to repeat? [yes/no]: ').lower()
    if answer in ['y','yes']: return 'yes'
    elif answer in ['n','no']: return 'no'
    else:
        print('Try again!')
        return ask_to_repeat()

def say_bye():
    print(f'Bye {name} !', 'Reach out anytime =)',sep='\n')