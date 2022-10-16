import phone_dictionary_note as pn

pd = {}


def init(new_pd=None):
    global pd
    if isinstance(new_pd, dict):
        pd = new_pd
    else:
        pd = {}


def get_phone_dictionary():
    return pd


def add_note(note):
    pd.setdefault(note['soname'][0], []).append(note)
    return True


def find_note_by_phone(phone):
    for letter in pd:
        for i in range(len(pd[letter])):
            if pd[letter][i]['phone'] == phone:
                return pd[letter][i]
    return None


def remove_note_by_phone(phone):
    for letter in pd:
        for i in range(len(pd[letter])):
            if pd[letter][i]['phone'] == phone:
                pd[letter].pop(i)
                if len(pd[letter]) == 0:
                    pd.pop(letter)
                return True
    return False
