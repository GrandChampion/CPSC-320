# Basic Recursive solution from back
def basicLCSfromBack(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    else:
        # len - 1이 string의 마지막 문자이다.
        if A[len(A) - 1] == B[len(B) - 1]:
            return basicLCSfromBack(A[:len(A) - 2], B[:len(B) - 2]) + 1
        else:
            return max(basicLCSfromBack(A[:len(A) - 1], B), basicLCSfromBack(A, B[:len(B) - 1]))


##############################################################################################################################
# Basic Recursive solution from front
def basicLCSfromFront(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    else:
        if A[0] == B[0]:
            return basicLCSfromFront(A[1:], B[1:]) + 1
        else:
            return max(basicLCSfromFront(A[1:], B), basicLCSfromFront(A, B[1:]))


##############################################################################################################################
# Memoization (while loop or recursion)
# 2D memoization은 helper가 필요하다.
# API
# Input: two words, A and B
# Output: size of the least common sequence string
# Effect: 1) Initialize solution array 2) call helper
def memoLCSfromBack(A, B):
    Solution = [[-1] * len(B) for i in range(len(A))]
    return memoLCSfromBackHelper(Solution, A, B)


# API
# Input: 2D array, 2개의 단어
# Output: LCS 의 길이
def memoLCSfromBackHelper(sol, str1, str2):
    # 순서: memo 테이블이 -1이 아닌지 체크 -> str의 length가 0인지 체크 -> 두 str의 문자가 같은지 체크 -> else (memo 테이블 위/왼쪽 체크)
    # 주의 사항: sol[i]와 sol[:i]의 차이는 sol[:i]의 경우 마지막 인덱스를 포함하지 않는다.
    # 테이블의 선택된 셀에 있는 값이 -1이 아닌 경우
    if sol[len(str1) - 1][len(str2) - 1] != -1:
        return sol[len(str1) - 1][len(str2) - 1]
    # 단어의 길이가 0인 경우
    elif len(str1) == 0 or len(str2) == 0:
        return 0
    # 두 단어의 마지막 문자가 같은 경우
    elif str1[len(str1) - 1] == str2[len(str2) - 1]:
        sol[len(str1) - 1][len(str2) - 1] = memoLCSfromBackHelper(sol,
                                                                  str1[:len(str1) - 1], str2[:len(str2) - 1]) + 1
    # 다 아닌 경우, 위하고 왼쪽 체크
    else:
        sol[len(str1) - 1][len(str2) - 1] = max(memoLCSfromBackHelper(sol, str1[:len(str1) - 1],
                                                                      str2),
                                                memoLCSfromBackHelper(sol, str1, str2[:len(str2) - 1]))
    return sol[len(str1) - 1][len(str2) - 1]


##############################################################################################################################

# API
# Input (memo helper와 같다): 2D array, 2개의 단어
# Output: 실제 LCS 문자열
def extractLCSString(sol, str1, str2) -> str:
    # base case: 2개의 단어중 길이가 하나라도 0인경우
    if len(str1) == 0 or len(str2) == 0:
        return ""
    # 단어의 마지막 문자가 같은 경우
    elif str1[len(str1) - 1] == str2[len(str2) - 1]:
        return extractLCSString(sol, str1[:len(str1) - 1], str2[:len(str2) - 1]) + str1[len(str1) - 1]
    # 다 아닌 경우, 테이블에서 위쪽과 왼쪽 중, 큰쪽에 LCS 문자열을 구하는 함수 호출
    else:
        if sol[len(str1) - 2][len(str2) - 1] > sol[len(str1) - 1][len(str2) - 2]:
            return extractLCSString(sol, str1[:len(str1) - 1], str2)
        else:
            return extractLCSString(sol, str1, str2[:len(str2) - 1])


# word1 = "babeeec"
# word2 = "bcbdc"
# theSolution = [[-1]*len(word2) for i in range(len(word1))]
# memoLCSfromBackHelper(theSolution, word1, word2)
# print(extractLCSString(theSolution, word1, word2))

##############################################################################################################################

# 2D 다이나믹 프로그래밍의 경우, helper가 필요 없다.
# 다이나믹 프로그래밍의 테이블은 row와 colmn에 한층씩 추가해 주어야 한다.
def dynamicLCS(str1, str2):
    # Initialize solution array
    solution = [[-1] * (len(str2) + 1) for i in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        solution[i][0] = 0
    for j in range(len(str2) + 1):
        solution[0][j] = 0
    # 실제 비교
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                solution[i][j] = solution[i - 1][j - 1] + 1
            else:
                solution[i][j] = max(solution[i - 1][j], solution[i][j - 1])
    return solution[i][j]

# print(dynamicLCS("oocs", "oaes"))
