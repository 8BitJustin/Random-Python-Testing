# def remove_exclamation_marks(string):
#     new_string = string
#     for i in string:
#         if i == '!':
#             new_string = string.replace(i, '')
#
#     return new_string
#
# print(remove_exclamation_marks('Hello World!!'))
# print(remove_exclamation_marks('q'))
# print(remove_exclamation_marks('pFe!exYb!VsH !!tQqEQF'))


def string_to_array(string):

    new_string = string.split()

    text = []

    for i in new_string:
        text.append(i)

    print(text)

string_to_array('hi mim')
string_to_array(' ')