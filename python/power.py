import sys
import re
import time as t
#from terminal import terminal as term

class battery:
    def __init__(self):
        battery.reload(self)

    def reload(self):
        bat0dir = '/sys/class/power_supply/BAT0/'
        with open(bat0dir + 'status', 'r') as s_file:
            self.status = s_file.read().replace('\n','')
        with open(bat0dir + 'charge_full', 'r') as cf_file:
            self.power_full = float(cf_file.read())
        with open(bat0dir + 'charge_now', 'r') as cn_file:
            self.power_now = float(cn_file.read())
    
    def get_val(self, base = 100):
        val = (self.power_now / self.power_full) * base
        return val
    
    def get_bar(self, base = 100):
        pval = round(battery.get_val(self))
        val = round(battery.get_val(self, base))
        delta = base - val
        bar = "|" * val
        bar += "[A]" + ("." * delta)
        color = "[G]"
        if pval <= 40:
            color = "[Y]"
        if pval <= 20:
            color = "[R]"
        return "[A][[" + color + bar + "[A]][E]"

    def is_charging(self):
        if self.status == "Charging":
            return True
        else:
            return False

    def is_full(self):
        if self.status == "Full":
            return True
        else:
            return False

#def main(args):
#    if len(args) > 0 and args[0] == "display":
#        try:
#            base = 100
#            if len(args) > 1 and re.search("^\d+$", args[1]):
#                base = int(args[1])
#            batt = battery()
#            while True:
#                batt.reload()
#                term.clear()
#                term.out(batt.get_bar(base))
#                state_color = "[R]"
#                if batt.is_charging() or batt.is_full():
#                    state_color = "[G]"
#                term.out(state_color + batt.status + " [C]" + str(round(batt.get_val(),2)) + "%   [A]" + t.ctime())
#                t.sleep(1)
#        except KeyboardInterrupt:
#            term.out("...exited")
#            
#
########################################################################################
#if __name__ == "__main__":
#    main(sys.argv[1:])


