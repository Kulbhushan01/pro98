def swapFileData(file1, file2):
    try:
        with open(file1, 'r') as file1_handle:
            data_a = file1_handle.read()

        with open(file2, 'r') as file2_handle:
            data_b = file2_handle.read()

        with open(file1, 'w') as file1_handle:
            file1_handle.write(data_b)

        with open(file2, 'w') as file2_handle:
            file2_handle.write(data_a)

        print("Files swapped successfully!")
    
    except Exception as e:
        print("An error occurred:", str(e))


file1 = "demo1.txt"
file2 = "demo2.txt"

swapFileData(file1, file2)
