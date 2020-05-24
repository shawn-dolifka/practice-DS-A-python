def draw_line(tick_length, label=''):
    line = '-' * tick_length
    if label:
        line += ' ' + label
    else:
        pass
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
    else:
        pass

def draw_ruler(inches, major_tick_length):
    draw_line(major_tick_length, '0')
    for j in range(1, 1 + inches):
        draw_interval(major_tick_length - 1)
        draw_line(major_tick_length, str(j))

#draw_ruler(1,3)
draw_interval(3)