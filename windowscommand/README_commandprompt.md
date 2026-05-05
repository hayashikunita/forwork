# Windows コマンドプロンプト (CMD) コマンド集

コマンドプロンプトでよく使うコマンドの学習用リファレンスです。

## 目次
- [基本コマンド](#基本コマンド)
- [ファイル・ディレクトリ操作](#ファイルディレクトリ操作)
- [テキスト処理](#テキスト処理)
- [プロセス管理](#プロセス管理)
- [ネットワーク](#ネットワーク)
- [システム情報](#システム情報)
- [バッチファイル](#バッチファイル)
- [高度なバッチ技術](#高度なバッチ技術)
- [ディスク管理](#ディスク管理)
- [ファイル圧縮・展開](#ファイル圧縮展開)
- [環境変数](#環境変数)
- [セキュリティとアクセス制御](#セキュリティとアクセス制御)
- [デバッグとトラブルシューティング](#デバッグとトラブルシューティング)
- [パフォーマンス最適化](#パフォーマンス最適化)
- [システムメンテナンス](#システムメンテナンス)

---

## 基本コマンド

### ヘルプの表示
```cmd
REM コマンドのヘルプを表示
help
help <コマンド名>
<コマンド名> /?

REM 例
help dir
dir /?
```

### 画面クリア
```cmd
cls
```

### 現在のディレクトリ表示
```cmd
cd
```

### コマンドプロンプトのタイトル変更
```cmd
title 新しいタイトル
```

### コマンド履歴表示
```cmd
doskey /history
```

---

## ファイル・ディレクトリ操作

### ディレクトリ内容の表示
```cmd
REM 基本的なリスト表示
dir

REM 詳細表示
dir /W    REM ワイド形式（横に並べる）
dir /B    REM ベア形式（ファイル名のみ）
dir /S    REM サブディレクトリも含めて表示
dir /A    REM すべてのファイル（隠しファイル含む）
dir /AH   REM 隠しファイルのみ
dir /AD   REM ディレクトリのみ
dir /A-D  REM ファイルのみ（ディレクトリを除外）

REM 並び替え
dir /O:N  REM 名前順
dir /O:S  REM サイズ順
dir /O:D  REM 日付順
dir /O:-D REM 日付の逆順

REM 特定の拡張子のみ表示
dir *.txt
dir *.py *.md

REM ページング表示
dir /P
dir | more
```

### ディレクトリ移動
```cmd
REM ディレクトリ移動
cd <パス>
cd ..          REM 親ディレクトリへ
cd \           REM ルートディレクトリへ
cd %USERPROFILE%  REM ホームディレクトリへ

REM ドライブ変更とディレクトリ移動を同時に
cd /D D:\folder

REM 前のディレクトリに戻る（doskey使用）
doskey cd=cd $* ^& set OLDCD=%CD%
```

### ディレクトリ作成・削除
```cmd
REM ディレクトリ作成
mkdir newfolder
md newfolder

REM 階層ディレクトリ作成
mkdir parent\child\grandchild

REM ディレクトリ削除（空の場合のみ）
rmdir foldername
rd foldername

REM ディレクトリを中身ごと削除
rmdir /S foldername
rd /S /Q foldername  REM 確認なしで強制削除

REM ディレクトリツリー表示
tree
tree /F  REM ファイルも含めて表示
tree /A  REM ASCII文字で表示
```

### ファイル作成・コピー・移動・削除
```cmd
REM 空ファイル作成
type nul > newfile.txt
echo. > newfile.txt
copy nul newfile.txt

REM ファイルコピー
copy source.txt destination.txt
copy *.txt D:\backup\
copy file1.txt+file2.txt merged.txt  REM ファイル結合

REM 上書き確認なしでコピー
copy /Y source.txt destination.txt

REM ディレクトリごとコピー
xcopy source destination /E /I
xcopy source destination /E /I /Y  REM 確認なし
xcopy source destination /E /I /H  REM 隠しファイルも含む

REM より高機能なコピー（robocopy）
robocopy source destination /E
robocopy source destination /E /XO  REM 新しいファイルのみ
robocopy source destination /MIR    REM ミラーリング（完全同期）

REM ファイル移動
move source.txt destination.txt
move *.log D:\logs\

REM ファイル削除
del file.txt
erase file.txt
del *.tmp
del /Q *.log       REM 確認なし
del /F file.txt    REM 読み取り専用ファイルも削除
del /S *.bak       REM サブディレクトリ内も削除

REM ファイル名変更
ren oldname.txt newname.txt
rename old.txt new.txt
```

### ファイル内容の表示・編集
```cmd
REM ファイル内容を表示
type file.txt
more file.txt      REM ページング表示
more < file.txt

REM ファイルに書き込み（上書き）
echo テキスト > file.txt

REM ファイルに追記
echo 追加テキスト >> file.txt

REM ファイルをメモ帳で開く
notepad file.txt

REM 複数ファイルを結合して表示
type file1.txt file2.txt

REM バイナリファイルの比較
fc /B file1.bin file2.bin

REM テキストファイルの比較
fc file1.txt file2.txt
```

### ファイル検索
```cmd
REM ファイル名で検索
dir /S /B *keyword*
dir /S /B *.txt

REM ファイル内容で検索
findstr "検索文字列" file.txt
findstr /S /I "error" *.log  REM サブディレクトリ内、大文字小文字無視
findstr /R "pattern" *.txt   REM 正規表現使用

REM where コマンドで実行可能ファイルを検索
where python
where /R C:\ *.exe  REM 再帰的に検索
```

### ファイル属性
```cmd
REM ファイル属性を表示
attrib file.txt
attrib *.*  REM すべてのファイルの属性を表示

REM 属性設定
attrib +R file.txt  REM 読み取り専用に設定
attrib -R file.txt  REM 読み取り専用を解除
attrib +H file.txt  REM 隠しファイルに設定
attrib -H file.txt  REM 隠しファイルを解除
attrib +S file.txt  REM システムファイルに設定
attrib +A file.txt  REM アーカイブ属性を設定

REM 複数属性を同時に設定
attrib +R +H file.txt  REM 読み取り専用かつ隠しファイル
attrib -R -H -S file.txt  REM すべての属性を解除

REM サブディレクトリ内も含めて属性変更
attrib +R *.txt /S
attrib -H -S /S /D  REM すべてのファイルとディレクトリから隠し・システム属性を削除
```

### ファイルの詳細情報
```cmd
REM ファイルのタイムスタンプ情報
dir /T:C file.txt  REM 作成日時
dir /T:A file.txt  REM 最終アクセス日時
dir /T:W file.txt  REM 最終更新日時

REM ファイルのハッシュ値を計算（PowerShell使用）
powershell "Get-FileHash file.txt -Algorithm SHA256"
powershell "Get-FileHash file.txt -Algorithm MD5"
powershell "Get-FileHash file.txt -Algorithm SHA1"

REM ファイルの所有者情報
dir /Q file.txt

REM ファイルの詳細情報（WMIC使用）
wmic datafile where name="C:\\path\\to\\file.txt" get Name,FileSize,CreationDate,LastModified

REM ファイルサイズを取得
for %%A in (file.txt) do echo %%~zA bytes

REM ファイルの完全パスを取得
for %%A in (file.txt) do echo %%~fA

REM ファイルのドライブとパスを取得
for %%A in (file.txt) do echo Drive: %%~dA, Path: %%~pA

REM ファイル名と拡張子を分離
for %%A in (file.txt) do (
    echo ファイル名: %%~nA
    echo 拡張子: %%~xA
)
```

### ファイルのバックアップと復元
```cmd
REM 単一ファイルのバックアップ
copy file.txt file.txt.bak
copy file.txt file_%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%.bak

REM タイムスタンプ付きバックアップ
set TIMESTAMP=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%
copy file.txt file_%TIMESTAMP%.bak

REM ディレクトリの差分バックアップ
xcopy C:\source C:\backup /D /E /I /Y

REM robocopyで増分バックアップ
robocopy C:\source C:\backup /MIR /XO /R:3 /W:10
robocopy C:\source C:\backup /E /XO /XC /LOG:backup.log

REM バックアップスクリプトの例
@echo off
set SOURCE=C:\important_data
set BACKUP=D:\backups\%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
if not exist "%BACKUP%" mkdir "%BACKUP%"
robocopy "%SOURCE%" "%BACKUP%" /E /XO /R:2 /W:5 /LOG:backup_%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%.log
if %ERRORLEVEL% LEQ 7 (
    echo バックアップ成功
) else (
    echo バックアップ失敗
)

REM 世代管理バックアップ（古いバックアップを削除）
forfiles /P "D:\backups" /M "*" /D -30 /C "cmd /c del @path"
forfiles /P "D:\backups" /M "*" /D -30 /C "cmd /c rd /S /Q @path"
```

### ファイルの比較と差分
```cmd
REM テキストファイルの比較
fc file1.txt file2.txt
fc /N file1.txt file2.txt  REM 行番号付き
fc /L file1.txt file2.txt  REM テキストモード
fc /LB 5 file1.txt file2.txt  REM バッファサイズ指定

REM バイナリファイルの比較
fc /B file1.bin file2.bin

REM 比較結果をファイルに出力
fc file1.txt file2.txt > diff.txt

REM 大文字小文字を無視して比較
fc /C file1.txt file2.txt

REM タブとスペースを同じとして比較
fc /W file1.txt file2.txt

REM comp コマンドでバイナリ比較
comp file1.bin file2.bin
comp /A file1.txt file2.txt  REM ASCII文字で表示
comp /L file1.txt file2.txt  REM 行番号表示

REM ディレクトリ比較（PowerShell使用）
powershell "Compare-Object (Get-ChildItem C:\dir1) (Get-ChildItem C:\dir2) -Property Name, Length"

REM ファイル内容の差分を詳細表示（PowerShell使用）
powershell "Compare-Object (Get-Content file1.txt) (Get-Content file2.txt)"
```

### ファイルの分割と結合
```cmd
REM ファイルを複数に分割（PowerShell使用）
powershell "$content = Get-Content file.txt; $size = 1000; for($i=0; $i -lt $content.Length; $i+=$size) { $content[$i..[Math]::Min($i+$size-1, $content.Length-1)] | Out-File "part_$([Math]::Floor($i/$size)).txt" }"

REM バイナリファイルを分割（PowerShell使用）
powershell "$file = 'large.bin'; $size = 10MB; $reader = [System.IO.File]::OpenRead($file); $buffer = New-Object byte[] $size; $count = 0; while(($bytesRead = $reader.Read($buffer, 0, $buffer.Length)) -gt 0) { [System.IO.File]::WriteAllBytes("${file}_part${count}", $buffer[0..($bytesRead-1)]); $count++ }; $reader.Close()"

REM テキストファイルの結合
copy file1.txt + file2.txt + file3.txt combined.txt
copy /B file1.txt+file2.txt+file3.txt combined.txt

REM バイナリファイルの結合
copy /B part1.bin+part2.bin+part3.bin complete.bin

REM 複数ファイルを順番に結合
type file1.txt > combined.txt
type file2.txt >> combined.txt
type file3.txt >> combined.txt

REM ワイルドカードで複数ファイルを結合
copy *.txt all.txt
for %%f in (*.txt) do type "%%f" >> combined.txt

REM CSVファイルをヘッダー付きで結合
type file1.csv > combined.csv
for %%f in (file*.csv) do (
    for /F "skip=1 tokens=*" %%a in (%%f) do echo %%a >> combined.csv
)
```

### バイナリファイル操作
```cmd
REM バイナリファイルのダンプ表示（certutil使用）
certutil -encodehex file.bin output.hex

REM 16進数ダンプ（PowerShell使用）
powershell "Format-Hex file.bin | Out-File hexdump.txt"

REM バイナリファイルの一部を抽出（PowerShell使用）
powershell "$stream = [System.IO.File]::OpenRead('file.bin'); $stream.Seek(100, 'Begin'); $buffer = New-Object byte[] 50; $stream.Read($buffer, 0, 50); [System.IO.File]::WriteAllBytes('extract.bin', $buffer); $stream.Close()"

REM Base64エンコード/デコード
certutil -encode file.bin file.b64
certutil -decode file.b64 file.bin

REM バイナリファイルのパターン検索（PowerShell使用）
powershell "$bytes = [System.IO.File]::ReadAllBytes('file.bin'); $pattern = [byte[]](0x89, 0x50, 0x4E, 0x47); for($i=0; $i -lt $bytes.Length-$pattern.Length; $i++) { $match = $true; for($j=0; $j -lt $pattern.Length; $j++) { if($bytes[$i+$j] -ne $pattern[$j]) { $match = $false; break } }; if($match) { Write-Host \"Found at offset: $i\" } }"
```

### ファイルのタイムスタンプ操作
```cmd
REM ファイルのタイムスタンプを現在時刻に更新
copy /B file.txt +,, file.txt
type nul >> file.txt

REM PowerShellでタイムスタンプを設定
powershell "(Get-Item file.txt).LastWriteTime = '2026-01-01 12:00:00'"
powershell "(Get-Item file.txt).CreationTime = '2026-01-01 12:00:00'"
powershell "(Get-Item file.txt).LastAccessTime = '2026-01-01 12:00:00'"

REM 現在時刻にタッチ
powershell "(Get-Item file.txt).LastWriteTime = Get-Date"

REM 複数ファイルのタイムスタンプを一括更新
for %%f in (*.txt) do copy /B "%%f" +,, "%%f"

REM 別のファイルのタイムスタンプをコピー
powershell "$source = Get-Item source.txt; $target = Get-Item target.txt; $target.CreationTime = $source.CreationTime; $target.LastWriteTime = $source.LastWriteTime"

REM 特定の日付より新しいファイルを検索
forfiles /D +2026/01/01 /C "cmd /c echo @path @fdate"
forfiles /D -7 /C "cmd /c echo @path"  REM 7日以内に更新されたファイル
```

### シンボリックリンクとジャンクション
```cmd
REM シンボリックリンクを作成（管理者権限必要）
mklink symlink.txt C:\original\file.txt
mklink /D symlink_dir C:\original\directory

REM ハードリンクを作成
mklink /H hardlink.txt C:\original\file.txt

REM ジャンクション（ディレクトリのハードリンク）を作成
mklink /J junction_dir C:\original\directory

REM シンボリックリンクの情報を表示
dir /AL  REM シンボリックリンクのみ表示
dir /A:L  REM リンクのみ表示

REM リンクを削除（リンク先は削除されない）
del symlink.txt
rmdir symlink_dir

REM ジャンクションの削除
rmdir junction_dir

REM fsutil でリンク情報を確認
fsutil reparsepoint query symlink.txt
```

---

## テキスト処理

### テキスト検索
```cmd
REM find コマンド（単純な文字列検索）
find "検索文字列" file.txt
find /I "error" file.txt        REM 大文字小文字を区別しない
find /V "not this" file.txt     REM 指定文字列を含まない行
find /N "pattern" file.txt      REM 行番号付きで表示
find /C "word" file.txt         REM マッチした行数をカウント

REM findstr コマンド（正規表現対応）
findstr "pattern" file.txt
findstr /I "error warning" *.log  REM 複数パターン、大文字小文字無視
findstr /R "^\[ERROR\]" app.log   REM 正規表現使用
findstr /V "debug" file.txt       REM 指定文字列を含まない行
findstr /N /C:"search phrase" file.txt  REM フレーズ検索、行番号付き
```

### テキスト並べ替え
```cmd
REM ソート
sort file.txt
sort /R file.txt  REM 逆順
dir | sort        REM パイプで使用

REM 重複行の削除
sort file.txt | uniq
```

### テキスト処理
```cmd
REM 行数をカウント
find /C /V "" file.txt

REM 先頭N行を表示（PowerShell使用）
powershell "Get-Content file.txt -Head 10"

REM 末尾N行を表示（PowerShell使用）
powershell "Get-Content file.txt -Tail 10"

REM 特定の行を抽出（PowerShell使用）
powershell "(Get-Content file.txt)[9]"  REM 10行目を表示（0始まり）
powershell "(Get-Content file.txt)[9..19]"  REM 10-20行目を表示

REM 空行を削除
findstr /V "^$" file.txt > output.txt

REM 重複行を削除してソート
sort file.txt | uniq > output.txt

REM 行頭に行番号を付ける
for /F "tokens=*" %%a in (file.txt) do echo !LINE!: %%a

REM 文字列の置換（PowerShell使用）
powershell "(Get-Content file.txt) -replace 'old', 'new' | Set-Content output.txt"

REM 複数ファイルの内容を結合
copy /B file1.txt+file2.txt+file3.txt merged.txt
type file1.txt file2.txt file3.txt > merged.txt

REM 文字数をカウント
for /F %%a in ('type file.txt ^| find /C /V ""') do set LINES=%%a
echo 行数: %LINES%
```

### 高度なテキスト検索
```cmd
REM 正規表現パターンの例
findstr /R "^[0-9]" file.txt  REM 数字で始まる行
findstr /R "[a-zA-Z]*@[a-zA-Z]*\.com" file.txt  REM メールアドレスっぽい行
findstr /R "\<ERROR\>" file.txt  REM ERROR という単語を含む行
findstr /R "^.*ERROR.*$" file.txt  REM ERRORを含む行全体
findstr /R "[0-9]\{3\}-[0-9]\{4\}" file.txt  REM 電話番号パターン

REM 複数パターンでOR検索
findstr /C:"error" /C:"warning" /C:"fatal" app.log

REM 複数ファイルから検索し、ファイル名も表示
findstr /S /N /I "TODO" *.java *.py *.js

REM 検索結果を別ファイルに保存
findstr /S /I "error" *.log > errors.txt 2>&1

REM パターンファイルを使用した検索
REM patterns.txt に検索パターンを1行ずつ記載
findstr /G:patterns.txt file.txt

REM 行頭・行末のパターン
findstr /R "^START" file.txt  REM STARTで始まる行
findstr /R "END$" file.txt  REM ENDで終わる行
findstr /R "^$" file.txt  REM 空行

REM 特定の列の値で検索（CSV）
for /F "tokens=2 delims=," %%a in (data.csv) do (
    echo %%a | findstr "search_term"
)
```

### ファイルの検証（チェックサム）
```cmd
REM MD5チェックサム
certutil -hashfile file.txt MD5

REM SHA256チェックサム
certutil -hashfile file.txt SHA256

REM SHA1チェックサム
certutil -hashfile file.txt SHA1

REM PowerShellで複数アルゴリズム
powershell "Get-FileHash file.txt -Algorithm MD5"
powershell "Get-FileHash file.txt -Algorithm SHA256"
powershell "Get-FileHash file.txt -Algorithm SHA512"

REM チェックサムをファイルに保存
certutil -hashfile file.txt SHA256 > file.txt.sha256

REM 複数ファイルのチェックサムを一括生成
for %%f in (*.txt) do certutil -hashfile "%%f" SHA256 >> checksums.txt

REM チェックサムの検証
@echo off
set EXPECTED=abc123...
for /F "tokens=*" %%a in ('certutil -hashfile file.txt SHA256 ^| findstr /V ":"') do set HASH=%%a
if "%HASH%"=="%EXPECTED%" (
    echo チェックサム一致
) else (
    echo チェックサム不一致
)

REM PowerShellでチェックサム検証
powershell "$expected = 'abc123...'; $actual = (Get-FileHash file.txt).Hash; if($actual -eq $expected) { Write-Host 'OK' } else { Write-Host 'NG' }"
```

### 大量ファイル処理
```cmd
REM ファイル名の一括変更（連番追加）
setlocal EnableDelayedExpansion
set count=1
for %%f in (*.jpg) do (
    ren "%%f" "image_!count!.jpg"
    set /A count+=1
)

REM ファイル名の文字列置換
for %%f in (*.txt) do (
    set filename=%%f
    set newname=!filename:old=new!
    ren "%%f" "!newname!"
)

REM 拡張子の一括変更
ren *.txt *.bak
for %%f in (*.jpeg) do ren "%%f" "%%~nf.jpg"

REM ファイル名を小文字に変換（PowerShell使用）
powershell "Get-ChildItem *.TXT | Rename-Item -NewName { $_.Name.ToLower() }"

REM ファイル名からスペースを削除
for %%f in ("* *.txt") do (
    set "name=%%f"
    set "name=!name: =!"
    ren "%%f" "!name!"
)

REM 特定サイズ以上のファイルを検索して移動
for /F "tokens=*" %%f in ('dir /S /B /A-D ^| powershell "Where-Object { (Get-Item $_).Length -gt 10MB }"') do (
    move "%%f" C:\large_files\
)

REM ファイルを日付別フォルダに整理
for %%f in (*.*) do (
    for /F "tokens=1-3 delims=/ " %%a in ('echo %%~tf') do (
        if not exist "%%a-%%b-%%c" mkdir "%%a-%%b-%%c"
        move "%%f" "%%a-%%b-%%c\"
    )
)

REM 重複ファイルの検出（ハッシュ値で比較）
@echo off
setlocal EnableDelayedExpansion
echo ファイル名,ハッシュ値 > hashes.csv
for %%f in (*.*) do (
    for /F "tokens=*" %%h in ('certutil -hashfile "%%f" MD5 ^| findstr /V ":"') do (
        echo %%f,%%h >> hashes.csv
    )
)
REM hashes.csv を確認して重複を見つける
```

### ログファイル解析
```cmd
REM エラー行を抽出
findstr /I "error" app.log > errors.txt

REM 複数のキーワードで抽出
findstr /I "error warning critical" app.log > issues.txt

REM 特定の時間帯のログを抽出
findstr "2026-05-05 1[0-5]:" app.log > afternoon.log

REM ログファイルの統計情報
find /C "ERROR" app.log
find /C "WARNING" app.log
find /C "INFO" app.log

REM IPアドレスを抽出
findstr /R "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" access.log > ips.txt

REM アクセスログから特定のステータスコードを抽出
findstr "200" access.log > success.log
findstr "404" access.log > notfound.log
findstr "500" access.log > servererror.log

REM ログファイルのローテーション
@echo off
set LOGFILE=app.log
set MAXSIZE=10485760
for %%A in (%LOGFILE%) do set SIZE=%%~zA
if %SIZE% GTR %MAXSIZE% (
    set TIMESTAMP=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
    set TIMESTAMP=!TIMESTAMP: =0!
    move %LOGFILE% %LOGFILE%.!TIMESTAMP!
    type nul > %LOGFILE%
)

REM ログファイルから特定の期間を抽出（PowerShell使用）
powershell "Get-Content app.log | Where-Object { $_ -match '2026-05-0[1-5]' } | Out-File filtered.log"

REM ログの集計（エラーの出現回数）
@echo off
echo エラー種別ごとの出現回数: > summary.txt
for /F "tokens=*" %%e in ('findstr /I "ERROR" app.log ^| findstr /R "ERROR[0-9]*" ^| sort ^| uniq -c') do (
    echo %%e >> summary.txt
)
```

### CSVファイル操作
```cmd
REM CSVの特定列を抽出
for /F "tokens=1,3 delims=," %%a in (data.csv) do (
    echo %%a,%%b
)

REM CSVファイルの行数をカウント
find /C /V "" data.csv

REM ヘッダーを除いた行数
for /F "skip=1" %%a in ('find /C /V "" data.csv') do echo %%a

REM CSVファイルをフィルタリング
@echo off
for /F "skip=1 tokens=1,2,3 delims=," %%a in (data.csv) do (
    if %%b GTR 30 (
        echo %%a,%%b,%%c >> filtered.csv
    )
)

REM CSVファイルのソート
sort data.csv > sorted.csv

REM CSVファイルの列を追加
@echo off
for /F "tokens=* delims=" %%a in (data.csv) do (
    echo %%a,NewColumn >> output.csv
)

REM CSV to JSON 変換（PowerShell使用）
powershell "Import-Csv data.csv | ConvertTo-Json | Out-File data.json"

REM CSV to XML 変換（PowerShell使用）
powershell "Import-Csv data.csv | Export-Clixml data.xml"

REM CSVファイルの結合（横方向）
paste file1.csv file2.csv > combined.csv

REM 重複行の削除
sort data.csv | uniq > unique.csv
```

### テキストエディタ操作
```cmd
REM メモ帳でファイルを開く
notepad file.txt
start notepad file.txt

REM 複数ファイルを開く
for %%f in (*.txt) do start notepad "%%f"

REM デフォルトエディタで開く
start file.txt

REM 特定のエディタで開く
start "" "C:\Program Files\Editor\editor.exe" file.txt

REM VSCodeで開く
code file.txt
code .

REM 行番号を指定して開く
code -g file.txt:10:5  REM 10行目5列目

REM ファイルを読み取り専用で開く
attrib +R file.txt
notepad file.txt
attrib -R file.txt
```

### ファイル変換
```cmd
REM 文字コード変換（PowerShell使用）
REM UTF-8 to Shift-JIS
powershell "Get-Content file.txt -Encoding UTF8 | Out-File -Encoding Default output.txt"

REM Shift-JIS to UTF-8
powershell "Get-Content file.txt -Encoding Default | Out-File -Encoding UTF8 output.txt"

REM UTF-8 with BOM to UTF-8 without BOM
powershell "$content = Get-Content file.txt -Raw; [System.IO.File]::WriteAllText('output.txt', $content, (New-Object System.Text.UTF8Encoding $false))"

REM 改行コードの変換（LF to CRLF）
powershell "(Get-Content file.txt -Raw) -replace '\n', \"\r\n\" | Set-Content output.txt"

REM 改行コードの変換（CRLF to LF）
powershell "(Get-Content file.txt -Raw) -replace '\r\n', '\n' | Set-Content output.txt"

REM タブをスペースに変換
powershell "(Get-Content file.txt) -replace '\t', '    ' | Set-Content output.txt"

REM 全角を半角に変換（PowerShell使用）
powershell "[System.Text.Encoding]::ASCII.GetString([System.Text.Encoding]::GetEncoding('shift_jis').GetBytes((Get-Content file.txt -Raw)))"

REM DOSからUnix形式のテキストに変換
powershell "(Get-Content file.txt) | Set-Content -NoNewline output.txt; Add-Content output.txt ''"
```

### ファイルの監視
```cmd
REM ファイルの変更を監視（PowerShell使用）
powershell "$watcher = New-Object System.IO.FileSystemWatcher; $watcher.Path = 'C:\folder'; $watcher.Filter = '*.txt'; $watcher.EnableRaisingEvents = $true; Register-ObjectEvent $watcher 'Changed' -Action { Write-Host \"File changed: $($Event.SourceEventArgs.Name)\" }; Wait-Event; Unregister-Event -SourceIdentifier *"

REM ディレクトリの変更を継続的に監視
powershell "$watcher = New-Object System.IO.FileSystemWatcher; $watcher.Path = 'C:\folder'; $watcher.IncludeSubdirectories = $true; $watcher.EnableRaisingEvents = $true; while($true) { $result = $watcher.WaitForChanged([System.IO.WatcherChangeTypes]::All, 1000); if($result.TimedOut -eq $false) { Write-Host \"$($result.ChangeType): $($result.Name)\" } }"

REM ファイルサイズの変化を監視
@echo off
set FILE=monitoring.log
set PREVSIZE=0
:monitor
for %%A in (%FILE%) do set SIZE=%%~zA
if not "%SIZE%"=="%PREVSIZE%" (
    echo ファイルサイズ変更: %PREVSIZE% -> %SIZE% bytes
    set PREVSIZE=%SIZE%
)
timeout /T 5 /NOBREAK >nul
goto monitor
```

---

## プロセス管理

### プロセス一覧・情報取得
```cmd
REM 実行中のプロセス一覧
tasklist
tasklist /V      REM 詳細表示
tasklist /FI "STATUS eq RUNNING"  REM 実行中のみ
tasklist /FI "MEMUSAGE gt 100000" REM メモリ使用量でフィルタ

REM 特定プロセスの検索
tasklist | find "chrome"
tasklist /FI "IMAGENAME eq chrome.exe"
```

### プロセスの起動・停止
```cmd
REM プロセス起動
start notepad.exe
start https://www.google.com
start "" "C:\Program Files\app.exe"  REM パスにスペースがある場合

REM バックグラウンドで起動
start /B program.exe

REM 最小化して起動
start /MIN notepad.exe

REM 待機してから起動
start /WAIT program.exe

REM プロセス停止
taskkill /IM notepad.exe
taskkill /PID 1234
taskkill /F /IM chrome.exe  REM 強制終了
taskkill /F /FI "MEMUSAGE gt 500000"  REM 条件で終了
```

---

## ネットワーク

### 接続テスト
```cmd
REM Ping
ping google.com
ping 8.8.8.8
ping -t google.com  REM 継続的にping
ping -n 10 google.com  REM 10回ping

REM 経路確認
tracert google.com
tracert 8.8.8.8

REM ポート接続テスト
telnet google.com 80
```

### ネットワーク情報
```cmd
REM IP設定を表示
ipconfig
ipconfig /all  REM 詳細表示

REM DNS情報をクリア
ipconfig /flushdns

REM IPアドレスの解放・取得（DHCP）
ipconfig /release
ipconfig /renew

REM ネットワーク統計
netstat
netstat -a     REM すべての接続とリスニングポート
netstat -n     REM アドレスとポートを数値で表示
netstat -o     REM プロセスIDを表示
netstat -ano   REM すべて、数値、プロセスID
netstat -ano | findstr :80  REM ポート80の接続

REM ルーティングテーブル
route print
route add 192.168.1.0 MASK 255.255.255.0 192.168.0.1  REM ルート追加
route delete 192.168.1.0  REM ルート削除

REM ARP テーブル
arp -a

REM DNS名前解決
nslookup google.com
nslookup 8.8.8.8
```

### ファイアウォール（管理者権限必要）
```cmd
REM ファイアウォール状態確認
netsh advfirewall show allprofiles

REM ファイアウォールを有効/無効化
netsh advfirewall set allprofiles state on
netsh advfirewall set allprofiles state off

REM ファイアウォールルール追加
netsh advfirewall firewall add rule name="Allow Port 8080" dir=in action=allow protocol=TCP localport=8080
```

### ファイルダウンロード
```cmd
REM PowerShell経由でダウンロード
powershell -Command "Invoke-WebRequest -Uri 'https://example.com/file.zip' -OutFile 'file.zip'"

REM bitsadmin でダウンロード
bitsadmin /transfer myDownloadJob /download /priority normal https://example.com/file.zip C:\Downloads\file.zip

REM curl（Windows 10 1803以降）
curl https://example.com/file.txt -o file.txt
curl -L https://example.com/file.zip -o file.zip  REM リダイレクトに従う
```

---

## システム情報

### システム情報取得
```cmd
REM システム詳細情報
systeminfo
systeminfo | findstr /C:"OS"  REM OS情報のみ
systeminfo | findstr /C:"System Boot Time"  REM 起動時間

REM コンピュータ名
hostname
echo %COMPUTERNAME%

REM ユーザー名
echo %USERNAME%
whoami

REM OSバージョン
ver
winver  REM GUIで表示

REM 環境情報
set  REM すべての環境変数を表示
```

### ディスク情報
```cmd
REM ディスク一覧
wmic logicaldisk get name,size,freespace
fsutil fsinfo drives

REM ボリューム情報
vol
vol C:

REM ディスク使用状況
dir /S  REM 総サイズを表示
```

### ドライバー・ハードウェア情報
```cmd
REM ドライバー一覧
driverquery
driverquery /V  REM 詳細表示

REM ハードウェア情報（WMIC使用）
wmic cpu get name,maxclockspeed,numberofcores
wmic memorychip get capacity,speed
wmic diskdrive get model,size
wmic baseboard get product,manufacturer,version
wmic bios get serialnumber
```

### サービス管理（管理者権限必要）
```cmd
REM サービス一覧
net start
sc query

REM サービス状態確認
sc query wuauserv

REM サービス開始・停止
net start "サービス名"
net stop "サービス名"
sc start サービス名
sc stop サービス名

REM サービスの自動起動設定
sc config サービス名 start= auto
sc config サービス名 start= disabled
```

### ユーザー・グループ管理（管理者権限必要）
```cmd
REM ローカルユーザー一覧
net user
net user ユーザー名  REM ユーザー詳細

REM ユーザー作成
net user newuser password /add

REM ユーザー削除
net user username /delete

REM グループ一覧
net localgroup

REM グループにユーザー追加
net localgroup Administrators username /add
```

---

## バッチファイル

### 基本構文
```cmd
@echo off
REM これはコメント

REM 変数の定義
set NAME=太郎
set /A NUMBER=42

REM 変数の使用
echo こんにちは、%NAME%さん
set /A RESULT=%NUMBER% + 10
echo 結果: %RESULT%

REM ユーザー入力
set /P INPUT="名前を入力してください: "
echo あなたの名前は %INPUT% です

REM 条件分岐
if "%INPUT%"=="太郎" (
    echo こんにちは、太郎さん
) else (
    echo こんにちは、%INPUT%さん
)

REM ファイル存在チェック
if exist file.txt (
    echo ファイルが存在します
) else (
    echo ファイルが見つかりません
)

REM ディレクトリ存在チェック
if exist "C:\folder\" (
    echo ディレクトリが存在します
)

REM 数値比較
if %NUMBER% GTR 10 (
    echo 10より大きい
)
REM GTR (>), LSS (<), GEQ (>=), LEQ (<=), EQU (==), NEQ (!=)

REM 論理演算
if %NUMBER% GTR 10 if %NUMBER% LSS 100 (
    echo 10より大きく100より小さい
)

REM エラーレベルチェック
if %ERRORLEVEL% EQU 0 (
    echo コマンド成功
) else (
    echo コマンド失敗
)
```

### ループ
```cmd
REM 単純なループ
for %%i in (1 2 3 4 5) do (
    echo %%i
)

REM ファイルのループ
for %%f in (*.txt) do (
    echo %%f
)

REM サブディレクトリを含むファイル検索
for /R %%f in (*.txt) do (
    echo %%f
)

REM ディレクトリのループ
for /D %%d in (*) do (
    echo %%d
)

REM 数値範囲のループ
for /L %%i in (1,1,10) do (
    echo %%i
)

REM ファイル内容を1行ずつ処理
for /F "tokens=*" %%a in (file.txt) do (
    echo %%a
)

REM コマンド出力を処理
for /F "tokens=*" %%a in ('dir /B') do (
    echo %%a
)

REM CSVファイルを処理（カンマ区切り）
for /F "tokens=1,2,3 delims=," %%a in (data.csv) do (
    echo 名前:%%a, 年齢:%%b, 職業:%%c
)
```

### サブルーチン（関数）
```cmd
@echo off

REM メイン処理
call :greet 太郎
call :add 10 20
exit /B

REM サブルーチン定義
:greet
echo こんにちは、%~1さん
exit /B

:add
set /A RESULT=%~1 + %~2
echo %~1 + %~2 = %RESULT%
exit /B
```

### エラーハンドリング
```cmd
@echo off

REM コマンド実行とエラーチェック
del nonexistent.txt 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ファイルが見つかりません
)

REM エラーメッセージを抑制
command 2>nul

REM 出力をファイルにリダイレクト
command > output.txt 2>&1

REM 標準出力とエラー出力を別ファイルに
command > output.txt 2> error.txt
```

### 便利なバッチ技
```cmd
REM スクリプトのあるディレクトリに移動
cd /D "%~dp0"

REM 管理者権限チェック
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 管理者権限が必要です
    exit /B 1
)

REM 一時停止
pause

REM 指定秒数待機
timeout /T 5 /NOBREAK

REM タイムスタンプ取得
echo %DATE% %TIME%
set TIMESTAMP=%DATE:~-10,4%%DATE:~-5,2%%DATE:~-2,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%

REM バッチファイルの引数
echo 第1引数: %1
echo 第2引数: %2
echo すべての引数: %*
echo 引数の数: %0
```

---

## 高度なバッチ技術

### 配列の実装
```cmd
@echo off
setlocal EnableDelayedExpansion

REM 配列の定義
set array[0]=apple
set array[1]=banana
set array[2]=orange
set array[3]=grape

REM 配列の要素にアクセス
echo !array[0]!
echo !array[2]!

REM 配列をループ処理
for /L %%i in (0,1,3) do (
    echo 要素%%i: !array[%%i]!
)

REM 動的に配列に追加
set count=0
for %%f in (*.txt) do (
    set files[!count!]=%%f
    set /A count+=1
)

REM 配列の内容を表示
for /L %%i in (0,1,%count%) do (
    if defined files[%%i] echo !files[%%i]!
)
```

### 遅延環境変数展開
```cmd
@echo off
setlocal EnableDelayedExpansion

REM 通常の展開では正しく動作しない例
set count=0
for %%f in (*.txt) do (
    set /A count=%count%+1  REM これは常に1になる
)
echo 通常の展開: %count%

REM 遅延展開を使った正しい例
set count=0
for %%f in (*.txt) do (
    set /A count=!count!+1  REM これは正しくカウントされる
)
echo 遅延展開: !count!

REM 変数の値を使った計算
set x=10
set y=20
set /A result=!x!+!y!
echo !x! + !y! = !result!
```

### 関数の戻り値
```cmd
@echo off
setlocal EnableDelayedExpansion

REM 戻り値を受け取る
call :multiply 5 7 result
echo 結果: %result%

call :isFileExists "test.txt" exists
if %exists%==1 (
    echo ファイルが存在します
) else (
    echo ファイルが存在しません
)

exit /B

:multiply
set /A temp=%~1 * %~2
set "%~3=%temp%"
exit /B

:isFileExists
if exist "%~1" (
    set "%~2=1"
) else (
    set "%~2=0"
)
exit /B
```

### 日付と時刻の処理
```cmd
@echo off

REM 現在の日付と時刻
echo 日付: %DATE%
echo 時刻: %TIME%

REM 日付の分解（日本語環境: YYYY/MM/DD）
for /F "tokens=1-3 delims=/" %%a in ("%DATE%") do (
    set YEAR=%%a
    set MONTH=%%b
    set DAY=%%c
)
echo 年: %YEAR%, 月: %MONTH%, 日: %DAY%

REM 時刻の分解
for /F "tokens=1-4 delims=:., " %%a in ("%TIME%") do (
    set HOUR=%%a
    set MINUTE=%%b
    set SECOND=%%c
    set MSEC=%%d
)
echo 時: %HOUR%, 分: %MINUTE%, 秒: %SECOND%

REM ファイル名用のタイムスタンプ
set TIMESTAMP=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%  REM スペースを0に置換
echo タイムスタンプ: %TIMESTAMP%

REM タイムスタンプ付きログファイル作成
set LOGFILE=log_%TIMESTAMP%.txt
echo ログ開始 > %LOGFILE%
```

### エラーハンドリングの高度な技術
```cmd
@echo off
setlocal EnableDelayedExpansion

REM エラーハンドラ関数を使用
call :withErrorHandling someCommand arg1 arg2
if !ERRORLEVEL! NEQ 0 (
    echo コマンド実行に失敗しました
    goto :error
)

REM 複数のコマンドを実行し、どれか失敗したら終了
call :executeWithCheck dir C:\
call :executeWithCheck copy file.txt backup.txt
call :executeWithCheck del temp.txt

echo すべて成功しました
goto :end

:withErrorHandling
%* 2>nul
if !ERRORLEVEL! NEQ 0 (
    echo エラー: コマンド '%*' が失敗しました (終了コード: !ERRORLEVEL!)
)
exit /B !ERRORLEVEL!

:executeWithCheck
%*
if !ERRORLEVEL! NEQ 0 (
    echo エラー: コマンド '%*' が失敗しました
    goto :error
)
exit /B 0

:error
echo スクリプトをエラーで終了します
exit /B 1

:end
echo スクリプト完了
exit /B 0
```

### 文字列操作の高度な技術
```cmd
@echo off
setlocal EnableDelayedExpansion

set STRING=Hello World 12345

REM 文字列の長さを取得
set str=%STRING%
set len=0
:strlen_loop
if not "!str:~%len%!"==" " set /A len+=1 & goto :strlen_loop
echo 文字列の長さ: %len%

REM 部分文字列の抽出
set SUBSTR=%STRING:~0,5%  REM 先頭5文字
echo 先頭5文字: %SUBSTR%

set SUBSTR=%STRING:~6%  REM 7文字目以降
echo 7文字目以降: %SUBSTR%

set SUBSTR=%STRING:~-5%  REM 末尾5文字
echo 末尾5文字: %SUBSTR%

set SUBSTR=%STRING:~6,5%  REM 7文字目から5文字
echo 7文字目から5文字: %SUBSTR%

REM 文字列の置換
set NEWSTR=%STRING:Hello=Hi%
echo 置換後: %NEWSTR%

set NEWSTR=%STRING: =%  REM スペースを削除
echo スペース削除: %NEWSTR%

REM 大文字・小文字変換（PowerShell使用）
for /F "delims=" %%a in ('powershell "'%STRING%'.ToUpper()"') do set UPPER=%%a
echo 大文字: %UPPER%

for /F "delims=" %%a in ('powershell "'%STRING%'.ToLower()"') do set LOWER=%%a
echo 小文字: %LOWER%
```

### プログレスバーの実装
```cmd
@echo off
setlocal EnableDelayedExpansion

set total=50
set current=0

:progress_loop
if !current! GEQ !total! goto :progress_end

REM プログレスバーを表示
set /A percent=!current!*100/!total!
set bar=
set /A barlen=!current!*40/!total!
for /L %%i in (1,1,!barlen!) do set bar=!bar!█
for /L %%i in (!barlen!,1,39) do set bar=!bar!░

REM カーソル位置を保存して上書き表示
echo [!bar!] !percent!%%

REM 何か処理をシミュレート
timeout /T 0.1 /NOBREAK >nul
set /A current+=1

REM 前の行をクリア
echo [1A[2K
goto :progress_loop

:progress_end
echo [████████████████████████████████████████] 100%%
echo 完了！
```

### メニューシステムの実装
```cmd
@echo off
setlocal EnableDelayedExpansion

:menu
cls
echo ========================================
echo          メインメニュー
echo ========================================
echo.
echo 1. ファイル一覧表示
echo 2. ディレクトリ作成
echo 3. システム情報表示
echo 4. ネットワーク情報表示
echo 5. 終了
echo.
set /P choice="選択してください (1-5): "

if "%choice%"=="1" goto :option1
if "%choice%"=="2" goto :option2
if "%choice%"=="3" goto :option3
if "%choice%"=="4" goto :option4
if "%choice%"=="5" goto :exit

echo 無効な選択です。
pause
goto :menu

:option1
cls
echo ファイル一覧:
dir /B
echo.
pause
goto :menu

:option2
cls
set /P dirname="ディレクトリ名を入力: "
mkdir "%dirname%" 2>nul
if !ERRORLEVEL! EQU 0 (
    echo ディレクトリ '%dirname%' を作成しました。
) else (
    echo ディレクトリの作成に失敗しました。
)
pause
goto :menu

:option3
cls
echo システム情報:
systeminfo | findstr /C:"OS" /C:"System"
echo.
pause
goto :menu

:option4
cls
echo ネットワーク情報:
ipconfig | findstr /C:"IPv4" /C:"Subnet" /C:"Gateway"
echo.
pause
goto :menu

:exit
echo プログラムを終了します。
exit /B 0
```

---

## ディスク管理

### CHKDSK（ディスクチェック）
```cmd
REM ディスクチェック（読み取り専用）
chkdsk C:

REM エラー修復（管理者権限必要）
chkdsk C: /F

REM 不良セクタ回復を含む完全チェック
chkdsk C: /R

REM 次回起動時にチェック予約
chkdsk C: /F /R
```

### DISKPART（ディスクパーティション管理）
```cmd
REM diskpart 起動（管理者権限必要）
diskpart

REM diskpart 内のコマンド
list disk        REM ディスク一覧
select disk 1    REM ディスク選択
list partition   REM パーティション一覧
list volume      REM ボリューム一覧
detail disk      REM ディスク詳細
clean           REM ディスククリーン（注意！）
```

### ディスククリーンアップ
```cmd
REM ディスククリーンアップ起動
cleanmgr

REM 自動クリーンアップ
cleanmgr /sagerun:1

REM ドライブを指定してクリーンアップ
cleanmgr /d C:
```

### シャドウコピー（VSS）
```cmd
REM シャドウコピー一覧（管理者権限必要）
vssadmin list shadows

REM シャドウコピーのストレージ情報
vssadmin list shadowstorage

REM シャドウコピー作成
vssadmin create shadow /for=C:

REM シャドウコピー削除
vssadmin delete shadows /for=C: /oldest
```

### ディスクの最適化
```cmd
REM デフラグ分析
defrag C: /A

REM デフラグ実行
defrag C: /O

REM SSDの最適化（TRIM）
defrag C: /L

REM すべてのドライブを最適化
defrag /C /O
```

---

## ファイル圧縮・展開

### 組み込みの圧縮機能
```cmd
REM ファイル・フォルダを圧縮（NTFS圧縮）
compact /C file.txt
compact /C /S:C:\folder  REM フォルダとサブフォルダを圧縮

REM 圧縮を解除
compact /U file.txt

REM 圧縮状態を確認
compact /Q file.txt
dir /A:C  REM 圧縮ファイルのみ表示
```

### PowerShellを使用した圧縮・展開
```cmd
REM ZIP圧縮（PowerShell 5.0以降）
powershell "Compress-Archive -Path 'C:\source\*' -DestinationPath 'C:\archive.zip'"
powershell "Compress-Archive -Path 'file1.txt','file2.txt' -DestinationPath 'archive.zip'"

REM 既存のZIPに追加
powershell "Compress-Archive -Path 'newfile.txt' -Update -DestinationPath 'archive.zip'"

REM ZIP展開
powershell "Expand-Archive -Path 'archive.zip' -DestinationPath 'C:\destination'"
powershell "Expand-Archive -Path 'archive.zip' -DestinationPath 'C:\destination' -Force"  REM 上書き
```

### makecab / expand コマンド
```cmd
REM CABファイルを作成
makecab file.txt file.cab

REM CABファイルを展開
expand file.cab -F:* C:\destination
expand archive.cab file.txt  REM 特定のファイルのみ展開

REM CABファイルの内容を表示
expand archive.cab -D
```

### tar コマンド（Windows 10 1803以降）
```cmd
REM tar.gz を作成
tar -czf archive.tar.gz folder\

REM tar ファイルを作成
tar -cf archive.tar file1.txt file2.txt

REM tar.gz を展開
tar -xzf archive.tar.gz
tar -xzf archive.tar.gz -C C:\destination  REM 展開先を指定

REM tar ファイルを展開
tar -xf archive.tar

REM tar ファイルの内容を表示
tar -tzf archive.tar.gz
tar -tf archive.tar

REM zip 形式（tar でも可能）
tar -cf archive.zip --format=zip file1.txt file2.txt
tar -xf archive.zip
```

---

## 環境変数

### 環境変数の表示
```cmd
REM すべての環境変数
set

REM 特定の環境変数
echo %PATH%
echo %USERPROFILE%
echo %TEMP%
echo %PROGRAMFILES%
echo %SYSTEMROOT%
```

### 環境変数の設定
```cmd
REM 現在のセッションのみ設定
set MYVAR=value
echo %MYVAR%

REM 環境変数に追加
set PATH=%PATH%;C:\new\path

REM 永続的な環境変数設定（管理者権限必要）
setx MYVAR "value"  REM ユーザー環境変数
setx MYVAR "value" /M  REM システム環境変数

REM PATH に追加（永続的）
setx PATH "%PATH%;C:\new\path"
```

### よく使う環境変数
```cmd
%CD%               REM 現在のディレクトリ
%DATE%             REM 現在の日付
%TIME%             REM 現在の時刻
%RANDOM%           REM ランダムな数値
%ERRORLEVEL%       REM 最後のコマンドの終了コード
%COMPUTERNAME%     REM コンピュータ名
%USERNAME%         REM ユーザー名
%USERPROFILE%      REM ユーザープロファイルディレクトリ
%HOMEDRIVE%        REM ホームドライブ
%HOMEPATH%         REM ホームパス
%SYSTEMROOT%       REM Windowsディレクトリ（通常 C:\Windows）
%PROGRAMFILES%     REM Program Files ディレクトリ
%TEMP%             REM 一時ファイルディレクトリ
%TMP%              REM 一時ファイルディレクトリ
```

---

## パイプとリダイレクト

### パイプ
```cmd
REM 前のコマンドの出力を次のコマンドに渡す
dir | find ".txt"
tasklist | findstr "chrome"
ipconfig | find "IPv4"
```

### リダイレクト
```cmd
REM 出力をファイルに書き込み（上書き）
dir > output.txt
echo text > file.txt

REM 出力をファイルに追記
dir >> output.txt
echo text >> file.txt

REM エラー出力をファイルに
command 2> error.txt

REM 標準出力とエラー出力を同じファイルに
command > output.txt 2>&1

REM 出力を破棄
command > nul
command 2> nul
command > nul 2>&1

REM ファイルから入力
sort < input.txt
```

### 複数コマンドの実行
```cmd
REM 順次実行（前のコマンドの成否に関わらず実行）
command1 & command2 & command3

REM 前のコマンドが成功した場合のみ次を実行
command1 && command2

REM 前のコマンドが失敗した場合のみ次を実行
command1 || command2

REM 複合例
mkdir newfolder && cd newfolder && echo success

REM グループ化
(command1 & command2) > output.txt
```

---

## よく使う便利なコマンド

### ファイル操作
```cmd
REM 特定の拡張子を一括削除
del /S /Q *.tmp

REM ファイル名を一括変更
ren *.txt *.bak

REM ディレクトリサイズを計算
dir /S | find "File(s)"

REM 空のディレクトリを削除
for /F "delims=" %%d in ('dir /AD /B /S ^| sort /R') do rd "%%d" 2>nul

REM ファイルの行数をカウント
find /C /V "" file.txt
```

### システム管理
```cmd
REM システムをシャットダウン（管理者権限必要）
shutdown /s /t 0          REM 即座にシャットダウン
shutdown /r /t 0          REM 再起動
shutdown /h               REM 休止状態
shutdown /a               REM シャットダウンをキャンセル
shutdown /s /t 3600       REM 1時間後にシャットダウン

REM タスクスケジューラでタスク作成
schtasks /create /tn "MyTask" /tr "C:\script.bat" /sc daily /st 09:00

REM タスク一覧
schtasks /query

REM レジストリ操作（注意！）
reg query HKLM\Software
reg add HKCU\Software\MyApp /v Version /t REG_SZ /d "1.0"
reg delete HKCU\Software\MyApp /v Version /f

REM イベントログ表示
wevtutil qe System /c:10 /f:text  REM 最新10件
```

### ネットワーク管理
```cmd
REM 共有フォルダ一覧
net share

REM ネットワークドライブマッピング
net use Z: \\server\share
net use Z: /delete

REM ネットワーク接続一覧
net use

REM Windowsファイアウォール状態
netsh advfirewall show allprofiles state

REM Wi-Fi パスワード表示
netsh wlan show profile name="SSID名" key=clear
```

---

## ショートカットキー

- **Ctrl+C**: コマンド中断
- **Ctrl+V**: 貼り付け（Windows 10以降）
- **Ctrl+M**: マークモード（テキスト選択）
- **F1**: コマンドを1文字ずつ再入力
- **F3**: 前回のコマンドを再入力
- **F7**: コマンド履歴を表示（GUI）
- **F8**: コマンド履歴をインクリメンタルサーチ
- **↑/↓**: コマンド履歴を移動
- **Tab**: ファイル名・ディレクトリ名の補完
- **Esc**: 現在の入力をクリア

---

## DOSKEYエイリアス

doskey を使ってコマンドのエイリアスを作成できます。

```cmd
REM エイリアス作成
doskey ls=dir /B $*
doskey ll=dir $*
doskey ..=cd ..
doskey ...=cd ..\..
doskey ~=cd %USERPROFILE%

REM エイリアス一覧表示
doskey /macros

REM エイリアスを削除
doskey ls=

REM エイリアスを永続化（バッチファイルで読み込み）
REM alias.txt に保存
doskey /macros > alias.txt
REM 読み込み
doskey /macrofile=alias.txt
```

---

## Tips

### コマンドプロンプトの設定
```cmd
REM 管理者としてコマンドプロンプトを起動
REM Win+X → A（または Win+R → cmd → Ctrl+Shift+Enter）

REM カラー変更
color 0A  REM 緑色の文字
color 1F  REM 青背景、白文字
REM 0=黒, 1=青, 2=緑, 3=水, 4=赤, 5=紫, 6=黄, 7=白
REM 8=灰, 9=明青, A=明緑, B=明水, C=明赤, D=明紫, E=明黄, F=輝白

REM プロンプト変更
prompt $P$G         REM デフォルト（C:\>）
prompt $P$_$G       REM 2行表示
prompt $D $T $P$G   REM 日付と時刻を表示
```

### 文字コード変更
```cmd
REM UTF-8に変更
chcp 65001

REM Shift-JISに変更
chcp 932

REM 現在のコードページ確認
chcp
```

### クリップボード操作
```cmd
REM コマンド出力をクリップボードにコピー
dir | clip
type file.txt | clip

REM ファイルの内容をクリップボードにコピー
clip < file.txt
```

---

## セキュリティとアクセス制御

### ファイル・フォルダのアクセス権限
```cmd
REM アクセス権限を表示
icacls file.txt
icacls C:\folder

REM 権限を付与（管理者権限必要）
icacls file.txt /grant ユーザー名:F  REM フルコントロール
icacls file.txt /grant ユーザー名:R  REM 読み取り
icacls file.txt /grant ユーザー名:W  REM 書き込み
icacls file.txt /grant ユーザー名:M  REM 変更

REM 権限を削除
icacls file.txt /remove ユーザー名

REM 継承を無効化
icacls file.txt /inheritance:r

REM 継承を有効化
icacls file.txt /inheritance:e

REM 権限をリセット
icacls file.txt /reset

REM サブフォルダにも適用
icacls C:\folder /grant ユーザー名:F /T

REM 所有者を変更（管理者権限必要）
takeown /F file.txt
takeown /F C:\folder /R /D Y  REM フォルダとサブフォルダ
```

### 暗号化
```cmd
REM ファイルを暗号化（EFS - 管理者権限必要）
cipher /E file.txt
cipher /E /S:C:\folder  REM フォルダ配下すべて

REM 暗号化を解除
cipher /D file.txt

REM 暗号化状態を確認
cipher /C file.txt
dir /A:E  REM 暗号化ファイルのみ表示

REM 暗号化証明書のバックアップ
cipher /X:backup.pfx
```

### ユーザーアカウント制御（UAC）
```cmd
REM 管理者権限で実行が必要かチェック
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 管理者権限が必要です
    echo 管理者として実行してください
    pause
    exit /B 1
)

REM バッチファイルから管理者権限で再起動
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /B
)
```

### パスワードとセキュアな入力
```cmd
REM パスワード入力（表示されない - PowerShell使用）
for /F "delims=" %%p in ('powershell -Command "$p = Read-Host -AsSecureString 'パスワード'; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($p))"') do set PASSWORD=%%p

REM 簡易的なパスワード入力（エコーオフ）
set /P "PASSWORD=パスワードを入力: "
```

### ファイアウォールの詳細設定
```cmd
REM ファイアウォールルールの一覧
netsh advfirewall firewall show rule name=all

REM 特定のルールを表示
netsh advfirewall firewall show rule name="ルール名"

REM ルール追加（インバウンド）
netsh advfirewall firewall add rule name="My App" dir=in action=allow program="C:\app.exe" enable=yes
netsh advfirewall firewall add rule name="Allow 8080" dir=in action=allow protocol=TCP localport=8080

REM ルール追加（アウトバウンド）
netsh advfirewall firewall add rule name="Block App" dir=out action=block program="C:\app.exe"

REM ルール削除
netsh advfirewall firewall delete rule name="ルール名"

REM 特定のIPアドレスをブロック
netsh advfirewall firewall add rule name="Block IP" dir=in action=block remoteip=192.168.1.100

REM ルールを無効化/有効化
netsh advfirewall firewall set rule name="ルール名" new enable=no
netsh advfirewall firewall set rule name="ルール名" new enable=yes
```

---

## デバッグとトラブルシューティング

### バッチファイルのデバッグ
```cmd
@echo off
REM デバッグモードを有効化
if "%DEBUG%"=="1" (
    echo デバッグモード有効
    @echo on
)

REM 各コマンドの実行を表示しながら実行
@echo on
dir
echo Hello
@echo off

REM トレースログ出力
set LOGFILE=debug.log
echo [%DATE% %TIME%] スクリプト開始 >> %LOGFILE%
echo [%DATE% %TIME%] コマンド実行 >> %LOGFILE%
command >> %LOGFILE% 2>&1

REM エラー発生時の詳細情報
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] コマンド失敗: %ERRORLEVEL% >> %LOGFILE%
    echo 現在のディレクトリ: %CD% >> %LOGFILE%
    echo 環境変数PATH: %PATH% >> %LOGFILE%
)
```

### ステップ実行
```cmd
@echo off
setlocal EnableDelayedExpansion

set DEBUG=1

:debug_execute
if "%DEBUG%"=="1" (
    echo 次のコマンドを実行: %1 %2 %3 %4 %5
    pause
)
%*
if !ERRORLEVEL! NEQ 0 (
    echo エラー発生: 終了コード !ERRORLEVEL!
    pause
)
exit /B !ERRORLEVEL!

REM 使用例
call :debug_execute dir
call :debug_execute copy file.txt backup.txt
```

### システムファイルチェッカー
```cmd
REM システムファイルの整合性チェック（管理者権限必要）
sfc /scannow

REM 特定のファイルをチェック
sfc /scanfile=C:\Windows\System32\kernel32.dll

REM スキャンのみ（修復しない）
sfc /verifyonly

REM オフラインシステムのスキャン
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
```

### DISM（Deployment Image Servicing and Management）
```cmd
REM システムイメージの健全性チェック（管理者権限必要）
DISM /Online /Cleanup-Image /CheckHealth

REM より詳細なスキャン
DISM /Online /Cleanup-Image /ScanHealth

REM システムイメージの修復
DISM /Online /Cleanup-Image /RestoreHealth

REM Windows Updateからソースを取得して修復
DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:D:\sources\install.wim:1
```

### イベントログの確認
```cmd
REM システムイベントログを表示
wevtutil qe System /c:20 /rd:true /f:text

REM アプリケーションイベントログ
wevtutil qe Application /c:20 /rd:true /f:text

REM エラーのみ表示
wevtutil qe System "/q:*[System[(Level=2)]]" /c:10 /f:text

REM 特定の時間範囲
wevtutil qe System "/q:*[System[TimeCreated[@SystemTime>='2026-01-01T00:00:00']]]" /f:text

REM イベントログをファイルに出力
wevtutil epl System C:\system_events.evtx

REM イベントログをクリア（管理者権限必要）
wevtutil cl System
```

### ネットワーク診断
```cmd
REM ネットワークアダプタのリセット
netsh winsock reset
netsh int ip reset
ipconfig /flushdns

REM TCP/IPスタックのリセット
netsh int tcp reset

REM ネットワーク診断
netsh interface show interface
netsh interface ip show config

REM パケットロスの確認
ping -n 100 8.8.8.8

REM ネットワーク統計の連続表示
netstat -e -t 5  REM 5秒ごとに更新

REM DNSキャッシュの確認
ipconfig /displaydns

REM Windows ネットワーク診断の実行
msdt /id NetworkDiagnosticsWeb
```

### プロセスのトラブルシューティング
```cmd
REM プロセスの詳細情報
tasklist /V /FO LIST /FI "IMAGENAME eq chrome.exe"

REM プロセスが使用しているDLL
tasklist /M /FI "IMAGENAME eq app.exe"

REM プロセスのサービス情報
tasklist /SVC

REM 応答していないプロセス
tasklist /FI "STATUS eq NOT RESPONDING"

REM プロセスツリー表示（PowerShell使用）
powershell "Get-Process | Select-Object Name,Id,@{N='ParentProcessId';E={$_.Parent.Id}} | Format-Table"

REM プロセスのメモリダンプ作成（デバッグ用）
REM Sysinternalsツール procdump.exe が必要
procdump -ma process.exe dump.dmp
```

---

## パフォーマンス最適化

### システムパフォーマンスの監視
```cmd
REM パフォーマンスカウンタの一覧
typeperf -q

REM CPU使用率を監視
typeperf "\Processor(_Total)\%% Processor Time" -si 1 -sc 10

REM メモリ使用状況を監視
typeperf "\Memory\Available MBytes" -si 1 -sc 10

REM ディスクI/Oを監視
typeperf "\PhysicalDisk(_Total)\Disk Reads/sec" "\PhysicalDisk(_Total)\Disk Writes/sec" -si 1

REM 複数のカウンタをファイルに記録
typeperf -cf counters.txt -o performance.csv -si 5 -sc 100
```

### リソースモニタ
```cmd
REM リソースモニタを起動
resmon

REM パフォーマンスモニタ
perfmon

REM タスクマネージャー
taskmgr
```

### メモリ管理
```cmd
REM 物理メモリ情報
systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"

REM メモリ使用量の多いプロセス
tasklist /V | sort /R /+65  REM メモリサイズでソート

REM 仮想メモリ（ページファイル）情報
wmic pagefile list /format:list

REM メモリキャッシュのクリア（空きメモリを作る）
REM Sysinternalsツール RAMMap.exe が必要
rammap -Et  REM スタンバイリストをクリア
```

### スタートアップ最適化
```cmd
REM スタートアップ項目を表示
wmic startup get Caption,Command,Location

REM 自動起動するサービスを表示
wmic service where StartMode="Auto" get Name,State,Status

REM タスクスケジューラのタスク一覧
schtasks /query /fo LIST /v

REM 起動時間を遅らせるサービスの設定（管理者権限必要）
sc config "サービス名" start= delayed-auto
```

### ディスクパフォーマンス
```cmd
REM ディスクI/O統計
diskperf -y  REM ディスクパフォーマンスカウンタを有効化

REM ディスク速度テスト（PowerShell使用）
powershell "$file = 'testfile.tmp'; $data = New-Object byte[] 100MB; [System.Random]::new().NextBytes($data); Measure-Command { [IO.File]::WriteAllBytes($file, $data) }; Remove-Item $file"

REM ファイルシステムの統計
fsutil fsinfo statistics C:

REM ボリュームの空き容量チェック
fsutil volume diskfree C:
```

### プロセス優先度の変更
```cmd
REM プロセスの優先度を変更
wmic process where name="app.exe" call setpriority "above normal"
REM 優先度: idle, below normal, normal, above normal, high priority, realtime

REM startコマンドで優先度を指定して起動
start /LOW notepad.exe
start /HIGH app.exe
start /REALTIME critical_app.exe
REM /LOW, /NORMAL, /HIGH, /REALTIME, /ABOVENORMAL, /BELOWNORMAL
```

---

## システムメンテナンス

### Windows Update
```cmd
REM Windows Update の状態確認（PowerShell使用）
powershell "Get-WindowsUpdate"

REM 更新プログラムのインストール
powershell "Install-WindowsUpdate -AcceptAll -AutoReboot"

REM 更新履歴を表示
powershell "Get-WindowsUpdateLog"

REM Windows Update サービスの管理
net stop wuauserv
net start wuauserv
sc query wuauserv
```

### システムの復元
```cmd
REM 復元ポイントの作成（管理者権限必要）
wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "手動復元ポイント", 100, 7

REM 復元ポイント一覧
powershell "Get-ComputerRestorePoint"

REM システムの復元を実行
rstrui.exe
```

### 一時ファイルのクリーンアップ
```cmd
REM 一時ファイルを削除
del /F /S /Q %TEMP%\*
del /F /S /Q C:\Windows\Temp\*

REM ブラウザキャッシュの削除
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8  REM 一時ファイル
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 2  REM Cookie
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 1  REM 履歴

REM Windows Updateのクリーンアップ
DISM /Online /Cleanup-Image /StartComponentCleanup
DISM /Online /Cleanup-Image /SPSuperseded
```

### レジストリのバックアップと復元
```cmd
REM レジストリをバックアップ
reg export HKLM\Software backup.reg
reg export HKCU backup_user.reg

REM レジストリ全体をバックアップ
reg export HKLM backup_hklm.reg
reg export HKCU backup_hkcu.reg

REM レジストリを復元
reg import backup.reg

REM 特定のキーを削除
reg delete HKCU\Software\TestKey /f
```

### ドライバーの管理
```cmd
REM インストール済みドライバー一覧
driverquery
pnputil /enum-drivers

REM ドライバーの詳細情報
driverquery /V /FO LIST

REM サードパーティドライバーのバックアップ
dism /online /export-driver /destination:C:\drivers_backup

REM ドライバーのインストール
pnputil /add-driver C:\driver\driver.inf /install

REM ドライバーの削除
pnputil /delete-driver oem0.inf /uninstall /force
```

### ディスクエラーチェックの自動化
```cmd
@echo off
REM 定期的なディスクチェックスクリプト

echo ディスクチェックを開始します...

REM Cドライブのチェック
echo Cドライブをチェック中...
chkdsk C: /F /R /X

if %ERRORLEVEL% EQU 0 (
    echo Cドライブ: 正常
) else (
    echo Cドライブ: エラーが見つかりました
)

REM 他のドライブも同様にチェック
for %%d in (D E F) do (
    if exist %%d:\ (
        echo %%d: ドライブをチェック中...
        chkdsk %%d: /F
    )
)

echo ディスクチェック完了
pause
```

### システム情報の定期レポート
```cmd
@echo off
setlocal EnableDelayedExpansion

REM タイムスタンプ
set TIMESTAMP=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

set REPORT=system_report_%TIMESTAMP%.txt

echo システムレポート > %REPORT%
echo 作成日時: %DATE% %TIME% >> %REPORT%
echo. >> %REPORT%

echo ========== システム情報 ========== >> %REPORT%
systeminfo >> %REPORT%
echo. >> %REPORT%

echo ========== ディスク情報 ========== >> %REPORT%
wmic logicaldisk get name,size,freespace,filesystem >> %REPORT%
echo. >> %REPORT%

echo ========== メモリ情報 ========== >> %REPORT%
wmic memorychip get Capacity,Speed,Manufacturer >> %REPORT%
echo. >> %REPORT%

echo ========== CPU情報 ========== >> %REPORT%
wmic cpu get Name,NumberOfCores,MaxClockSpeed >> %REPORT%
echo. >> %REPORT%

echo ========== 実行中のプロセス（トップ10） ========== >> %REPORT%
tasklist | sort /R /+65 | more +1 | findstr /V "^$" | more +1 >> %REPORT%
echo. >> %REPORT%

echo ========== ネットワーク設定 ========== >> %REPORT%
ipconfig /all >> %REPORT%
echo. >> %REPORT%

echo ========== サービス状態 ========== >> %REPORT%
net start >> %REPORT%

echo レポートを作成しました: %REPORT%
pause
```

---

## コマンドプロンプト vs PowerShell

CMDは古典的なWindowsシェルで、シンプルな操作に適しています。  
より高度な操作や自動化には、PowerShellの使用をお勧めします。

**CMDが適している場合:**
- 簡単なファイル操作
- 従来のバッチファイルの実行
- レガシーシステムとの互換性が必要な場合

**PowerShellが適している場合:**
- オブジェクト指向のデータ処理
- システム管理タスク
- モダンなスクリプティング
- .NETライブラリの利用

---

## 参考リンク

- [Windows コマンドリファレンス](https://docs.microsoft.com/ja-jp/windows-server/administration/windows-commands/windows-commands)
- [バッチファイルの基礎](https://docs.microsoft.com/ja-jp/windows-server/administration/windows-commands/batch-file-basics)
- [コマンドラインリファレンス A-Z](https://ss64.com/nt/)
