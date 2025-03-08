import dpdata
dpdata.LabeledSystem('00.data/OUTCAR').to('deepmd/npy', 'data', set_size=2)
import os
files=os.listdir('data')
my=[]
for file in files:
    if file.endswith('.raw'):
        my.append(file)
for file in files:
    if not file.endswith('.raw'):
        #新建文件夹
        os.makedirs('data/data_'+file[-1])
        #将file移动到新文件夹
        os.rename('data/'+file,'data/data_'+file[-1]+'/'+file)
        #将my中的文件夹复制到新文件夹,不是移动
        for i in my:
            os.system('cp data/'+i+' data/data_'+file[-1]+'/'+i)
            
