class Solution:
    def clumsy(self, n: int) -> int:
        st = [n]
        n -= 1
        op = {
            2: lambda x, y: x * y,
            3: lambda x, y: x // y,
            0: lambda x, y: x + y,
            1: lambda x, y: x - y,
        }
        op_idx = 2
        chunk = []
        while n > 0:
            if op_idx >= 2:
                tmp = op[op_idx](st.pop(), n)
                st.append(tmp)
                n -= 1
                op_idx = (op_idx + 1) % 4
            elif op_idx == 0:
                chunk.append(st.pop())
                chunk.append(n)
                st.append(n-1)
                n -= 2
                op_idx = (op_idx + 1) % 4
            else:
                op_idx = (op_idx + 1) % 4

        chunk.append(st.pop())
        tmp = chunk[0]
        op_idx = 0
        for i in range(1, len(chunk)):
            tmp = op[op_idx](tmp, chunk[i])
            op_idx = (op_idx+1) % 2

        return tmp