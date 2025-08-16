from openai import OpenAI
import os
from commons.common import Common
from dotenv import load_dotenv

load_dotenv()
common = Common()
config  = common.load_config()
model = config['openai']['model']
maxtokens = int(config['openai']['maxtokens'])
temperature = float(config['openai']['temperature'])

def openai_answer(system_prompt , df = None,  txt = None):
    try:
        prompt = system_prompt["content"]
        print(prompt)
        open_ai_key = os.environ.get('OPENAI_API_KEY')
        client = OpenAI(api_key=open_ai_key)

        data = ""
        if df is not None:
            temp_str = f' reference1 : {df} ,'
            data += temp_str
        if txt is not None:
            temp_str = f' reference2: {txt} ,'
            data += temp_str

        try:
            response = client.chat.completions.create(
                model=model, # ここで使用したいモデルを指定してください
                messages=[
                    {"role": "system", "content": str(prompt)},
                    {"role": "assistant", "content": data}
                ],
                max_tokens= maxtokens,
                temperature= temperature
            )
        except Exception as e:
            print("Error occurred:", str(e))

        usage = response.usage
        print(f"--- OpenAI API 応答 (モデル: {model}) ---")
        print(f"プロンプトトークン (入力): {usage.prompt_tokens} tokens")
        print(f"完了トークン (出力): {usage.completion_tokens} tokens")
        print(f"合計トークン: {usage.total_tokens} tokens")
        print(f"----------------------------------------")

        # 応答からテキストコンテンツを抽出
        # 応答を処理するコード
        if response.choices and response.choices[0].message and response.choices[0].message.content:
            print("AIからの応答:", response.choices[0].message.content.strip())
        else:
            print("エラー: OpenAIからの応答にコンテンツが含まれていませんでした。")
            return None
        
    except Exception as e:
        return f"エラーが発生しました: {e}"
