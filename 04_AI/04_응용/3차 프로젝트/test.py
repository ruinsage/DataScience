import pickle
def search_keyword_index(key_word,all_keys):
    sum_keyword_place = 0
    for num in range(len(all_keys)): # 업체별
        max_value = 0
        keys = all_keys[num]
        for word in key_word: # 키워드 단어별
            tuple_count = 0
            for index, key in enumerate(keys): # 튜플 별
                check_point = 0
                if key[0] == word: # 키워드 단어와 일치하면
                    if tuple_count < all_keys[num][index][1]: # 최대값이 빈도수보다 낮으면
                        check_point = all_keys[num][index][1]
                        # print(f'{all_keys[num][index][0]}:{check_point}')
                        tuple_count = tuple_count + check_point
                        max_value = tuple_count + max_value
                        # if sum_keyword_place < max_value:
                        #     target_index = num
                        #     print(f'인덱스:{num}')
                        if sum_keyword_place < max_value:
                            sum_keyword_place = max_value
                            target_index = num
    print(sum_keyword_place)
    print(target_index)
    print(all_keys[target_index])
    return target_index


all_keys = [[('온천', 21), ('수영장', 8), ('그냥', 7), ('최고', 6), ('사우나', 5)],
            [('온천', 11), ('수영장', 18),('바다',12)],
            [('바다',10)],
            [('온천', 2)],
            [('바다',12),('온천', 10), ('수영장', 25)]]


# with open("all_keys.pickle","rb") as fr:
#     all_keys = pickle.load(fr)


key_word = ['온천']

search_keyword_index(key_word,all_keys)


