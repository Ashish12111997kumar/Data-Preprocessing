string='Grow Gratitude'
G=string[0]
len_str=len(string)
count_G=string.count('G')
print("G-->",G)
print('len_str-->',len_str)
print("Count_G-->",count_G)


#################################


#first methode


print("First method")
print('\n')
print('\n')
from collections import Counter
string1='Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'
Cnt_char=Counter(string1)
print(Cnt_char)
print('\n')
print('\n')
print('\n')


# 2nd method

print("second Method")
print('\n')
print('\n')
cnt=dict()
for i in string1:
  if i in cnt.keys():
    cnt[i]+=1
  else:
    cnt[i]=1
print(Cnt_char)
###############################################

string2='Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth'
one_char=string2[0]
first_three=string2[0:3]
last_three=string2[-1:-4:-1]
print('one_char-->',one_char)
print('first_three-->',first_three)
print('last_three-->',last_three)
#############################################

for i in range(108):
  print("🪐")
############################################

string5='Grow Gratitude'
repl=string.replace('Grow','Growth of')
print(repl)
#############################################
pdf="""elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"""
reverse=pdf[::-1]
print(reverse)