import fitz # PyMuPDFのインポート名
import os

def extract_text_from_pdf_pymupdf(pdf_path, output_txt_path=None):
    """
    PyMuPDF (fitz) を使用してPDFからテキストを抽出し、ファイルに出力または文字列として返す。

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
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            print(f"ページ {page_num + 1} を処理中...")
            text = page.get_text() # テキストを抽出
            if text:
                all_text += f"\n--- ページ {page_num + 1} ---\n"
                all_text += text
            else:
                all_text += f"\n--- ページ {page_num + 1} (テキストなしまたは抽出不可) ---\n"
        
        doc.close() # ドキュメントを閉じる

        if output_txt_path:
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(all_text)
            print(f"テキストを '{output_txt_path}' に保存しました。")
            return all_text
        
        else:
            print("テキスト抽出が完了しました。")
            return all_text

    except Exception as e:
        print(f"PDFのテキスト抽出中にエラーが発生しました: {e}")
        return None

# # --- 使用例 ---
# if __name__ == "__main__":
#     pdf_file = 'sample.pdf' 
#     output_text_file = 'extracted_text_pymupdf.txt'

#     print("\n--- PyMuPDF でテキストをファイルに保存 ---")
#     extract_text_from_pdf_pymupdf(pdf_file, output_text_file)

#     print("\n--- PyMuPDF でテキストを文字列として取得 ---")
#     extracted_string = extract_text_from_pdf_pymupdf(pdf_file)
#     if extracted_string:
#         print("\n--- 抽出されたテキストの一部 ---")
#         print(extracted_string[:500])
#         print("...")