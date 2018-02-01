def sort_dictionary(dic):
    list=[]
    for k,v in dic.items():
        list.append((k,v))
        list.sort()
    return list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))