import json
import os
import codecs
import chardet
codecs.register_error('none', lambda e: ('???', e.end))


#------------------------------------
#ファイル名の一括取得
#------------------------------------
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
#------------------------------------
#ファイルリストの中身から文字列検索
#------------------------------------
#保存するファイル設定
#ファイルがあった場合、削除する
if os.path.exists('検出結果.html')==True:
   os.remove('検出結果.html')
file = open('検出結果.html', 'a', encoding='UTF-8')
roop_num=1;
for data in file_list:
    #if roop_num > 5:
    #   break;
    print('-------------------------')
    print(str(roop_num)+":"+str(data))
    print('-------------------------')    
    file.write('<h2>'+'-------------------------'+'<br>');
    file.write(str(roop_num)+":"+str(data)+'</br>');
    file.write('-------------------------'+'</h2>');
    #ファイルの文字コードを見る
    with open('file_list/'+data, 'rb') as f:
         file_encode=chardet.detect(f.read());
    #１行ずつ展開
    #文字コードによって読み取りを変える
    if file_encode['encoding'] == 'utf-8':
        with open('file_list/'+data, 'r', encoding='UTF-8', errors='none') as f:
             text_list = f.readlines()
    if file_encode['encoding'] == 'CP932' or file_encode['encoding'] == 'SHIFT_JIS':
        with open('file_list/'+data, 'r', encoding='CP932', errors='none') as f:
             text_list = f.readlines()

    print(file_encode['encoding'])
    
    #print(len(text_list));
    #ファイルの中身でループ
    text_line=1;
    for text in text_list:
        #print(text)
        #ワードリストで更にループ
        for word in word_box:
            #print(word)
            if text.find(word)>=0:
               print(word+"を検知")
               print(str(text_line)+"行目")                
               file.write('<h3>'+word+"を検知"+'</h3>');
               file.write('<p><b>'+str(text_line)+"行目"+'</b></p>');
               #文言にタグを入れる
               text_output = text.replace(word,'<span style="background-color:#ffcc99">'+word+'</span>');
               try:
                   #print(text)
                   file.write('<p>'+text_output+'</p>');
               except :
                   #print("エラー：読み取れない文字列が含まれています")
                   file.write('<p>'+"エラー：読み取れない文字列が含まれています"+'</p>');
        text_line+=1;
    roop_num+=1;
file.close()
