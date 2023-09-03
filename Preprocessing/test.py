import torch
from transformers import AutoModel, AutoTokenizer
import os
from pyvi import ViTokenizer
import re
import utils
import data_prep

#
# def word_tokenize():
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     for filename in os.listdir(folder_path):
#         if filename.endswith('.txt'):
#             input_file_path = os.path.join(folder_path, filename)
#             output_file_path = os.path.join(output_folder_path, f"result_{filename}")
#             with open(input_file_path, 'r', encoding='utf-8') as input_file:
#                 text = input_file.read()
#                 tokens = ViTokenizer.tokenize(text)

#             with open(output_file_path, 'w', encoding='utf-8') as output_file:
#                 output_file.write(tokens)
                
folder_path = r'F:\Preprocessing_VNItext\Dataset\noidung'
output_folder_path = r'F:\Preprocessing_VNItext\Dataset\outputdataset'             
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
        result = []
        for filename in os.listdir(output_folder_path):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(output_folder_path, filename)
                with open(output_folder_path, 'r', encoding='utf-8') as input_file:
                    tokens = input_file.read()
                    tokens = self.remove_html_tag(tokens)
                    tokens = self.remove_html_tag(tokens)
                    tokens = re.sub('&.{3,4};', ' ', tokens)
                    tokens = utils.convertwindown1525toutf8(tokens)
                    tokens = tokens.lower()
                    tokens = self.replace_common_token(tokens)
                    tokens = self.remove_emoji(tokens)
                    tokens = re.sub(data_prep.RE_CLEAR_1, ' ', tokens)
                    tokens = re.sub(data_prep.RE_CLEAR_2, ' ', tokens)
                    tokens = re.sub(data_prep.RE_CLEAR_3, ' ', tokens)
                    tokens = utils.chuan_hoa_dau_cau_tieng_viet(tokens)
                with open(output_folder_path, 'w', encoding='utf-8') as output_file:
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
txt = word_tokenize()
print(txt)
                
# if __name__ == '__main__':
#     txt = word_tokenize()
#     print("deo hieu sao loi")

    # print(is_valid_vietnam_word(txt))
    