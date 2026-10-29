# iphone-mirroring-operator（日本語）

Mac の「**iPhone ミラーリング**」と computer use を使って、Mac から iPhone のアプリを操作する **Claude Code / Codex 用のスキル**です。Mac 版のアプリや API がない iPhone アプリで、画面を読む・設定を変える・項目を作ることができます。

入っている手順：

- **SwitchBot**：シーンとオートメーション（天気の条件を含む）の読み取り・作成・編集、明るさと色温度のスライダーを狙った値に合わせる方法、SwitchBot API での確認
- **Obsidian**：文字の受け渡し。Mac から打った文字は iPhone に届かないため、Obsidian のノートと iPhone のクリップボードを経由して文字を入れます

English: [README.md](../README.md)

## 必要なもの

- **macOS 15 Sequoia 以降**の Mac（`/System/Applications/iPhone Mirroring.app` があること）と、同じ Apple アカウントの iOS 18 以降の iPhone（地域によっては使えません）
- computer use が使えるエージェント：Claude Code（デスクトップアプリの computer use）か、computer use が使える Codex
- SwitchBot API で確かめる場合（任意）：Python 3 と、自分の SwitchBot のトークンとシークレット
- 文字の受け渡しを使う場合（任意）：Mac と iPhone の両方に Obsidian、両者で同期される Vault（iCloud など）

## 入れ方

リポジトリを clone して、スキルのフォルダを各クライアントのスキル置き場へリンクします。

```bash
git clone https://github.com/atsu-mada/iphone-mirroring-operator.git
```

**Claude Code**

```bash
ln -s "$PWD/iphone-mirroring-operator/src/skills/iphone-mirroring-operator" ~/.claude/skills/iphone-mirroring-operator
```

新しいセッションで `/iphone-mirroring-operator` と呼びます。

**Codex**

```bash
ln -s "$PWD/iphone-mirroring-operator/src/skills/iphone-mirroring-operator" ~/.codex/skills/iphone-mirroring-operator
```

お使いの Codex が読むスキル置き場（`~/.codex/skills` か `~/.agents/skills`）に置いてください。新しいセッションで `$iphone-mirroring-operator` と呼びます。

### SwitchBot API（任意）

`apps/switchbot/scripts/switchbot_api.py` は、環境変数 `SWITCHBOT_TOKEN` と `SWITCHBOT_SECRET` からトークンとシークレットを読みます。値は SwitchBot アプリの開発者向けオプションで取得し（[SwitchBot API の公式ドキュメント](https://github.com/OpenWonderLabs/SwitchBotAPI)）、自分のシェルや秘密情報の管理ツールから渡してください。`.env`、プロンプト、Git には置かないでください。

```bash
python3 -I src/skills/iphone-mirroring-operator/apps/switchbot/scripts/switchbot_api.py devices   # または scenes / run "<シーン名>"
```

自分の設定を記録するときは、`apps/switchbot/current-settings.example.md` をコピーして `current-settings.md` を作ります（Git の対象外）。

## 安全の決まり

スキルはエージェントに次のことを求めます。

- 変更は一覧で見せ、ユーザーが OK してから保存する。読むために開いた編集画面は保存せずに戻る
- Mac のパスワード、Touch ID、iPhone のパスコードは**入力しない**（ユーザーが解除する）
- **購入、送信、投稿、リンクのタップはしない**。アカウント設定や通知設定も変えない。途中で出た許可の確認は拒否か「Cancel」
- 照明など現実の機器は、頼まれたときだけ動かし、動かしたあとは時間帯に合う状態へ戻す
- 意図しない画面が開いたら何も変えずに閉じ、保存してしまった可能性があれば正直に報告する

## 分かっている制限

- **Mac から打った文字は iPhone に届きません。** 文字は「a」に化け、Mac のクリップボードも共有されません。文字は Obsidian 経由で渡します（1行だけのノートを作る → iPhone で開いて `cmd+a`・`cmd+c` → 貼り付け先で `cmd+v`）
- iPhone の Spotlight は検索語を入れられないので使えません。アプリはホーム画面から開きます
- iPhone 本体を操作するとミラーリングが切れます。作業中は iPhone をロックして置いておきます
- 数値が出ないスライダーがあり、ドラッグは数 px ずれて止まります。1px ずつ寄せ、保存後の画面か API で値を読みます。ミラーリングの窓が動くと座標もずれます
- スライダーの目盛りや画面の文言は、2026年10月時点の macOS 26 と SwitchBot アプリで測ったものです。アプリの更新で変わることがあります

## ライセンス

[MIT](../LICENSE)
