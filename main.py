from text_encryption import encypher
import utils 

def main():
    act = utils.determine_operation()
    lang = utils.determine_lang()
    step = utils.enter_step()
    text = utils.enter_text()
    if act == 'cod':
        print(f'> Your encrypted message: {encypher(text,lang,step,act)}')
    else:
        print(f'> Your decrypted message: {encypher(text,lang,step,act)}')
    print()

    repeat = utils.ask_to_repeat()
    if repeat == 'no':
        return utils.say_bye()
    main()

utils.say_hello()
if __name__ == '__main__':
   main()