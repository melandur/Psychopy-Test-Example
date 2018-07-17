#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:     Michael Müller
Date:       17/07/2018
Version:    1.0
"""
# import
from __future__ import division
import os
import pandas as pd
from psychopy.iohub import launchHubServer
from psychopy.constants import *
from psychopy import visual, core, data, event, logging, gui


class Psychopy_Example:

    def gui(self, test):
        # get path location of python file
        self.thisDir = os.getcwd()
        os.chdir(self.thisDir)

        # store info about the experiment session
        self.expName = test
        self.expInfo = {u'session': u'001', u'participant': u''}
        dlg = gui.DlgFromDict(dictionary=self.expInfo, title=self.expName)
        if dlg.OK == False: core.quit()
        self.expInfo['date'] = data.getDateStr()
        self.expInfo['expName'] = self.expName

        self.filename = '%s_%s_%s' % (self.expInfo['participant'], self.expName, self.expInfo['date'])

        # setub folder structure for file saving
        if not os.path.exists(str(self.thisDir) + '\\data\\' + self.filename):
            os.makedirs(str(self.thisDir) + '\\data\\' + self.filename)


        # save a log file for detail verbose info
        self.logFile = logging.LogFile(str(self.thisDir) + '\\data\\' + self.filename + '\\' + self.filename + '.log', level=logging.EXP)
        logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

        self.endExpNow = False  # flag for 'escape' or other condition => quit the exp

        # setup the Window
        self.win = visual.Window(size=(1280, 1024),
                            fullscr=True,
                            screen=0,
                            allowGUI=False,
                            allowStencil=False,
                            monitor='testMonitor',
                            color=[-1, -1, -1],
                            colorSpace='rgb',
                            blendMode='avg',
                            useFBO=True,
                            )

        # store frame rate of monitor if we can measure it successfully
        self.expInfo['frameRate'] = self.win.getActualFrameRate()
        if self.expInfo['frameRate'] != None:
            self.frameDur = 1.0 / round(self.expInfo['frameRate'])
        else:
            self.frameDur = 1.0 / 60.0  # couldn't get a reliable measure so guess


    def iohubserver(self):
        # init the iohub process
        self.io = launchHubServer()
        self.kb_device = self.io.devices.keyboard


    def clock(self):
        # crate timers
        self.globalClock = core.Clock()  # to track the time since experiment started
        self.routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


    def text_slide(self, text):
        # initialize components for text slide
        text = visual.TextStim(win=self.win, ori=0, name='text',
                               text=text,
                               font='Arial',
                               pos=[0, 0], height=0.1, wrapWidth=None,
                               color='white', colorSpace='rgb', opacity=1,
                               depth=0.0)

        slideclock = core.Clock()
        # ------Prepare to start Routine "Instruction"-------
        self.t = 0
        slideclock.reset()  # clock
        frameN = 0
        # update component parameters for each repeat
        key_resp_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_1.status = NOT_STARTED
        # keep track of which components have finished
        InstructionComponents = []
        InstructionComponents.append(text)
        InstructionComponents.append(key_resp_1)
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "Instruction"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            self.t = slideclock.getTime()
            # update/draw components on each frame

            # *text* updates
            if self.t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = self.t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)

            # *key_resp_3* updates
            if self.t >= 0.0 and key_resp_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_1.tStart = self.t  # underestimates by a little under one frame
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.status = STARTED
                # keyboard checking is just starting
            if key_resp_1.status == STARTED:
                theseKeys = event.getKeys()

                # check for quit:
                if "escape" in theseKeys:
                    self.endExpNow = True
                if "return" in theseKeys:
                    continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                slideclock.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if self.endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                self.win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                self.slideclock.reset()

            frameN = frameN + 1

        # -------Ending Routine "Instruction"-------
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


    def image_trial(self, time_box):
        # ------Prepare to start Routine "trial"-------
        # initialize components for Routine "trial"
        trialClock = core.Clock()
        self.image = visual.ImageStim(win=self.win, image='trial_ressources/thunder.png')

        # some image configurations
        # self.image.setPos()
        self.image.setSize([0.5, 1.1])
        # self.image.setOri()

        # set textbox for time
        self.counter = visual.TextStim(win=self.win, ori=0, name='counter',
                                 text=u"", font='Arial',
                                 pos=[-0.9, -0.9], height=0.1, wrapWidth=None,
                                 color='white', colorSpace='rgb', opacity=1,
                                 depth=0.0)

        self.t = 0
        trialClock.reset()  # clock
        frameN = 0
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED

        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(self.image)
        trialComponents.append(key_resp_2)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # When you need to clear old keyboard events / (re)-start getting the key release durations
        self.kb_device.clearEvents()

        # *** Andrey: keyboard timing (tria #1) ***
        self.kb_presses_duration = list()  # A list of key press duration values
        self.kb_release_times = list()  # A list of key release time values
        self.kb_press_times = list()  # A list of key press time values
        self.kb_char = list()

        time_diff = core.getTime() - trialClock.getTime()  # Time difference between experiment start and trial start
        self.io.clearEvents("all")

        # -------Start Routine "trial"-----a--
        continueRoutine = True
        press_key, release_key, press_duration, key_char = "", "", "", ""
        timeout = 5

        while continueRoutine:
            # get current time
            self.t = trialClock.getTime()

            # update/draw components on each frame
            # *text* updates
            if self.t >= 0.0 and self.image.status == NOT_STARTED:
                # keep track of start time/frame for later
                self.image.tStart = self.t  # underestimates by a little under one frame
                self.image.frameNStart = frameN  # exact frame index
                self.image.setAutoDraw(True)

            # *key_resp_2* updates
            if self.t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = self.t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0

            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                # check for quit:
                if "escape" in theseKeys:
                    self.endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys.extend(theseKeys)
                    key_resp_2.rt.append(key_resp_2.clock.getTime())

            # get pressing and char of key
            for ke in self.kb_device.getPresses():
                self.kb_press_times.append(ke.time - time_diff)
                press_key = round(ke.time - time_diff, 3)
                key_char = event.getKeys()
                self.kb_char.append(key_char)

            # get release and duration of key pressing
            for ke1 in self.kb_device.getReleases():
                self.kb_presses_duration.append(ke1.duration)
                self.kb_release_times.append(ke1.time - time_diff)
                release_key = round(ke1.time - time_diff, 3)
                press_duration = round(ke1.duration, 3)
                print("Press:[{ktime}], Release:[{ktime1}], Duration:[{kduration}], Char:{char}"
                      .format(ktime=press_key, ktime1=release_key, kduration=press_duration, char=key_char))

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                self.routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            if time_box:
                self.counter.setText(text=str(round(timeout - trialClock.getTime(), 2)))
                self.counter.setAutoDraw(True)

            # check for quit (the Esc key)
            if self.endExpNow or event.getKeys(keyList=["escape"]):
                self.io.quit()
                core.quit()

            if trialClock.getTime() >= timeout:
                break

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                self.win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                self.routineTimer.reset()

            frameN += 1

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                if time_box:
                    self.counter.setAutoDraw(False)


    def export_excel(self):
        # get shortest length of list
        shortest_length = min(len(self.kb_press_times),
                              len(self.kb_release_times),
                              len(self.kb_presses_duration),
                              len(self.kb_char))

        # resize all lists to the same size
        self.kb_press_times = self.kb_press_times[-shortest_length:]
        self.kb_release_times = self.kb_release_times[-shortest_length:]
        self.kb_presses_duration = self.kb_presses_duration[-shortest_length:]
        self.kb_char = self.kb_char[-shortest_length:]

        # export key events as column
        df = pd.DataFrame(
            {'Press_key': self.kb_press_times,
             'Release_Key': self.kb_release_times,
             'Duration': self.kb_presses_duration,
             'Char': self.kb_char
             })
        # create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(str(self.thisDir) + '\\data\\' + self.filename + '\\' + str(self.filename) + '.xlsx', engine='xlsxwriter')

        # convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet1')

        # close the Pandas Excel writer and output the Excel file.
        writer.save()


    def end(self):
        # kill all
        self.win.close()
        core.quit()


if __name__ == '__main__':

    # assign class
    c = Psychopy_Example()

    # start experiment gui
    c.gui(test='Your_Test_Name')

    # start io hub server
    c.iohubserver()

    # start timers
    c.clock()

    # show first text slide
    c.text_slide(text='Please press any key if you notice something in the following image \n(Start with "Enter")')

    # start image trial
    c.image_trial(time_box=True)

    # show second slide
    c.text_slide(text='Congrats you have survived ;-) \nPlease contact the Staff')

    # export data of trial
    c.export_excel()

    # close window and quit core
    c.end()

