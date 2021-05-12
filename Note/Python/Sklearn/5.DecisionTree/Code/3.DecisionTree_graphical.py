#引用
import numpy as np
from sklearn import tree
#資料準備------------------------------------------------------

#樣本
X=np.array([[180, 85],[174, 80],[170, 75],  #樣本-男
            [167, 45],[158, 52],[155, 44]]) #樣本-女
#答案
Y=np.array(['man','man','man','woman','woman','woman'])

#使用演算法----------------------------------------------------
#宣告
decision_Tree=tree.DecisionTreeClassifier()

#訓練
decision_Tree.fit(X,Y)

#將決策樹畫成圖表

from sklearn.tree import export_graphviz

export_graphviz(decision_Tree,out_file='tree.dot')  #輸出DOT檔


#目前不可用
"""
#輸出圖片
import pydot
from six import StringIO
#from sklearn.externals.six import StringIO #舊版用法

dot_Data=StringIO()
export_graphviz(decision_Tree,out_file=dot_Data)    #輸出到變數


#graph=pydot.graph_from_dot_data(dot_Data.getvalue())
graph=pydot.graph_from_dot_data(dot_Data.getvalue())
graph[0].create_png()
graph.write_png('tree.png')
"""