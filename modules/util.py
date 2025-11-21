def read(file):
    pass

def write(file,msg):
    fid = open(file,'w')
    fid.write(msg)
    fid.close()