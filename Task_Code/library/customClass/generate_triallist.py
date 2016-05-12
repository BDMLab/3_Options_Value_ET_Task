##############################################################################
# CustomClass Rules                                                          #
# =================                                                          #
#                                                                            #
#1. All custom classes must inherit sreb.EBObject and the constructor        #
#   must call sreb.EBObject's constructor. If a class starts with _ then it  #
#   is considered internal and will not be treated as a custom class.        #
#                                                                            #
#2. The custom class will only use the default constructor.                  #  
#   ie. a constructor with no parameters.                                    #
#                                                                            #
#3. To add a property provide getter and have an attribute that does not     #
#   starts with an underscore(_) or an upper case letter, and have the       #
#   attribute of a know type. Known types are int,float,str,EBPoint,EBColor, #
#   tuple, and list.                                                         #
#   If an attribute's default value is of type tuple and only has two        #
#   items, the property will be treated as an EBPoint. Similarly, if an      #
#   attribute's default value is a tuple of 3 items the property will be     #
#   treated as an EBColor.  The input type of the setter and the output type #
#   of the getter is expected to be the same as the type of the attribute.   #
#                                                                            #
#4. If only getter is provided, the property will be a readonly property.    # 
#                                                                            #
#6. The custom class may be instanciated during development to obtain        # 
#   class info. Avoid such things as display mode change, remote connections # 
#   in the constructor.                                                      #
#                                                                            # 
#7. Any method in the custom class can be called using the Execute action    #
#   By default, the return type of the method is string unless a doc string  #
#   with the following constraint is available                               #
#	a. The doc string starts with "RETURN:" (case matters)             #
#       b. Following the text "RETURN:" provide a default value of the type  #
#          or the __repr__ value of the class. eg. str for string            #
#8. If a property's setter metthod has default values for it's parameters,   #
#    the property will not accept references or equation.                    #
##############################################################################


import sreb
import random
import sreb.time
import numpy as np


class CustomClassTemplate(sreb.EBObject):
	def __init__(self):
		sreb.EBObject.__init__(self)
		self.triallist = 0

	# Make variables readable and writable
	def getTriallist(self):
		return self.triallist




	## Putting the "self" thing in the brackets of the method lets the next thing in the brackets "come in" from the GUI
	## So when we call this method with an Execute Action node, that node will ask us for the value for
	## randomList, and we supply it with the BDMLIST.value that we created in the BDM block
	def GenerateProtoBlocks(self,randomList):    
		
		# First I would like to use the costum class to transform the list structure to an np array,
		# because arrays are easier to work with.		
		BDM_Array = np.array(randomList)
		BDM_Array = BDM_Array[3:]

	
		# Sorting the array based on the second column:
		BDM_Array = BDM_Array[BDM_Array[:,1].argsort()]


		# Median split of the BDM_Array
		BDM_Array_Low = BDM_Array[0:len(BDM_Array)/2]
		BDM_Array_High = BDM_Array[len(BDM_Array)/2:]
		
		### Generate high-value triplets by randomly combing items with values above the median:
		High_Triplets = (['Item_1', 'Value_1', 'Item_2,', 'Value_2', 'Item_3', 'Value_3'])
		Order = np.arange(36)
		np.random.shuffle(Order)
		counter = 0
		for x in Order:
    			if counter == 0:
        				triplet = []
    			counter +=1
    			triplet.append(BDM_Array_High[x])
    			if counter == 3:
        				High_Triplets = np.vstack((High_Triplets, np.concatenate((triplet[0], triplet[1], triplet[2]))))
        				counter = 0
		
		### Generate low-value triplets by randomly combing items with values below the median:
		Low_Triplets = (['Item_1', 'Value_1', 'Item_2,', 'Value_2', 'Item_3', 'Value_3'])
		Order = np.arange(36)
		np.random.shuffle(Order)
		counter = 0
		for x in Order:
    			if counter == 0:
        				triplet = []
    			counter +=1
    			triplet.append(BDM_Array_Low[x])
    			if counter == 3:
        				Low_Triplets = np.vstack((Low_Triplets, np.concatenate((triplet[0], triplet[1], triplet[2]))))
        				counter = 0
			
		### Generate the mixed-value triplets
		# Generate triplet arrays
		L1_H2_Triplets = (['Item_1', 'Value_1', 'Item_2,', 'Value_2', 'Item_3', 'Value_3'])
		L2_H1_Triplets = (['Item_1', 'Value_1', 'Item_2,', 'Value_2', 'Item_3', 'Value_3'])

		# Generate the order ranges
		High_Order = np.arange(36); np.random.shuffle(High_Order)
		Low_Order = np.arange(36); np.random.shuffle(Low_Order)

		# Splitting the order ranges
		High_Order1 = High_Order[0:12]; High_Order2 = High_Order[12:24]; High_Order3 = High_Order[24:36]
		Low_Order1 = Low_Order[0:12]; Low_Order2 = Low_Order[12:24]; Low_Order3 = Low_Order[24:36]

		# Generating the triplets
		for x in range(12):
    			L1_H2 = [BDM_Array_Low[Low_Order1[x]], BDM_Array_High[High_Order1[x]], BDM_Array_High[High_Order2[x]]]
    			L2_H1 = [BDM_Array_Low[Low_Order2[x]], BDM_Array_Low[Low_Order3[x]], BDM_Array_High[High_Order3[x]]]
    			L1_H2_Triplets = np.vstack((L1_H2_Triplets, np.concatenate((L1_H2[0], L1_H2[1], L1_H2[2]))))
    			L2_H1_Triplets = np.vstack((L2_H1_Triplets, np.concatenate((L2_H1[0], L2_H1[1], L2_H1[2]))))
		

		### Upper Left
		# Pick 3 triplets from each type
		Upper_Left_Shift0 = np.vstack((High_Triplets[1:4], L1_H2_Triplets[1:4], L2_H1_Triplets[1:4], Low_Triplets[1:4]))
		# Shift the triplets so that each item appear in each position
		Upper_Left_Shift1 = np.roll(Upper_Left_Shift0, 2, axis=1)
		Upper_Left_Shift2 = np.roll(Upper_Left_Shift0, 4, axis=1)

		# Join them all together
		Upper_Left = np.vstack((Upper_Left_Shift0, Upper_Left_Shift1, Upper_Left_Shift2))
		# Add the information about the empty square
		Upper_Left = np.insert(Upper_Left, 0, ['empty.png'], axis=1); Upper_Left = np.insert(Upper_Left, 1, ['-1'], axis=1)
		Upper_Left = np.insert(Upper_Left, 8, ['300'], axis=1); Upper_Left = np.insert(Upper_Left, 9, ['195'], axis=1)
		Upper_Left = np.insert(Upper_Left, 10, ['122'], axis=1); Upper_Left = np.insert(Upper_Left, 11, ['107'], axis=1) ;Upper_Left = np.insert(Upper_Left, 12, ['109'], axis=1)
		# Add triplet index
		Upper_Left = np.insert(Upper_Left, 0, np.array(range(1,13)*3), axis=1)
		#Add headings
		Upper_Left = np.insert(Upper_Left, 0, np.array(('triplet_index', 'UL_Item', 'UL_Value', 'UR_Item', 'UR_Value',
                        'LL_Item', 'LL_Value', 'LR_Item', 'LL_Value', 'Blocker_X', 'Blocker_Y', 'Key1', 'Key2', 'Key3')), axis=0)

		### Upper Right
		# Pick 3 triplets from each type
		Upper_Right_Shift0 = np.vstack((High_Triplets[4:7], L1_H2_Triplets[4:7], L2_H1_Triplets[4:7], Low_Triplets[4:7]))
		# Shift the triplets so that each item appear in each position
		Upper_Right_Shift1 = np.roll(Upper_Right_Shift0, 2, axis=1)
		Upper_Right_Shift2 = np.roll(Upper_Right_Shift0, 4, axis=1)

		# Join them all together
		Upper_Right = np.vstack((Upper_Right_Shift0, Upper_Right_Shift1, Upper_Right_Shift2))
		# Add the information about the empty square
		Upper_Right = np.insert(Upper_Right, 2, ['empty.png'], axis=1); Upper_Right = np.insert(Upper_Right, 3, ['-1'], axis=1)
		Upper_Right = np.insert(Upper_Right, 8, ['685'], axis=1); Upper_Right = np.insert(Upper_Right, 9, ['195'], axis=1)
		Upper_Right = np.insert(Upper_Right, 10, ['97'], axis=1); Upper_Right = np.insert(Upper_Right, 11, ['122'], axis=1); Upper_Right = np.insert(Upper_Right, 12, ['109'], axis=1)
		# Add triplet index
		Upper_Right = np.insert(Upper_Right, 0, np.array(range(13,25)*3), axis=1)
		#Add headings
		Upper_Right = np.insert(Upper_Right, 0, np.array(('triplet_index', 'UL_Item', 'UL_Value', 'UR_Item', 'UR_Value',
                         'LL_Item', 'LL_Value', 'LR_Item', 'LL_Value', 'Blocker_X', 'Blocker_Y', 'Key1', 'Key2', 'Key3')), axis=0)
		
		### Lower_Left
		# Pick 3 triplets from each type
		Lower_Left_Shift0 = np.vstack((High_Triplets[7:10], L1_H2_Triplets[7:10], L2_H1_Triplets[7:10], Low_Triplets[7:10]))
		# Shift the triplets so that each item appear in each position
		Lower_Left_Shift1 = np.roll(Lower_Left_Shift0, 2, axis=1)
		Lower_Left_Shift2 = np.roll(Lower_Left_Shift0, 4, axis=1)

		# Join them all together
		Lower_Left = np.vstack((Lower_Left_Shift0, Lower_Left_Shift1, Lower_Left_Shift2))
		# Add the information about the empty square
		Lower_Left = np.insert(Lower_Left, 4, ['empty.png'], axis=1); Lower_Left = np.insert(Lower_Left, 5, ['-1'], axis=1)
		Lower_Left = np.insert(Lower_Left, 8, ['300'], axis=1); Lower_Left = np.insert(Lower_Left, 9, ['580'], axis=1)
		Lower_Left = np.insert(Lower_Left, 10, ['97'], axis=1); Lower_Left = np.insert(Lower_Left, 11, ['107'], axis=1) ; Lower_Left = np.insert(Lower_Left, 12, ['109'], axis=1)
		# Add triplet index
		Lower_Left = np.insert(Lower_Left, 0, np.array(range(25,37)*3), axis=1)
		#Add headings
		Lower_Left = np.insert(Lower_Left, 0, np.array(('triplet_index', 'UL_Item', 'UL_Value', 'UR_Item', 'UR_Value', 'LL_Item',
                         'LL_Value', 'LR_Item', 'LR_Value', 'Blocker_X', 'Blocker_Y', 'Key1', 'Key2', 'Key3')), axis=0)

		### Lower_Right
		# Pick 3 triplets from each type
		Lower_Right_Shift0 = np.vstack((High_Triplets[10:13], L1_H2_Triplets[10:13], L2_H1_Triplets[10:13], Low_Triplets[10:13]))
		# Shift the triplets so that each item appear in each position
		Lower_Right_Shift1 = np.roll(Lower_Right_Shift0, 2, axis=1)
		Lower_Right_Shift2 = np.roll(Lower_Right_Shift0, 4, axis=1)

		# Join them all together
		Lower_Right = np.vstack((Lower_Right_Shift0, Lower_Right_Shift1, Lower_Right_Shift2))
		# Add the information about the empty square
		Lower_Right = np.insert(Lower_Right, 6, ['empty.png'], axis=1); Lower_Right = np.insert(Lower_Right, 7, ['-1'], axis=1)
		Lower_Right = np.insert(Lower_Right, 8, ['685'], axis=1); Lower_Right = np.insert(Lower_Right, 9, ['580'], axis=1);
		Lower_Right = np.insert(Lower_Right, 10, ['97'], axis=1); Lower_Right = np.insert(Lower_Right, 11, ['122'], axis=1); Lower_Right = np.insert(Lower_Right, 12, ['107'], axis=1)
		# Add triplet index
		Lower_Right = np.insert(Lower_Right, 0, np.array(range(37,49)*3), axis=1)
		#Add headings
		Lower_Right = np.insert(Lower_Right, 0, np.array(('triplet_index', 'UL_Item', 'UL_Value', 'UR_Item', 'UR_Value', 'LL_Item', 'LL_Value',
		 'LR_Item', 'LR_Value', 'Blocker_X', 'Blocker_Y', 'Key1', 'Key2', 'Key3')), axis=0)

		### Generate blocks
		Block_1 = np.vstack((Upper_Left[0:13], Upper_Right[13:25], Lower_Left[25:37], Lower_Right[25:37]))
		Block_2 = np.vstack((Lower_Right[0:13], Upper_Left[13:25], Upper_Right[25:37], Lower_Left[1:13]))
		Block_3 = np.vstack((Upper_Right[0:13], Lower_Right[13:25], Lower_Left[13:25], Upper_Left[25:37]))
		
		### Randomise presentation order
		Complete = False
		while Complete == False:
    			np.random.shuffle(Block_1[1:]); np.random.shuffle(Block_2[1:]); np.random.shuffle(Block_3[1:])
    			# Randomly determine block order
			block_order = random.choice(range(6))
    			if block_order == 0:
        				trial_list = np.vstack((Block_1, Block_2[1:], Block_3[1:]))
    			elif block_order == 1:
        				trial_list = np.vstack((Block_3, Block_1[1:], Block_2[1:]))
    			elif block_order == 2:
        				trial_list = np.vstack((Block_2, Block_3[1:], Block_1[1:]))
    			elif block_order == 3:
        				trial_list = np.vstack((Block_3, Block_2[1:], Block_1[1:]))
    			elif block_order == 4:
        				trial_list = np.vstack((Block_2, Block_1[1:], Block_3[1:]))
    			elif block_order == 5:
        				trial_list = np.vstack((Block_1, Block_3[1:], Block_2[1:]))
    		
			# Check that no triplets with the same items are next to each other
			problem_counter = 0
    			if trial_list[48][0] == trial_list[49][0]:
        				problem_counter += 1
    			if trial_list[96][0] == trial_list[97][0]:
        				problem_counter += 1
    			if problem_counter == 0:
            			Complete = True

		
		# Return the trial_list as a list
		self.triallist = trial_list.tolist()
		



		
