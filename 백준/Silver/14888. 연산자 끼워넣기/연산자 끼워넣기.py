n = int(input())
num = list(map(int, input().split()))
arr = list(map(int, input().split()))

alpha_list = ['+','-','*','/']

minimum = 1e9
maximum = -1e9

def dfs(depth,total,plus,minus,mul,div):
    global maximum,minimum
    
    if depth == n:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
        
    
    if plus:
        dfs(depth+1,total + num[depth],plus-1,minus,mul,div)
    if minus:
        dfs(depth+1,total - num[depth],plus,minus-1,mul,div)
    if mul:
        dfs(depth+1,total * num[depth],plus,minus,mul-1,div)
    if div:
        dfs(depth+1,int(total / num[depth]),plus,minus,mul,div-1)
        
            
        

        
dfs(1,num[0],arr[0],arr[1],arr[2],arr[3])
print(maximum)
print(minimum)


