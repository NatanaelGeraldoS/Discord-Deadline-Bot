import datetime


def convertdate(data):
    # print("Asdad")
    # print(data.year)
    # print(data.month)
    # print(data.day)
    # print(datetime.date(data.year, data.month, data.day))
    return datetime.date(data.year, data.month, data.day)
# AI Tugas 2 (Aplha Beta Pruning) - 11/10/2021


def takedate(data):
    date = data[data.index(' - ')+3:]
    # print(date)
    day = date[:2]
    # print(day)
    month = date[3:5]
    # print(month)
    year = date[6:]
    # print(year)
    # print(datetime.date(int(year), int(month), int(day)))
    return datetime.date(int(year), int(month), int(day))


def bubblesort(list):

    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1, 0, -1):
        for idx in range(iter_num):
            if takedate(list[idx]) > takedate(list[idx+1]):
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
