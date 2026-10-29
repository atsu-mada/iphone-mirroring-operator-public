# SwitchBot Scenes

## シーンを調べる

| 知りたいこと | 方法 | 照明 |
| --- | --- | --- |
| 実際の明るさと色温度 | API の `run` で順に実行して読み、最後に時間帯に合うシーンへ戻す | 切り替わる |
| 設定の中身（モード、どの機器を操作するか） | ミラーリングで編集画面を開いて説明文を読み、保存せずに戻る | 変わらない |

両方を組み合わせる。API で 2700K のような値が出ても、編集画面では「Nightlight mode」や「Turns on to previous state」のことがある（API は前の値を返すため）。

編集画面の説明文の例：

| 説明文 | 意味 |
| --- | --- |
| Turns on to Full light mode | シーリングの全灯 |
| Turns on to Nightlight mode | シーリングの常夜灯 |
| Turns on to scene | シーリング内蔵のプリセット（中身は画面に出ない。API で実測する） |
| Turns on to previous state | 直前の状態で点灯 |
| Turns on to brightness 80%, color temperature 3833k | Customize で決めた値 |
| Turns on to White, brightness 80% | 電球の白モード（色温度は画面に出ない） |
| Turns off (0s fade out) | 消灯 |

## シーンを作る・編集する

1. 新規は Home の「＋」→「Add Scene」。既存は一覧で名前を押す
2. 名前欄：クリック → `cmd+a` → `Delete` → `cmd+v`（[../obsidian/README.md](../obsidian/README.md) でコピーした名前）
3. 機器を足す：「Add action」→「Smart Devices」→ 機器 →「Turns on」。既にある機器の行を押すと、同じ「Turns on／Turns off／Toggles on/off」から選び直しになる（保存済みの値は読み込まれない）
4. 照明ごとの設定は下の表のとおり。機器の画面で「Save」→ シーン画面の説明文で確かめる
5. 元のシーンに合わせて Notifications はオフ。最後に下の「Save」
6. シーン名の横のアイコンを押すと「Icon Settings」が開く。変えないときは「Cancel」

## 照明ごとの設定項目

### Ceiling Light Pro F3

「Turns on」→「Previous State」か「Select Light」。「Select Light」の下に4つ：

| 項目 | 内容 |
| --- | --- |
| Nightlight | 常夜灯 |
| Full light | 全灯 |
| Scenes | ライト内蔵のプリセット |
| Customize | 明るさ（上）と色温度（下、左 2700K〜右 6500K）のスライダー。数値は出ない。OK →「Save」後の説明文で読む |

### Color Bulb 2242

「Turns on」→ Fade Rate（既定 Instant）、「Previous Status」か「Customize」。「Customize」の中：

| 項目 | 内容 |
| --- | --- |
| Brightness | スライダー。% が表示される |
| Mode → White | Favorites（4色）と Color Temp のスライダー（2700K〜6500K）。値は出ないので、シーンを `run` して API で読む。Favorites は読み込みが遅れて空に見えることがある |
| Mode → Color／Dynamic | 色やエフェクト（2026-10-26 時点では未使用） |

## スライダーの目盛り（ミラーリングの既定の大きさ、2026-10-26）

合わせ方は [../../references/value-tuning.md](../../references/value-tuning.md)。

| スライダー | 1px あたり | 実測した位置（全画面座標の終点 x → 値） |
| --- | --- | --- |
| シーリング 明るさ | 約 0.5% | 右向き 755 → 80%、735 → 70% |
| シーリング 色温度 | 約 20〜24K | 右向き 665 → 3484K、666 → 3522K、686 → 3988K、687 → 4008K／左向き 644 → 2999K |
| 電球 明るさ | 約 0.5% | 右向き 754 → 80%、734 → 70% |
| 電球 色温度 | 約 21〜23K | 右向き 653 → 3999K、654 → 4015K／左向き 627 → 3490K、601 → 2997K |

ミラーリングのウインドウの位置が変わると座標もずれる。上の数値は目安にして、毎回1回目の実測で補正する。
