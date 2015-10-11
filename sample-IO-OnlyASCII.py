# -*- coding: utf-8 -*-
import codecs
if __name__ == "__main__":

    fin  = codecs.open("data-in-sjis.txt","r","shift_jis")
    fout_euc = codecs.open("data-out-euc.txt","w","euc_jp")
    fout_utf = codecs.open("data-out-utf8.txt","w","utf-8")

    for row in fin:
        fout_euc.write(row)
        fout_utf.write(row)

    fin.close()
    fout_euc.close()
    fout_utf.close()
