# 백준 1000번 A+B
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 A와 B가 주어진다. (0<A, B<10)
# 출력 : 첫째 줄에 A+B를 출력한다.

A, B = input().split()
print(int(A)+int(B))

a,b = map(int, input().split())
print(a+b)

# 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수로 저장한다.
# input()함수는 사용자로부터 문자열을 입력받을 때 사용한다.
