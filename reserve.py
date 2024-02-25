from Byte import Byte
from Const import Const


class Kuznechik:
    def __init__(self, key):
        self.k1 = Const(key[:32])
        self.k2 = Const(key[32:])
        self.data = []

    def L(self, num):
        for _ in range(16):
            res = Byte(0)
            nums = (1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148)
            for j in range(16):
                res += Byte(nums[j]) * num[j]
            num <<= 1
            num += res
        return num

    def Constants(self):
        data = []
        for i in range(1, 33):
            C = Const(i)
            self.L(C)
            data.append(C)
        return data

    pi_list = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46,
               153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66,
               139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44,
               81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191,
               114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158,
               178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169,
               62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220,
               232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65,
               173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172,
               29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144,
               202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
               116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

    def X(self, k, constant):
        temp = Const([constant[i] + k[i] for i in range(16)])
        return temp

    def S(self, num):
        s_temp = Const([Byte(self.pi_list[num[i].value]) for i in range(16)])
        return s_temp

    def main(self):
        constants = self.Constants()
        for i in range(32):
            x = self.X(self.k1, constants[i])
            s = c.S(x)
            l = c.L(s)
            x2 = self.X(l, self.k2)
            self.k1, self.k2 = Const(str(self.k2)), Const(str(x2))
            print(self.k1, self.k2)


c = Kuznechik('7766554433221100FFEEDDCCBBAA9988EFCDAB89674523011032547698BADCFE')
c.main()