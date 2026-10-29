---
name: iphone-mirroring-operator
description: Operate apps on the user's iPhone from the Mac through the iPhone Mirroring app with computer use - read app screens, change settings, and create items in apps that have no usable Mac or API route. App-specific procedures live in one folder per app under apps/ (currently SwitchBot scenes and automations, and Obsidian as a text bridge for typing Japanese into iPhone apps). Use for "iPhoneのアプリを操作して", "ミラーリングで設定して", "SwitchBotのシーン/オートメーションを変えて", or when an iPhone-only setting must be read or changed. Does not unlock the Mac or iPhone, enter passwords, buy anything, send messages, or tap links; text typed from the Mac does not reach the iPhone, so typing goes through the Obsidian bridge.
---

# iPhone Mirroring Operator

## Shared client contract

- Codex invocation: `$<iphone-mirroring-operator>`
- Claude Code invocation: `/iphone-mirroring-operator`
- Resolve bundled files relative to this skill's own folder (the folder that holds this `SKILL.md`).
- Apply the active client's own authentication, approval, browser/app, connector, and external-action rules. A capability or permission available in one client does not transfer to the other.

Mac の「iPhone ミラーリング」アプリを computer use で操作して、iPhone のアプリを読み取り・設定する。どのアプリにも共通する操作は `references/`、アプリ固有の手順と設定は `apps/<app>/` に置く。

| 共通 | 内容 |
| --- | --- |
| [references/mirroring-basics.md](references/mirroring-basics.md) | 接続とロック、操作モード、画面の読み方、まとめて送るときの注意、キー操作、スクロール、保存しない戻り方 |
| [references/value-tuning.md](references/value-tuning.md) | スライダーとピッカーで狙った数値に合わせる手順 |

| アプリ | フォルダ | 内容 |
| --- | --- | --- |
| SwitchBot | [apps/switchbot/](apps/switchbot/README.md) | API とアプリの役割分担、シーン（[scenes.md](apps/switchbot/scenes.md)）、オートメーション（[automations.md](apps/switchbot/automations.md)）、今の設定の書き方の例（[current-settings.example.md](apps/switchbot/current-settings.example.md)） |
| Obsidian | [apps/obsidian/](apps/obsidian/README.md) | 日本語の文字を iPhone へ渡すためのコピー元 |

新しいアプリを足すときは `apps/<app>/README.md` を作り、上の表に1行足す。どのアプリでも使える気づきは `references/` に、そのアプリだけの気づきは `apps/<app>/` に書く。

## Input contract

- 対象のアプリと、読むだけか変更するか。変更なら、名前・数値・条件の一覧
- Mac が macOS 15 以降で、`/System/Applications/iPhone Mirroring.app` があること

## Safety gates

- 変更は、内容を一覧で見せてユーザーの OK をもらってから保存する。読み取りの途中で開いた編集画面は、保存せずに戻る
- Mac のパスワード、Touch ID、iPhone のパスコードはユーザーが入れる。エージェントは入力しない
- 購入、送信、投稿、リンクのタップ、アカウント設定・通知設定の変更はしない。途中で出た通知許可などの確認は、拒否または「Cancel」を選ぶ
- 照明の実行など、現実の機器が動く操作は、ユーザーが頼んだとき（値の確認や調整を含む）だけ行う。確認のために動かしたあとは、その時間帯に合う状態へ戻して伝える
- 意図しない画面が開いたら、何も変えずに閉じる。保存してしまった可能性があれば、正直に報告する
- iPhone 本体が操作されるとミラーリングは切れる。作業中は iPhone をロックして置いてもらう

## Workflow

1. `request_access` で「iPhone Mirroring」を許可してもらい、開く。ロック画面ならユーザーに解除を頼んで待つ
2. [references/mirroring-basics.md](references/mirroring-basics.md) の方法で画面を読み、目的のアプリを開く
3. 対象アプリの `apps/<app>/README.md` の手順で読み取る。結果と変更案をユーザーに見せる
4. 名前などの文字入力が要るなら、[apps/obsidian/README.md](apps/obsidian/README.md) のテキスト受け渡しを使う
5. OK をもらったら変更して保存し、保存後の一覧画面か API で反映を確かめる。数値を合わせるときは [references/value-tuning.md](references/value-tuning.md) の手順で寄せる
6. 作業用に作ったノートを片付け、動かした機器を戻し、変更内容と確認結果、残った注意点を報告する
7. 今回の作業で分かったことを、共通なら `references/`、アプリ固有なら `apps/<app>/` に書き足す。設定を変えたら、そのアプリの「今の設定」の表も更新する

## Success definition

頼まれた読み取りまたは変更が終わり、保存後の画面か API で反映を確かめ、作業用のノートが残っていない。
