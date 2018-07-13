SESSION=main
tmux="tmux -2"

$tmux has-session -t $SESSION
if [ $? -eq 0 ]; then
	$tmux attach -t $SESSION
	exit 0;
fi

$tmux new-session -d -s $SESSION
$tmux new-window -t $SESSION:0
$tmux send-keys -t $SESSION:0.0 "menu" Enter
$tmux select-pane -t $SESSION:0.0

$tmux attach -t $SESSION
