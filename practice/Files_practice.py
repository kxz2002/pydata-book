f=open("F:/Repos/pydata-book/practice/test.txt","r",encoding="UTF-8")
# print(f,type(f))

#read
# print(f"read 10 bytes {f.read(10)}") read 10 bytes 1234567890
# print(f"read all {f.read()}")

#readlines
# lines = f.readlines()
# print(f"type of lines {type(lines)}") type of lines <class 'list'>
# print(lines) ['12345678901\n', '12345678902\n', '12345678903\n', '12345678904']

#readline
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(line1) 12345678901
# print(line2) 12345678902
# print(line3) 12345678903

#for循环实现文件行读取
# for line in f:
#     print(f"line content: {line}")

#解除文件占用
f.close()

#with open 语法
#调用完之后自动关闭，不需要close
# with open("F:/Repos/pydata-book/practice/test.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(f"line content: {line}")

#练习案例
# f = open("F:/Repos/pydata-book/practice/test2.txt","r",encoding="UTF-8")
# count = 0
# for line in f:
#     line = line.strip()
#     words = line.split(" ")
#     for item in words:
#         if(item == "abcd"):
#             count+=1

# print(f"abcd has shown {count} times")
# f.close()

#写的操作write
#如果打开了已经存在的文件，会把文件里的内容覆盖掉
#如果打开了不存在的文件，就会直接新建一个
f = open("F:/Repos/pydata-book/practice/test3.txt","w",encoding="UTF-8")
f.write("hello world\n") #只是写到了缓存区里，并没有刷新进入硬盘
f.flush() #刷进硬盘
f.close #close自带了flush

#append mode
#只是把内容追加在了末尾，模式改为a，其余都与a相同
f = open("F:/Repos/pydata-book/practice/test3.txt","a",encoding="UTF-8")
f.write("hello python!")
f.flush()
f.close()




