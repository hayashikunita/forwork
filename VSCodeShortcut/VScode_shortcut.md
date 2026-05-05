# VS Code ショートカットキー集

Visual Studio Codeで最も使える実用的なショートカットキーのリファレンスです。

## 目次
- [必須ショートカット（絶対に覚えるべき）](#必須ショートカット絶対に覚えるべき)
- [ファイル・エディタ操作](#ファイルエディタ操作)
- [編集操作](#編集操作)
- [カーソル移動・選択](#カーソル移動選択)
- [マルチカーソル](#マルチカーソル)
- [検索・置換](#検索置換)
- [コード編集](#コード編集)
- [リファクタリング](#リファクタリング)
- [デバッグ](#デバッグ)
- [ターミナル](#ターミナル)
- [表示・ビュー](#表示ビュー)
- [Git操作](#git操作)
- [拡張機能関連](#拡張機能関連)

---

## 必須ショートカット（絶対に覚えるべき）

### コマンドパレット
```
Ctrl + Shift + P  または F1
→ すべてのコマンドにアクセス。これだけ覚えれば他は検索可能
```

### クイックオープン
```
Ctrl + P
→ ファイル名で素早く開く（最重要）

使い方の例：
- "main.py" と入力してファイルを開く
- ">" を先頭につけると Ctrl+Shift+P と同じ
- "@" を先頭につけると現在のファイルのシンボル検索
- ":" を先頭につけると行番号指定
- "#" を先頭につけるとワークスペース全体のシンボル検索
```

### 設定画面
```
Ctrl + ,
→ 設定画面を開く
```

### ファイル保存
```
Ctrl + S  ファイル保存
Ctrl + K S  すべてのファイルを保存
```

### 元に戻す・やり直し
```
Ctrl + Z  元に戻す
Ctrl + Y  やり直し
```

---

## ファイル・エディタ操作

### ファイル操作
```
Ctrl + N  新しいファイル
Ctrl + O  ファイルを開く
Ctrl + W  エディタを閉じる
Ctrl + K W  すべてのエディタを閉じる
Ctrl + Shift + T  閉じたエディタを再度開く

Ctrl + Tab  次のエディタに切り替え
Ctrl + Shift + Tab  前のエディタに切り替え
Ctrl + 1, 2, 3...  エディタグループに切り替え
```

### エディタグループ
```
Ctrl + \  エディタを分割（サイドバイサイド）
Ctrl + K Ctrl + Left/Right  エディタグループ間でフォーカス移動

Ctrl + K Left/Right/Up/Down  エディタグループの配置を変更
Alt + Left/Right  エディタの履歴を前後に移動
```

### サイドバー
```
Ctrl + B  サイドバーの表示/非表示
Ctrl + Shift + E  エクスプローラーを開く
Ctrl + Shift + F  検索パネルを開く
Ctrl + Shift + G  ソース管理（Git）を開く
Ctrl + Shift + D  デバッグパネルを開く
Ctrl + Shift + X  拡張機能パネルを開く
```

---

## 編集操作

### 基本編集
```
Ctrl + X  行の切り取り（選択なしで実行すると行全体）
Ctrl + C  行のコピー（選択なしで実行すると行全体）
Ctrl + V  貼り付け

Ctrl + Shift + K  行の削除
Ctrl + Enter  下に行を挿入
Ctrl + Shift + Enter  上に行を挿入

Alt + Up/Down  行を上下に移動
Shift + Alt + Up/Down  行を上下にコピー
```

### インデント
```
Ctrl + ]  インデントを増やす
Ctrl + [  インデントを減らす
Tab  選択行のインデントを増やす
Shift + Tab  選択行のインデントを減らす

Ctrl + K Ctrl + F  選択範囲をフォーマット
Shift + Alt + F  ドキュメント全体をフォーマット
```

### コメント
```
Ctrl + /  行コメントの切り替え
Shift + Alt + A  ブロックコメントの切り替え
```

### 折りたたみ
```
Ctrl + Shift + [  現在のブロックを折りたたむ
Ctrl + Shift + ]  現在のブロックを展開
Ctrl + K Ctrl + 0  すべて折りたたむ
Ctrl + K Ctrl + J  すべて展開

Ctrl + K Ctrl + 1〜7  レベル指定で折りたたみ
```

---

## カーソル移動・選択

### カーソル移動（基本）
```
Home  行の先頭へ
End  行の末尾へ
Ctrl + Home  ファイルの先頭へ
Ctrl + End  ファイルの末尾へ

Ctrl + Left/Right  単語単位で移動
Ctrl + Up/Down  画面をスクロール（カーソルは移動しない）
```

### カーソル移動（高度）
```
Ctrl + G  指定行にジャンプ
Ctrl + P  その後 :行番号
Alt + PageUp/PageDown  ページスクロール

Ctrl + U  最後のカーソル位置に戻る
```

### 選択
```
Shift + 矢印キー  文字単位で選択
Shift + Ctrl + Left/Right  単語単位で選択
Shift + Home/End  行の先頭/末尾まで選択
Shift + Ctrl + Home/End  ファイルの先頭/末尾まで選択

Ctrl + A  すべて選択
Ctrl + L  現在行を選択

Alt + Shift + Left/Right  選択範囲を広げる/縮める（スマート選択）
```

### ブラケットマッチング
```
Ctrl + Shift + \  対応するブラケットにジャンプ
```

---

## マルチカーソル

### マルチカーソル（最重要）
```
Alt + Click  カーソルを追加
Ctrl + Alt + Up/Down  上下にカーソルを追加

Ctrl + D  選択中の単語と同じ次の単語を選択（連打で複数選択）
Ctrl + Shift + L  選択中の単語と同じすべての単語を選択

Alt + Shift + I  選択した各行の末尾にカーソルを追加
Alt + Shift + Drag  矩形選択（列選択モード）
Shift + Alt + Right  選択範囲を広げる
```

### マルチカーソルの実用例
```
1. 複数の変数名を一括変更
   - Ctrl + D で同じ単語を複数選択
   - そのまま入力して一括置換

2. 複数行の末尾に同じテキストを追加
   - Alt + Shift + I で各行末にカーソル
   - テキストを入力

3. 列単位での編集
   - Alt + Shift + Drag で矩形選択
   - 入力すると選択範囲すべてに反映
```

---

## 検索・置換

### 基本検索
```
Ctrl + F  検索
Ctrl + H  置換
F3  次を検索
Shift + F3  前を検索
Enter  検索ボックスで次を検索
Shift + Enter  検索ボックスで前を検索

Alt + C  大文字小文字を区別
Alt + W  単語単位で検索
Alt + R  正規表現検索
```

### ファイル横断検索
```
Ctrl + Shift + F  ワークスペース全体で検索
Ctrl + Shift + H  ワークスペース全体で置換

検索結果からの操作：
F4  次の検索結果にジャンプ
Shift + F4  前の検索結果にジャンプ
```

### 高度な検索テクニック
```
正規表現の例：
- \d+  数字
- [A-Z]  大文字
- .*  任意の文字列
- ^  行の先頭
- $  行の末尾

置換での後方参照：
検索: function (\w+)
置換: const $1 = function
→ function名を保持したまま構文変換
```

---

## コード編集

### IntelliSense・補完
```
Ctrl + Space  IntelliSenseをトリガー
Ctrl + Shift + Space  パラメーターヒントを表示
Tab または Enter  補完候補を確定

Ctrl + .  クイックフィックス（電球アイコン）
```

### コードナビゲーション
```
F12  定義へ移動
Alt + F12  定義をピーク表示（ポップアップ）
Ctrl + K F12  定義を横に開く
Shift + F12  参照を検索

Ctrl + T  ワークスペース全体のシンボル検索
Ctrl + Shift + O  現在のファイルのシンボル検索
```

### コード折りたたみとナビゲーション
```
Ctrl + K Ctrl + I  ホバー情報を表示
Ctrl + Shift + [  リージョンを折りたたむ
Ctrl + Shift + ]  リージョンを展開
```

### スニペット
```
Ctrl + K Ctrl + X  スニペット挿入
Tab  次のタブストップへ移動
Shift + Tab  前のタブストップへ移動
```

---

## リファクタリング

### リネーム
```
F2  シンボル名変更（変数、関数、クラス名などをすべて変更）
```

### リファクタリング操作
```
Ctrl + Shift + R  リファクタリング操作を表示
Ctrl + .  クイックフィックス

よく使うリファクタリング：
- 関数の抽出
- 変数の抽出
- インポートの整理
- 未使用のimportを削除
```

---

## デバッグ

### デバッグ実行
```
F5  デバッグ開始/続行
Ctrl + F5  デバッグなしで実行
F9  ブレークポイントの設定/解除
F10  ステップオーバー
F11  ステップイン
Shift + F11  ステップアウト
Shift + F5  デバッグ停止
Ctrl + Shift + F5  再起動

Ctrl + K Ctrl + I  変数の値をホバー表示
```

### ブレークポイント管理
```
F9  ブレークポイントのトグル
Ctrl + Shift + F9  すべてのブレークポイントを削除
```

---

## ターミナル

### ターミナル操作
```
Ctrl + @  または Ctrl + `  統合ターミナルの表示/非表示
Ctrl + Shift + @  新しいターミナルを作成
Ctrl + Shift + 5  ターミナルを分割

Ctrl + PageUp/PageDown  ターミナル間を切り替え
Ctrl + C  ターミナルのプロセスを中断
Ctrl + L  ターミナルをクリア
```

### ターミナルの実用テクニック
```
1. Ctrl + Click  ターミナルのファイルパスをクリックして開く
2. Ctrl + @  で素早くターミナルとエディタを切り替え
3. 複数ターミナルを使い分け（開発サーバー、テスト、Git用など）
```

---

## 表示・ビュー

### 表示切り替え
```
F11  全画面モード切り替え
Ctrl + =  ズームイン
Ctrl + -  ズームアウト
Ctrl + 0  ズームリセット

Ctrl + K Z  Zen モード（集中モード）
Esc Esc  Zen モード解除
```

### パネル
```
Ctrl + J  パネル（ターミナル、出力、問題など）の表示/非表示
Ctrl + Shift + M  問題パネルの表示
Ctrl + Shift + U  出力パネルの表示
Ctrl + Shift + Y  デバッグコンソールの表示
```

### ミニマップとブレッドクラム
```
Ctrl + Shift + M  ミニマップの表示/非表示（設定から）
Ctrl + Shift + .  ブレッドクラムにフォーカス
```

---

## Git操作

### ソース管理
```
Ctrl + Shift + G  ソース管理パネルを開く
Ctrl + Enter  コミットメッセージを確定してコミット

エディタでの Git 操作：
Alt + Left/Right  変更履歴を前後に移動
Ctrl + K Ctrl + G  Git の変更箇所にジャンプ
```

### Diff 表示
```
Ctrl + K Ctrl + D  差分を表示
F7  次の差分へ
Shift + F7  前の差分へ
```

---

## 拡張機能関連

### 便利な拡張機能のショートカット例

#### Markdown Preview Enhanced
```
Ctrl + K V  Markdownプレビューを横に開く
Ctrl + Shift + V  Markdownプレビューを開く
```

#### Python
```
Shift + Enter  Pythonコードを実行
Ctrl + Shift + P → "Python: Select Interpreter"  インタープリター選択
```

#### GitHub Copilot
```
Tab  提案を受け入れ
Ctrl + →  単語単位で提案を受け入れ
Alt + ]  次の提案
Alt + [  前の提案
Ctrl + Enter  別の提案を表示
```

---

## カスタマイズとヒント

### ショートカットキーのカスタマイズ
```
Ctrl + K Ctrl + S  キーボードショートカット設定を開く

検索して自分好みに変更可能：
- 既存のショートカットを変更
- 新しいショートカットを追加
- ショートカットをリセット
```

### 生産性を上げるコツ

#### 1. ワークスペースの保存
```
File > Save Workspace As...
複数のフォルダを一つのワークスペースとして保存
```

#### 2. タスクの自動化
```
Ctrl + Shift + B  ビルドタスクを実行
tasks.json でカスタムタスクを定義
```

#### 3. スニペットの作成
```
File > Preferences > User Snippets
よく使うコードパターンをスニペットとして登録
```

### よく使う連続コマンド

#### ファイル保存 → フォーマット → 実行
```
1. Ctrl + S  保存
2. Shift + Alt + F  フォーマット
3. F5  デバッグ実行
```

#### 複数箇所の編集
```
1. Ctrl + F  検索
2. Alt + Enter  すべての一致箇所を選択
3. Esc  検索を閉じる
4. 編集開始（マルチカーソル状態）
```

---

## プラットフォーム別の違い

### macOS の場合
```
Ctrl → Cmd
Alt → Option

主な違い：
- Cmd + P  クイックオープン
- Cmd + Shift + P  コマンドパレット
- Cmd + ,  設定
- Cmd + B  サイドバー表示/非表示
```

### Linux の場合
```
基本的にはWindows と同じ
一部のウィンドウマネージャーとの競合に注意
```

---

## 効率化のベストプラクティス

### レベル1: 初心者（まずこれを覚える）
```
1. Ctrl + P  ファイルを開く
2. Ctrl + Shift + P  コマンドパレット
3. Ctrl + D  同じ単語を複数選択
4. Ctrl + /  コメント切り替え
5. Alt + Up/Down  行を移動
```

### レベル2: 中級者
```
1. F12  定義へ移動
2. Ctrl + .  クイックフィックス
3. Alt + Shift + F  コードフォーマット
4. Ctrl + G  行番号指定ジャンプ
5. Ctrl + H  置換
6. F2  リネーム
```

### レベル3: 上級者
```
1. Ctrl + K Ctrl + 0/J  すべて折りたたみ/展開
2. Ctrl + Shift + L  同じ単語をすべて選択
3. Alt + Shift + I  各行末にカーソル
4. Ctrl + K Z  Zen モード
5. Ctrl + T  ワークスペースシンボル検索
6. 正規表現を使った検索置換
```

---

## トラブルシューティング

### ショートカットが効かない場合
```
1. Ctrl + K Ctrl + S でショートカット設定を確認
2. 拡張機能との競合を確認
3. キーバインディングの "when" 条件を確認
4. OS やウィンドウマネージャーとの競合を確認
```

### よくある競合
```
- Ctrl + Space: IME（日本語入力）と競合
  → keybindings.json で変更可能
- Ctrl + Shift + F: Windows の検索と競合
  → Windows 設定で無効化可能
```

---

## 参考リンク

- [VS Code 公式キーボードショートカット（Windows）](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [VS Code 公式ドキュメント](https://code.visualstudio.com/docs)
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [キーバインディングのカスタマイズ](https://code.visualstudio.com/docs/getstarted/keybindings)