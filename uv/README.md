使うコマンド：

初回のみ
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv init --app uv_sample1

uv init --lib uv_sample3

cd uv_sample1

uv venv

.venv\Scripts\activate

(uv_sampleN) PS C:\Users\XXX\ となっていたら正解

uv add pandas


uv syncでlib共有



