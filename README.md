# Browser-Style Clickable Tabs for tmux

A minimal, modern tmux configuration that gives you top, browser-style clickable tabs and full mouse support over SSH.

## Features

- 🗂️ **Top Status Bar**: Tab bar at the top of the terminal screen, styled like browser tabs.
- 🖱️ **Full Mouse Support**: Click tab titles to switch windows, drag pane borders to resize, scroll wheel enabled.
- 🔢 **1-Based Indexing**: Tabs start at `1` to align naturally with keyboard shortcuts (`Ctrl-b 1`, `Ctrl-b 2`, etc.).
- 🔄 **Auto-Renumbering**: Automatically cleans up tab numbering when tabs are closed.
- 🏷️ **Automatic Window Titles**: Tabs show the active running command or directory name automatically.

## Quick Installation

### Option 1: Direct Download (One-liner for local or SSH server)

```bash
curl -sL https://gist.githubusercontent.com/SamPom100/80369305e20cea359d97946ef742fa82/raw/.tmux.conf -o ~/.tmux.conf
```

### Option 2: Clone repository

```bash
git clone https://github.com/SamPom100/tmux-config.git ~/tmux-config
cp ~/tmux-config/.tmux.conf ~/.tmux.conf
```

## Basic Usage

| Action | Command / Shortcut |
|---|---|
| **Start tmux** | `tmux` |
| **Switch Tabs** | **Click tab title at top** or `Ctrl-b <number>` |
| **New Tab** | `Ctrl-b c` |
| **Rename Tab** | `Ctrl-b ,` |
| **Close Tab** | Type `exit` or `Ctrl-d` |
| **Vertical Split** | `Ctrl-b %` |
| **Horizontal Split** | `Ctrl-b "` |
