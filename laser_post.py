prev_prev_line = ''
prev_line = ''
step = 0.1
fout = open('post.gcode', 'wt')
with open('gcode.gcode') as fp:
    line = fp.readline()
    while line:
        
        if prev_line.startswith('S'):
            x_index = prev_prev_line.index('X') + 1
            y_index = prev_prev_line.index('Y') + 1
            x = float(prev_prev_line[x_index:(x_index+6)])
            y = float(prev_prev_line[y_index:(y_index+6)])
            
            x_index_next = line.index('X') + 1
            y_index_next = line.index('Y') + 1
            x_next = float(line[x_index_next:(x_index_next+6)])
            y_next = float(line[y_index_next:(y_index_next+6)])
            
            x_offset = x_next - x
            y_offset = y_next - y
            
            f_index = line.index('F')
            f = line[f_index:(f_index+4)]
            
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
		