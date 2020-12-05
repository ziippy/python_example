# decision tree
import matplotlib.pyplot as plt
import random
from sklearn import datasets, tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

# 데이터 읽어오기
digits = datasets.load_digits()

# 이미지를 표시
for label, img in zip(digits.target[:10], digits.images[:10]):
    plt.subplot(2, 5, label+1)
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Digit: {0}'.format(label))
#plt.show()

print(label, img, img.shape)

#
images = digits.images
labels = digits.target

# 차원을 하나 줄인다.
images = images.reshape(images.shape[0], -1)

# 결정트리 생성
n_samples = len(images)
train_size = int(n_samples * 2/3)
classifier = tree.DecisionTreeClassifier(max_depth=3)
classifier.fit(images[:train_size], labels[:train_size])

# 결정트리의 성능을 확인
expected = labels[train_size:]
predicted = classifier.predict(images[train_size:])

print('Accuracy: \n', accuracy_score(expected, predicted))
print('Confusion matrix: \n', confusion_matrix(expected, predicted))



