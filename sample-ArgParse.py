# coding: utf-8
#
# python�ł̃R�}���h���C�������̏���
# argparse������
# optparse�͔񐄏�
#
# -h �͕W���ő��݂���B
#

import argparse

if __name__ == '__main__':
      parser = argparse.ArgumentParser()
      parser.add_argument('-b', dest='var_bbb', action='store_true', help=u':option�t���O�n')   # ON/OFF
      ## parser.add_argument('-b', '--var_bbb', action='store_true, help=u':option�t���O�n'')   # ON/OFF
      parser.add_argument('-a', dest='var_aaa', action='store', default='zzz', help=u':option������n')      # ���������
      parser.add_argument('-c', dest='var_ccc', action='store', type=int, default=0, help=u':option���l�n')  # ���l����
      parser.add_argument('var_else', action='store', type=str, help=u':�K�{�����t�@�C�����Ƃ�')             # �K�{����

      args = parser.parse_args()

      print args.var_bbb, type(args.var_bbb)    # True or False, <type 'bool'>
      print args.var_aaa, type(args.var_aaa)    # ������ or None, <type 'str'>
      print args.var_ccc, type(args.var_ccc)    # ���l or None, <type 'int'> # ���l���傫���Ǝ�����'long'�ɂȂ����B
      print args.var_else, type(args.var_else)  # �K�{, <type 'str'>
