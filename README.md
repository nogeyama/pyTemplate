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


------------------------------------
UnicodeDecodeError
UnicodeEncodeError

http://lab.hde.co.jp/2008/08/pythonunicodeencodeerror.html
http://www.gembook.org/2011-03-11.html
http://blog.story-fact.com/?eid=970842

# まとめ
# ・内部表現（unicode）と外部表現（str）は混ぜない．
#   外部表現はすぐ内部表現に変換し，
#   外部に出力する際は，直前で外部表現に一括変換する．
#   変数のデフォルト型は内部表現unicodeに統一する．
#   （これと反対にstrを基準にすることも不可能ではないし，一見楽．
#     しかし，視点が逆になるのでその人々（の記事）とコミュニケーションをするのは難しい．）
# ・print用の.encode('utf-8')は直前に一括して変換すべし．
# ・python2.7はdefaultcodingがasciiであるため自動変換でERRORが発生する．
#   自動変換が発生しないようにコーディングする必要がある．
# ・print,pipeはstrで出力．
#   printやpipeは明示的にencodeしないとダメ．
# ・writeはunicodeで出力 （これ紛らわしい）．
#   出力はunicodeを与えればよい．
#   codecs.open（fp）を経由するものは入力unicodeが指定文字コードに自動変換される．
# ・printがpipeに比べて少し柔軟，かつ，ロケールへの変換であって，defaultcodingではないので，より混乱する．
#   リダイレクトした途端にERRORが発生してしまう．
#   pipeの動作も常に確認すべき．
# ・python3では，defaultcodingがutf-8になるので，
#   環境，プログラム，データの全てがutf-8環境の場合楽ちんになる．
#   しかし，python2.7との互換性問題が出る．

