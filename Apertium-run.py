import apertium
import typing
import random


def main ():
    #print(apertium.translate('es', 'en',apertium.translate('en', 'es', 'self').replace("*",'')).replace("*",""))
    languages = {}
    for lang_from , lang_to in [key.split('-') for key in apertium.pairs.keys()]:
        languages.setdefault(lang_from,[]).append(lang_to)
    languages = trim_languages_leaves(languages)
    generate_random_walks('eng','Our country is in serious trouble. We dont have victories anymore. We used to have victories, but we dont have them. When was the last time anybody saw us beating, lets say, China in a trade deal? They kill us. I beat China all the time. All the time.', languages,10)
    #print(apertium.pairs)

def trim_languages_leaves(languages:dict)-> dict:
    for lang_from, langs_to in languages.items():
        #print(f"{lang_from} contains the languages {langs_to}")
        languages[lang_from]= [lang_to for lang_to in langs_to if '_' not in lang_to and lang_to in languages]
        #print(f"{lang_from} contains the languages {languages[lang_from]}")

    return languages

def unknown_char_translate(from_lang, to_lang, text) -> str: 
    return apertium.translate(from_lang, to_lang, text).replace('*', '')\

def generate_random_walks(lang: str, text:str, languages: dict, min_times: int):
    random_choice = ''
    i=0
    while True:
        if i >= min_times and 'eng' in languages[lang] :
            #print(lang, 'eng')
            print(unknown_char_translate(lang, 'eng', text))
            break
        else:
            #print(languages[lang])
            random_choice = random.choice(languages[lang])
            #print(lang, random_choice)
            text = unknown_char_translate(lang, random_choice, text)
            print(text)
            lang = random_choice
        i +=1





if __name__ == "__main__":
    main()