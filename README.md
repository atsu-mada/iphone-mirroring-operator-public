# iphone-mirroring-operator

An agent skill for **Claude Code** and **Codex** that operates apps on your iPhone from your Mac, through macOS **iPhone Mirroring** and computer use. It reads app screens, changes settings, and creates items in iPhone apps that have no usable Mac app or API.

The bundled procedures cover:

- **SwitchBot** – read, create, and edit scenes and automations (including weather conditions), tune brightness and color-temperature sliders to target values, and check the result through the SwitchBot API.
- **Obsidian** – a text bridge: typing from the Mac does not reach the iPhone, so text is passed through an Obsidian note and the iPhone clipboard.

日本語の説明は [docs/README.ja.md](docs/README.ja.md) にあります。

## Requirements

- A Mac on **macOS 15 Sequoia or later** with `/System/Applications/iPhone Mirroring.app`, and an iPhone on iOS 18 or later signed in to the same Apple Account (iPhone Mirroring is not available in every region).
- An agent client with computer use: Claude Code (desktop app, computer-use tools) or Codex with computer use.
- For the SwitchBot API check (optional): Python 3 and your own SwitchBot token and secret.
- For the text bridge (optional): Obsidian on both Mac and iPhone, with a vault synced between them (for example through iCloud).

## Install

Clone the repository, then link the skill folder into your client's skills directory.

```bash
git clone https://github.com/atsu-mada/iphone-mirroring-operator.git
```

**Claude Code**

```bash
ln -s "$PWD/iphone-mirroring-operator/src/skills/iphone-mirroring-operator" ~/.claude/skills/iphone-mirroring-operator
```

Start a new session and call it with `/iphone-mirroring-operator`.

**Codex**

```bash
ln -s "$PWD/iphone-mirroring-operator/src/skills/iphone-mirroring-operator" ~/.codex/skills/iphone-mirroring-operator
```

Use the skills folder your Codex version reads (`~/.codex/skills` or `~/.agents/skills`). Start a new session and call it with `$iphone-mirroring-operator`.

### SwitchBot API (optional)

`apps/switchbot/scripts/switchbot_api.py` reads the token and secret from the `SWITCHBOT_TOKEN` and `SWITCHBOT_SECRET` environment variables. Get them from the SwitchBot app's developer options (see the [SwitchBot API docs](https://github.com/OpenWonderLabs/SwitchBotAPI)) and pass them from your own shell or secret manager. Never put them in `.env` files, prompts, or Git.

```bash
python3 -I src/skills/iphone-mirroring-operator/apps/switchbot/scripts/switchbot_api.py devices   # or: scenes / run "<scene name>"
```

To keep a record of your own setup, copy `apps/switchbot/current-settings.example.md` to `current-settings.md` (ignored by Git).

## Safety rules

The skill tells the agent to:

- Show every change as a list and save it only after you say OK. Edit screens opened only for reading are left without saving.
- **Never enter** your Mac password, Touch ID, or iPhone passcode – you unlock them yourself.
- **Never buy, send, post, or tap links**, and never change account or notification settings. Permission prompts that appear midway are declined or cancelled.
- Run real devices (such as lights) only when you ask, and return them to the state that fits the time of day afterwards.
- Close unexpected screens without changing anything, and report honestly if something may have been saved.

## Known limits

- **Typing from the Mac does not reach the iPhone.** Typed letters arrive as "a", and the Mac clipboard is not shared. Text goes through the Obsidian bridge: make a one-line note, open it on the iPhone, copy it there with `cmd+a` / `cmd+c`, and paste with `cmd+v`.
- Spotlight on the iPhone cannot be used (no search text), so apps are opened from the home screen.
- Using the iPhone itself disconnects mirroring. Keep it locked and put down while the agent works.
- Sliders show no numbers in some apps, and drags stop a few pixels off. The skill tunes values in 1 px steps and reads the result from the saved screen or the API. Coordinates change when the mirroring window moves.
- Measured slider scales and screen texts were recorded on macOS 26 with the SwitchBot app as of October 2026; app updates may change them.

## Layout

```
src/skills/iphone-mirroring-operator/
  SKILL.md                 entry point (workflow, safety gates)
  references/              mirroring basics, value tuning
  apps/switchbot/          scenes, automations, settings example, API script
  apps/obsidian/           text bridge
  agents/openai.yaml       Codex display metadata
```

The skill text is written in Japanese.

## License

[MIT](LICENSE)
