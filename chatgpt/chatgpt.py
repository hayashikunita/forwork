import openai
from dotenv import load_dotenv
import os




# OpenAI API キーを設定
# .env ファイルを読み込む
# load_dotenv()

# model = config['openai']['model']
# maxtokens = config['Database']['maxtokens']
# temperature = config['Database']['temperature']


def openai_answer(system_prompt):
    try:
        open_ai_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = open_ai_key
        # ChatGPT API にリクエストを送信
        response = openai.ChatCompletion.create(
            model=model,  
            messages=[
                {"role": "system", "content": "あなたは親切なアシスタントです。"},
                {"role": "user", "content": system_prompt}
            ],
            max_tokens=maxtokens,
            temperature=temperature
        )

        usage = response.usage
        print(f"--- OpenAI API 応答 (モデル: {model}) ---")
        print(f"プロンプトトークン (入力): {usage.prompt_tokens} tokens")
        print(f"完了トークン (出力): {usage.completion_tokens} tokens")
        print(f"合計トークン: {usage.total_tokens} tokens")
        print(f"----------------------------------------")

        # レスポンスを取得
        return response['choices'][0]['message']['content']
    

    except Exception as e:
        return f"エラーが発生しました: {e}"

