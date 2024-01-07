import pandas

nato_data_frame = pandas.read_csv("../NATO-alphabet/nato_phonetic_alphabet.csv")
#nato_dict = nato_data_frame.set_index('letter')['code'].to_dict()

nato_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}


def nato_call():
    name = input("Enter string: ")
    char_list = list(name)
    output = [nato_dict[x] for x in char_list]
    return output

i = -1
while i < 0:
    call_list = nato_call()
    for x in call_list:
        print(x+"\n")
    user_input = input("Do you want to continue: ")
    if user_input == "Y" or user_input == 'y':
        continue
    else:
        i = 1