class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        ans_list = []
        for i in range(1, len(path_list)):
            if path_list[i] in ('', '.'):
                continue
            elif path_list[i] == '..':
                if len(ans_list) > 0:
                    ans_list.pop()
            else:
                ans_list.append(path_list[i])
        return '/' + '/'.join(ans_list)