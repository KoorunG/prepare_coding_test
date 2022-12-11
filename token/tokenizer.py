import re

# 파일경로
# path = "token/test2.txt"
# f = open(path, "r", encoding="utf8")

names = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''

# column 지정
col = 6
words_list = []
for i, words in enumerate(names.splitlines()):
    # 정규식으로 필터링
    # words_list.extend([s.replace("\n", "") for s in words.split()])
    words_list.extend([re.sub("[,.]", "", s) for s in words.split()])
# 파싱한 단어중 최대 길이
max_len = len(max(words_list, key=len))
new_list = [n.ljust(max_len + 1) for n in words_list]
result = ''
for i, s in enumerate(new_list):
    if i % col == 0:
        s = '\n' + s
    result += s
# 출력
print(result)
# f.close()

