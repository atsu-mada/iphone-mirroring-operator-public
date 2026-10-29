# SwitchBot Automations

## 作る・編集する

1. 新規は Automations タブの「＋」（直接「Create Automation」が開く）。既存はカードの名前を押す
2. 名前欄：クリック → `cmd+a` → `Delete` → `cmd+v`（[../obsidian/README.md](../obsidian/README.md) でコピーした名前）
3. When：「Add condition」→「Schedules」→「Time」→ ピッカーで時刻を合わせて OK →「Every day」など →「Save」。時刻ごとに条件を1つずつ足す（どれか1つで動く）
4. 前提条件：「Advanced Options」を開くと And 欄が出る →「Add precondition」
5. Perform：「Add action」→「Activate Scene」→ シーン
6. 下の「Save」。「アプリの通知をオンにするか」と聞かれたら「Cancel」。オートメーションはそのまま保存される

## 前提条件（And）の種類

| 種類 | 内容 |
| --- | --- |
| Smart Devices | 機器の状態（温湿度計の値など） |
| Period | 曜日や期間 |
| At a location／Not at a location (Beta) | 位置情報（常時の位置情報の許可が要る） |
| Outdoor Weather (Beta) | 屋外の天気 |

## 天気の条件

- 選べる項目：屋外の気温（以上／以下）、湿度（以上／以下）、**Raining／Snowing／Cloudy／Sunny**。1つの条件で選べるのは1つだけ
- 項目を選ぶと Location 欄が出る。検索履歴にある自分の都市（例：「<City>, <Country>」）を選ぶ。ミラーリング越しでは文字を入力できないので、事前に iPhone 本体で一度検索して履歴に入れておく
- 複数の天気を「または」でつなぐときは、条件を2つ足し、「All preconditions are met ⇆」を押して「Any of these preconditions are met」を選ぶ
- 晴れ用と悪天候用を同じ時刻で分けるときは、両方に天気の条件を付ける。片方だけだと、条件のない方が毎回動いて重なる
- 晴れ・曇り・雨のどれにも当たらない天気（雪など）の日は、どちらも動かない
