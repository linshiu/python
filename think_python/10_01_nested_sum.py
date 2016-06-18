def nested_sum(nestedList, newList = [0]):
        '''
        nestedList: list composed of nested lists containing int.
        newList: list. The flat list conposed of all the items present
        in the nested lists.
        Returns the sum of all the int in the nested list
        '''
        #Helper function to flatten the list
        def flatlist(nestedList):
                '''
                Returns a flat list
                '''
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == int:
                                newList.append(nestedList[i])
                        else:
                                flatlist(nestedList[i])
                return newList
 
        flatlist(nestedList)
        print sum(newList)


test = [[10,10,10],[50],[15,15]]


 
nested_sum(test)

