# Problem 2.c
heightList = [195, 200, 192, 230, 212, 200, 210, 205, 218, 177, 185, 197]
weightList = [96, 98, 86, 140, 116, 92, 117, 113, 136, 81, 79, 92]

min = 79
max = 140
newmin = 1
newmax = 5

for val in weightList:
    output = ((val - min) / (max - min)) * (newmax - newmin) + newmin
    print(output)

minMaxHeightList = [2.3585, 2.7358, 2.1321, 5.00, 3.6415, 2.7358, 3.4906, 3.1132, 4.0943, 1.00, 1.6038, 2.5094]
minMaxMeanHeight = sum(minMaxHeightList) / len(minMaxHeightList)
heightVariance = 0

minMaxWeightList = [2.1148, 2.2459, 1.4590, 5.00, 3.4262, 1.8525, 3.4918, 3.2295, 4.7377, 1.1311, 1.00, 1.8525]
minMaxMeanWeight = sum(minMaxWeightList) / len(minMaxWeightList)
weightVariance = 0

for val in minMaxHeightList:
    heightVariance += ((val - minMaxMeanHeight) ** 2)
heightVariance /= (len(heightList) - 1)

for val in minMaxWeightList:
    weightVariance += ((val - minMaxMeanWeight) ** 2)
weightVariance /= (len(weightList) - 1)

# Variances
print(heightVariance)
print(weightVariance)
# Means
print(minMaxMeanHeight)
print(minMaxMeanWeight)
# Standard deviations
print(heightVariance ** 0.5)
print(weightVariance ** 0.5)


# Problem 2.b
heightList = [195, 200, 192, 230, 212, 200, 210, 205, 218, 177, 185, 197]
weightList = [96, 98, 86, 140, 116, 92, 117, 113, 136, 81, 79, 92]

meanHeight = sum(heightList) / len(heightList)
meanWeight = sum(weightList) / len(weightList)

heightVariance = 0
weightVariance = 0

for val in heightList:
    heightVariance += ((val - meanHeight) ** 2)
heightVariance /= (len(heightList) - 1)

for val in weightList:
    weightVariance += ((val - meanWeight) ** 2)
weightVariance /= (len(weightList) - 1)

# SDs
heightSD = heightVariance ** 0.5
weightSD = weightVariance ** 0.5

# Collect list of z-scores
zScoresHeight = []
zScoresWeight = []

for val in heightList:
    output = (val - meanHeight) / heightSD
    zScoresHeight.append(output)

for val in weightList:
    output = (val - meanWeight) / weightSD
    zScoresWeight.append(output)

# Get means of z-scores
zScoreHeightMean = sum(zScoresHeight) / len(zScoresHeight)
zScoreWeightMean = sum(zScoresWeight) / len(zScoresWeight)

print(zScoreHeightMean)
print(zScoreWeightMean)

# Get variances
zScoreHeightVariance = 0
zScoreWeightVariance = 0

for val in zScoresHeight:
    zScoreHeightVariance += ((val - zScoreHeightMean) ** 2)
zScoreHeightVariance /= (len(zScoresHeight) - 1)

for val in zScoresWeight:
    zScoreWeightVariance += ((val - zScoreWeightMean) ** 2)
zScoreWeightVariance /= (len(zScoresWeight) - 1)

print(zScoreHeightVariance)
print(zScoreWeightVariance)


X1 = [3, 10, 4]
X2 = [6, 1, 5]
X3 = [8, 5, 8]
X4 = [7, 2, 1]
X5 = [1, 2, 3]
X6 = [1, 2, 9]

# Problem 3.1a
# r = 1 for Minkowski Distance (Manhattan distance)
sum1 = 0
for i in range(3):
    sum1 += abs(X5[i] - X6[i])
print(sum1 ** (1 / 1))

# Problem 3.1b
# r = 2 for Minkowski Distance (Euclidian distance)
sum2 = 0
for i in range(3):
    sum2 += (abs(X5[i] - X6[i]) ** 2)
print(sum2 ** (1 / 2))

# Problem 3.1c
# r = infinity for Minkowski Distance (Supremum distance)
distances = []
for i in range(3):
    distances.append(abs(X5[i] - X6[i]))
final_dist = max(distances)
print(final_dist)

# Problem 3.1d
# Calculating cosine similarity measure
dotprod = 0
for i in range(3):
    dotprod += (X5[i] * X6[i])

mag1 = 0
mag2 = 0
for i in range(3):
    mag1 += (X5[i] ** 2)
    mag2 += (X6[i] ** 2)
mag1 = mag1 ** (1 / 2)
mag2 = mag2 ** (1 / 2)

cosine = dotprod / (mag1 * mag2)
print(cosine)
