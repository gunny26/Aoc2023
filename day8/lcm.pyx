#!/usr/bin/python3
import time

def lcm_with_offset(*offset_and_step):
    """
    list of two entry list

    [offset1, step1], [offset2, step2], ... [offsetN, stepN]
    """
    min_value = None  # finding min values, by offset
    for entry in offset_and_step:
        if min_value is None:
            min_value = list(entry)
        else:
            if entry[0] < min_value[0]:  # using offset to chose mininmal value
                min_value = list(entry)
                # min_values = [cdef int int(entry[0]), cdef int int(entry[1])]
    print("chosen min value: ", min_value)

    other_values = list(offset_and_step)
    other_values.remove(min_value)

    print("other values to compare: ", other_values)

    cdef int progress = 1  # progress counter
    cdef float starttime = time.time()

    while True:

        ret = []
        for entry in other_values:
            diff = min_value[0] - entry[0]
            # print(entry, diff, max(diff, 0) % entry[1])
            if diff < 0:  # some other values are greater, keep on
                ret.append(False)
            else:
                ret.append(max(diff, 0) % entry[1] == 0)

        if ret.count(True) > 2:
            print(ret)

        if all(ret):  # check if all other series without remainder
            print(ret)
            break  # thats it

        min_value[0] += min_value[1]
        # print(min_value)
        # print()

        if progress % (10 ** 6) == 0:
            print(f"{10**6} iterations done in {(time.time()-starttime):0.2f}")
            starttime = time.time()
        progress += 1

    return min_value[0]

if __name__ == "__main__":
    print(lcm_with_offset([100, 3], [110, 4], [120, 5]))
    print(lcm_with_offset([123234, 3], [23452345, 4], [12312312, 5]))

