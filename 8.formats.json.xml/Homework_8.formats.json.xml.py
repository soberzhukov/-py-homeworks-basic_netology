import json
from pprint import pprint
from collections import Counter
import xml.etree.ElementTree as et


def read_json():
    with open('newsafr.json') as f:
        data = json.load(f)
    items = data['rss']['channel']['items']
    result_list = list()
    for item in items:
        description = item['description'].split(' ')
        result_list += description
    return result_list


def read_xml():
    parser = et.XMLParser(encoding='utf-8')
    tree = et.parse('newsafr.xml', parser)
    root = tree.getroot()
    items_list = root.findall('channel/item')
    result_list = list()
    for item in items_list:
        description = item.find('description').text.split(' ')
        result_list += description
    return result_list


def show_top_words(items_list, lenght_word=6, top_words=10):
    fix_list = list()
    for word in items_list:
        if len(word) >= lenght_word:
            fix_list.append(word)
    counter_dict = dict(Counter(fix_list))
    list_with_tuples = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    for i in list_with_tuples[:top_words]:
        print(i[0])


# show_top_words(read_json())
# show_top_words(read_xml())