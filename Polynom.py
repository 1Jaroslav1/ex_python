import numpy as np
import matplotlib.pyplot as plt

class Polynom:
    def __init__(self, arr=[]):
        self._arr = arr
        self._degree = len(arr) - 1

    def get_arr(self):
        return self._arr

    def get_degree(self):
        return self._degree

    def keyboard_input(self):
        self._arr = list(map(int,input().split()))
        self._degree = len(self._arr)
    
    def file_input(self, file_name):
        file = open(file_name)
        self._arr = file_name.readlines().split()
        self._degree = len(self._arr)
        file.close()

    def draw(self):
        x = np.linspace(-10, 10, num=100)
        f = []

        new_arr = self._arr[::-1]
        for i in x:
            var = 0
            for k in range(self._degree+1):
                var += pow(i, k) * new_arr[k]
            print(i, var)
            f.append(var)
        
        plt.plot(x, f)
        plt.grid()
        plt.axvline()
        plt.axhline()
        plt.show()

    def get_value_in(self, x):
        new_arr = self._arr[::-1]
        var = 0
        for k in range(self._degree + 1):
            var += pow(x, k) * new_arr[k]

        return var

    def get_derivative(self, derivative_degree):
        if derivative_degree > self._degree:
            return [0]
        else:
            poly = self._arr[::-1]
            for i in range(derivative_degree):
                poly = [poly[i] * i for i in range(1, len(poly))]

            return poly[::-1]

    def __add__(self, p):
        if isinstance(p, Polynom):
            arr1 = self._arr
            arr2 = p.get_arr()
            new_arr = []

            min_length = min(len(arr1), len(arr2))
            max_length = max(len(arr1), len(arr2))

            z = [0]*(max_length-min_length)
            if len(arr1) < len(arr2):
                arr1 = z + arr1
            else:
                arr2 = z + arr2
            for i in range(max_length):
                new_arr.append(arr1[i] + arr2[i])
        else:
            new_arr = [k + p for k in self._arr]
        return new_arr

    def __sub__(self, p):
        if isinstance(p, Polynom):
            arr1 = self._arr
            arr2 = p.get_arr()
            new_arr = []

            min_length = min(len(arr1), len(arr2))
            max_length = max(len(arr1), len(arr2))

            z = [0]*(max_length-min_length)
            if len(arr1) < len(arr2):
                arr1 = z + arr1
            else:
                arr2 = z + arr2
            for i in range(max_length):
                new_arr.append(arr1[i] - arr2[i])
        else:
            new_arr = [k - p for k in self._arr]
        return new_arr

    def __mul__(self, p):
        if isinstance(p, Polynom):
            arr1 = self._arr
            arr2 = p.get_arr()

            new_arr = [0] * (len(arr1) + len(arr2) - 1)

            for i1, k1 in enumerate(arr1):
                for i2, k2 in enumerate(arr2):
                    new_arr[i1 + i2] += k1 * k2
        else:
            new_arr = [k * p for k in self._arr]
        return new_arr

    def __str__(self):
        ans = ""
        arr = self._arr
        d = self._degree
        for k in arr:
            if k != 0:
                if k == 1:
                    ans += f"x^{d}+"
                else:
                    ans += f"{k}x^{d}+"
            d -= 1
        if ans:
            return ans[:-1]
        return ans
