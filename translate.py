def translate(bilingual_dict,english_words_list):
    swedish_words_list=[]
    for key in english_words_list:
        for key1 in bilingual_dict.keys():
            if key==key1:
                swedish_words_list1=bilingual_dict[key]
                swedish_words_list.append(swedish_words_list1)
    return swedish_words_list


bilingual_dict= {'amount': 'god', 'happy': 'gott', 'give': 'ge', 'the': 'de', 'year': 'ar', 'please': 'snalla du'}
english_words_list=["please","give","the","amount"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
