#!/usr/bin/env python2
# -*- coding: utf-8 -*-


######################## CITATION ##########################
##### BDM Auction modified from:
#####
##### De Martino, B., Fleming, S. M., Garrett, N., & Dolan, R. J. (2012). Confidence in value-based choice. Nature Neuroscience, 16(1), 105-110.
#####
#####




"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.01), July 06, 2014, at 23:51
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

# Import useful packages
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import psychopy
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from pyglet.window import key # to detect key state, whether key is held down, to move slider on key hold
import pandas as pd
from pandas.core.frame import DataFrame as DF
from scipy import stats

# Store info about the experiment session
expName = u'BDMAuction'
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
spreadsheet = 'spreadsheets/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None,
    originPath=None, savePickle=True, saveWideText=True, dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# set up variable to track current state of key press, to move slider when keys held down

keyState = key.KeyStateHandler()

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )
win.winHandle.push_handlers(keyState)
win.setMouseVisible(False)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    
# Initialize components for Routine "PreAuction"
PreAuctionClock = core.Clock()
PreAuctionText = visual.TextStim(win=win, ori=0, name='PreAuctionText',
    text=u'This script will run the auction for your choices. Press Space to see if you won.',
    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
    

# Create some handy timers
globalClock = core.Clock()
routineTimer = core.CountdownTimer()
    
########################## Start Experiment ##############################

#------Prepare to start Routine "PreAuction"-------
t = 0
PreAuctionClock.reset()
frameN = -1
# update component parameters for each repeat
PreAuctionResp = event.BuilderKeyResponse()
PreAuctionResp.status = NOT_STARTED
PreAuctionComponents = []
# keep track of which components have finished
PreAuctionComponents.append(PreAuctionText)
PreAuctionComponents.append(PreAuctionResp)
for thisComponent in PreAuctionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "PreAuction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = PreAuctionClock.getTime()
    frameN = frameN + 1

     # *PreAuctionText* updates
    if t >= 0.0 and PreAuctionText.status == NOT_STARTED:
        PreAuctionText.tStart = t
        PreAuctionText.frameNStart = frameN
        PreAuctionText.setAutoDraw(True)

    # *PreAuctionResp* updates
    if t >= 0 and PreAuctionResp.status == NOT_STARTED:
        PreAuctionResp.tStart = t
        PreAuctionResp.frameNStart = frameN
        PreAuctionResp.status = STARTED
        PreAuctionResp.clock.reset()
        event.clearEvents(eventType='keyboard')
    if PreAuctionResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if 'escape' in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:
            PreAuctionResp.keys = theseKeys[-1]
            PreAuctionResp.rt = PreAuctionResp.clock.getTime()
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:
        routineTimer.reset()
        break
    continueRoutine = False
    for thisComponent in PreAuctionComponents:
        if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=['escape']):
        core.quit()

    # refresh the screen
    if continueRoutine:
        win.flip()
    else:
        routineTimer.reset()

#-------Ending Routine "PreAuction"-------
for thisComponent in PreAuctionComponents:
    if hasattr(thisComponent, 'setAutoDraw'):
        thisComponent.setAutoDraw(False)
# check responses
if PreAuctionResp.keys in ['', [], None]:
    PreAuctionResp.keys = None

# store data for thisExp (ExperimentHandler)
thisExp.addData('PreAuctionResp.keys', PreAuctionResp.keys)
if PreAuctionResp.keys != None:
    thisExp.addData('PreAuctionResp.rt', PreAuctionResp.rt)
thisExp.nextEntry()


######################## AUCTION #########################################
# Load the choices and BDM-values to run the BDMAuction
CHOICES = pd.read_csv("CHOICE_RESULTS_FILE.txt", delim_whitespace=True,header=0)
BDM_RESULTS = pd.read_csv("BDM_RESULTS_FILE.txt",delim_whitespace=True,header=0)

# Remove the practice trials
CHOICES = CHOICES.loc[4:,:].copy()
BDM_RESULTS = BDM_RESULTS.loc[3:, :].copy()

# Pick a winning item
BDM_ITM = CHOICES.loc[np.random.choice(CHOICES.index, 1)[0], 'Chosen_Img']

# Gather the BDM Bid
BDM_BID = np.round(BDM_RESULTS.loc[BDM_RESULTS['BDM_ITM'] == BDM_ITM, 'BDM_VAL'].values[0], 2)

# run the auction
class auction:
    BDM_PRICE = float((np.random.choice(range(1, 300), 1)))/100 # assign a price to the item randomly from between 0.01 and 3 pounds
    # check if S's bid for that item was above or below the price
    if BDM_BID >= BDM_PRICE:
        win_item=True
    elif BDM_BID < BDM_PRICE:
        win_item=False

    # set text for the auction screen
    if win_item==True:
        auc_res_txt = u'Congratulations! You won the following item at auction. \nThis item was picked randomly from your preferred items during the choice task.'
        auc_prc_txt = u'Your bid of \xa3' + '{0:.2f}'.format(BDM_BID) + u' matched or exceeded the randomly generated price of \xa3' + '{0:.2f}'.format(BDM_PRICE) + '.\n\n[Press space bar to continue]'
        cost = BDM_PRICE
    elif win_item==False:
        auc_res_txt = u'Sorry, you did not win the following item at auction. \nThis item was picked randomly from your preferred items during the choice task.'
        auc_prc_txt = u'Your bid of \xa3' + '{0:.2f}'.format(BDM_BID) + u' was lower than the randomly generated price of \xa3' + '{0:.2f}'.format(BDM_PRICE) + '.\n\n[Press space bar to continue]'
        cost = 0
        # add up each component of S's payment

            # find the image path of the auction item
    rand_itm_img = 'images/%s' %BDM_ITM

# calculates the final monitary payment
class score:
    base = 15
    final_pymt = base - auction.cost

    pymt_expl_bdwn = u'\xa3' + '{0:.2f}'.format(base) + u' base payment' + u'\n- \xa3' + '{0:.2f}'.format(auction.cost) + ' cost of auction item'
    pymt_expl_tot = u'Your total payment is: \xa3' + '{0:.2f}'.format(final_pymt) + '\n\nThis concludes the experiment. \nThank you for participating!'


# Initialize components for Routine "auc_disp"
auc_dispClock = core.Clock()
pic_auc_itm = visual.ImageStim(win=win, name='pic_auc_itm',
    image=auction.rand_itm_img, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
auc_txt1 = visual.TextStim(win=win, ori=0, name='auc_txt1',
    text=auction.auc_res_txt, font=u'Arial',
    pos=[0, 0.6], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
auc_txt2 = visual.TextStim(win=win, ori=0, name='auc_txt2',
    text=auction.auc_prc_txt, font=u'Arial',
    pos=[0, -0.6], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)


#------Prepare to start Routine "auc_disp"-------
t = 0
auc_dispClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_auc_disp = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_auc_disp.status = NOT_STARTED
# keep track of which components have finished
auc_dispComponents = []
auc_dispComponents.append(pic_auc_itm)
auc_dispComponents.append(auc_txt1)
auc_dispComponents.append(auc_txt2)
for thisComponent in auc_dispComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "auc_disp"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = auc_dispClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *pic_auc_itm* updates
    if t >= 0.2 and pic_auc_itm.status == NOT_STARTED:
        # keep track of start time/frame for later
        pic_auc_itm.tStart = t  # underestimates by a little under one frame
        pic_auc_itm.frameNStart = frameN  # exact frame index
        pic_auc_itm.setAutoDraw(True)

    # *auc_txt1* updates
    if t >= 0.2 and auc_txt1.status == NOT_STARTED:
        # keep track of start time/frame for later
        auc_txt1.tStart = t  # underestimates by a little under one frame
        auc_txt1.frameNStart = frameN  # exact frame index
        auc_txt1.setAutoDraw(True)

    # *auc_txt2* updates
    if t >= 0.2 and auc_txt2.status == NOT_STARTED:
        # keep track of start time/frame for later
        auc_txt2.tStart = t  # underestimates by a little under one frame
        auc_txt2.frameNStart = frameN  # exact frame index
        auc_txt2.setAutoDraw(True)

    # *key_resp_auc_disp* updates
    if t >= 0.2 and key_resp_auc_disp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_auc_disp.tStart = t  # underestimates by a little under one frame
        key_resp_auc_disp.frameNStart = frameN  # exact frame index
        key_resp_auc_disp.status = STARTED
        # keyboard checking is just starting
        key_resp_auc_disp.clock.reset()  # now t=0
    if key_resp_auc_disp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_auc_disp.keys = theseKeys[-1]  # just the last key pressed
            key_resp_auc_disp.rt = key_resp_auc_disp.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in auc_dispComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "auc_disp"-------
for thisComponent in auc_dispComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_auc_disp.keys in ['', [], None]:  # No response was made
   key_resp_auc_disp.keys=None
# store data for thisExp (TrialHandler)
thisExp.addData('auction.win_item', auction.win_item)
thisExp.addData('auction.price', auction.BDM_PRICE)
thisExp.addData('auction.bid', BDM_BID)
thisExp.addData('auction.rand_itm_img', auction.rand_itm_img)
thisExp.addData('score.base', score.base)


thisExp.addData('score.final_pymt', score.final_pymt)
thisExp.nextEntry()


# Initialize components for Routine "pymt_disp"
pymt_dispClock = core.Clock()
pymt_disp_txt1 = visual.TextStim(win=win, ori=0, name='pymt_disp_txt1',
    text=score.pymt_expl_bdwn, font=u'Arial',
    pos=[0, 0.6], height=0.07, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
pymt_disp_txt2 = visual.TextStim(win=win, ori=0, name='pymt_disp_txt2',
    text=score.pymt_expl_tot, font=u'Arial',
    pos=[0, -0.65], height=0.07, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

#------Prepare to start Routine "pymt_disp"-------
t = 0
pymt_dispClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_pymt_disp = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_pymt_disp.status = NOT_STARTED
# keep track of which components have finished
pymt_dispComponents = []
pymt_dispComponents.append(pic_auc_itm)
pymt_dispComponents.append(pymt_disp_txt1)
pymt_dispComponents.append(pymt_disp_txt2)
pymt_dispComponents.append(key_resp_pymt_disp)
for thisComponent in pymt_dispComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pymt_disp"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pymt_dispClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    if auction.win_item==True:
        # *pic_auc_itm* updates
        if t >= 0.0 and pic_auc_itm.status == NOT_STARTED:
            # keep track of start time/frame for later
            pic_auc_itm.tStart = t  # underestimates by a little under one frame
            pic_auc_itm.frameNStart = frameN  # exact frame index
            pic_auc_itm.setAutoDraw(True)

    # *pymt_disp_txt1* updates
    if t >= 0.0 and pymt_disp_txt1.status == NOT_STARTED:
        # keep track of start time/frame for later
        pymt_disp_txt1.tStart = t  # underestimates by a little under one frame
        pymt_disp_txt1.frameNStart = frameN  # exact frame index
        pymt_disp_txt1.setAutoDraw(True)

    # *pymt_disp_txt2* updates
    if t >= 0.0 and pymt_disp_txt2.status == NOT_STARTED:
        # keep track of start time/frame for later
        pymt_disp_txt2.tStart = t  # underestimates by a little under one frame
        pymt_disp_txt2.frameNStart = frameN  # exact frame index
        pymt_disp_txt2.setAutoDraw(True)

    # *key_resp_pymt_disp* updates
    if t >= 2.0 and key_resp_pymt_disp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_pymt_disp.tStart = t  # underestimates by a little under one frame
        key_resp_pymt_disp.frameNStart = frameN  # exact frame index
        key_resp_pymt_disp.status = STARTED
        # keyboard checking is just starting
        key_resp_pymt_disp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_pymt_disp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_pymt_disp.keys = theseKeys[-1]  # just the last key pressed
            key_resp_pymt_disp.rt = key_resp_pymt_disp.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pymt_dispComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "pymt_disp"-------
for thisComponent in pymt_dispComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_pymt_disp.keys in ['', [], None]:  # No response was made
    key_resp_pymt_disp.keys=None


thisExp.nextEntry()
win.close()
core.quit()

################### Ending BDM Auction ###################################
