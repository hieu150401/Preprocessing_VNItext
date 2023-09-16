# from sklearn.feature_extraction.text import TfidfVectorizer
# import os

# def load_data(output_folder_path):
#     result = []
#     for filename in os.listdir(output_folder_path):
#             if filename.endswith('.txt'):
#                 input_file_path = os.path.join(output_folder_path, filename)
#                 with open(input_file_path, 'r', encoding='utf-8') as input_file:
#                     text = input_file.read()
#                     result = get_stopwords(text,threshold=300)
               
#     return result


# def get_stopwords(documents, threshold=300):
#     """
#     :param documents: list of documents
#     :param threshold:
#     :return: list of words has idf <= threshold
#     """
#     tfidf = TfidfVectorizer(min_df=100)
#     tfidf_matrix = tfidf.fit_transform(documents)
#     features = tfidf.get_feature_names()
#     stopwords = []
#     print(min(tfidf.idf_), max(tfidf.idf_), len(features))
#     for index, feature in enumerate(features):
#         if tfidf.idf_[index] <= threshold:
#             stopwords.append(feature)
#     return stopwords


# if __name__ == '__main__':
#     stopwords = load_data(r"D:\Users\Admin\Desktop\corpus-full.pre")
#     with open('F:\Preprocessing_VNItext-1\Preprocessing\stopwords.txt', 'w', encoding='utf8') as fp:
#         for word in stopwords:
#             fp.write(word + '\n')