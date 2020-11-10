# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ in '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        lst = list(map(int, input().split()))
        min_index = lst.index(min(lst))
        left = lst[ : min_index]
        right = lst[min_index : ]
        if left == sorted(left, reverse = True) and right == sorted(right, reverse = False):
            print("Yes")
        else:
            print("No")
