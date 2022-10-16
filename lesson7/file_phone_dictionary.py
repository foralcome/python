import phone_dictionary_note
import phone_dictionary
import json
import xml.etree.ElementTree as ET


def save_phone_dictionary_to_file_csv(pd, file_name='phones.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        for letter in pd:
            for note in pd[letter]:
                file_data.write(separator.join(note.values()) + '\n')
    return True


def load_phone_dictionary_from_file_csv(file_name='phones.csv', separator=';'):
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            soname, name, phone, description = line_data.rstrip().split(separator, 4)
            note = phone_dictionary_note.create(soname, name, phone, description)
            phone_dictionary.add_note(note)
    return True


def save_phone_dictionary_to_file_json(pd, file_name='phones.json'):
    with open(file_name, 'w') as file_data:
        file_data.write(json.dumps(pd))
    return True


def load_phone_dictionary_from_file_json(file_name='phones.json'):
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            phone_dictionary.init(json.loads(line_data))
    return True


def save_phone_dictionary_to_file_xml(pd, file_name='phones.xml'):
    xml_dictionary = ET.Element('phone_dictionary')
    for letter in pd:
        xml_letter = ET.SubElement(xml_dictionary, 'letter')
        xml_letter.set('letter', letter)  # установите артрибут xml элементу
        for note in pd[letter]:
            xml_note = ET.SubElement(xml_letter, 'note')
            xml_note.set('soname', note['soname'])
            xml_note.set('name', note['name'])
            xml_note.set('phone', note['phone'])
            xml_note.set('description', note['description'])
    tree = ET.ElementTree(xml_dictionary)
    tree.write(file_name)
    return True


def load_phone_dictionary_from_file_xml(file_name='phones.xml'):
    for event, elem in ET.iterparse(file_name):
        if elem.tag == 'note':
            soname = elem.attrib['soname']
            name = elem.attrib['name']
            phone = elem.attrib['phone']
            description = elem.attrib['description']
            note = phone_dictionary_note.create(soname, name, phone, description)
            phone_dictionary.add_note(note)
    return True
