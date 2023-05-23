class Node:
    def __init__(self, data):#khởi tạo giá trị nút gốc lưu giá trị là data,hai con trỏ (left và right) là nút con trái và nút con phải.
        self.goc = data
        self.left = None
        self.right = None

def in_node(node, level=2):#node đại diện cho 1 tham số của cây, level là độ thụt lề cho cây
    if node is not None:# nếu giá trị của tham số node có thì đệ quy duyệt nút con trái với độ thụt lề là -1
        in_node(node.left, level - 1)
        in_node(node.right, level + 3)# đệ quy gọi nút con phải với độ tht lề 3
        print("    " * level + str(node.goc))#sử dụng khoảng trắng để tạo hình đi kèm với độ thụt lề level định hình
        #dạng cây

# Tạo cây
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Hiển thị hình cây theo thứ tự sau
print("Hình cây theo thứ tự sau:")
in_node(root)