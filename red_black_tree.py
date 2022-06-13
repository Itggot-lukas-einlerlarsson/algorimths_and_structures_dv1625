"""Funktioner och klasser för RB-Träd"""
#from graphviz_tool import tree_to_graphviz

class Node:
    """Klassen för alla noder i trädet så jag har tillgång till deras egenskaper"""
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.color = 'RED'

    def data_lst(self):
        """ generate data into a list for bfs()"""
        data_lst = []
        data_lst.append(self.value)
        data_lst.append(self.color)
        if self.left_child:
            data_lst.append(self.left_child.value)
        else:
            data_lst.append(None)
        if self.right_child:
            data_lst.append(self.right_child.value)
        else:
            data_lst.append(None)
        return data_lst

class RedBlackTree:
    """Klassen för hela Röd-Svarta trädets funktioner och diverse."""
    def __init__(self):
        """Konstruktor"""
        self.nil_leaf = Node()
        self.root = self.nil_leaf
        self.nil_leaf.color = 'BLACK'
        self.nil_leaf.left_child = self.nil_leaf
        self.nil_leaf.right_child = self.nil_leaf
        #self.nil_leaf.parent = self.nil_leaf

    def __del__(self):
        """Destruktor"""
        #print("Destruktor körs")
        delattr(self, "left_child")
        delattr(self, "right_child")
        delattr(self, "key")
        delattr(self, "parent")
        delattr(self, "color")

    def rb_insert_fixup(self, input_node):
        """Fixar om trädet vid insert"""
        while input_node.parent.color == 'RED':
            if input_node.parent == input_node.parent.parent.left_child:
                y_node = input_node.parent.parent.right_child
                if y_node.color == 'RED':
                    input_node.parent.color = 'BLACK'
                    y_node.color = 'BLACK'
                    input_node.parent.parent.color = 'RED'
                    input_node = input_node.parent.parent
                else:
                    if input_node == input_node.parent.right_child:
                        input_node = input_node.parent
                        self.left_rotate(input_node)
                    input_node.parent.color = 'BLACK'
                    input_node.parent.parent.color = 'RED'
                    self.right_rotate(input_node.parent.parent)
            else:
                y_node = input_node.parent.parent.left_child
                if y_node.color == 'RED':
                    input_node.parent.color = 'BLACK'
                    y_node.color = 'BLACK'
                    input_node.parent.parent.color = 'RED'
                    input_node = input_node.parent.parent
                else:
                    if input_node == input_node.parent.left_child:
                        input_node = input_node.parent
                        self.right_rotate(input_node)
                    input_node.parent.color = 'BLACK'
                    input_node.parent.parent.color = 'RED'
                    self.left_rotate(input_node.parent.parent)
        self.root.color = 'BLACK'
    def rb_insert(self, node_to_insert):
        """Sätter in noder"""
        y_nod = self.nil_leaf
        x_nod = self.root
        z_nod = Node(node_to_insert)
        while x_nod != self.nil_leaf:
            y_nod = x_nod
            if z_nod.value < x_nod.value:
                x_nod = x_nod.left_child
            else:
                x_nod = x_nod.right_child
        z_nod.parent = y_nod
        if y_nod == self.nil_leaf:
            self.root = z_nod
        elif z_nod.value < y_nod.value:
            y_nod.left_child = z_nod
        else:
            y_nod.right_child = z_nod
        z_nod.left_child = self.nil_leaf
        z_nod.right_child = self.nil_leaf
        self.rb_insert_fixup(z_nod)
    def right_rotate(self, node_to_rotate):
        """Roterar trädet åt höger"""
        y_node = node_to_rotate.left_child
        node_to_rotate.left_child = y_node.right_child
        if y_node.right_child != self.nil_leaf:
            y_node.right_child.parent = node_to_rotate
        y_node.parent = node_to_rotate.parent
        if node_to_rotate.parent == self.nil_leaf:
            self.root = y_node
        elif node_to_rotate == node_to_rotate.parent.right_child:
            node_to_rotate.parent.right_child = y_node
        else:
            node_to_rotate.parent.left_child = y_node
        y_node.right_child = node_to_rotate
        node_to_rotate.parent = y_node
    def left_rotate(self, node_to_rotate):
        """Roterar trädet åt vänster"""
        y_node = node_to_rotate.right_child
        node_to_rotate.right_child = y_node.left_child
        if y_node.left_child != self.nil_leaf:
            y_node.left_child.parent = node_to_rotate
        y_node.parent = node_to_rotate.parent
        if node_to_rotate.parent == self.nil_leaf:
            self.root = y_node
        elif node_to_rotate == node_to_rotate.parent.left_child:
            node_to_rotate.parent.left_child = y_node
        else:
            node_to_rotate.parent.right_child = y_node
        y_node.left_child = node_to_rotate
        node_to_rotate.parent = y_node
    def rb_delete_fixup(self, node_to_delete):
        """Fixar om trädet vid borttagning av en nod"""
        while node_to_delete != self.root and node_to_delete.color == 'BLACK':
            if node_to_delete == node_to_delete.parent.left_child:
                w_node = node_to_delete.parent.right_child
                if w_node.color == 'RED':
                    w_node.color = 'BLACK'
                    node_to_delete.parent.color = 'RED'
                    self.left_rotate(node_to_delete.parent)
                    w_node = node_to_delete.parent.right_child
                if w_node.left_child.color == 'BLACK' and w_node.right_child.color == 'BLACK':
                    w_node.color = 'RED'
                    node_to_delete = node_to_delete.parent
                else:
                    if w_node.right_child.color == 'BLACK':
                        w_node.left_child.color = 'BLACK'
                        w_node.color = 'RED'
                        self.right_rotate(w_node)
                        w_node = node_to_delete.parent.right_child
                    w_node.color = node_to_delete.parent.color
                    node_to_delete.parent.color = 'BLACK'
                    w_node.right_child.color = 'BLACK'
                    self.left_rotate(node_to_delete.parent)
                    node_to_delete = self.root
            else:
                w_node = node_to_delete.parent.left_child
                if w_node.color == 'RED':
                    w_node.color = 'BLACK'
                    node_to_delete.parent.color = 'RED'
                    self.right_rotate(node_to_delete.parent)
                    w_node = node_to_delete.parent.left_child
                if w_node.right_child.color == 'BLACK' and w_node.left_child.color == 'BLACK':
                    w_node.color = 'RED'
                    node_to_delete = node_to_delete.parent
                else:
                    if w_node.left_child.color == 'BLACK':
                        w_node.right_child.color = 'BLACK'
                        w_node.color = 'RED'
                        self.left_rotate(w_node)
                        w_node = node_to_delete.parent.left_child
                    w_node.color = node_to_delete.parent.color
                    node_to_delete.parent.color = 'BLACK'
                    w_node.left_child.color = 'BLACK'
                    self.right_rotate(node_to_delete.parent)
                    node_to_delete = self.root
        node_to_delete.color = 'BLACK'
    def rb_delete(self, node_to_delete):
        """Tar väck en nod från trädet"""
        z_nod = self.nil_leaf
        node = self.root
        while node != self.nil_leaf:
            if node.value == node_to_delete:
                z_nod = node
            if node.value < node_to_delete:
                node = node.left_child
            else:
                node = node.right_child
        if z_nod == self.nil_leaf:
            return
        y_nod = z_nod
        y_orginal_color = y_nod.color
        if z_nod.left_child == self.nil_leaf:
            x_nod = z_nod.left_child
            self.rb_transplant(z_nod, z_nod.right_child)
        elif z_nod.right_child == self.nil_leaf:
            x_nod = z_nod.left_child
            self.rb_transplant(z_nod, z_nod.left_child)
        else:
            y_nod = self.find_min_helper(z_nod.right_child)
            y_orginal_color = y_nod.color
            x_nod = y_nod.right_child
            if y_nod.parent == z_nod:
                x_nod.parent = y_nod
            else:
                self.rb_transplant(y_nod, y_nod.right_child)
                y_nod.right_child = z_nod.right_child
                y_nod.right_child.parent = y_nod
            self.rb_transplant(z_nod, y_nod)
            y_nod.left_child = z_nod.left_child
            y_nod.left_child.parent = y_nod
            y_nod.color = z_nod.color
        if y_orginal_color == 'BLACK':
            self.rb_delete_fixup(x_nod)
        del node_to_delete
    def rb_transplant(self, u_node, v_node):
        """Byter postioner på noderna"""
        if u_node.parent == self.nil_leaf:
            self.root = v_node
        elif u_node == u_node.parent.left_child:
            u_node.parent.left_child = v_node
        else:
            u_node.parent.right_child = v_node
        v_node.parent = u_node.parent
    def find_min_helper(self, curr_node):
        """Hittar den minsta noden och ger det till rb_delete funktionen"""
        min_node = curr_node
        if min_node == self.nil_leaf:
            return None
        while min_node.left_child != self.nil_leaf:
            min_node = min_node.left_child
        return min_node
    def find(self, value):
        """Kollar om värdet finns i en nod i trädet och returnar None/Noden"""
        curr_node = self.root
        while curr_node != self.nil_leaf and value != curr_node.value:
            if value < curr_node.value:
                curr_node = curr_node.left_child
            else:
                curr_node = curr_node.right_child
        if curr_node == self.nil_leaf:
            return None
        return curr_node
    def height(self):
        """Returnar höjden för trädet"""
        if self.root != self.nil_leaf:
            if self.root.left_child == self.nil_leaf and self.root.right_child == self.nil_leaf:
                return None
        return self.recursive_height(self.root, 0)
    def recursive_height(self, cur_node, cur_height):
        """Rekursiv subfunktion till height funktionen"""
        if cur_node == self.nil_leaf:
            return -1
        left_height = self.recursive_height(cur_node.left_child, cur_height+1)
        right_height = self.recursive_height(cur_node.right_child, cur_height+1)
        if right_height > left_height:
            return 1+right_height
        return 1+left_height
    def recrusive_path(self, value, cur_node, path_to_node):
        """Rekursiv subfunktion till hitta path"""
        path_to_node.append(cur_node.value)
        if value == cur_node.value:
            return cur_node
        if value < cur_node.value and cur_node.left_child != self.nil_leaf:
            return self.recrusive_path(value, cur_node.left_child, path_to_node)
        return self.recrusive_path(value, cur_node.right_child, path_to_node)
    def recursive_bfs_function(self, root, height, bfs_list):
        """Rekursiv funktion till att BFS listan"""
        curr_node = []
        if root is self.nil_leaf:
            return
        if height == 1 and root.value != 0:
            curr_node.append(root.value)
            curr_node.append(root.color)
            curr_node.append(root.left_child.value)
            curr_node.append(root.right_child.value)
            bfs_list.append(curr_node)
        elif height > 1:
            self.recursive_bfs_function(root.left_child , height-1, bfs_list)
            self.recursive_bfs_function(root.right_child , height-1, bfs_list)
    def insert(self, value):
        """Sätter in noder"""
        if self.search(value) is True:
            return None
        return self.rb_insert(value)
    def remove(self, value):
        """Tar bort noder"""
        if self.search(value) is False:
            return None
        self.rb_delete(value)
        del value
    def min(self):
        """Returnerar min-value"""
        min_node = self.root
        if min_node == self.nil_leaf:
            return None
        while min_node.left_child != self.nil_leaf:
            min_node = min_node.left_child
        return min_node.value
    def max(self):
        """Returnerar max-value"""
        max_value = self.root
        if max_value == self.nil_leaf:
            return None
        while max_value.right_child != self.nil_leaf:
            max_value = max_value.right_child
        return max_value.value
    def bfs(self):
        """ Returns a 2D list with nodes, breadth first """
        bfs_list = []
        queue = []
        queue.append(self.root)
        node = None
        while len(queue) > 0:
            bfs_list.append(queue[0].data_lst())
            node = queue.pop(0)
            if node.left_child != self.nil_leaf:
                queue.append(node.left_child)
            if node.right_child != self.nil_leaf:
                queue.append(node.right_child)
        return bfs_list
    def path(self, value):
        """Returnar pathen till noden ink. rotnoden"""
        path_to_node = []
        if self.root == self.nil_leaf:
            return None
        if self.search(value) is False:
            return None
        self.recrusive_path(value, self.root, path_to_node)
        return path_to_node
    def search(self, value):
        """Letar efter nod och returernar en bool (True/False)"""
        curr_node = self.root
        while curr_node != self.nil_leaf and value != curr_node.value:
            if value < curr_node.value:
                curr_node = curr_node.left_child
            else:
                curr_node = curr_node.right_child
        if curr_node == self.nil_leaf:
            return False
        return True

def main():
    ex_list = [-146, 195, -440, 247, -205, -470, -129, 251, 350, 29, 111, -144, 32, -154,
                         374, -93, -351, 23, 297, 307, -314, 450, 203, -10, 283, 142, 252, 76, 119,
                         153, -191, 458, 465, -301, -478, 312, 40, -265, -302, 381, -68, -120, -404,
                         64, -226, -3, 148, 75, 82, -27, -462, 363, -266, 424, 94, -454, -348, -245,
                         -382, 205, 427, 50, 464, -444, -23, -455, -204, -474, -26, -151, -373, 432,
                         463, -187, -40, -229, -184, -46, -456, -386, -73, 164, -400, -293, 302,
                         159, 118, 104, -87, -6, 170, -222, -88, -329, -337, -164, 174, -425, 196,
                         -30, -280, 340, 33, 453, -346, -398, 15, -72, -447, -98, -45, -64, -295,
                         349, -284, 377, 58, -459, -476, 273, -426, -148, -322, -288, 135, 110,
                         -186, -55, -111, 185, 352, 367, 376, 189, -160, 96, -480, 81, -344, 171,
                         54, 344, -209, -378, 68, -308, -70, -358, -417, -457, 65, -14, -52, -12,
                         -240, -392, 183, 172, -336, -321, 86, 403, 0, 462, -464, -97, 235, -393,
                         8, -216, 457, 198, 249, -217, -225, -374, -359, 175, 433, 446, 166, 320,
                         -112, 71, 288, -407, 216, -449, 27, -41, 91, -367, 217, 77, -379, -206,
                         423, 10, 139, -200]


    new_bst = RedBlackTree()
    for value in ex_list:
        new_bst.insert(value)

    #for value in ex_list[0:45]:
    #    new_bst.remove(value)
    #new_bst.remove(247)
    #new_bst.
    #new_bst.print_bfs()
    #node_list = new_bst.bfs()
    #tree_to_graphviz(node_list, "test.dot")

#main()
