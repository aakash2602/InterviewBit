class Solution():

    def LCA(self, A, B, C):
        queue, lca_node = self.get_lca(A, B, C)
        if lca_node:
            return lca_node.val
        return -1

    def get_lca(self, node, val1, val2):
        if node == None:
            return [], None
        # print (node.val)
        lqueue, lca_nodel = self.get_lca(node.left, val1, val2)
        # print (lqueue)
        rqueue, lca_noder = self.get_lca(node.right, val1, val2)
        # print (rqueue)
        if lqueue and rqueue:
            lqueue.extend(rqueue)
            return lqueue, node
        elif lqueue or rqueue:
            if node.val == val1 or node.val == val2:
                if lqueue:
                    lqueue.append(node)
                    return lqueue, node
                if rqueue:
                    rqueue.append(node)
                    return rqueue, node
            else:
                # return lqueue+rqueue, lca_node
                if lqueue:
                    return lqueue, lca_nodel
                if rqueue:
                    return rqueue, lca_noder
        else:
            if node.val == val1 and node.val == val2:
                return [node, node], node
            elif node.val == val1 or node.val == val2:
                # print (node.val)
                return [node], None
            else:
                return [], None