import pdfplumber
import os

def extract_text_from_pdf_pdfplumber(pdf_path, output_txt_path=None):
    """
    pdfplumber を使用してPDFからテキストを抽出し、ファイルに出力または文字列として返す。

    Args:
        pdf_path (str): 読み込むPDFファイルのパス。
        output_txt_path (str, optional): 抽出したテキストを保存するファイルのパス。
                                         Noneの場合、テキストは文字列として返される。

    Returns:
        str or None: output_txt_pathがNoneの場合は抽出されたテキスト、
                     それ以外の場合はNone。エラーが発生した場合はNone。
    """
    if not os.path.exists(pdf_path):
        print(f"エラー: PDFファイルが見つかりません - {pdf_path}")
        return None

    all_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                print(f"ページ {page_num + 1} を処理中...")
                text = page.extract_text()
                if text:
                    all_text += f"\n--- ページ {page_num + 1} ---\n"
                    all_text += text
                else:
                    all_text += f"\n--- ページ {page_num + 1} (テキストなしまたは抽出不可) ---\n"
        
        if output_txt_path:
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(all_text)
            print(f"テキストを '{output_txt_path}' に保存しました。")
            return None
        else:
            print("テキスト抽出が完了しました。")
            return all_text

    except Exception as e:
        print(f"PDFのテキスト抽出中にエラーが発生しました: {e}")
        return None

# # --- 使用例 ---
# if __name__ == "__main__":
#     # テスト用のPDFファイルパス (ご自身の環境に合わせて変更してください)
#     # 例: カレントディレクトリに 'sample.pdf' がある場合
#     pdf_file = 'sample.pdf' 
#     output_text_file = 'extracted_text_pdfplumber.txt'

#     # 1. テキストをファイルに保存する例
#     print("\n--- pdfplumber でテキストをファイルに保存 ---")
#     extract_text_from_pdf_pdfplumber(pdf_file, output_text_file)

#     # 2. テキストを文字列として取得する例
#     print("\n--- pdfplumber でテキストを文字列として取得 ---")
#     extracted_string = extract_text_from_pdf_pdfplumber(pdf_file)
#     if extracted_string:
#         # 取得したテキストの一部を表示
#         print("\n--- 抽出されたテキストの一部 ---")
#         print(extracted_string[:500]) # 最初の500文字を表示
#         print("...")

#     # 存在しないPDFファイルを指定した場合の例
#     print("\n--- 存在しないPDFファイルを指定した場合 ---")
#     extract_text_from_pdf_pdfplumber('non_existent.pdf', 'output.txt')