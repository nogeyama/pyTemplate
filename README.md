http://python.keicode.com/lang/control-basic-rule.php


() �A[]�A{} �ň͂߂΁A���s�͂ł��܂��B

if a < b and c < d and e < f and g < h:
     x = 1
     y = 2


if (   a < b # ( ��t���ĉ��s
   and c < d 
   and e < f 
   and g < h ):
     x = 1
     y = 2

if x < y : print 'Hello!'


L = [ [1,2,3], [4,5,6], [7,8,9] ]

M = [ [1,2,3], # ���s���ďc�𑵂���
      [4,5,6],
      [7,8,9] ]


------------------------------------
���ꕶ�����܂ރt�@�C���p�X�̈���

// �����񒆂�' ', '$', '`', '\' �ɂ�ESC����('\')��t�^����DLinux�̃p�X�������ӎ����āD
// ������S�̂�""�ň͂ށD


------------------------------------
UnicodeDecodeError
UnicodeEncodeError

http://lab.hde.co.jp/2008/08/pythonunicodeencodeerror.html
http://www.gembook.org/2011-03-11.html
http://blog.story-fact.com/?eid=970842

# �܂Ƃ�
# �E�����\���iunicode�j�ƊO���\���istr�j�͍����Ȃ��D
#   �O���\���͂��������\���ɕϊ����C
#   �O���ɏo�͂���ۂ́C���O�ŊO���\���Ɉꊇ�ϊ�����D
#   �ϐ��̃f�t�H���g�^�͓����\��unicode�ɓ��ꂷ��D
#   �i����Ɣ��΂�str����ɂ��邱�Ƃ��s�\�ł͂Ȃ����C�ꌩ�y�D
#     �������C���_���t�ɂȂ�̂ł��̐l�X�i�̋L���j�ƃR�~���j�P�[�V����������͓̂���D�j
# �Eprint�p��.encode('utf-8')�͒��O�Ɉꊇ���ĕϊ����ׂ��D
# �Epython2.7��defaultcoding��ascii�ł��邽�ߎ����ϊ���ERROR����������D
#   �����ϊ����������Ȃ��悤�ɃR�[�f�B���O����K�v������D
# �Eprint,pipe��str�ŏo�́D
#   print��pipe�͖����I��encode���Ȃ��ƃ_���D
# �Ewrite��unicode�ŏo�� �i���ꕴ��킵���j�D
#   �o�͂�unicode��^����΂悢�D
#   codecs.open�ifp�j���o�R������͓̂���unicode���w�蕶���R�[�h�Ɏ����ϊ������D
# �Eprint��pipe�ɔ�ׂď����_��C���C���P�[���ւ̕ϊ��ł����āCdefaultcoding�ł͂Ȃ��̂ŁC��荬������D
#   ���_�C���N�g�����r�[��ERROR���������Ă��܂��D
#   pipe�̓������Ɋm�F���ׂ��D
# �Epython3�ł́Cdefaultcoding��utf-8�ɂȂ�̂ŁC
#   ���C�v���O�����C�f�[�^�̑S�Ă�utf-8���̏ꍇ�y����ɂȂ�D
#   �������Cpython2.7�Ƃ̌݊�����肪�o��D

