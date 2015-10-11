# -*- coding: utf-8 -*-
# 最初の行には日本語を埋めておこう
# console,pipe,fileの出力毎に対処必要
#

import codecs
if __name__ == "__main__":

    fin  = codecs.open(u"data-inp-sjis.txt","r","shift_jis")
    fout_euc = codecs.open(u"data-out-euc.txt","w","euc_jp")
    fout_utf = codecs.open(u"data-out-utf8.txt","w","utf-8",'backslashreplace')

    for row in fin:
       
        #print row        # unicode ==> consoleOK,pipeNG
        print type(row),"row=unicode"

        row2 = row.encode('shift_jis')
        print row2  # ==> できた！consoleOK&pipeOK&write(OK&NG)<==まぎらわしい！結局writeはNG
        print type(row2),"row2=str"

        row3 = u'１初@'.encode('shift_jis')+row.encode('shift_jis')
        print row3  # ==> できた！consoleOK&pipeOK&writeNG
        print type(row3),"row3=str"

        row4 = u'２2初@'+row
        row41 = row4.encode('shift_jis')
        print row41  # ==> できた！consoleOK&pipeOK&writeNG
        print type(row41),"row41=str"

        fout_euc.write(row)
        fout_utf.write(row)  # これは当然できた．無加工．writeOK

        #fout_utf.write(row2)  # これも実は中身が日本語だとNG writeNG

        #fout_utf.write(row3) # writeNG

        fout_utf.write(row4)  # writeOK as Unicode
        #fout_utf.write(row41) # writeNG


    fout_euc.write(u'足した文字列')
    fout_utf.write(u'足した文字列')  # < writeOK as Unicode！

    fin.close()
    fout_euc.close()
    fout_utf.close()

