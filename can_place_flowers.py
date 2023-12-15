class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        free = 0

        for index, item in enumerate(flowerbed):
            if index == 0:
                if flowerbed[index] == 1:
                    planted += 1
                else:
                    if len(flowerbed) > 1 and flowerbed[index + 1] == 0:
                        free += 1
                        flowerbed[index] = 1
            elif index == len(flowerbed) - 1:
                if flowerbed[index] == 1:
                    planted += 1
                else:
                    if flowerbed[index - 1] == 0:
                        free += 1
                        flowerbed[index] = 1
            else:
                if item == 0:
                    if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                        free += 1
                        flowerbed[index] = 1
                    else:
                        planted += 1
        print(f"free is {free}")
        print(f"n is {n}")
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                free = 1
            elif flowerbed[0] == 1:
                free = 0

        if free >= n:
            return (True)
        else:
            return (False