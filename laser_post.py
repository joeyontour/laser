prev_prev_line = ''
prev_line = ''
step = 0.1
fout = open('post.gcode', 'wt')
with open('gcode.gcode') as fp:
    line = fp.readline()
    while line:
        
        if prev_line.startswith('S'):
            x = float(prev_prev_line[4:10])
            y = float(prev_prev_line[12:17])
            x_offset = float(line[4:10]) - x
            y_offset = float(line[12:17]) - y
            f = line[18:22]
            x_new = 0.0
            y_new = 0.0
            
            
            if x_offset > 0:
                x_new = x + step
            else:
                x_new = x - step
                
            if y_offset > 0:
                y_new = y + step
            else:
                y_new = y - step   
            fout.write('G1 X' + '%.2f' % x + ' Y' + '%.2f' % y + ' ' + prev_line)
            fout.write('G1 X' + '%.2f' % x_new + ' Y' + '%.2f' % y_new + ' ' + f + '\n')
            fout.write('G1 X' + '%.2f' % x + ' Y' + '%.2f' % y + '\n')
        else:
            if not line.startswith('S'):
                fout.write(line)
        prev_prev_line = prev_line
        prev_line = line
        line = fp.readline()
		
fout.close()
		