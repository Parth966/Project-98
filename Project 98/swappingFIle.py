def swapFileData():
    file1input = input("What is the file path for file 1?")
    file2input = input("What is the file path for file 2?")
    with open (file1input,"r") as a:
        data_a = a.read()

    with open (file2input,"r") as a:
        data_b = a.read()

    with open (file1input,"w") as a:
        a.write(data_b)

    with open (file2input,"w") as a:
        a.write(data_a)

swapFileData()
