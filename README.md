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
- 🏷️ **Auto-Named Sessions**: Numbered sessions running Claude Code or Codex take a lowercase name from the agent task title, such as `review-cr-309447414-test-request`. The name follows the task until you rename the session by hand.
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

### Codex goal titles

Codex can omit the task title for a session.
This happens when the session starts with `/goal`, and sometimes after a normal first prompt.
The optional hook uses the goal text, or else the first prompt, until Codex supplies a task title.
A URL in the text becomes its ticket or CR ID, or else its last named path segment.
It reads the local Codex databases and updates only the tmux pane.

From this checkout, install the hook:

```sh
mkdir -p ~/.codex/hooks
cp codex_tmux_title.py ~/.codex/hooks/
```

Add this handler to both `SessionStart` and `PreToolUse` in `~/.codex/hooks.json`:

```json
{
  "type": "command",
  "command": "python3 \"$HOME/.codex/hooks/codex_tmux_title.py\"",
  "timeout": 5
}
```

For `SessionStart`, use the matcher `startup|resume|clear|compact`.
For `PreToolUse`, use a new group without a matcher.
Keep the existing handlers.
Use `/hooks` in Codex to review and trust the new handlers.
Then start a new Codex session.

### Claude Code goal titles

Claude Code does not make a session title when the first prompt is `/goal`.
The tab then shows `✳ Claude Code`.
The optional hook sets the session title from the goal text.
It shortens URLs the same way as the Codex hook.
It acts only when the session has no title.
Other sessions keep the title from Claude Code.

From this checkout, install the hook:

```sh
mkdir -p ~/.claude/hooks
cp claude_goal_title.py ~/.claude/hooks/
```

Add this group to `hooks.UserPromptSubmit` in `~/.claude/settings.json`:

```json
{
  "hooks": [
    {
      "type": "command",
      "command": "python3 \"$HOME/.claude/hooks/claude_goal_title.py\"",
      "timeout": 5
    }
  ]
}
```

Keep the existing hooks.
A running session loads the hook and sets its title on the next prompt.
The hook was tested with Claude Code 2.1.280.

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
