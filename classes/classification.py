class classification:

    def svm(X,y,x_test,kernel1,degree1,nilai_c,coef01,):
        SVM = svm.SVC(C=nilai_c, kernel=kernel1, degree=degree1, gamma='auto', coef0=coef01)
        SVM.fit(X,y)
        predictions_NZ = SVM.predict(x_test)
        return predictions_NZ
