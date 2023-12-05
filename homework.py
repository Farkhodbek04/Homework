""" 
1) shunday funksiya yozingki, u ikkita parametreni qabul qilsin. birinchi parametredagi barcha sozlar ikkinchi parametrda bo`lishi kerak. 
2) shunday funksiya yozingki u bittra parametrani str typda qabul qilsin va osha sozni ichidagi unli harflar sonini qaytarsin 
3)shunday funksiya yozingki u ichida raqamlarni qabul qilsin va 0 llar sonini qaytarsin 
4) shunday funksiya yozingki u ikkita parametr qabul qilsin va birinchi parametralarni ichidagi barcha unli harflar ikkinchisida mavjudligini tekshiring 
5) barcha natijalar githubga yuklanib reponi linkini yuboring
"""

## Problem_1
def check_person(func):
    def wrapper(name:str,full_name:list[str]):
        if name in full_name:
            return func(name,full_name)
        return "Invalid name!"
    return wrapper

@check_person
def person(name:str,full_name:list[str])->str:
    return (f"Hello {name} ")
# print(person("farxodbek",["farxodbek", "jaloldinov"]))

## Problem_2
def count_wovel(words:str)->int:
    words=words.lower()
    wovels="aeoui"
    counter=0
    for i in wovels:
        counter+=words.count(i)
    return f"There are {counter} wovels in the text"

# print(count_wovel("hELLO, I am farkhodbek"))

## Problem_3

def count_0(nums:str)->int:
    return nums.count("0")
# print(count_0("12131230231"))

## Problem_4
def check_words(func):
    def wrapper(w1:str, w2:str):
        w2=w2.lower()
        wovels="aeoui"
        for i in w1.lower():
            if i in wovels and i not in w2:
                return "Wrong input!"
        return func(w1,w2)
    return wrapper

@check_words
def words(w1:str, w2:str)->bool:
    return True
print(words("saloim", "olqwcsdawqfwdfwdcsaxqxzcvdsam something"))