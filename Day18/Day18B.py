import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
#Load Input Data
iris=datasets.load_iris( )
#Taking first two features sepal length,petal length for all rows
X=iris.data[:,:2] 
Y=iris.target

#Plot  SVM boundaries with original data.
x_min = X[: , 0].min( )-1
x_max=X[: , 0].max( ) + 1
y_min, y_max = X[: , 1].min( )-1, X[: , 1].max( ) + 1
#Create mesh to plot
h=(x_max/x_min)/100
xx,yy= np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
X_plot=np.c_[xx.ravel( ), yy.ravel( )]
#Give the value of regularization parameter
c=1.0
#Create SVM classifier object
svc_classifier=svm.SVC(kernel='linear', C=c, decision_function_shape='ovr').fit(X,Y)
Z=svc_classifier.predict(X_plot)
Z=Z.reshape(xx.shape)
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.contourf(xx,yy,Z,cmap=plt.cm.tab10,alpha=0.3)
plt.scatter(X[: , 0],X[: , 1],c=Y , cmap=plt.cm.Set1)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min( ), xx.max( ) )
plt.title('SVC with linear kernel')
plt.show( )
