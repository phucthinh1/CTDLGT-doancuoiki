class Node:
    def __init__(self, data):#khởi tạo giá trị nút gốc lưu giá trị là data,hai con trỏ (left và right) là nút con trái và nút con phải.
        self.ben_trai = None
        self.ben_phai = None
        self.goc = data

    # tạo hàm in cây
    def in_cay(self):
        # nếu có phần tử con nào bên trái thì in ra
        if self.ben_trai:
            self.ben_trai.in_cay()

        # in gốc
        print(self.goc)

        # nếu có phần tử con nào bên phải thì in ra
        if self.ben_phai:
            self.ben_phai.in_cay()

    def chen_so(self, nhap_so):
        # so sánh phẩn tử con mới với gốc
        if self.goc:
            # nhập số vào, nếu phần tử được nhập vào bé hơn so với gốc thì nó nằm bên trái
            if nhap_so < self.goc:
                if self.ben_trai is None:
                    self.ben_trai= Node(nhap_so)
                else:
                    self.ben_trai.chen_so(nhap_so)

            # nhập số vào, nếu phần tử được nhập vào lớn hơn so với gốc thì nó nằm bên phải
            elif nhap_so > self.goc:
                if self.ben_phai is None:
                    self.ben_phai = Node(nhap_so)
                else:
                    self.ben_phai.chen_so(nhap_so)
        else:
            self.goc = nhap_so


root = Node(69)
root.chen_so(39)
root.chen_so(79)
root.chen_so(608)
root.chen_so(75)
root.chen_so(30)
root.chen_so(80)

root.in_cay()


