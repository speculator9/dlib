def find_key(file: list, key: str):
    """Function returns the start and end of the Keyword ass tuple in num list
    1. file: list of output of f.readlines()
    2. key: str of key
    """
    # define empty list for tuples of start and end
    num_list = []

    # iterate over the lines in file (file is list from f.readlines()
    for line_num, line in enumerate(file):
        # if the key is in the line do following
        if key == line:
            num = []
            line_list = []

                       # take the slice of the file starting from that line+1
            slice = file[line_num + 1:]

            # loop over slice
            for line_num_, line_ in enumerate(slice):
                # if * is in the slice means start of new dyna
                if "*" not in line_:
                    num.append(line_num + line_num_ + 1)
                    line_list.append(line_)
                else:
                    break

            num_list.append(line_list)

    return num_list
