import keyboard
import time
import sys

FACING = {'north', 'south', 'west', 'east'}
HALF = {'top', 'bottom'}
SHAPE = {'inner_left', 'inner_right', 'outer_left', 'outer_right', 'straight'}

def replace(rfrom, rto):
    return {f'//replace {rfrom}[facing={f},half={h},shape={s}] {rto}[facing={f},half={h},shape={s}]\n' for f in FACING for h in HALF for s in SHAPE}

    
if __name__=='__main__':
    rfrom = ''
    rto = ''
    if len(sys.argv) > 1:
        rfrom = sys.argv[1]
        rto = sys.argv[2]
    else:
        rfrom = input('FROM:')
        rto = input('TO:')

    repl = replace(rfrom, rto)
    print('PRESS space to continue')
    keyboard.wait('space')

    for e in repl:
        print(e)
        keyboard.send('t')
        time.sleep(0.5)
        keyboard.write(e,0)
        print('PRESS space to continue')
        keyboard.wait('space')
    