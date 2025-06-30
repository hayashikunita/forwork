import os
import configparser
import tomllib

# dirname
# path
# getFile

class Common:

    def __init__(self):
        pass

    @classmethod
    def chatgpt_dir_path(cls):   
        current_script_path = os.path.abspath(__file__)
        # -> /chatgpt/commons/my_script.py

        # 2. スクリプトがあるディレクトリを取得 (1つ上の階層)
        current_dir = os.path.dirname(current_script_path)
        # -> /chatgpt/commons

        # 3. さらにその親ディレクトリを取得 (2つ上の階層)
        parent_dir = os.path.dirname(current_dir)
        return parent_dir

    @classmethod
    def commons_dir_path(cls):
        current_script_path = os.path.abspath(__file__)
        # 2. スクリプトがあるディレクトリを取得 (1つ上の階層)
        current_dir_path = os.path.dirname(current_script_path)
        # -> /chatgpt/commons
        return current_dir_path

    @classmethod
    def data_dir_path(cls):

        chatgpt_dir_path = cls.chatgpt_dir_path()
        data_dir_path = os.path.join(chatgpt_dir_path, 'data')
        # -> /chatgpt/commons
        return data_dir_path
    
    @classmethod
    def csv_dir_path(cls):

        data_dir_path = cls.data_dir_path()
        csv_dir_path = os.path.join(data_dir_path,'csv')
        # -> /chatgpt/commons
        return csv_dir_path
    
    @classmethod
    def pdf_dir_path(cls):

        data_dir_path = cls.data_dir_path()
        pdf_dir_path = os.path.join(data_dir_path,'pdf')
        # -> /chatgpt/commons
        return pdf_dir_path

    @classmethod
    def excel_dir_path(cls):

        data_dir_path = cls.data_dir_path()
        excel_dir_path = os.path.join(data_dir_path,'excel')
        # -> /chatgpt/commons
        return excel_dir_path
    
    @classmethod
    def xbrl_dir_path(cls):

        data_dir_path = cls.data_dir_path()
        xbrl_dir_path = os.path.join(data_dir_path,'xbrl')
        # -> /chatgpt/commons
        return xbrl_dir_path
    
    @classmethod
    def utils_dir_path(cls):

        chatgpt_dir_path = cls.chatgpt_dir_path()
        utils_dir_path = os.path.join(chatgpt_dir_path, 'utils')
        # -> /chatgpt/commons
        return utils_dir_path
    
    @classmethod
    def prompts_dir_path(cls):

        chatgpt_dir_path = cls.chatgpt_dir_path()
        prompts_dir_path = os.path.join(chatgpt_dir_path, 'prompts')
        # -> /chatgpt/commons
        return prompts_dir_path
    
    # -----------------file取得-----------------
    @classmethod
    def load_config(cls):

        current_script_path = os.path.abspath(__file__)
        # -> /chatgpt/commons/my_script.py

        # 2. スクリプトがあるディレクトリを取得 (1つ上の階層)
        current_dir = os.path.dirname(current_script_path)
        # -> /chatgpt/commons

        # 3. さらにその親ディレクトリを取得 (2つ上の階層)
        parent_dir = os.path.dirname(current_dir)
        # -> /chatgpt
        
        # 4. 2つ上の階層にある目的のファイルへのパスを生成
        # ここでは /project/data/target.txt を目指します
        file_path = os.path.join(parent_dir, 'setting.ini')
        # -> /chatgpt/setting.ini

        config = configparser.ConfigParser()
        config.read(file_path)
        return  config


    @classmethod
    def load_systemprompt(cls, name:str):

        toml_name = f'{name}.toml'        
        # 3. さらにその親ディレクトリを取得 (2つ上の階層)
        target_dir = cls.prompts_dir_path()
        # -> /chatgpt        
        # ここでは /project/data/target.txt を目指します
        file_path = os.path.join(target_dir, toml_name)
        # -> /chatgpt/setting.ini
        with open(file_path, "rb") as f:    
            system_prompt_toml = tomllib.load(f)
            system_prompt = system_prompt_toml["prompt"]
            return system_prompt

