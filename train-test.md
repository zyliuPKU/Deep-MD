**下载文件示例数据**：

   curl https://dp-public.oss-cn-beijing.aliyuncs.com/community/DeePMD-kit-FastLearn.tar
   
   tar xvf DeePMD-kit-FastLearn.tar
  
**训练**：

   cd DeePMD-kit-FastLearn/01.train

   dp train input.json

**测试**：

   将rmse.py和corr.py放入01.train文件夹下

   python3 rmse.py #输出rmse随步数的关系

   dp freeze -o graph.pb

   dp compress -i graph.pb -o graph-compress.pb

   dp test -m graph.pb -s ../data/data_3

   python3 corr.py #绘图预测结果和验证集上的结果，并计算相关系数


引用了部分https://zhuanlan.zhihu.com/p/643167506的内容。
