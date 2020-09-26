import os


def hello(num):
    print("hello!", num)

hello(19390)

# path<パス>とは、ファイルへのアドレスのようなもの(文字列)
# 例: /Users/aina/ダウンロード/画像1.jpg
def return_files_of_directory(path):
    answer = []
    for fname in os.listdir(path):
        answer.append(path + "/" + fname)
    return answer

# . は現在のディレクトリ
# print(return_files_of_directory("1st year"))



# fnames = os.listdir(".") # 現在のディレクトリのファイル一覧をリストで返す
# for fname in fnames:

#     if os.path.isdir(fname) == True:
#         print(fname, "is directory!")
#     else:
#         print(fname, "is file")