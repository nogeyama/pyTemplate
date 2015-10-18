# coding: utf-8
#
# python34
# pythonでのコマンドライン引数の処理
# argparseが推奨
# optparseは非推奨
#
# -h は標準で存在する。
#

import argparse

if __name__ == '__main__':
      parser = argparse.ArgumentParser()
      parser.add_argument('-b', dest='var_bbb', action='store_true', help=u':optionフラグ系')   # ON/OFF
      ## parser.add_argument('-b', '--var_bbb', action='store_true, help=u':optionフラグ系'')   # ON/OFF
      parser.add_argument('-a', dest='var_aaa', action='store', default='zzz', help=u':option文字列系')      # 文字列引数
      parser.add_argument('-c', dest='var_ccc', action='store', type=int, default=0, help=u':option数値系')  # 数値引数
      parser.add_argument('var_else', action='store', type=str, help=u':必須引数ファイル名とか')             # 必須引数

      args = parser.parse_args()

      print( args.var_bbb, type(args.var_bbb))    # True or False, <type 'bool'>
      print( args.var_aaa, type(args.var_aaa))    # 文字列 or None, <type 'str'>
      print( args.var_ccc, type(args.var_ccc))    # 数値 or None, <type 'int'> # 数値が大きいと自動で'long'になった。
      print( args.var_else, type(args.var_else))  # 必須, <type 'str'>
