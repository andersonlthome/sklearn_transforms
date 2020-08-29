from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumnsAndClassCancelStudent(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data1 = data.drop(labels=self.columns, axis='columns')
        data2 = data1.drop(data1[
            (data1["REPROVACOES_DE"] == 0) & (data1["NOTA_DE"] == 0) | 
            (data1["REPROVACOES_EM"] == 0) & (data1["NOTA_EM"] == 0) | 
            (data1["REPROVACOES_MF"] == 0) & (data1["NOTA_MF"] == 0) | 
            (data1["REPROVACOES_GO"] == 0) & (data1["NOTA_GO"] == 0) ].index) 
        
        return data2 # data.drop(labels=self.columns, axis='columns')

# # Drop where NOTA=0 and the student cancel the class
# class DropLinesClassCancelStudent(BaseEstimator, TransformerMixin):     
#     def fit(self, X, y=None):
#         return self
    
#     def transform(self, X):
#         data = X.copy()
#         return data.drop(data[
#             (data["REPROVACOES_DE"] == 0) & (data["NOTA_DE"] == 0) | 
#             (data["REPROVACOES_EM"] == 0) & (data["NOTA_EM"] == 0) | 
#             (data["REPROVACOES_MF"] == 0) & (data["NOTA_MF"] == 0) | 
#             (data["REPROVACOES_GO"] == 0) & (data["NOTA_GO"] == 0) ].index)   
    
