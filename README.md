# Browser-Style Clickable Tabs & GUI Toolbar for tmux


> ` + │ - │ ◧ │ ⬒ │ ⛶ │ 🚪 │ 🖱 │ ↕    1: 🤖 gemini: ~    2: 📁 ~    22:51 `

## Features

- 🗂️ **Top Status Bar**: Browser-style tabs pinned across the top of your terminal window.
- 🖱️ **Clickable GUI Toolbar**: Top-left mouse buttons for quick actions:
  - ` + ` — New Tab *(opens in current working directory)*
  - ` - ` — **Smart Close** *(closes active split pane -> closes tab -> exits tmux if last tab!)*
  - ` ◧ ` — Split Screen Side-by-Side (Vertical)
  - ` ⬒ ` — Split Screen Top/Bottom (Horizontal)
  - ` ⛶ ` — Zoom / Fullscreen Toggle *(expands active pane to 100%)*
  - ` 🚪 ` — **Detach Session** *(exits to shell, leaving all tabs/agents running in background)*
  - ` 🖱 `: Release mouse capture for five seconds
  - ` ↕ ` — Scroll / History Mode Toggle *(click to turn ON/OFF)*
- 🤖 **Smart AI Agent Badges**: Automatic `🤖 gemini: ~` or `🤖 agy: ~` badges when running AI CLIs, and `📁 ~` for clean folder paths.
- 🔢 **1-Based Indexing & Auto-Renumbering**: Tabs start at `1` (`Ctrl-b 1`, `Ctrl-b 2`) and renumber automatically when closed.
- 📋 **System Clipboard & Mouse Support**: Click the mouse button for native text selection. Mouse capture returns after five seconds.

## ⚡ Quick 1-Line Installation

Run this single command on any local computer or SSH server:

```bash
curl -sL https://raw.githubusercontent.com/SamPom100/tmux-config/main/.tmux.conf -o ~/.tmux.conf
```

Or clone the repository:

```bash
git clone https://github.com/SamPom100/tmux-config.git ~/tmux-config
cp ~/tmux-config/.tmux.conf ~/.tmux.conf
```

## 💡 Shell Shortcuts (zsh)

Download [tmux.zsh](tmux.zsh):

```sh
curl -fsSL https://raw.githubusercontent.com/SamPom100/tmux-config/main/tmux.zsh -o ~/.tmux.zsh
```

If your `~/.zshrc` contains `alias tmux="tmux attach || tmux"`, remove that line.
Add this line to your `~/.zshrc`:

```zsh
source "$HOME/.tmux.zsh"
```

Open a new terminal to load the shortcuts.

| Command | Behavior |
|---|---|
| `tls` | Lists sessions, or prints `nothing running` when no sessions exist. |
| `attach` | Opens the session selector. |
| `attach <name>` | Attaches to the named session. |
| `attach ` then Tab | Shows session names and completes partial names. |

## ⌨️ Controls & Shortcuts

### Toolbar Buttons (Mouse Clickable)

| Button | Action |
|---|---|
| **` + `** | **New Tab** *(opens in current folder)* |
| **` - `** | **Smart Close** *(pane -> tab -> exit tmux)* |
| **` \| `** | **Split Side-by-Side** (Vertical) |
| **` _ `** | **Split Top/Bottom** (Horizontal) |
| **` ⛶ `** | **Zoom / Fullscreen Toggle** *(expands pane to 100%)* |
| **` 🚪 `** | **Detach Session** *(leave running in background)* |
| **` 🖱 `** | **Release mouse capture for five seconds** |
| **` ↕ `** | **Scroll Mode Toggle** *(click to enter/exit history)* |

### Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| **Click Tab Title** | Switch directly to tab |
| **Right-click Top-Left Toolbar**, then **Rename** | Rename current session |
| `Ctrl-b` then `1` .. `9` | Jump directly to Tab 1-9 |
| `Ctrl-b` then `c` | New Tab |
| `Ctrl-b` then `,` | Rename current tab |
| `Ctrl-b` then `\|` | Split Side-by-Side |
| `Ctrl-b` then `-` | Split Top/Bottom |
| `Ctrl-b` then `z` | Zoom / Fullscreen toggle active pane |
| `Ctrl-b` then `d` | Detach session *(leave running in background)* |
| `Ctrl-b` then `/` | Search text in current tab |
| `Ctrl-b` then `Shift-S` | Search text across ALL tabs |
| `Ctrl-b` then `m` | Toggle mouse support |
| `Ctrl-b` then `f` | Open clean 1-line tab list |

---

### Reconnect Anytime
```bash
tmux attach
```
