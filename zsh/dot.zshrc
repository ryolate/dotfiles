# .zshrc
# manual: man zshall

bindkey -e # emacs keymap

HISTFILE=~/.histfile
HISTSIZE=1000000
SAVEHIST=1000000

# tmux uses vi-style key bindings if EDITOR contains 'vi'.
export EDITOR=vim

# see EXPANSION OF PROMPT SEQUENCES in man zshmisc.
export PROMPT="%B%F{green}%n %F{blue}%T %b%f[%1~]
%F{blue}->%B %# %b%f"

if [ -f ~/.zshrc.user ]; then
    . ~/.zshrc.user
fi
