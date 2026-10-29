# SwitchBot

照明（Ceiling Light Pro F3、Color Bulb 2242）のシーンとオートメーションを扱う。

| ファイル | 内容 |
| --- | --- |
| この README | API とアプリの役割分担、API の使い方、アプリの画面構成 |
| [scenes.md](scenes.md) | シーンの読み取り・調査・作成・編集、照明ごとの設定項目と目盛り |
| [automations.md](automations.md) | オートメーションの作成・編集、天気の条件 |
| [current-settings.example.md](current-settings.example.md) | 今のシーンとオートメーションを記録する表の例。コピーして `current-settings.md` として自分の設定を書く |

## API でできることと、アプリでしかできないこと

| 操作 | 方法 |
| --- | --- |
| 機器の今の状態（電源・明るさ・色温度）、シーンの一覧、シーンの実行 | API（下の `switchbot_api.py`） |
| シーンの中身の読み取り・作成・編集、オートメーションのすべて | アプリのみ（ミラーリング） |

API が返すのは「今の機器の状態」で、シーンの設定そのものではない。常夜灯（Nightlight）や「直前の状態で点灯」は数値で表せず、その前の値がそのまま返る。

## API の使い方

トークンとシークレットは SwitchBot アプリの開発者向けオプションで取得する（手順は [SwitchBot API の公式ドキュメント](https://github.com/OpenWonderLabs/SwitchBotAPI) を参照）。スクリプトは環境変数 `SWITCHBOT_TOKEN` と `SWITCHBOT_SECRET` から読む。

- 値はユーザーが自分のシェルや秘密情報の管理ツール（キーチェーン、1Password CLI など）で渡す。エージェントは値を読まない・表示しない・ファイルに書かない
- `.env` やリポジトリにキーを置かない

```bash
S=<このスキルのフォルダ>/apps/switchbot/scripts/switchbot_api.py
# SWITCHBOT_TOKEN と SWITCHBOT_SECRET は、ユーザーが事前に環境変数として渡しておく
python3 -I "$S" devices        # または scenes / run "<シーン名>"
```

- `run` はシーンを実行し、8秒待ってから2台の状態を出す。照明が実際に切り替わるので、ユーザーが頼んだとき（値の確認や調整を含む）だけ使う
- 確認のために実行したあとは、その時間帯に合うシーン（夕方なら「夕方」）を実行して戻し、戻したことを伝える

## アプリの画面

- 下のタブ：Home／Automations／Shop／Profile
- 右上の「＋」：Home タブでは Add Device／Add Scene／Add Automation などのメニュー。Automations タブでは直接「Create Automation」が開く
- シーン一覧：Home の「Quick Scenes >」。上に Quick Scenes、下に Not in Quick Scenes が並ぶ。行の名前を押すと編集画面、右の ▶ は**実行**なので押さない
- オートメーション一覧：Automations タブ。カードの名前を押すと編集画面、右のスイッチはオン・オフなので押さない
