#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for li in range(list_length):
        try:
            res = my_list_1[li]/my_list_2[li]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("Out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except Exception as e:
            print(e)
        finally:
            res_list.append(res)
    return res_list
