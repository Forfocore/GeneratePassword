def next_array(array, max_symbol):
    array_count= [i for i in range(0, len(array))]
    c_symbols = max_symbol

    if len(array) == 0:
        return None

    else:
        if array[0] == c_symbols - 1:
            array[0] = 0
            plus = True

            if len(array) > 1:
                for i in array_count:
                    if i > 0:
                        if plus:
                            if array[i] < c_symbols - 1:
                                array[i] = array[i] + 1
                                break

                            elif array[i] == c_symbols - 1:
                                array[i] = 0
                                if i == len(array) - 1:
                                    array.append(0)
                                    break

            else:
                array.append(0)
        elif array[0] < c_symbols - 1:
            array[0] = array[0] + 1

    return array