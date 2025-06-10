import os
from  chatgpt import openai_answer
from openai import OpenAI
import os
from commons.common import Common
from dotenv import load_dotenv
from utils.csv2df import csv_to_dataframe

load_dotenv()
common = Common()
config  = common.load_config()
model = config['openai']['model']
maxtokens = int(config['openai']['maxtokens'])
temperature = float(config['openai']['temperature'])

def main():

    df = ""
    csv_path = common.csv_dir_path()
    full_path = os.path.join(csv_path, "Nikkei225-15min-2007-2020.csv")
    df = csv_to_dataframe(full_path)
    print(df)

    txt = ""

    system_prompt = common.load_systemprompt("trader")
    openai_answer(system_prompt,str(df),txt)

if __name__ == "__main__":
    
    main()
