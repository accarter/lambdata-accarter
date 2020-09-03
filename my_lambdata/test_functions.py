from my_lambdata.ds_utilities import ConfusionMatrix

cm = ConfusionMatrix(85, 58, 8, 36)
print('Accuracy', cm.accuracy())
print('Precision', cm.precision())
print('Recall', cm.recall())
