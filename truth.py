if 0:# khi if chỉ có giá trị 0 thì python tự hiểu 0 là false và sẽ chạy điều kiện else khi false
    print("True")
else:
    print("False")

name = input("Please enter your name:  ")
#if name:#khi string rỗng thì python tự hiểu là false và chạy điều kiện else khi false
if name != "":
    print("Hello, {}".format(name))
else:
    print("You are a man with no name")