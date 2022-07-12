import re  # 청규식

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > cafe, case, care (0) | caffe(x)
# ^ (^de)  : 문자열의 시작 > desk, destination (0) | fade(x)
# $ (se$)  : 문자열의 끝 > case, base(0) | face(x)


def print_match(m):
    if m:
        print("m.group:", m.group())  # 일치하는 문자열 반환             매치 되지 않으면 오류 발생
        print("m.String:", m.string)  # 입력받은 문자열
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


m = p.match("case")  # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

a = p.search("good care")  # search : 주어진 문자열중에 일치하는것이 있는지 확인
print_match(a)

lit = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로
print_match(lit)
