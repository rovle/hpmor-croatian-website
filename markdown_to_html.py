# load a text file and iterate over lines

import datetime 
chapters_to_publish = [
        '1 - Dan vrlo niske vjerojatnosti',
        '2 - Sve u što vjerujem je pogrešno'
        ]


def format_italics(string):
    inside_italics = False
    formatted_string = ''
    for char in string:
        if char == '*':
            inside_italics = not inside_italics
            if inside_italics:
                formatted_string += '<em>'
            if not inside_italics:
                formatted_string += '</em>'
        else:
            formatted_string += char
    return formatted_string


def format_chapter_name(chapter):
    number, name = chapter.split('-')
    chapter_name = f'Poglavlje {number.strip()}. {name.strip()}'
    return chapter_name

def get_dropdown_menu_entry(chapter, selected=False):
    number, name = chapter.split('-')
    chapter_name = f'Poglavlje {number.strip()}. {name.strip()}'
    if selected:
        open_tag = f'<option value="/chapters/{number.strip()}" selected>'
    else:
        open_tag = f'<option value="/chapters/{number.strip()}">'
    entry = open_tag + chapter_name + '</option>'
    return entry

chapter_names = [format_chapter_name(chapter)
                                for chapter in chapters_to_publish]



    


for ix, chapter in enumerate(chapters_to_publish):
    navigation = '<div class="nav-dropdown">' + \
                    '<select name="chapter" class="nav-select">'
    for chapter_ in chapters_to_publish:
        if chapter_ == chapter:
            navigation += get_dropdown_menu_entry(chapter_, selected=True)
        else:
            navigation += get_dropdown_menu_entry(chapter_)
    navigation += '</select></div>'
    if chapter != chapters_to_publish[0]:
        back_button = f'<div class="nav-prev"><a href="/chapters/{ix}">' + \
                            '&laquo; Prethodno</a></div>'
        navigation = back_button + navigation 
    if chapter != chapters_to_publish[-1]:
        forward_button = f'<div class="nav-next"><a href="/chapters/{ix+2}">' + \
                            'Sljedeće &raquo;</a></div>'
        navigation = navigation + forward_button
   
    navigation = '<form action="" method="GET" id="nav-form-top"' + \
                    ' target="_top">' + \
                    navigation +' </form>'


    new_chapter_text = ''
    with open(f'Poglavlja_markdown/{chapter}.md', 'r') as f:
        for line in f.readlines():
            if len(line) == 1:
                continue
            pre = '<div class="paragraph"><p>'
            post = '</p></div>'
            new_chapter_text += pre + format_italics(line) + post

    vrijeme = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    vrijeme = f'Zadnje ažurirano: {vrijeme}.'
    print(vrijeme)

    with open('chapter_template.html', 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('NAVIGACIJA',  navigation)
    filedata = filedata.replace('NASLOV_POGLAVLJA', chapter_names[ix])
    filedata = filedata.replace('OVDJE_IDU_PARAGRAFI', new_chapter_text)
    filedata = filedata.replace('VRIJEME', vrijeme)
    filedata = filedata.replace(r'\...', '...')
    filedata = filedata.replace(r'\"', '"')

    print(new_chapter_text)

    with open(f'chapters/{ix+1}.html', 'w') as file:
        file.write(filedata)

"""
new = ''
with open('001.txt', 'r') as f:
    f = f.readlines()
    for line in f:
        if len(line) == 1:
            continue
        print(len(line))
        pre = '<div class="paragraph"><p>'
        post = '</p></div>'
        new = new + (pre + line + post)


# save the result to a new file
with open('001_fixed.txt', 'w') as f:
    f.write(new)"""
