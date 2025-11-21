def open_file(file):    
    fid = open(file,'r')
    lines = fid.readlines()
    for line in lines:
    for line in lines:
        print(line.rstrip())

    print(line)
    fid.close()

open_file("testFile")


'''def open_file(file):    
    fid = open(file,'r')
    # lines = fid.readlines()
    #for line in lines:
    for line in fid:
        print(line.rstrip())

    print(line)
    fid.close()'''