import json
import os
import codecs
codecs.register_error('none', lambda e: ('???', e.end))


#ファイル名の一括取得
file_list=os.listdir(path='file_list')
#辞書（という名の配列）一覧を作成する
with open('word_data.txt', 'r', encoding='UTF-8', errors='none') as f:
     word_list = f.readlines()
word_box = []
#
for word in word_list:   
    word = str(word.replace( '\n' , '' ));#改行を消す
    word = str(word.replace( '\r\n' , '' ));#改行を消す
    word = str(word.replace( '　' , '' ));#スペースを消す
    word_box.append(word);

    
#ファイルリストの確認
'''
for data in file_list:
    print(data);
'''
#ファイルリストの中身から文字列検索
roop_num=1;
for data in file_list:
    #if roop_num > 5:
    #   break;
    print('-------------------------')
    print(str(roop_num)+":"+str(data))
    print('-------------------------')
    #ファイルを読込jsonデータを見る
    #json_open = open('file_list/'+data, 'r', encoding='UTF-8', errors='none')
    #json_load = json.load(json_open)
    #１行ずつ展開
    with open('file_list/'+data, 'r', encoding='UTF-8', errors='none') as f:
         text_list = f.readlines()
    #print(len(text_list));
    #ファイルの中身でループ
    text_line=1;
    for text in text_list:
        #ワードリストで更にループ
        for word in word_box:
            #print(word)
            if text.find(word)>0:
               print(word+"を検知")
               print(str(text_line)+"行目")
               try:
                   print(text)
               except :
                   print("エラー：読み取れない文字列が含まれています")
               text_line+=1;
                
    roop_num+=1;
    
