import time as t
from terminal import terminal as term
from power import battery

if __name__ == "__main__":

    GROUND = 128
    try:
        batt = battery()
        while True:
            batt.reload()

            pval = round(batt.get_val(),2)

            val = int(round(batt.get_val(GROUND)))
            delta = GROUND - val

            bar = '\u25AE' * val
            bar += '[A]' + ('-' * delta)
    
            line_p1 = '  ' + batt.status + ' '
            line_p2 = str(pval) + '%'
            line_p4 = t.ctime() + '  '
            
            line_p3 = (GROUND - len(line_p1) - len(line_p2) - len(line_p4)) * ' '

            scolor = '[R]'
            if batt.is_charging() or batt.is_full():
                scolor = '[G]'

            line = scolor + line_p1 + '[C]' + line_p2 + line_p3 + '[A]' + line_p4

            color = "[G]"
            if pval <= 40:
                color = "[Y]"
            if pval <= 20:
                color = "[R]"

            term.out(color + bar,'\n')
            term.out(line,'\r')
            t.sleep(1)

    except KeyboardInterrupt as e:
        term.out("\n\n\nBye Bye")
