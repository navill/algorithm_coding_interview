"""
아나그램이 서로 인접하도록 문자열 배열을 정렬하는 메서드 구현
ex: ['abed', 'bead', 'bade', 'later', 'alert', 'alter', 'altered', 'alerted']

버킷 정렬을 변형
{abde: [abed, bead, bade]}
{aelrt: [later, alert, alter]}
{adeelrt: [altered, alerted]}
"""


def group_anagrams():
    strings = initialise_anagrams()
    anagrams = {}
    for i in range(len(strings)):
        word = "".join(sorted(strings[i].lower()))
        if word not in anagrams:
            # setdefault를 이용해 dictionary에 키가 없을 경우 새로 생성한다
            # => 초기값을 만든다.
            anagrams.setdefault(word, [])
        # 키에 해당하는 아나그램을 추가한다.
        anagrams[word].append(strings[i])
    keys = list(anagrams.keys())
    print(keys)
    index = 0
    for i in range(len(keys)):
        values = anagrams.get(keys[i])
        for j in range(len(values)):
            strings[index] = values[j]
            index += 1
    print(strings)


def initialise_anagrams():
    strings = [None] * 8
    strings[0] = "abed"
    strings[1] = "later"
    strings[2] = "bead"
    strings[3] = "alert"
    strings[4] = "altered"
    strings[5] = "bade"
    strings[6] = "alter"
    strings[7] = "alerted"
    return strings


group_anagrams()
