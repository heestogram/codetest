def time_calc(in_time, out_time):
    result = 0
    if int(in_time[3:]) <= int(out_time[3:]):
        result += 60*(int(out_time[:2]) - int(in_time[:2]))
        result += (int(out_time[3:]) - int(in_time[3:]))
    else:
        result += 60*(int(out_time[:2]) - int(in_time[:2])-1)
        result += (60-(int(in_time[3:])-int(out_time[3:])))
    return result

print(time_calc("05:34","06:10"))