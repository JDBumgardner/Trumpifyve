from __future__ import print_function
import os.path
import apertium
import typing
import random
import re
import json


PATTERN = re.compile(r'[#\@\*;]+')
path = '/home/jacob/Coding projects/Trumpifyve/campaignCorpus/Trump_Campaign_Corpus/trump_campaign_corpus.json'
min_langs = 5
batch_size=128
write_path = '/home/jacob/Coding projects/Trumpifyve/apertiumFiles'
lang = 'eng'

def main ():
    
    #print(apertium.translate('es', 'en',apertium.translate('en', 'es', 'self').replace("*",'')).replace("*",""))
    languages = {}
    for lang_from , lang_to in [key.split('-') for key in apertium.pairs.keys()]:
        languages.setdefault(lang_from,[]).append(lang_to)
    languages = trim_languages_leaves(languages)
    translators = create_translators(languages)
    trump_lines = read_corpus(path)
    #write_json(batch_size, write_path,trump_lines, lang, translators)
    #print(apertium.pairs)
    a = "And we have nothing. We can't even go there. We have nothing. And every time we give Iraq equipment, the first time a bullet goes off in the air, they leave it."
    with open('/tmp/donaldtemp.json', "w") as f:
        json.dump(generate_random_walk('eng', a, translators, 10),f)
        print("\r", i, end="")



def create_translators(languages: dict) -> dict:
    translators = {}
    for key in languages:
        translators[key] = [] 
        for item in languages[key]:
            #print(key, item)
            translators[key].append((item,apertium.Translator(key,item)))
    return translators

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def write_json(batch_size: int, write_path: str, trump_lines: list, lang:str, translators: dict):
    trump_pairs = []
    for i, chunk in enumerate(chunks(trump_lines,batch_size)):
        path = os.path.join(write_path, '{}.json'.format(i))
        if os.path.exists(path):
            continue
        else:
            #current_batch_pair = list(zip(chunk, normalize(chunk)))
            current_batch_pair = [(item, generate_random_walk(lang, item, translators ,min_langs)) for item in chunk]
            trump_pairs += current_batch_pair
            with open(path, "w") as f:
                json.dump(current_batch_pair,f)
                print("\r", i, end="")


def read_corpus(path: str) -> list:
    with open(path) as f:
        campaign_corpus=json.load(f)
    trump_lines = []
    for item in campaign_corpus:
        if item['is_as_spoken'] is True:
            turns = item["doc"]
            if type(turns) is not list:
                turns = [turns]
            for turn in turns:
                if turn["person"] == 'Donald Trump':
                    samples = turn["p"]
                    if type(samples) is not list:
                        samples = [samples]
                    for sample in samples:
                        if type(sample) is not str:
                            continue
                        trump_lines.append(sample)
    return trump_lines


def trim_languages_leaves(languages:dict)-> dict:
    for lang_from, langs_to in languages.items():
        #print(f"{lang_from} contains the languages {langs_to}")
        languages[lang_from]= [lang_to for lang_to in langs_to if '_' not in lang_to and lang_to in languages]
        #print(f"{lang_from} contains the languages {languages[lang_from]}")
    return languages

def unknown_char_translate(translator, text:str) -> str: 
    #print("original text = ", text)
    #print('translated text = ', translator.translate(text))
    #print("substituted stuff = ", PATTERN.sub('',translator.translate(text)))
    return PATTERN.sub('', translator.translate(text))
    #return apertium.translate(from_lang, to_lang, text).replace('*', '')\

def generate_random_walk(lang: str, text:str, translators: dict, min_times: int) -> str:
    random_choice = ''
    i=0
    original_lang = lang
    while i < min_times or original_lang not in [language for language , translator in translators[lang]]:
        #print(languages[lang])
        to_lang, translator = random.choice(translators[lang])
        #print(lang, random_choice)
        #print(text)
        text = unknown_char_translate(translator, text)
        #print(text)
        lang = to_lang
        i +=1
    #print(lang, 'eng')
    #print(unknown_char_translate(lang, 'eng', text))
    original_translator = [translator for language, translator in translators[lang] if language == original_lang]
    return unknown_char_translate(original_translator[0], text)


if __name__ == "__main__":
    main()