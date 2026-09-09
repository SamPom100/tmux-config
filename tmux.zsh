if (( ! $+functions[compdef] )); then
   autoload -Uz compinit
   compinit
fi

alias tls="tmux list-sessions -F '#{session_name}: #{session_windows} tab(s) | Active Tab: #W (#{pane_current_path})' 2>/dev/null || print -r -- 'nothing running'"

function attach() {
   if (( $# > 0 )); then
      tmux attach-session -t "$1"
   elif [[ -n "$TMUX" ]]; then
      tmux choose-tree -sZ
   else
      tmux attach-session \; choose-tree -sZ
   fi
}

function _attach() {
   local -a sessions
   sessions=("${(@f)$(tmux list-sessions -F '#S' 2>/dev/null)}")
   _describe -t sessions 'tmux session' sessions
}

compdef _attach attach
zstyle ':completion:*:*:attach:*' menu yes select
