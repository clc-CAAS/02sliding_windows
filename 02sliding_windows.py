#!bin/python
import os
import sys
import argparse
#eg:python 02sliding_windows.py -i lobed_unlobed_A01_index.xls -name lobed_unlobed_A01_index.xls -len 42666085 -win 3000000 -sliding 30000 -o A01_sliding.txt

parser=argparse.ArgumentParser(description='calculate the index with a sliding window for per chomosome')
parser.add_argument('-i', type =argparse.FileType('r'),help='the name file')
parser.add_argument('-name', type =str,help='the index name file')
parser.add_argument('-len', type = int ,help='the chromosome length')
parser.add_argument('-win', type =int,help='the window size')
parser.add_argument('-sliding', type =int,help='the sliding window size')
parser.add_argument('-o', type =argparse.FileType('w'),help='the output file name')
args=parser.parse_args()

debug=True

value=args.len//args.sliding+1
end=0
for index in range(0,value):
	if end < args.len:
		start=index*args.sliding
		end=start+args.win
		command1="awk '{if($2>="+str(start)+" && $2<"+str(end)+") print$0}' "+args.name+" > tem_file"
		os.system(command1)
		new_file=open('tem_file','r')
		value1=0
		value2=0
		value3=0
		value4=0
		num=0
		for eachline in new_file:
			eachline=eachline.strip()
			i=eachline.split()
			num+=1
			value1+=float(i[5])
			value2+=float(i[7])
			value3+=float(i[8])
			value4+=float(i[9])
		if num != 0:
			average1=value1/num
			average2=value2/num
			average3=value3/num
			average4=value4/num
			args.o.write('%s\t%s\t%s\t%f\t%f\t%f\t%f\t%s\n' % (i[0],start,end,average1,average2,average3,average4,num))
	else:
		start=index*args.sliding
		end=args.len
		command1="awk '{if($2>="+str(start)+" && $2<"+str(end)+") print$0}' "+args.name+" > tem_file"
		os.system(command1)
		new_file=open('tem_file','r')
		value1=0
		value2=0
		value3=0
		value4=0
		num=0
		for eachline in new_file:
			eachline=eachline.strip()
			i=eachline.split()
			num+=1
			value1+=float(i[5])
			value2+=float(i[7])
			value3+=float(i[8])
			value4+=float(i[9])
		if num != 0:
			average1=value1/num
			average2=value2/num
			average3=value3/num
			average4=value4/num
			args.o.write('%s\t%s\t%s\t%f\t%f\t%f\t%f\t%s\n' % (i[0],start,end,average1,average2,average3,average4,num))
		break
#####chr start end pool-snpindx1 pool-snpindx2 delta confidence_interval

args.i.close()
args.o.close()


