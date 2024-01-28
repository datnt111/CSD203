'''
writing exercises
câu 1.
1
2, 1
3, 10, 5, 16, 8, 4, 2, 1
4, 2, 1
5, 16, 8, 4, 2, 1
6, 3, 10, 5, 16, 8, 4, 2, 1
7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
8, 4, 2, 1
9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
câu 2.1
Các trường hợp cơ bản là:
if base > limit: - Trả về -1 khi base lớn hơn limit.
elif base == limit: - Trả về 1 khi base bằng limit.
câu 2.2
Nhận diện các trường hợp đệ quy của hàm puzzle(..):
Trường hợp đệ quy nằm trong phần else:
return base * puzzle(base + 1, limit) - Gọi hàm puzzle đệ quy với base tăng dần cho đến khi đạt đến điều kiện cơ bản.
câu 2.3
Hiển thị kết quả của các cuộc gọi sau:
a. print(puzzle(14,10))
Base (14) lớn hơn limit (10), nên trả về -1.
Output: -1
b.print(puzzle(4,7))
Base (4) nhỏ hơn limit (7), nên chương trình đi vào trường hợp đệ quy.
Nó nhân 4 với kết quả của cuộc gọi đệ quy puzzle(5, 7).
Quá trình này tiếp tục cho đến khi đạt đến trường hợp cơ bản với base == limit.
Output: 4 * 5 * 6 * 7 * 1 = 840
c. print(puzzle(0,0))
Base (0) bằng limit (0), nên trả về 1.
Output: 1
câu 3:
output:
1
2
3
câu 4:
output:
4
3
1
0
câu 5:
output:
5
4
1
0
1
4
5
'''
#câu6:
def sum(n):
    if n==1:
        return 1
    return 1/n + sum(n-1)
'''
câu 7.1:
khi b=0 trả về 0, k thực hiện đệ quy nào nữa
câu 7.2:
mystery(2,25)=50      
mystery(3,31)=93      
mystery(a,b)=a*b      
khi thay + bằng * thì:      
mystery(2,25)=0      
mystery(3,31)=0      
mystery(a,b)=0
câu 7.3:
có 4 lần gọi cụ thể là mistery (3,7) mistery(6,3) mistery(12,1) mistery(24,0)
câu 8:
Output:    
6    
4    
2    
2    
1    
1    
4    
3    
1    
1    
3    
6
câu 9:
Output: 311361142246
'''
#Pratical exercises
#câu 1:
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
#câu 2:
def findmin(arr,n):
    if n==1:
        return arr[0]
    else:
        return min(arr[n-1],findmin(arr,n-1))
#câu 3:
def findsum(arr,n):
    if n==1:
        return arr[0]
    else:
        return arr[n-1]+findsum(arr,n-1)
#câu 4:
def ispalindrome(arr,n):
    if n==1:
        return 1
    if arr[n-1]!=arr[0]:
        return 0
    else:
        return ispalindrome(arr[1:n-1],n-2)
#câu 5:
def binarySearch(arr,low,high,target):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]>target:
            return binarySearch(arr,low,mid-1,target)
        elif arr[mid]<target:
            return binarySearch(arr,mid+1,high,target)
        else:
            return mid
    else:
        return -1
#câu 6:
def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
#câu 7:
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
#câu 8:
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
#câu 9:
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#câu 10:
def addReciprocals(n):
    if n==1:
        return 1
    else:
        return 1/n+addReciprocals(n-1)
#câu 11:
def stirling(n,k):
    if n==0 and k==0:
        return 1
    if k==0 and n!=0:
        return 0
    if n==0 and k!=0:
        return 0
    return stirling(n-1,k-1)-(n-1)*stirling(n-1,k)
#câu12:
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def insert(self,x):
        if self.val:
            if x<self.val:
                if self.left is None:
                    self.left=TreeNode(x)
                else:
                    self.left.insert(x)
            elif x>self.val:
                if self.right is None:
                    self.right=TreeNode(x)
                else:
                    self.right.insert(x)
        else:
            self.val=x
def height(root):
    if root is None:
        return 0
    else:
        left_height=height(root.left)
        right_height=height(root.right)
        return max(left_height,right_height)+1
#câu 13:
def size(root):
    if root is None:
        return 0
    else:
        left_size=size(root.left)
        right_size=size(root.right)
        return left_size+right_size+1