def read_file_safely(filename):
    try:
        file=open(filename, 'r')
        data=file.read()
        flie.close()
        return data
    
    except FileNotFoundError:
        return "File not found."
    
print(read_file_safely("demo.txt"))
