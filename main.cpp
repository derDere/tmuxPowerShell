#include <iostream>
#include <cstdlib>

using namespace std;

int main(void) {
  system("setsid python /opt/tmuxPowerShell/python/tmux_power_bar.py >/dev/null 2>&1 < /dev/null &");

  system("/opt/tmuxPowerShell/tmuxMain.sh");
  
  system("pkill -f \"python /opt/tmuxPowerShell/python/tmux_power_bar.py\"");
  
  return 0;
}