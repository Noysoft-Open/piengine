
lines = []

keyword = {
    "camera" : "camera",
}

def readfile(filepath):

    try:
        file = open(filepath, 'r')
        for line in file:
            line = line.split()
            if line != " " or line != "\n" or line != "\t":
                lines.append(line)
    except:
        raise Exception("File not found: %s" % filepath)
    

def parse():
    for l in lines:
        if keyword["camera"] == "camera":
            print("%s \n" % l)

readfile("data.txt")
parse()