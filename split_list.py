def split_list(list, n):
    for index in range(len(list)):
        yield list[index:index+n]


#------ main ------
#use
# example_list => list
# num          => int
result = list(split_list(exampe_list, num)


# result => list : [ [], [], [], []....]              
