class ConfusionMatrix:
    '''
    Models a simple confusion matrix.
    '''

    def __init__(self, tn, fp, fn, tp):
        '''
        Create a ConfusionMatrix with the specified true positive,
        false positive, false negative, and true positive values.
        '''
        self.matrix = [[tn, fp], [fn, tp]]

    def accuracy(self):
        '''
        The accuracy for this ConfusionMatrix.
        '''
        diagonal, total = 0, 0
        for i, row in enumerate(self.matrix):
            diagonal += row[i]
            total += sum(row)
        return diagonal / total

    def precision(self):
        '''
        The precision for this ConfusionMatrix
        '''
        false_pos = self.matrix[0][1]
        true_pos = self.matrix[1][1]
        return true_pos / (true_pos + false_pos)

    def recall(self):
        '''
        The recall for this ConfusionMatrix
        '''
        false_neg = self.matrix[1][0]
        true_pos = self.matrix[1][1]
        return true_pos + (false_neg + true_pos)
