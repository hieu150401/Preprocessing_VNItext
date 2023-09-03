import regex as re
import utils
from pyvi import ViTokenizer
import os
EMAIL = re.compile(r"([\w0-9_\.-]+)(@)([\d\w\.-]+)(\.)([\w\.]{2,6})")
URL = re.compile(r"https?:\/\/(?!.*:\/\/)\S+")
PHONE = re.compile(r"(09|01[2|6|8|9])+([0-9]{8})\b")
MENTION = re.compile(r"@.+?:")
NUMBER = re.compile(r"\d+.?\d*")
DATETIME = '\d{1,2}\s?[/-]\s?\d{1,2}\s?[/-]\s?\d{4}'

RE_HTML_TAG = re.compile(r'<[^>]+>')
RE_CLEAR_1 = re.compile("[^_<>\s\p{Latin}]")
RE_CLEAR_2 = re.compile("__+")
RE_CLEAR_3 = re.compile("\s+")


folder_path = r'F:\Preprocessing_VNItext\Dataset\noidung'
output_folder_path = r'F:\Preprocessing_VNItext\Dataset\outputdataset' 

class TextPreprocess():
    @staticmethod
    def replace_common_token(txt):
        txt = re.sub(EMAIL, ' ', txt)
        txt = re.sub(URL, ' ', txt)
        txt = re.sub(MENTION, ' ', txt)
        txt = re.sub(DATETIME, ' ', txt)
        txt = re.sub(NUMBER, ' ', txt)
        return txt

    @staticmethod
    def remove_emoji(txt):
        txt = re.sub(':v', '', txt)
        txt = re.sub(':D', '', txt)
        txt = re.sub(':3', '', txt)
        txt = re.sub(':\(', '', txt)
        txt = re.sub(':\)', '', txt)
        return txt

    @staticmethod
    def remove_html_tag(txt):
        return re.sub(RE_HTML_TAG, ' ', txt)
            
    def word_tokenize():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        result = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(folder_path, filename)
                output_file_path = os.path.join(output_folder_path, f"result_{filename}")
                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    text = input_file.read()
                    tokens = ViTokenizer.tokenize(text)
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(tokens)
            
        result.append(tokens)
        return result
    
    
    def preprocess(self):
        # if not os.path.exists(folder_path):
        #     os.makedirs(folder_path)

        result = []
        for filename in os.listdir(output_folder_path):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(output_folder_path, filename)
                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    text = input_file.read()
                    tokens = ViTokenizer.tokenize(text)
                    tokens = self.remove_html_tag(tokens)
                    tokens = self.remove_html_tag(tokens)
                    tokens = re.sub('&.{3,4};', ' ', tokens)
                    tokens = utils.convertwindown1525toutf8(tokens)
                    tokens = tokens.lower()
                    tokens = self.replace_common_token(tokens)
                    tokens = self.remove_emoji(tokens)
                    tokens = re.sub(RE_CLEAR_1, ' ', tokens)
                    tokens = re.sub(RE_CLEAR_2, ' ', tokens)
                    tokens = re.sub(RE_CLEAR_3, ' ', tokens)
                    tokens = utils.chuan_hoa_dau_cau_tieng_viet(tokens)
                with open(input_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(tokens)
        # txt = self.remove_html_tag(txt)
        # txt = re.sub('&.{3,4};', ' ', txt)
        # txt = utils.convertwindown1525toutf8(txt)
        # if tokenize:
        #     txt = ViTokenizer.tokenize(txt)
        # txt = txt.lower()
        # txt = self.replace_common_token(txt)
        # txt = self.remove_emoji(txt)
        # txt = re.sub(RE_CLEAR_1, ' ', txt)
        # txt = re.sub(RE_CLEAR_2, ' ', txt)
        # txt = re.sub(RE_CLEAR_3, ' ', txt)
        # txt = utils.chuan_hoa_dau_cau_tieng_viet(txt)
        return result
