import monkdata as m
import dtree as d
import pprint as p
import sys
import random
import math
# import drawtree as dr
def assignment1():
  print("monk1 entropy: ", d.entropy(m.monk1))
  print("monk1Test entropy: ",d.entropy(m.monk1test))
  print("monk2 entropy: ",d.entropy(m.monk2))
  print("monk2test entropy: ",d.entropy(m.monk2test))
  print("monk3 entropy: ",d.entropy(m.monk3))
  print("monk3test entropy: ",d.entropy(m.monk3test))

def assignment2():
  print("Average Gain for ", "Monk-1")
  print(d.averageGain(m.monk1, m.attributes[0]), d.averageGain(m.monk1, m.attributes[1]), d.averageGain(m.monk1, m.attributes[2]), d.averageGain(m.monk1, m.attributes[3]), d.averageGain(m.monk1, m.attributes[4]), d.averageGain(m.monk1, m.attributes[5]))

  print("Average Gain for ", "Monk-2")
  print(d.averageGain(m.monk2, m.attributes[0]), d.averageGain(m.monk2, m.attributes[1]), d.averageGain(m.monk2, m.attributes[2]), d.averageGain(m.monk2, m.attributes[3]), d.averageGain(m.monk2, m.attributes[4]), d.averageGain(m.monk2, m.attributes[5]))

  print("Average Gain for ", "Monk-3")
  print(d.averageGain(m.monk3, m.attributes[0]), d.averageGain(m.monk3, m.attributes[1]), d.averageGain(m.monk3, m.attributes[2]), d.averageGain(m.monk3, m.attributes[3]), d.averageGain(m.monk3, m.attributes[4]), d.averageGain(m.monk3, m.attributes[5]))

def assignment3():
  print("Monk1")
  monk1Tree = d.buildTree(m.monk1, m.attributes)
  print(1-d.check(monk1Tree, m.monk1))
  print(1-d.check(monk1Tree, m.monk1test))
  print(monk1Tree)

  print("Monk2")
  monk2Tree = d.buildTree(m.monk2, m.attributes)
  print(1-d.check(monk2Tree, m.monk2))
  print(1-d.check(monk2Tree, m.monk2test))
  print(monk2Tree)

  print("Monk3")
  monk3Tree = d.buildTree(m.monk3, m.attributes)
  print(1-d.check(monk3Tree, m.monk3))
  print(1-d.check(monk3Tree, m.monk3test))
  print(monk3Tree)

  print("Monk1 --  2 Levels")
  monk1Tree = d.buildTree(m.monk1, m.attributes, 2)
  print(1-d.check(monk1Tree, m.monk1))
  print(1-d.check(monk1Tree, m.monk1test))
  print(monk1Tree)

  print("Monk2 --  2 Levels")
  monk2Tree = d.buildTree(m.monk2, m.attributes, 2)
  print(1-d.check(monk2Tree, m.monk2))
  print(1-d.check(monk2Tree, m.monk2test))
  print(monk2Tree)

  print("Monk3 --  2 Levels")
  monk3Tree = d.buildTree(m.monk3, m.attributes, 2)
  print(1-d.check(monk3Tree, m.monk3))
  print(1-d.check(monk3Tree, m.monk3test))
  print(monk3Tree)

# Split based on a certain attribute
def split(dataset, attribute):
  datasubsets= []
  for value in attribute.values:
    datasubsets.append([x for x in dataset if x.attribute[attribute] == value])
  return datasubsets
def myBuildTree(dataset, levels):
  treeLevels=[]
  splits = []
  treeLevels.append(dataset)
  datasubsets = dataset
  datasubsetsAvgGains = []
  for level in range(0, levels):
    print("\n===Level #: ", level)
    if level  == 0:
      attribAvgGains = []
      largestGain =  0
      largestAttribIndex = 0
      if len(datasubsets)>5:
        for attribute in range(0,len(m.attributes)):
          avgGain = d.averageGain(datasubsets, m.attributes[attribute])
          if avgGain > largestGain:
            largestGain = avgGain
            largestAttribIndex = attribute
          attribAvgGains.append(avgGain)
          print("Attribute: ", attribute, "\t\tAverage gain: ", avgGain)
          datasubsetsAvgGains.append(attribAvgGains)
        print("---Splitting at attribute: ", m.attributes[largestAttribIndex])
        datasubsets = split(datasubsets, m.attributes[largestAttribIndex])
        splits.append(m.attributes[largestAttribIndex])
        treeLevels.append(datasubsets)

    elif level >0:
      print("---No. of datasets: ", len(datasubsets))
      newdatasubsets = []
      for i in range(0,len(datasubsets)):
        print("\n---Datasubset: ", i, "\t\tEntropy: ", d.entropy(datasubsets[i]))
        attribAvgGains = []
        newdatasubsets=[]
        largestGain =  0
        largestAttribIndex = 0
        if len(datasubsets[i])>5:
          for attribute in range(0,len(m.attributes)):
            avgGain = d.averageGain(datasubsets[i], m.attributes[attribute])
            if avgGain > largestGain:
              largestGain = avgGain
              largestAttribIndex = attribute
            attribAvgGains.append(avgGain)
            print("Attribute: ", attribute, "\t\tAverage gain: ", avgGain)
          if avgGain > 0:
            print("---Splitting at attribute: ", m.attributes[largestAttribIndex].name)
            newdatasubsets.append(split(datasubsets[i], m.attributes[largestAttribIndex]))
            splits.append(m.attributes[largestAttribIndex])
          else:
            print("---Skipping splitting at attribute: ", m.attributes[largestAttribIndex].name, "Dataset #", i)
          datasubsetsAvgGains.append(attribAvgGains)

      if len(newdatasubsets[0]) > 1:
        datasubsets = newdatasubsets[0]
        print("---No. of New datasets: ", len(datasubsets))
      treeLevels.append(datasubsets)

  return splits
def assignment3_p2():
  print("\n#####Start Assignment 3 part 2")
  splits = myBuildTree(m.monk1, 2)
  print("splits", splits)
  print(d.buildTree(m.monk1, m.attributes, 2))


def partition(data, fraction):
  ldata = list(data)
  random.shuffle(ldata)
  breakPoint = int(len(data) * fraction)
  return ldata[:breakPoint], ldata[breakPoint:]

def assignment4_p1(data, attributes, fraction):
  trainData, validData = partition(data, fraction)
  dataTree = d.buildTree(trainData, attributes)
  orgErr = 1-d.check(dataTree, validData)
  print("ORIGINAL ERR", orgErr)
  orgTree = dataTree
  bestPrunedTree = orgTree
  cont = True
  while cont:
    err = orgErr
    bestErrorRate = err
    prunedTrees = d.allPruned(bestPrunedTree)
    print(len(prunedTrees))
    for i in range(0, len(prunedTrees)):
      err = 1-d.check(prunedTrees[i], validData)
      print(i, err)
      if err < bestErrorRate:
        bestErrorRate = err
        bestPrunedTree = prunedTrees[i]
        print("Best Error Rate:", bestPrunedTree, bestErrorRate)

    if bestErrorRate > orgErr:
      return orgTree
    elif bestPrunedTree == dataTree:
      break
    #else:
      # if bestPrunedTree == prunedTrees:
      # prunedTrees = d.allPruned(bestPrunedTree)


    orgTree = bestPrunedTree
    orgErr = bestErrorRate






# assignment1()
# assignment2()
# assignment3()
# assignment3_p2()
def getPrunedChildren(toPrune, bestErrorRate, validData):
  bestPrunedTreesGrandChildren = []
  for bestPrunedTreeIndex in range(0, len(toPrune)):
    #print(toPrune[bestPrunedTreeIndex])
    prunedTreesChildren = []
    prunedTreesChildren = d.allPruned(toPrune[bestPrunedTreeIndex])
    #print(len(prunedTreesChildren))
    notFound = False
    for i in range(0, len(prunedTreesChildren)):
      tempPrunedTreesGrandChildren = []
      err = 1-d.check(prunedTreesChildren[i], validData)
      #print(i, err)
      if err <= bestErrorRate:
        #bestErrorRate = err
        tempPrunedTreesGrandChildren.append(getPrunedChildren([prunedTreesChildren[i]], err, validData))
      else:
        notFound = True


        #print("Best Error Rate:", prunedTreesChildren[i], bestErrorRate)
        #print(len(tempPrunedTreesGrandChildren))
    if notFound:
      tempPrunedTreesGrandChildren.append(toPrune[bestPrunedTreeIndex])
    bestPrunedTreesGrandChildren += tempPrunedTreesGrandChildren
    #print(len(bestPrunedTreesGrandChildren))
  return bestPrunedTreesGrandChildren

def assignment4_p3(data, attributes, fraction):
  trainData, validData = partition(data, fraction)
  dataTree = d.buildTree(trainData, attributes)
  orgErr = 1-d.check(dataTree, validData)
  #print("ORIGINAL ERR", orgErr)
  orgTree = dataTree
  #########################
  bestPrunedTreesList = []
  toPrune=[]
  toPrune.append(orgTree)
  #bestPrunedTreesList.append(orgTree)
  err = orgErr
  bestErrorRate = err
  bestPrunedTreesList = getPrunedChildren(toPrune, bestErrorRate, validData)

  if len(bestPrunedTreesList) == 0:
    toReturn = toPrune[0]
  else:
    toReturn = bestPrunedTreesList[0]

#   print(toReturn)
  #print("No. of best pruned trees:", len(bestPrunedTreesList))
  #for i in range(0, len(bestPrunedTreesList)):
    #print("Pruned Tree No. ", i, "test error rate: ", 1-d.check(bestPrunedTreesList[i], validData))
#   print("Pruned Tree ", "test error rate: ", 1-d.check(toReturn, validData))

  #return bestPrunedTreesList
  return 1-d.check(toReturn, validData)





  #bestPrunedTrees = [x for x in prunedTrees if d.check(x, validData)<=orgErr]
  #print(len(bestPrunedTrees))

  #worstPrunedTrees = [x for x in prunedTrees if d.check(x, validData)>orgErr]
  #print(len(worstPrunedTrees))

  #if bestErrorRate > orgErr:
  #  return orgTree
  #elif bestPrunedTree == dataTree:
    #break
  #else:
      # if bestPrunedTree == prunedTrees:
      # prunedTrees = d.allPruned(bestPrunedTree)


  #orgTree = bestPrunedTree
  #orgErr = bestErrorRate

# assignment4_p1(m.monk1, m.attributes, 0.3)
def assignment3_p4():
  errors = []
  for i in range(3, 9):
    print(i/10.0)
    error = assignment4_p3(m.monk1, m.attributes, i/10.0)
    print(error)
    errors.append(error)

  return errors

# assignment4_p3(m.monk1, m.attributes, 0.3)
#assignment3_p4()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()