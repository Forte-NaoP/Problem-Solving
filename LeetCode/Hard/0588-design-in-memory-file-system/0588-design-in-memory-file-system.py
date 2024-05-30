DIR = 0
FILE = 1

class Node:
    def __init__(self, id, pid, type, name = ''):
        self.id = id
        self.pid = pid
        self.type = type
        self.name = name
        if type == DIR:
            self.contents = dict()
        else:
            self.contents = ''

    def append(self, content, name = None):
        if self.type == DIR:
            self.contents[name] = content
        else:
            self.contents += content

    def get(self, sub = None):
        if self.type == DIR:
            return self.contents.get(sub)
        else:
            return self.contents

    def get_sub(self):
        if self.type == DIR:
            return self.contents
        return None

class FileSystem:

    def __init__(self):
        self.nxt = 0
        root = Node(0, 0, DIR)
        self.fs = {0: root}


    def __new_node(self, pid, type, name):
        self.nxt += 1
        node_id = self.nxt
        node = Node(node_id, pid, type, name)
        self.fs[node_id] = node
        return node_id


    def __leaf(self, path: List[str]):
        node_id = 0
        while path:
            nxt_name = path.pop()
            node_id = self.fs[node_id].get(nxt_name)
        return node_id


    def __mkdir_r(self, path: List[str]):
        dir_id = 0
        while path:
            nxt_name = path.pop()
            if self.fs[dir_id].get(nxt_name) is None:
                nxt_id = self.__new_node(dir_id, DIR, nxt_name)
                self.fs[dir_id].append(nxt_id, nxt_name)
            dir_id = self.fs[dir_id].get(nxt_name)
        return dir_id
    

    def ls(self, path: str) -> List[str]:
        if path == '/':
            node_id = 0
        else:
            path = path.split('/')[-1:0:-1]
            node_id = self.__leaf(path)
        
        if self.fs[node_id].type == DIR:
            return sorted(self.fs[node_id].get_sub().keys())
        else:
            return [self.fs[node_id].name]
        

    def mkdir(self, path: str) -> None:
        path = path.split('/')[-1:0:-1]
        self.__mkdir_r(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')
        file_name = path[-1]
        path = path[-2:0:-1]
        dir_id = self.__mkdir_r(path)
        if self.fs[dir_id].get(file_name) is None:
            file_id = self.__new_node(dir_id, FILE, file_name)
            self.fs[dir_id].append(file_id, file_name)
        file_id = self.fs[dir_id].get(file_name)
        self.fs[file_id].append(content)


    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split('/')[-1:0:-1]
        node_id = self.__leaf(path)

        return self.fs[node_id].get()