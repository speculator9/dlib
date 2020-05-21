def find_key(file: list, key: str):
    """Function returns the start and end of the Keyword ass tuple in num list
    1. file: list of output of f.readlines()
    2. key: str of key
    """
    # define empty list for tuples of start and end
    num = []
    # define empty list to add all the matches found
    dup = []
    # iterate over the lines in file (file is list from f.readlines()
    for line_num, line in enumerate(file):
        # if the key is in the line do following
        if key in line:
            # num.append(line_num)
            dup.append("found")
            # take the slice of the file starting from that line+1
            slice = file[line_num + 1:]

            # loop over slice
            for line_num_, line_ in enumerate(slice):
                # if * is in the slice means start of new keyword
                if "*" not in line_:
                    num.append(line_num + line_num_ + 1)
                else:
                    break
        # print(i)
    return num, len(num)
