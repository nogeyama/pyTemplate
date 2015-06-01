http://python.keicode.com/lang/control-basic-rule.php


() 、[]、{} で囲めば、改行はできます。

if a < b and c < d and e < f and g < h:
     x = 1
     y = 2


if (   a < b # ( を付けて改行
   and c < d 
   and e < f 
   and g < h ):
     x = 1
     y = 2

if x < y : print 'Hello!'


L = [ [1,2,3], [4,5,6], [7,8,9] ]

M = [ [1,2,3], # 改行して縦を揃える
      [4,5,6],
      [7,8,9] ]


------------------------------------
特殊文字を含むファイルパスの扱い

// 文字列中の' ', '$', '`', '\' にはESC文字('\')を付与する．Linuxのパス文字を意識して．
// 文字列全体は""で囲む．
