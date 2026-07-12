eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def encypher(text,language,step,act):
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

        if act == 'decod':
            if text[i] in curr:
                for j in range(len(curr)):
                    if 0 <= j - step < len(curr) and text[i] == curr[j]:
                        res.append(curr[j-step])
                    elif j - step < 0 and text[i] == curr[j]:
                        res.append(curr[(j-step)%len(curr)])
        else:
            if text[i] in curr:
                for j in range(len(curr)):
                    if 0 <= j + step < len(curr) and text[i] == curr[j]:
                        res.append(curr[j+step])
                    elif j + step >= len(curr) and text[i] == curr[j]:
                        res.append(curr[(j+step)%len(curr)])
    
    return ''.join(res)