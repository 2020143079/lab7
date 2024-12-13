
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
       
        ### YOUR CODE HERE ###    
       
        # arr의 원소가 list가 아닌 경우 2DError 발생    
        for i in arr:
            if not isinstance(i, list):
                raise not2DError
        # arr가 3D 이상인 경우 2DError 발생
        for i in arr:
            for j in i:
                if isinstance(j, list):
                    raise not2DError
        # 각 원소의 길이가 동일하지 않은 경우 unevenListError 발생
        first_length = len(arr[0])
        for i in range(len(arr)):
            if len(arr[i])!=first_length:
                raise unevenListError
        
        ######
        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###    

        # list_D2의 출력값 설정
        x = len(self)
        y = len(self[0])
        return 'list_2D: '+ str(x) + '*' + str(y)

        ######

    def transpose(self):

        ### YOUR CODE HERE ###

        # transposed list 반환 
        self_transposed = [[self[j][i] for j in range(len(self))] for i in range(len(self[0]))]

        return list_D2(self_transposed)
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        
        # 행렬 곱 조건 확인
        if len(self[0])!= len(others):
            raise improperMatrixError()
        
        # 결과 행렬 초기화
        result = []  # 빈 리스트로 초기화
        
        # 행렬 곱셈 계산
        for i in range(len(self)): 
            row = []  
            for j in range(len(others[0])):  
                cell = 0
                for k in range(len(self[0])):  
                    cell += self[i][k] * others[k][j]
                row.append(cell)  
            result.append(row)  
        
        return list_D2(result) 

        ######

    def avg(self):

        count = sum(len(r) for r in self)
        total = sum(sum(r) for r in self)
        return total / count


        ######
