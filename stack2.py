# tạo mảng stack
def create_stack():
    stack = []
    return stack

# tạo mảng ngăn xếp trống
def check_empty(stack):
    return len(stack) == 0


# thêm phần tử vào stack
def push(stack, item):
    stack.append(item)
    print("thêm phần tử: " + item)

# xáo phần tử khỏi stack
def pop(stack):
    if (check_empty(stack)):
        return "không có phần tử để xóa"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("xóa phần tử: " + pop(stack))

print("stack sau khi xóa phần tử: " + str(stack))

if not stack: #kiểm tra xe stack có rỗng hay không,nếu không thì in ra màn hình top của stack
    print("stack rỗng")
else:
    print("stack không rỗng, top là :", stack[-1])




# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(len(stack))
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
#
# stack.append(5)
#
# if not stack:
#     print("Stack is empty!")
# else:
#     print(f"Stack is not empty, top is: {stack[-1]}")