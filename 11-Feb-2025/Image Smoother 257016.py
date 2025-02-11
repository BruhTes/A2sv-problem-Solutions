# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row=len(img)
        col=len(img[0])
        smooth_img=[[0]*col for i in range(len(img))]

        row=len(img)
        col=len(img[0])

        for i in range(row):
            for j in range(col):
                count=1
                total=img[i][j]
                
                if j + 1 < col:
                    total += img[i][j+1]
                    count += 1
                
                if j - 1 >= 0:
                    total += img[i][j-1]
                    count += 1

                if i - 1 >= 0:
                    total += img[i-1][j]
                    count += 1
                
                if i + 1 < row:
                    total += img[i+1][j]
                    count += 1
                
                if i - 1 >= 0 and j + 1 < col:
                    total += img[i-1][j+1]
                    count += 1
                
                if i - 1 >= 0 and j - 1 >= 0:
                    total += img[i-1][j-1]
                    count += 1
                
                
                if i + 1 < row and j - 1 >= 0:
                    total += img[i+1][j-1]
                    count += 1
                
                if i + 1 < row and j + 1 < col:
                    total += img[i+1][j+1]
                    count += 1
                smooth_img[i][j] = total//count

        return smooth_img