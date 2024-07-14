def format_the_strings3():
    args3 =[2, 3.1415926, .0000001, .7, 5]
    # Expected output format
    #“002.00"
    #“003.14'
    #“000.OO
    #“000.70”
    #“005.00"
    output = []

    for i in args3:
        # Complete the function
        output.append("{:-6d}".format( int(i )))
    
    print(output)
    return output


def read_file(file_name):
    """
    INPUT: a file name
    OUTPUT: A list of strings (not a single string) where each string is a number
    Hint
    1. 0pen the file
    2. Read the File (Hint: you may need .split()and/or .replace())
    3. Close the File
    4.Return its contents
    """
    # TOD0: complete the function
    output = []
    with open(file_name,"r") as file:
        for line in file:
           content_split = line.strip()
           output.append(content_split)
    file.close()

    return output


def read_file1(file_name):
    with open(file_name,"r") as file:
        context = file.read()
    file.close()

    return context.split("\n")



def read_file2(file_name):
    output = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            output.append(line.strip())
    file.close()

    return output


def read_file3(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    file.close()

    return lines


print(read_file("roy.txt"))
print()
print(read_file2("roy.txt"))
print()
print(read_file3("roy.txt"))
