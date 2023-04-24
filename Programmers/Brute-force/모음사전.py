# 참고: https://school.programmers.co.kr/questions/43874

def dictionary():
    dic = {}
    cnt = 1

    text = 'A'

    dnext = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U'}

    dic[text] = cnt
    while True:
        if text == 'UUUUU':
            break

        # text가 5보다 작으면 뒤에 A를 붙인다.
        if len(text) < 5:
            text = text + 'A'

        elif len(text) == 5:
            #길이가 5인데 마지막 글자가 A/E/I/O인 경우 다음 글자로 변경
            if text[4] != 'U':
                text = text[0:4] + dnext[text[4]]

            else:
                if text[3] == 'U':
                    if text[2] == 'U':
                        if text[1] == 'U':
                            # AUUUU -> E
                            text = dnext[text[0]]
                        else:
                            # AAUUU -> AE
                            text = text[0] + dnext[text[1]]
                    else:
                        # AAAUU -> AAE
                        text = text[0:2] + dnext[text[2]]
                else:
                    # AAAAU -> AAAE
                    text = text[0:3] + dnext[text[3]]
        cnt += 1
        dic[text] = cnt

    return dic


def solution(word):
    dic = dictionary()

    return dic[word]