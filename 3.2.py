

alphabet = "abcdefghijklmnopqrstuvwxyz"
def modify_every_3rd_to_upper(values):
    for i in range(len(values), 3):
        values[i] = values[i].upper()

as_list = list(alphabet)
modify_every_3rd_to_upper(as_list)
print(as_list)