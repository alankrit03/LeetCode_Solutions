"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : [0,1,0,2,1,0,1,3,2,1,2,1]
OUTPUT: 6
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

class Solution:
    def trap(self, height) :
        n = len(height)
        if n == 0:
            return 0
        nsi = [0] * n
        psi = [0] * n

        def cal_greatest():
            c_nsi = height[n - 1]
            c_psi = height[0]

            for i in range(n):
                psi[i] = c_psi
                nsi[n - i - 1] = c_nsi

                if height[i] > c_psi:
                    c_psi = height[i]
                if height[n - i - 1] > c_nsi:
                    # print(f"i={i} c_nsi={c_nsi}")
                    c_nsi = height[n - i - 1]

        cal_greatest()
        # print('nsi= ',nsi)
        # print('psi= ',psi)

        total_rain = 0
        for i in range(1, n - 1):
            temp = min(nsi[i], psi[i])
            if temp > height[i]:
                total_rain += temp - height[i]

        return total_rain


sol = Solution()
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(arr))
