class TreeStore:
    def __init__(self, items):
        self.items = items

        self.item_id = dict()
        for i in items:
            self.item_id[i['id']] = i

        self.children_parent = dict()
        for i in items:
            parent_id = i['parent']
            if parent_id not in self.children_parent:
                self.children_parent[parent_id] = []
            self.children_parent[parent_id].append(i)

    def getAll(self):
        return self.items

    def getItem(self, id):
        return self.item_id.get(id)

    def getChildren(self, id):
        return self.children_parent.get(id)

    def getAllParents(self, id):
        parents = list()
        current_item = self.getItem(id)
        while current_item and current_item['parent'] != "root":
            parent_id = current_item['parent']
            parent_item = self.getItem(parent_id)
            if parent_item:
                parents.append(parent_item)
                current_item = parent_item
            else:
                break
        return parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

# Примеры использования:
#print(ts.getAll())
# [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

#print(ts.getItem(7))
# {"id":7,"parent":4,"type":None}

print(ts.getChildren(4))
# [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

#print(ts.getChildren(5))
# []

#print(ts.getAllParents(7))
# [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]