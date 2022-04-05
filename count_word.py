# pip install PySimpleGUI
import PySimpleGUI as sg

# Theme, you can change this if you want ;)
sg.theme('DarkAmber')


# Text transformation from file
def open_tranform_file(file_name):
    global words
    file = open(file_name, 'r')
    text = file.read()
    texts = text.lower()
    words = texts.split()
    words = [word.strip('.,!;:\'\"{}()[]?-=%$#&') for word in words]


# Number of words
def total_word(file_name):
    return len(words)


# Number of unique words
def unique_word(file_name):
    count = 0
    words2 = set(words)
    for word in words2:
        count += 1
    return count


# Unique word counting and sorting
def repeat_word(file_name):
    unique = {}
    for word in words:
        #if word in excluded_words:
            #continue
        if word not in unique:
            unique[word] = 1
        else:
            unique[word] += 1
    # Sorting
    repeat_sort = dict(sorted(unique.items(), key=lambda i: i[1], reverse=True))
    return repeat_sort


# Words that will be left out in the word cloud
# You can add new word or delete any
excluded_words_pl = ['w', 'z', 'że', 'o', 'a', 'na', 'się', 'i', 'oraz', 'lub', 'przez', 'są', 'dla', 'jest', 'być', 'ich', 'jak', 'po', 'ale', 'czy', 'który', 'która', 'które', 'także', 'co', 'jego', 'jej', 'ma']
excluded_words_en = ['and', 'or', 'then', 'these', 'those', 'that', 'in', 'an', 'a', 'the', 'but']
# Font parameters:
font_setup = ('Arial', 11, 'bold')

layout = [
    # Input calculations:
    [sg.Text("Choose a file: "),
    sg.Input(key='path',
    size = (10,1)),
    sg.FileBrowse(file_types=(("Text Files", "*.txt", ),))],
    # Input result:
    [sg.Text("Total word: "),
    sg.Text(key='t_word',
        size = (10,1),
        font=font_setup,
        text_color='#fecd5a')],
    [sg.Text("Unique word: "),
    sg.Text(key='u_word',
        size = (10,1),
        font=font_setup,
        text_color='#fecd5a')],
    [sg.Multiline(key='result',
        size = (10,10),
        font=font_setup,
        expand_y= True,
        expand_x= True,
        background_color = '#fecd5a',
        text_color='black')],

    # Buttons:
    [sg.Exit(size=(6, 2), button_color=('white', '#950000'), font=font_setup),
        sg.B('Clear', size=(6, 2), button_color=('white', '#950000'), font=font_setup),
        sg.B('Execute', key="execute", size=(12, 2), font=font_setup),
    ],

    # Footer:
    [sg.Text("Mariusz Dziedzic, 2022")]
]

# Main window:
window = sg.Window('Word Counter', layout, resizable=True,
    size=(450, 450),
    element_justification='center')
while True:
    event, values = window.read()

    # Exit
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event in ('Clear'):
        window['path'].update("")
        window['t_word'].update("")
        window['u_word'].update("")
        window['result'].update("")

    elif event in ('execute'):
        try:
            val = values['path']
            open_tranform_file(val)
            total = total_word(val)
            window['t_word'].update(total)
            unique = unique_word(val)
            window['u_word'].update(unique)
            result = repeat_word(val)
            window['result'].update(result)
        except:
            pass

window.close()
