# Windows PowerShell コマンド集

PowerShellでよく使うコマンドの学習用リファレンスです。

## 目次
- [基本コマンド](#基本コマンド)
- [ファイル・ディレクトリ操作](#ファイルディレクトリ操作)
- [テキスト処理](#テキスト処理)
- [プロセス管理](#プロセス管理)
- [ネットワーク](#ネットワーク)
- [システム情報](#システム情報)
- [パイプとフィルタ](#パイプとフィルタ)
- [変数と環境変数](#変数と環境変数)
- [スクリプト実行](#スクリプト実行)
- [高度なPowerShell技術](#高度なpowershell技術)
- [セキュリティとアクセス制御](#セキュリティとアクセス制御)
- [デバッグとトラブルシューティング](#デバッグとトラブルシューティング)
- [パフォーマンス最適化](#パフォーマンス最適化)
- [システム管理](#システム管理)
- [.NET統合](#net統合)
- [モジュール管理](#モジュール管理)

---

## 基本コマンド

### ヘルプの表示
```powershell
# コマンドのヘルプを表示
Get-Help <コマンド名>
Get-Help Get-Process -Full
Get-Help Get-Process -Examples

# 利用可能なコマンド一覧
Get-Command

# 特定のパターンでコマンドを検索
Get-Command *process*
```

### 画面クリア
```powershell
Clear-Host  # または cls
```

### 現在のディレクトリ
```powershell
Get-Location  # または pwd, gl
```

---

## ファイル・ディレクトリ操作

### ディレクトリ内容の表示
```powershell
# 基本的なリスト表示
Get-ChildItem  # または ls, dir, gci

# 詳細情報付きで表示
Get-ChildItem | Format-List

# 隠しファイルも含めて表示
Get-ChildItem -Force

# 再帰的に表示（サブディレクトリも含む）
Get-ChildItem -Recurse

# 特定の拡張子のみ表示
Get-ChildItem *.py
Get-ChildItem -Filter "*.txt"
Get-ChildItem -Include *.py, *.md -Recurse
```

### ディレクトリ移動
```powershell
Set-Location <パス>  # または cd, sl
Set-Location ..  # 親ディレクトリへ
Set-Location ~  # ホームディレクトリへ
Set-Location -  # 前のディレクトリへ戻る

# ディレクトリスタック操作
Push-Location <パス>  # 現在位置を保存して移動
Pop-Location  # 保存した位置に戻る
```

### ファイル作成・コピー・移動・削除
```powershell
# 新規ファイル作成
New-Item -ItemType File -Name "test.txt"
New-Item -ItemType File -Path "c:\temp\test.txt" -Value "初期内容"

# 新規ディレクトリ作成
New-Item -ItemType Directory -Name "newfolder"
mkdir newfolder  # エイリアス

# ファイルコピー
Copy-Item source.txt destination.txt
Copy-Item file.txt -Destination c:\backup\
Copy-Item -Path "*.txt" -Destination "c:\backup\" -Recurse

# ファイル移動
Move-Item source.txt destination.txt
Move-Item file.txt c:\temp\

# ファイル削除
Remove-Item file.txt
Remove-Item *.log
Remove-Item folder -Recurse  # ディレクトリを中身ごと削除
Remove-Item file.txt -Force  # 強制削除

# ファイル名変更
Rename-Item oldname.txt newname.txt
```

### ファイル内容の表示・編集
```powershell
# ファイル内容を表示
Get-Content file.txt  # または cat, gc, type

# 先頭N行を表示
Get-Content file.txt -Head 10

# 末尾N行を表示
Get-Content file.txt -Tail 10

# リアルタイムでファイルを監視（ログファイルなど）
Get-Content file.txt -Wait

# ファイルに書き込み（上書き）
"テキスト" | Out-File file.txt
Set-Content -Path file.txt -Value "テキスト"

# ファイルに追記
"追加テキスト" | Add-Content file.txt
Add-Content -Path file.txt -Value "追加行"
```

### ファイル検索
```powershell
# 名前でファイルを検索
Get-ChildItem -Path C:\ -Filter "*.txt" -Recurse -ErrorAction SilentlyContinue

# 特定サイズ以上のファイルを検索
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 1MB }
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 100MB -and $_.Length -lt 1GB }

# 最近更新されたファイルを検索
Get-ChildItem -Recurse | Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-7) }

# 古いファイルを検索
Get-ChildItem -Recurse | Where-Object { $_.LastWriteTime -lt (Get-Date).AddYears(-1) }

# 特定の日付範囲で検索
$startDate = Get-Date "2026-01-01"
$endDate = Get-Date "2026-12-31"
Get-ChildItem -Recurse | Where-Object { $_.CreationTime -ge $startDate -and $_.CreationTime -le $endDate }

# 隠しファイルのみ検索
Get-ChildItem -Path C:\ -Recurse -Force -Attributes Hidden -ErrorAction SilentlyContinue

# 空のファイルを検索
Get-ChildItem -Recurse -File | Where-Object { $_.Length -eq 0 }

# 空のディレクトリを検索
Get-ChildItem -Recurse -Directory | Where-Object { (Get-ChildItem $_.FullName).Count -eq 0 }

# 重複ファイルを検索（ハッシュ値で比較）
Get-ChildItem -Recurse -File | Get-FileHash | Group-Object -Property Hash | Where-Object { $_.Count -gt 1 } | ForEach-Object { $_.Group | Select-Object Path, Hash }
```

### ファイルの詳細情報
```powershell
# ファイルの完全な情報
Get-Item file.txt | Select-Object *

# ファイルのタイムスタンプ
$file = Get-Item file.txt
$file.CreationTime
$file.LastWriteTime
$file.LastAccessTime

# ファイルの属性
Get-ItemProperty file.txt | Select-Object Attributes
(Get-Item file.txt).Attributes

# ファイルのハッシュ値
Get-FileHash file.txt -Algorithm SHA256
Get-FileHash file.txt -Algorithm MD5
Get-FileHash file.txt -Algorithm SHA1
Get-FileHash file.txt -Algorithm SHA512

# ファイルの所有者情報
Get-Acl file.txt | Select-Object Owner
(Get-Acl file.txt).Owner

# ファイルのアクセス権限
Get-Acl file.txt | Select-Object -ExpandProperty Access

# ファイルのバージョン情報（実行ファイル）
(Get-Item app.exe).VersionInfo
[System.Diagnostics.FileVersionInfo]::GetVersionInfo("app.exe")

# ファイルの拡張属性
Get-Item file.txt -Stream *
```

### ファイルのバックアップと復元
```powershell
# タイムスタンプ付きバックアップ
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
Copy-Item file.txt "file_$timestamp.bak"

# ディレクトリのバックアップ
Copy-Item C:\source C:\backup -Recurse -Force

# 変更されたファイルのみバックアップ
$source = "C:\source"
$backup = "C:\backup"
Get-ChildItem $source -Recurse | Where-Object { 
    -not (Test-Path ($_.FullName -replace [regex]::Escape($source), $backup)) -or
    $_.LastWriteTime -gt (Get-Item ($_.FullName -replace [regex]::Escape($source), $backup)).LastWriteTime
} | ForEach-Object {
    $dest = $_.FullName -replace [regex]::Escape($source), $backup
    $null = New-Item -ItemType File -Path $dest -Force
    Copy-Item $_.FullName $dest -Force
}

# ZIP形式でバックアップ
Compress-Archive -Path C:\source\* -DestinationPath "backup_$(Get-Date -Format 'yyyyMMdd').zip"

# 世代管理バックアップ（30日以上古いバックアップを削除）
Get-ChildItem C:\backups -Filter "backup_*.zip" | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item

# 差分バックアップ（変更されたファイルのみ）
$lastBackup = Get-Date "2026-05-01"
Get-ChildItem C:\source -Recurse | Where-Object { $_.LastWriteTime -gt $lastBackup } | Copy-Item -Destination C:\incremental_backup
```

### ファイルの比較
```powershell
# ファイル内容の比較
Compare-Object (Get-Content file1.txt) (Get-Content file2.txt)

# 詳細な差分表示
$diff = Compare-Object (Get-Content file1.txt) (Get-Content file2.txt) -IncludeEqual
$diff | Where-Object { $_.SideIndicator -ne "==" }

# ハッシュ値で比較
$hash1 = Get-FileHash file1.txt
$hash2 = Get-FileHash file2.txt
if ($hash1.Hash -eq $hash2.Hash) {
    Write-Host "ファイルは同じです"
} else {
    Write-Host "ファイルは異なります"
}

# ディレクトリの比較
Compare-Object (Get-ChildItem C:\dir1) (Get-ChildItem C:\dir2) -Property Name, Length

# ファイルサイズの比較
$file1Size = (Get-Item file1.txt).Length
$file2Size = (Get-Item file2.txt).Length
Write-Host "Size difference: $($file1Size - $file2Size) bytes"
```

### ファイルの分割と結合
```powershell
# テキストファイルをN行ずつ分割
$content = Get-Content file.txt
$chunkSize = 1000
for ($i = 0; $i -lt $content.Length; $i += $chunkSize) {
    $end = [Math]::Min($i + $chunkSize - 1, $content.Length - 1)
    $content[$i..$end] | Out-File "part_$([Math]::Floor($i/$chunkSize)).txt"
}

# バイナリファイルを分割
$file = "large.bin"
$chunkSize = 10MB
$reader = [System.IO.File]::OpenRead($file)
$buffer = New-Object byte[] $chunkSize
$count = 0
while (($bytesRead = $reader.Read($buffer, 0, $buffer.Length)) -gt 0) {
    [System.IO.File]::WriteAllBytes("${file}_part${count}", $buffer[0..($bytesRead-1)])
    $count++
}
$reader.Close()

# ファイルの結合
Get-Content file1.txt, file2.txt, file3.txt | Set-Content merged.txt

# バイナリファイルの結合
$output = [System.IO.File]::Create("combined.bin")
Get-ChildItem "part_*.bin" | Sort-Object Name | ForEach-Object {
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    $output.Write($bytes, 0, $bytes.Length)
}
$output.Close()
```

### ファイルのタイムスタンプ操作
```powershell
# タイムスタンプを現在時刻に更新
(Get-Item file.txt).LastWriteTime = Get-Date

# 特定の日付に設定
(Get-Item file.txt).LastWriteTime = Get-Date "2026-01-01 12:00:00"
(Get-Item file.txt).CreationTime = Get-Date "2026-01-01 10:00:00"
(Get-Item file.txt).LastAccessTime = Get-Date "2026-01-01 14:00:00"

# 複数ファイルのタイムスタンプを一括更新
Get-ChildItem *.txt | ForEach-Object { $_.LastWriteTime = Get-Date }

# 別のファイルのタイムスタンプをコピー
$source = Get-Item source.txt
$target = Get-Item target.txt
$target.CreationTime = $source.CreationTime
$target.LastWriteTime = $source.LastWriteTime
$target.LastAccessTime = $source.LastAccessTime

# ファイル名から日付を抽出してタイムスタンプを設定
Get-ChildItem "photo_*.jpg" | ForEach-Object {
    if ($_.Name -match "(\d{4})(\d{2})(\d{2})") {
        $date = Get-Date "$($matches[1])-$($matches[2])-$($matches[3])"
        $_.CreationTime = $date
        $_.LastWriteTime = $date
    }
}
```

### シンボリックリンクとジャンクション
```powershell
# シンボリックリンク作成（管理者権限必要）
New-Item -ItemType SymbolicLink -Path "C:\link.txt" -Target "C:\original\file.txt"
New-Item -ItemType SymbolicLink -Path "C:\link_dir" -Target "C:\original\directory"

# ハードリンク作成
New-Item -ItemType HardLink -Path "C:\hardlink.txt" -Target "C:\original\file.txt"

# ジャンクション作成
New-Item -ItemType Junction -Path "C:\junction" -Target "C:\original\directory"

# リンクの確認
Get-Item C:\link.txt | Select-Object LinkType, Target
(Get-Item C:\link.txt).LinkType
(Get-Item C:\link.txt).Target

# すべてのシンボリックリンクを検索
Get-ChildItem -Recurse -Force | Where-Object { $_.LinkType -ne $null }

# リンク削除（リンク先は削除されない）
Remove-Item C:\link.txt
Remove-Item C:\link_dir
```

---

## テキスト処理

### パターンマッチング・検索
```powershell
# ファイル内でテキスト検索（grep相当）
Select-String -Path "*.txt" -Pattern "検索文字列"
Select-String -Path file.txt -Pattern "error" -CaseSensitive

# 正規表現で検索
Select-String -Path "*.log" -Pattern "\d{3}-\d{4}" -AllMatches

# 再帰的に検索
Get-ChildItem -Recurse -Include *.txt | Select-String -Pattern "TODO"
```

### テキスト変換
```powershell
# 文字列の置換
(Get-Content file.txt) -replace "old", "new" | Set-Content file.txt

# 複数の置換を一度に実行
$content = Get-Content file.txt
$content = $content -replace "old1", "new1" -replace "old2", "new2"
$content | Set-Content file.txt

# 大文字・小文字変換
"hello".ToUpper()  # HELLO
"WORLD".ToLower()  # world
(Get-Culture).TextInfo.ToTitleCase("hello world")  # Hello World

# 文字列の分割
"apple,banana,orange" -split ","
"apple banana orange" -split " "
"data1:data2:data3" -split ":"

# 文字列の結合
$array = @("apple", "banana", "orange")
$array -join ", "
$array -join "`n"  # 改行で結合

# トリム（空白削除）
" hello ".Trim()
" hello".TrimStart()
"hello ".TrimEnd()

# 文字列の長さ
"hello".Length

# 部分文字列の抽出
"hello world".Substring(0, 5)  # "hello"
"hello world".Substring(6)  # "world"

# 文字列の検索
"hello world".Contains("world")  # True
"hello world".IndexOf("world")  # 6
"hello world".StartsWith("hello")  # True
"hello world".EndsWith("world")  # True

# パディング
"42".PadLeft(5, '0')  # "00042"
"test".PadRight(10, '-')  # "test------"
```

### 正規表現
```powershell
# 基本的なマッチング
"hello123" -match "\d+"  # True
$matches[0]  # "123"

# 複数のマッチを抽出
$text = "Phone: 123-456-7890, Email: test@example.com"
[regex]::Matches($text, "\d{3}-\d{3}-\d{4}") | ForEach-Object { $_.Value }
[regex]::Matches($text, "\b[\w.-]+@[\w.-]+\.\w+\b") | ForEach-Object { $_.Value }

# キャプチャグループ
if ("2026-05-05" -match "(\d{4})-(\d{2})-(\d{2})") {
    Write-Host "Year: $($matches[1])"
    Write-Host "Month: $($matches[2])"
    Write-Host "Day: $($matches[3])"
}

# 名前付きキャプチャ
if ("John Doe" -match "(?<first>\w+) (?<last>\w+)") {
    Write-Host "First: $($matches['first'])"
    Write-Host "Last: $($matches['last'])"
}

# 正規表現で置換
"test123abc456" -replace "\d+", "[NUM]"
"hello world" -replace "\b(\w)\w+\b", '$1'  # 先頭文字のみ
```

### CSV/JSON/XML処理
```powershell
# CSVの読み込みと処理
$data = Import-Csv data.csv
$data | Where-Object { $_.Age -gt 30 }
$data | Select-Object Name, Age | Sort-Object Age -Descending

# CSVに出力
$data | Export-Csv output.csv -NoTypeInformation -Encoding UTF8

# CSVの特定列を抽出
$data | Select-Object Name, Email | Export-Csv filtered.csv -NoTypeInformation

# JSONの読み込み
$json = Get-Content data.json -Raw | ConvertFrom-Json
$json.users | Where-Object { $_.active -eq $true }

# JSONに変換
$data | ConvertTo-Json | Out-File output.json
$data | ConvertTo-Json -Depth 10 | Out-File output.json  # ネスト深いデータ

# XMLの読み込み
[xml]$xml = Get-Content data.xml
$xml.root.item | Where-Object { $_.status -eq "active" }

# XMLに変換
$data | Export-Clixml output.xml
$imported = Import-Clixml output.xml

# HTMLテーブルを生成
$data | ConvertTo-Html -Property Name, Age, Email | Out-File report.html

# カスタムHTMLレポート
$html = @"
<html>
<head><title>Report</title></head>
<body>
<h1>System Report</h1>
$(Get-Process | Select-Object -First 10 | ConvertTo-Html -Fragment)
</body>
</html>
"@
$html | Out-File report.html
```

### ログファイル解析
```powershell
# エラー行の抽出
Get-Content app.log | Select-String -Pattern "ERROR|FATAL"

# 特定の時間範囲でフィルタリング
Get-Content app.log | Where-Object { $_ -match "2026-05-05 (0[9]|1[0-5]):" }

# IPアドレスを抽出
$ips = Get-Content access.log | Select-String -Pattern "\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" -AllMatches | 
    ForEach-Object { $_.Matches.Value } | Sort-Object -Unique

# ログの統計
$errors = (Get-Content app.log | Select-String -Pattern "ERROR").Count
$warnings = (Get-Content app.log | Select-String -Pattern "WARNING").Count
Write-Host "Errors: $errors, Warnings: $warnings"

# エラータイプ別のカウント
Get-Content app.log | Select-String -Pattern "ERROR" | 
    ForEach-Object { ($_ -split "ERROR:")[1].Trim() } | 
    Group-Object | Sort-Object Count -Descending

# ログファイルのローテーション
$logFile = "app.log"
$maxSize = 10MB
if ((Get-Item $logFile).Length -gt $maxSize) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    Move-Item $logFile "${logFile}_$timestamp"
    New-Item $logFile -ItemType File
}

# 複数のログファイルを統合解析
Get-ChildItem *.log | ForEach-Object {
    $errorCount = (Get-Content $_.FullName | Select-String -Pattern "ERROR").Count
    [PSCustomObject]@{
        File = $_.Name
        ErrorCount = $errorCount
    }
} | Sort-Object ErrorCount -Descending
```

---

## プロセス管理

### プロセス一覧・情報取得
```powershell
# 実行中のプロセス一覧
Get-Process  # または ps, gps

# 特定プロセスの情報
Get-Process -Name "chrome"
Get-Process -Id 1234

# メモリ使用量でソート
Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 10

# CPU使用量でソート
Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 10
```

### プロセスの起動・停止
```powershell
# プロセス起動
Start-Process notepad.exe
Start-Process "https://www.google.com"  # デフォルトブラウザで開く
Start-Process python -ArgumentList "script.py"

# プロセス停止
Stop-Process -Name "notepad"
Stop-Process -Id 1234
Stop-Process -Name "chrome" -Force  # 強制終了
```

---

## ネットワーク

### 接続テスト
```powershell
# Ping
Test-Connection google.com
Test-Connection 8.8.8.8 -Count 4

# ポート接続テスト
Test-NetConnection google.com -Port 443
Test-NetConnection localhost -Port 8080
```

### ネットワーク情報
```powershell
# IPアドレス確認
Get-NetIPAddress
Get-NetIPConfiguration

# ネットワークアダプタ情報
Get-NetAdapter

# ルーティングテーブル
Get-NetRoute

# DNS情報
Resolve-DnsName google.com
nslookup google.com
```

### Web操作
```powershell
# Webページを取得
Invoke-WebRequest -Uri "https://example.com"

# ファイルダウンロード
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"

# REST API呼び出し
Invoke-RestMethod -Uri "https://api.example.com/data" -Method Get

# POSTリクエスト
Invoke-RestMethod -Uri "https://api.example.com/data" -Method Post -Body @{key="value"}
```

---

## システム情報

### システム情報取得
```powershell
# コンピュータ名
$env:COMPUTERNAME
hostname

# OSバージョン
Get-ComputerInfo | Select-Object WindowsVersion, OsArchitecture
[System.Environment]::OSVersion

# システム稼働時間
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime

# ディスク使用状況
Get-PSDrive
Get-Volume

# メモリ情報
Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity, Speed
```

### サービス管理
```powershell
# サービス一覧
Get-Service

# 実行中のサービスのみ表示
Get-Service | Where-Object {$_.Status -eq "Running"}

# 特定のサービス情報
Get-Service -Name "wuauserv"

# サービス開始・停止（管理者権限が必要）
Start-Service -Name "サービス名"
Stop-Service -Name "サービス名"
Restart-Service -Name "サービス名"
```

---

## パイプとフィルタ

### パイプライン基本
```powershell
# 結果を次のコマンドに渡す
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

# Where-Object でフィルタリング
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-ChildItem | Where-Object {$_.Length -gt 1MB}

# ForEach-Object で各要素を処理
Get-ChildItem *.txt | ForEach-Object { $_.Name }
1..10 | ForEach-Object { $_ * 2 }

# Select-Object でプロパティ選択
Get-Process | Select-Object Name, CPU, WorkingSet

# Measure-Object で統計
Get-ChildItem | Measure-Object -Property Length -Sum -Average -Maximum
```

### 出力の整形
```powershell
# テーブル形式
Get-Process | Format-Table Name, CPU, WorkingSet

# リスト形式
Get-Process | Format-List

# ワイド形式（複数列）
Get-Process | Format-Wide Name -Column 4

# グリッド表示（GUIウィンドウ）
Get-Process | Out-GridView
```

### 出力先の指定
```powershell
# ファイルに出力
Get-Process | Out-File processes.txt

# CSVに出力
Get-Process | Export-Csv processes.csv -NoTypeInformation

# JSONに出力
Get-Process | ConvertTo-Json | Out-File processes.json

# HTMLに出力
Get-Process | ConvertTo-Html | Out-File processes.html

# クリップボードにコピー
Get-Process | Out-String | Set-Clipboard
```

---

## 変数と環境変数

### 変数の使い方
```powershell
# 変数への代入
$name = "太郎"
$number = 42
$array = @(1, 2, 3, 4, 5)
$hash = @{
    Name = "太郎"
    Age = 30
}

# 変数の使用
Write-Output "こんにちは、$name さん"
$number + 10

# 配列操作
$array[0]  # 最初の要素
$array[-1]  # 最後の要素
$array.Count  # 要素数

# ハッシュテーブル操作
$hash["Name"]
$hash.Age
```

### 環境変数
```powershell
# 環境変数の表示
Get-ChildItem Env:
$env:PATH

# 環境変数の設定（現在のセッションのみ）
$env:MY_VAR = "value"

# プロセススコープで環境変数設定
[System.Environment]::SetEnvironmentVariable("MY_VAR", "value", "Process")

# ユーザースコープで環境変数設定（永続的）
[System.Environment]::SetEnvironmentVariable("MY_VAR", "value", "User")

# システムスコープで環境変数設定（管理者権限必要）
[System.Environment]::SetEnvironmentVariable("MY_VAR", "value", "Machine")
```

### 特殊変数
```powershell
$_  # パイプラインの現在のオブジェクト
$?  # 最後のコマンドの成功/失敗（True/False）
$LASTEXITCODE  # 最後の終了コード
$PWD  # 現在のディレクトリ
$HOME  # ホームディレクトリ
$PSVersionTable  # PowerShellバージョン情報
```

---

## スクリプト実行

### 実行ポリシー
```powershell
# 現在の実行ポリシーを確認
Get-ExecutionPolicy

# 実行ポリシーの変更（管理者権限必要）
Set-ExecutionPolicy RemoteSigned
Set-ExecutionPolicy Unrestricted

# 現在のプロセスのみ一時的に変更
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

### スクリプトの実行
```powershell
# スクリプトファイルを実行
.\script.ps1

# パラメータ付きで実行
.\script.ps1 -Param1 "value" -Param2 42

# バイパスして実行（一時的に実行ポリシーを無視）
powershell -ExecutionPolicy Bypass -File .\script.ps1

# コマンドを文字列で実行
powershell -Command "Get-Process | Sort-Object CPU -Descending | Select-Object -First 5"
```

### 基本的なスクリプト構文
```powershell
# コメント
# これは単一行コメント

<#
これは
複数行コメント
#>

# 条件分岐
if ($condition) {
    # 処理
} elseif ($condition2) {
    # 処理
} else {
    # 処理
}

# ループ
foreach ($item in $collection) {
    # 処理
}

for ($i = 0; $i -lt 10; $i++) {
    # 処理
}

while ($condition) {
    # 処理
}

# 関数定義
function Get-Greeting {
    param(
        [string]$Name
    )
    return "こんにちは、$Name さん"
}

# 関数呼び出し
Get-Greeting -Name "太郎"
```

---

## よく使う便利なワンライナー

### ファイル操作
```powershell
# 特定の拡張子ファイルを一括削除
Get-ChildItem -Filter "*.tmp" -Recurse | Remove-Item

# ファイル名の一括変更
Get-ChildItem *.txt | Rename-Item -NewName { $_.Name -replace '.txt','.md' }

# ディレクトリサイズを計算
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum

# 重複ファイルを検出（ハッシュ値で比較）
Get-ChildItem -Recurse | Get-FileHash | Group-Object -Property Hash | Where-Object { $_.Count -gt 1 }
```

### システム管理
```powershell
# CPU使用率上位プロセスを監視
while($true) { 
    Clear-Host
    Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | Format-Table
    Start-Sleep -Seconds 2
}

# 最近インストールされたソフトウェア
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | Sort-Object InstallDate -Descending | Select-Object DisplayName, InstallDate -First 10

# ポートをリッスンしているプロセスを確認
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"} | Select-Object LocalAddress, LocalPort, OwningProcess
```

### データ処理
```powershell
# CSVファイルを読み込んで処理
Import-Csv data.csv | Where-Object {$_.Age -gt 30} | Select-Object Name, Age

# 複数のテキストファイルを結合
Get-Content file1.txt, file2.txt, file3.txt | Set-Content merged.txt

# ログファイルからエラー行を抽出
Get-Content app.log | Select-String -Pattern "ERROR" | Out-File errors.txt
```

---

## 高度なPowerShell技術

### 高度な関数とスクリプト
```powershell
# パラメータ付き関数
function Get-SystemReport {
    param(
        [Parameter(Mandatory=$true)]
        [string]$OutputPath,
        
        [ValidateSet("Full", "Summary")]
        [string]$ReportType = "Summary",
        
        [switch]$IncludeProcesses
    )
    
    $report = @()
    $report += "System Report - $(Get-Date)"
    $report += "Computer: $env:COMPUTERNAME"
    
    if ($ReportType -eq "Full" -or $IncludeProcesses) {
        $report += "`nTop Processes:"
        $report += Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 | Out-String
    }
    
    $report | Out-File $OutputPath
}

# パイプライン入力を受け付ける関数
function Get-FileSize {
    param(
        [Parameter(ValueFromPipeline=$true)]
        [System.IO.FileInfo]$File
    )
    
    process {
        [PSCustomObject]@{
            Name = $File.Name
            SizeKB = [Math]::Round($File.Length / 1KB, 2)
            SizeMB = [Math]::Round($File.Length / 1MB, 2)
        }
    }
}

Get-ChildItem *.txt | Get-FileSize

# 複数の戻り値
function Get-DiskInfo {
    [CmdletBinding()]
    param([string]$DriveLetter = "C")
    
    $drive = Get-PSDrive $DriveLetter
    [PSCustomObject]@{
        Drive = $DriveLetter
        UsedGB = [Math]::Round($drive.Used / 1GB, 2)
        FreeGB = [Math]::Round($drive.Free / 1GB, 2)
        TotalGB = [Math]::Round(($drive.Used + $drive.Free) / 1GB, 2)
        PercentFree = [Math]::Round(($drive.Free / ($drive.Used + $drive.Free)) * 100, 2)
    }
}

# エラーハンドリング
function Invoke-SafeCommand {
    param([scriptblock]$Command)
    
    try {
        & $Command
        Write-Host "Success" -ForegroundColor Green
    }
    catch {
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "Line: $($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Yellow
    }
    finally {
        Write-Host "Cleanup completed"
    }
}
```

### オブジェクト操作
```powershell
# カスタムオブジェクトの作成
$person = [PSCustomObject]@{
    Name = "太郎"
    Age = 30
    Email = "taro@example.com"
}

# プロパティの追加
$person | Add-Member -MemberType NoteProperty -Name "Phone" -Value "090-1234-5678"

# メソッドの追加
$person | Add-Member -MemberType ScriptMethod -Name "GetAge" -Value {
    return $this.Age
}

# 複数のオブジェクトを作成
$people = @(
    [PSCustomObject]@{Name="太郎"; Age=30},
    [PSCustomObject]@{Name="花子"; Age=25},
    [PSCustomObject]@{Name="一郎"; Age=35}
)

# オブジェクトのフィルタリングとソート
$people | Where-Object { $_.Age -gt 25 } | Sort-Object Age

# オブジェクトのグループ化
$people | Group-Object { $_.Age -gt 30 } | ForEach-Object {
    Write-Host "Group: $($_.Name)"
    $_.Group
}

# 計算プロパティ
Get-Process | Select-Object Name, 
    @{Name="MemoryMB"; Expression={[Math]::Round($_.WorkingSet/1MB, 2)}},
    @{Name="CPUTime"; Expression={$_.CPU}}
```

### 並列処理
```powershell
# ForEach-Object -Parallel (PowerShell 7+)
1..10 | ForEach-Object -Parallel {
    Start-Sleep -Seconds 1
    "Task $_ completed"
} -ThrottleLimit 5

# 複数ファイルを並列処理
Get-ChildItem *.txt | ForEach-Object -Parallel {
    $hash = Get-FileHash $_.FullName
    [PSCustomObject]@{
        File = $_.Name
        Hash = $hash.Hash
    }
} -ThrottleLimit 10

# ジョブを使用した非同期処理
$job1 = Start-Job -ScriptBlock { Get-Process | Measure-Object }
$job2 = Start-Job -ScriptBlock { Get-Service | Measure-Object }

Wait-Job $job1, $job2
$result1 = Receive-Job $job1
$result2 = Receive-Job $job2

Remove-Job $job1, $job2

# ジョブの進捗監視
$jobs = 1..5 | ForEach-Object {
    Start-Job -ScriptBlock { 
        param($i)
        Start-Sleep -Seconds (Get-Random -Minimum 1 -Maximum 5)
        "Job $i completed"
    } -ArgumentList $_
}

while (Get-Job -State Running) {
    $completed = (Get-Job -State Completed).Count
    $total = $jobs.Count
    Write-Progress -Activity "Processing" -Status "$completed of $total completed" -PercentComplete (($completed / $total) * 100)
    Start-Sleep -Milliseconds 500
}
```

### モジュールの作成
```powershell
# スクリプトモジュール (.psm1)
# MyModule.psm1

function Get-Greeting {
    param([string]$Name)
    return "こんにちは、$Name さん"
}

function Get-Farewell {
    param([string]$Name)
    return "さようなら、$Name さん"
}

Export-ModuleMember -Function Get-Greeting, Get-Farewell

# モジュールの使用
Import-Module .\MyModule.psm1
Get-Greeting -Name "太郎"

# モジュールマニフェスト (.psd1)
New-ModuleManifest -Path MyModule.psd1 `
    -Author "Your Name" `
    -Description "My Custom Module" `
    -ModuleVersion "1.0.0" `
    -RootModule "MyModule.psm1"
```

### イベント処理
```powershell
# ファイルシステム監視
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "C:\folder"
$watcher.Filter = "*.txt"
$watcher.EnableRaisingEvents = $true

$action = {
    $path = $Event.SourceEventArgs.FullPath
    $changeType = $Event.SourceEventArgs.ChangeType
    Write-Host "File $changeType: $path" -ForegroundColor Green
}

Register-ObjectEvent $watcher "Created" -Action $action
Register-ObjectEvent $watcher "Changed" -Action $action
Register-ObjectEvent $watcher "Deleted" -Action $action

# イベントを待機
Wait-Event

# イベントの登録解除
Unregister-Event -SourceIdentifier *
$watcher.Dispose()
```

---

## セキュリティとアクセス制御

### ファイル・フォルダ権限
```powershell
# ACL（アクセス制御リスト）の取得
$acl = Get-Acl file.txt
$acl.Access

# 所有者の表示
$acl.Owner

# 権限の追加
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "ユーザー名",
    "FullControl",
    "Allow"
)
$acl.SetAccessRule($rule)
Set-Acl file.txt $acl

# 読み取り専用権限を追加
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "ユーザー名",
    "Read",
    "Allow"
)
$acl.AddAccessRule($rule)
Set-Acl file.txt $acl

# 特定ユーザーの権限を削除
$acl.Access | Where-Object { $_.IdentityReference -eq "ユーザー名" } | ForEach-Object {
    $acl.RemoveAccessRule($_)
}
Set-Acl file.txt $acl

# ディレクトリとサブディレクトリに権限を適用
Get-ChildItem C:\folder -Recurse | ForEach-Object {
    $acl = Get-Acl $_.FullName
    $acl.SetAccessRule($rule)
    Set-Acl $_.FullName $acl
}

# 所有者の変更
$acl = Get-Acl file.txt
$acl.SetOwner([System.Security.Principal.NTAccount]"DOMAIN\Username")
Set-Acl file.txt $acl
```

### 認証情報の管理
```powershell
# セキュアな文字列の作成
$secureString = ConvertTo-SecureString -String "MyPassword" -AsPlainText -Force

# 認証情報オブジェクトの作成
$credential = New-Object System.Management.Automation.PSCredential("username", $secureString)

# ユーザーに認証情報を入力させる
$credential = Get-Credential -Message "ログイン情報を入力してください"

# 認証情報をファイルに保存（暗号化）
$credential | Export-Clixml -Path credential.xml

# 認証情報を読み込む
$credential = Import-Clixml -Path credential.xml

# パスワードを平文に戻す（注意）
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($credential.Password)
$password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
```

### スクリプト署名
```powershell
# 自己署名証明書の作成
$cert = New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=MyCodeSigning" `
    -CertStoreLocation Cert:\CurrentUser\My

# スクリプトに署名
Set-AuthenticodeSignature -FilePath .\script.ps1 -Certificate $cert

# 署名の検証
Get-AuthenticodeSignature .\script.ps1

# 証明書のエクスポート
Export-Certificate -Cert $cert -FilePath mycert.cer
```

---

## デバッグとトラブルシューティング

### デバッグ技術
```powershell
# デバッグメッセージ
Write-Debug "This is a debug message"
$DebugPreference = "Continue"  # デバッグメッセージを表示

# 詳細メッセージ
Write-Verbose "This is a verbose message"
$VerbosePreference = "Continue"

# 警告メッセージ
Write-Warning "This is a warning"

# エラーメッセージ
Write-Error "This is an error"

# 実行トレース
Set-PSDebug -Trace 1  # 各コマンドを表示
Set-PSDebug -Trace 2  # 変数の値も表示
Set-PSDebug -Off      # トレースを無効化

# ブレークポイント
Set-PSBreakpoint -Script .\script.ps1 -Line 10
Set-PSBreakpoint -Script .\script.ps1 -Variable myVar
Set-PSBreakpoint -Command Get-Process

# ブレークポイントの一覧と削除
Get-PSBreakpoint
Remove-PSBreakpoint -Id 1

# スタックトレース
Get-PSCallStack

# エラー情報の詳細
try {
    # 何かの操作
}
catch {
    Write-Host "Error: $($_.Exception.Message)"
    Write-Host "Script: $($_.InvocationInfo.ScriptName)"
    Write-Host "Line: $($_.InvocationInfo.ScriptLineNumber)"
    Write-Host "Column: $($_.InvocationInfo.OffsetInLine)"
    $_.ScriptStackTrace
}
```

### パフォーマンス計測
```powershell
# 実行時間の計測
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
# 処理
$stopwatch.Stop()
Write-Host "Elapsed: $($stopwatch.Elapsed.TotalSeconds) seconds"

# Measure-Commandで計測
$time = Measure-Command {
    Get-ChildItem C:\ -Recurse -ErrorAction SilentlyContinue
}
Write-Host "Time: $($time.TotalSeconds) seconds"

# 複数のアプローチを比較
$method1Time = Measure-Command {
    1..1000 | ForEach-Object { $_ * 2 }
}

$method2Time = Measure-Command {
    for ($i = 1; $i -le 1000; $i++) { $i * 2 }
}

Write-Host "Method 1: $($method1Time.TotalMilliseconds)ms"
Write-Host "Method 2: $($method2Time.TotalMilliseconds)ms"
```

### ログ出力
```powershell
# ログファイルへの書き込み
function Write-Log {
    param(
        [string]$Message,
        [ValidateSet("INFO", "WARNING", "ERROR")]
        [string]$Level = "INFO"
    )
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] [$Level] $Message"
    Add-Content -Path "app.log" -Value $logMessage
    
    switch ($Level) {
        "INFO" { Write-Host $logMessage -ForegroundColor Green }
        "WARNING" { Write-Host $logMessage -ForegroundColor Yellow }
        "ERROR" { Write-Host $logMessage -ForegroundColor Red }
    }
}

# 使用例
Write-Log "スクリプト開始" -Level "INFO"
Write-Log "警告が発生しました" -Level "WARNING"
Write-Log "エラーが発生しました" -Level "ERROR"
```

---

## パフォーマンス最適化

PowerShellでは、LinuxやDOSコマンドとの互換性のため、多くのエイリアスが設定されています。

```powershell
# エイリアス一覧を表示
Get-Alias

# 特定のエイリアスを確認
Get-Alias ls
Get-Alias cd

# よく使うエイリアス
ls, dir → Get-ChildItem
cd → Set-Location
pwd → Get-Location
cat, type → Get-Content
cp, copy → Copy-Item
mv, move → Move-Item
rm, del → Remove-Item
mkdir, md → New-Item -ItemType Directory
cls, clear → Clear-Host
ps → Get-Process
kill → Stop-Process
```

---

## Tips

### コマンドの履歴
```powershell
# コマンド履歴を表示
Get-History
h

# 特定のコマンドを再実行
Invoke-History <ID>

# 履歴をファイルに保存
Get-History | Export-Csv history.csv

# 履歴をクリア
Clear-History
```

### Tab補完
- **Tab**: コマンド名、パラメータ名、ファイル名の補完
- **Ctrl+Space**: すべての候補を表示

### ショートカットキー
- **Ctrl+C**: コマンド中断
- **Ctrl+L**: 画面クリア（Clear-Host）
- **F7**: コマンド履歴を表示（GUI）
- **↑/↓**: コマンド履歴を移動
- **Ctrl+R**: コマンド履歴をインクリメンタルサーチ

### パフォーマンス計測とプロファイリング
```powershell
# メモリ使用量の監視
$process = Get-Process -Id $PID
Write-Host "Memory: $([Math]::Round($process.WorkingSet/1MB, 2))MB"

# システムパフォーマンスカウンタ
Get-Counter '\Processor(_Total)\% Processor Time'
Get-Counter '\Memory\Available MBytes'
Get-Counter '\PhysicalDisk(_Total)\Disk Reads/sec'

# 継続的な監視
Get-Counter '\Processor(_Total)\% Processor Time' -Continuous -SampleInterval 1

# 複数のカウンタを同時に監視
$counters = @(
    '\Processor(_Total)\% Processor Time',
    '\Memory\Available MBytes',
    '\PhysicalDisk(_Total)\Disk Reads/sec'
)
Get-Counter -Counter $counters -SampleInterval 2 -MaxSamples 10

# パフォーマンスデータをCSVに出力
Get-Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 60 | 
    Export-Counter -Path performance.csv
```

---

## システム管理

### Windows Update管理
```powershell
# Windows Updateモジュールのインストール
Install-Module PSWindowsUpdate -Force

# 利用可能な更新プログラムを確認
Get-WindowsUpdate

# 更新プログラムのインストール
Install-WindowsUpdate -AcceptAll -AutoReboot

# 更新履歴を表示
Get-WindowsUpdateLog

# 特定のKBをインストール
Get-WindowsUpdate -KBArticleID "KB5000001" | Install-WindowsUpdate
```

### レジストリ操作
```powershell
# レジストリの読み取り
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion"

# 特定の値を取得
(Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion").ProgramFilesDir

# レジストリ値の設定
Set-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Version" -Value "1.0"

# レジストリキーの作成
New-Item -Path "HKCU:\Software\MyApp"

# レジストリ値の作成
New-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Setting" -Value "Enabled" -PropertyType String

# レジストリキーの削除
Remove-Item -Path "HKCU:\Software\MyApp" -Recurse

# レジストリのバックアップ
$key = Get-Item "HKCU:\Software\MyApp"
$key | Export-Clixml "registry_backup.xml"

# レジストリの復元
$key = Import-Clixml "registry_backup.xml"
```

### スケジュールタスク
```powershell
# タスク一覧
Get-ScheduledTask

# 実行中のタスク
Get-ScheduledTask | Where-Object {$_.State -eq "Running"}

# タスクの作成
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\script.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
$settings = New-ScheduledTaskSettingsSet
Register-ScheduledTask -TaskName "MyTask" -Action $action -Trigger $trigger -Settings $settings

# タスクの実行
Start-ScheduledTask -TaskName "MyTask"

# タスクの停止
Stop-ScheduledTask -TaskName "MyTask"

# タスクの削除
Unregister-ScheduledTask -TaskName "MyTask" -Confirm:$false

# タスクの詳細情報
Get-ScheduledTaskInfo -TaskName "MyTask"
```

### イベントログ管理
```powershell
# イベントログ一覧
Get-EventLog -List

# システムログの最新10件
Get-EventLog -LogName System -Newest 10

# エラーのみ表示
Get-EventLog -LogName System -EntryType Error -Newest 20

# 特定の期間のイベント
$startDate = (Get-Date).AddDays(-7)
Get-EventLog -LogName System -After $startDate

# 特定のソースからのイベント
Get-EventLog -LogName Application -Source "Application Error"

# イベントログをエクスポート
Get-EventLog -LogName System -Newest 100 | Export-Csv system_events.csv -NoTypeInformation

# イベントログのクリア（管理者権限必要）
Clear-EventLog -LogName System

# Windows PowerShell 7+ の新しいコマンドレット
Get-WinEvent -LogName System -MaxEvents 10
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2}  # エラーのみ
```

### システムメンテナンス
```powershell
# 一時ファイルのクリーンアップ
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

# ディスククリーンアップ
Start-Process cleanmgr -ArgumentList "/sagerun:1"

# システムファイルチェック（管理者権限必要）
sfc /scannow

# DISM修復（管理者権限必要）  
Repair-WindowsImage -Online -RestoreHealth

# 復元ポイントの作成
Checkpoint-Computer -Description "Manual Restore Point" -RestorePointType "MODIFY_SETTINGS"

# 復元ポイント一覧
Get-ComputerRestorePoint

# システムの復元
Restore-Computer -RestorePoint 1
```

---

## .NET統合

### .NETクラスの使用
```powershell
# DateTime操作
$now = [DateTime]::Now
$today = [DateTime]::Today
$tomorrow = $now.AddDays(1)
$formatted = $now.ToString("yyyy-MM-dd HH:mm:ss")

# Math関数
[Math]::Round(3.14159, 2)  # 3.14
[Math]::Ceiling(3.14)  # 4
[Math]::Floor(3.99)  # 3
[Math]::Sqrt(16)  # 4
[Math]::Pow(2, 10)  # 1024

# 乱数生成
$random = New-Object System.Random
$random.Next(1, 100)  # 1-100の乱数

# GUID生成
[Guid]::NewGuid().ToString()

# 正規表現
$regex = [regex]::new("\d+")
$regex.IsMatch("abc123")  # True
$regex.Match("abc123").Value  # "123"

# ファイルI/O
[System.IO.File]::ReadAllText("file.txt")
[System.IO.File]::WriteAllText("file.txt", "content")
[System.IO.File]::AppendAllText("file.txt", "more content")

# ディレクトリ操作
[System.IO.Directory]::GetFiles("C:\folder", "*.txt")
[System.IO.Directory]::CreateDirectory("C:\newfolder")

# パス操作
[System.IO.Path]::Combine("C:\folder", "file.txt")
[System.IO.Path]::GetFileName("C:\folder\file.txt")  # "file.txt"
[System.IO.Path]::GetDirectoryName("C:\folder\file.txt")  # "C:\folder"
[System.IO.Path]::GetExtension("file.txt")  # ".txt"

# Web操作
$client = New-Object System.Net.WebClient
$client.DownloadFile("https://example.com/file.zip", "file.zip")
$content = $client.DownloadString("https://example.com")

# HTTPリクエスト
$request = [System.Net.WebRequest]::Create("https://api.example.com/data")
$request.Method = "GET"
$response = $request.GetResponse()
$stream = $response.GetResponseStream()
$reader = New-Object System.IO.StreamReader($stream)
$data = $reader.ReadToEnd()
```

### Windows Forms（GUI）
```powershell
Add-Type -AssemblyName System.Windows.Forms

# 簡単なメッセージボックス
[System.Windows.Forms.MessageBox]::Show("Hello World!")
[System.Windows.Forms.MessageBox]::Show("Continue?", "Confirm", "YesNo", "Question")

# ファイル選択ダイアログ
$openFileDialog = New-Object System.Windows.Forms.OpenFileDialog
$openFileDialog.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
if ($openFileDialog.ShowDialog() -eq "OK") {
    $selectedFile = $openFileDialog.FileName
    Write-Host "Selected: $selectedFile"
}

# フォルダ選択ダイアログ
$folderBrowserDialog = New-Object System.Windows.Forms.FolderBrowserDialog
if ($folderBrowserDialog.ShowDialog() -eq "OK") {
    $selectedFolder = $folderBrowserDialog.SelectedPath
    Write-Host "Selected: $selectedFolder"
}

# 簡単なフォーム
$form = New-Object System.Windows.Forms.Form
$form.Text = "My Application"
$form.Size = New-Object System.Drawing.Size(300, 200)

$button = New-Object System.Windows.Forms.Button
$button.Text = "Click Me"
$button.Location = New-Object System.Drawing.Point(100, 70)
$button.Add_Click({
    [System.Windows.Forms.MessageBox]::Show("Button Clicked!")
})

$form.Controls.Add($button)
$form.ShowDialog()
```

---

## モジュール管理

### モジュールの検索とインストール
```powershell
# インストール済みモジュール一覧
Get-Module -ListAvailable

# 現在読み込まれているモジュール
Get-Module

# モジュールの検索（PowerShell Gallery）
Find-Module -Name "*Azure*"

# モジュールのインストール
Install-Module -Name PSWindowsUpdate -Scope CurrentUser
Install-Module -Name ImportExcel -Force

# モジュールの読み込み
Import-Module PSWindowsUpdate

# モジュールの削除
Uninstall-Module -Name ModuleName

# モジュールの更新
Update-Module -Name PSWindowsUpdate

# モジュールのバージョン確認
Get-InstalledModule -Name PSWindowsUpdate

# 信頼されたリポジトリの設定
Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
```

### カスタムモジュールの作成
```powershell
# モジュールディレクトリの作成
$modulePath = "$HOME\Documents\PowerShell\Modules\MyModule"
New-Item -Path $modulePath -ItemType Directory -Force

# .psm1ファイルの作成
$moduleFile = @"
function Get-CustomGreeting {
    param([string]`$Name)
    return "こんにちは、`$Name さん"
}

function Get-SystemStatus {
    `$cpu = Get-Counter '\Processor(_Total)\% Processor Time' | Select-Object -ExpandProperty CounterSamples | Select-Object -ExpandProperty CookedValue
    `$memory = Get-Counter '\Memory\Available MBytes' | Select-Object -ExpandProperty CounterSamples | Select-Object -ExpandProperty CookedValue
    
    [PSCustomObject]@{
        CPUUsage = [Math]::Round(`$cpu, 2)
        AvailableMemoryMB = [Math]::Round(`$memory, 2)
        Timestamp = Get-Date
    }
}

Export-ModuleMember -Function Get-CustomGreeting, Get-SystemStatus
"@

$moduleFile | Out-File -FilePath "$modulePath\MyModule.psm1"

# マニフェストの作成
New-ModuleManifest -Path "$modulePath\MyModule.psd1" `
    -RootModule "MyModule.psm1" `
    -ModuleVersion "1.0.0" `
    -Author "Your Name" `
    -Description "My custom PowerShell module" `
    -FunctionsToExport @("Get-CustomGreeting", "Get-SystemStatus")

# モジュールのインポートとテスト
Import-Module MyModule
Get-CustomGreeting -Name "太郎"
Get-SystemStatus
```

---

## 高度なテクニックとベストプラクティス

### エラーハンドリングのベストプラクティス
```powershell
# Try-Catch-Finally
try {
    # リスク のある操作
    $content = Get-Content "nonexistent.txt" -ErrorAction Stop
}
catch [System.IO.FileNotFoundException] {
    Write-Warning "ファイルが見つかりません"
}
catch {
    Write-Error "予期しないエラー: $_"
    $_.Exception.GetType().FullName
}
finally {
    Write-Host "クリーンアップ処理"
}

# カスタムエラーのスロー
function Divide-Numbers {
    param([int]$a, [int]$b)
    
    if ($b -eq 0) {
        throw [System.DivideByZeroException]::new("ゼロで除算できません")
    }
    return $a / $b
}

# エラーアクション設定
Get-ChildItem C:\NonExistent -ErrorAction SilentlyContinue
Get-ChildItem C:\NonExistent -ErrorAction Stop
Get-ChildItem C:\NonExistent -ErrorVariable myError -ErrorAction SilentlyContinue
```

### パイプラインの最適化
```powershell
# 遅い方法（オブジェクトを毎回処理）
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 1MB} | ForEach-Object {$_.Name}

# 速い方法（フィルタを先に適用）
Get-ChildItem -Recurse -File | Where-Object Length -GT 1MB | Select-Object -ExpandProperty Name

# さらに速い方法（.NETメソッドを使用）
[System.IO.Directory]::GetFiles("C:\folder", "*", "AllDirectories") | 
    Where-Object {(Get-Item $_).Length -gt 1MB}
```

### セキュアなスクリプティング
```powershell
# パラメータ検証
function Set-UserAge {
    param(
        [Parameter(Mandatory=$true)]
        [ValidateRange(0, 150)]
        [int]$Age,
        
        [ValidateSet("Male", "Female", "Other")]
        [string]$Gender,
        
        [ValidatePattern("^[\w\.-]+@[\w\.-]+\.\w+$")]
        [string]$Email
    )
    
    Write-Host "Age: $Age, Gender: $Gender, Email: $Email"
}

# 入力のサニタイズ
function Invoke-SafeCommand {
    param([string]$Input)
    
    # 危険な文字を削除
    $sanitized = $Input -replace '[;&|<>]', ''
    
    # コマンドの実行
    Invoke-Expression $sanitized
}
```

### プログレスバーの実装
```powershell
# 基本的なプログレスバー
$items = 1..100
$i = 0
foreach ($item in $items) {
    $i++
    $percentComplete = ($i / $items.Count) * 100
    Write-Progress -Activity "Processing" -Status "$i of $($items.Count)" -PercentComplete $percentComplete
    Start-Sleep -Milliseconds 50
}

# 入れ子のプログレスバー
$files = Get-ChildItem -Path C:\folder -File
$fileCount = 0
foreach ($file in $files) {
    $fileCount++
    Write-Progress -Activity "Processing Files" -Status $file.Name -PercentComplete (($fileCount / $files.Count) * 100) -Id 1
    
    $lines = Get-Content $file.FullName
    $lineCount = 0
    foreach ($line in $lines) {
        $lineCount++
        Write-Progress -Activity "Processing Lines" -Status "Line $lineCount" -PercentComplete (($lineCount / $lines.Count) * 100) -ParentId 1 -Id 2
        # 処理
    }
}
```

---

## 参考リンク

- [PowerShell 公式ドキュメント](https://docs.microsoft.com/ja-jp/powershell/)
- [PowerShell Gallery](https://www.powershellgallery.com/)
- [about Topics](https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about)
- [PowerShell GitHub](https://github.com/PowerShell/PowerShell)
- [PowerShell Community](https://devblogs.microsoft.com/powershell/)
