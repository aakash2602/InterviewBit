class Solution():

    def simplifyPath(self, A):
        paths = A[1:].split('/')
        queue = []
        length = 0
        for path in paths:
            if path == '.':
                continue
            elif path == '..':
                if length > 0:
                    queue.pop(length-1)
                    length -= 1
            elif len(path) > 0:
                queue.append(path)
                length += 1
        return '/' + '/'.join(queue)

if __name__ == "__main__":
    sol = Solution()
    print (sol.simplifyPath("/a/./b/../../c/"))
