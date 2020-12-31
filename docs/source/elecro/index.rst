ELEcro
==========================================

.. _my_elecro:

ELEcro is a simple tool for viewing electrophysiological data. We created this tool to analyze data from our `TMSi polygraphy equipment <https://www.tmsi.com/?id=4>`_. ELEcro can read and write data in TMS32 (.S00), EDF (.EDF) and BrainVision Analyzer file formats (.VHDR). The strength and weakness of this software is its simplicity. It is very fast, but only has the features that we routinely need for our study.

.. image:: elecro.png
   :width: 70%
   :align: center

Getting started
-------------------------------------------


 -  Simply launch ELEcro and use the File/Open command to open your data. You can use the menus and time slider to view your data. There are also a couple of shortcuts:

 - Mouse scroll wheel: increases or decreases the vertical scale.
 - Up/Down arrows: increases or decreases the vertical scale.
 - Left/Right arrows: scrolls the time period.
 - Ctrl-H/Ctrl-Alt-H: increases or decreases the horizontal scale.
 - Home/End: go to first or last samples
 - Mouse right-click plus dragging: pans the viewing window.
 - Moving the mouse over the image generates text on the left side of the image showing the time sample and signal levels at the location selected.

Acquiring data
-------------------------------------------


 -  You will want to use your polygraph hardware to collect data. ELEcro imports EDF, TMS32 and BrainVision Analyzer format data. If your hardware does not support these formats, you can often translate formats using the `Biosig toolbox for Matlab/Octave <http://biosig.sourceforge.net>`_ . Alternatively, if you have TMSi hardware, you can try our own :ref:`EMG recorder <my_emg_recorder>` to acquire data – this will save data as either TMS32 or BrainVision format.

Analyzing data
-------------------------------------------


 -  Modern wireless polygraphic systems allow great mobility, and safety when using other devices (such as transcranial magnetic stimulation). However, it is possible for some of the signals to be dropped, due to radio frequency noise or the computer processing other tasks. For this reason, the TMSi Mobi system generates a ‘Saw’ signal (an additional simulated channel that shows a saw-shaped signal). ELEcro allows you to observe this Saw channel, and future versions will provide a tool to interpolate across these samples.

A common first step for analyzing electrophysiological data is to apply `temporal filters <https://en.wikipedia.org/wiki/Electronic_filter>`_ . Polygraphic data often has noise from the environment, particularly for mobile units. For example, the alternating current in a buildings wires can cause noise (50-60 Hz depending on your country). The signals also have low frequency drift as the electrode contact changes, as well as high frequency noise. A high-pass filter will remove low-frequencies, whereas a low-pass filter eliminates the high-frequency information. The next paragraphs ELEcro’s temporal filtering options.

Choose “Low Pass Filter” from the “Tools” menu to apply a Butterworth 4th order low pass filter. You will be asked to specify the frequency limit for you want to use. Note that the filter has considerable roll-off, so if you have sharp 50 Hz noise and want to eliminate this noise and all lower frequencies, try a high pass filter with ~60 Hz (the Tools/GenerateSineWaves command can be applied before a temporal filter to gauge this roll-off). ELEcro will only apply the filter to the physical electrodes, the trigger and saw signals will not be altered. This filter is run in both directions to prevent temporal bias. The pictures on this web page show how the filter can selectively remove frequencies (simulated data).

The Tool’s menu “Filter…” allows you to design one of the filters described by `Robert Bristow-Johnson <https://webaudio.github.io/Audio-EQ-Cookbook/Audio-EQ-Cookbook.txt>`_ . A window allows your to specify several features of your filter:

 - Type: This specifies the kind of filter to apply. Your options are Low Pass, High Pass, Band Pass CSG, Band Pass CZPG, Notch, All Pass, Peaking, Low Shelf and High Shelf. A `low pass filter <https://en.wikipedia.org/wiki/Low-pass_filter>`_  attenuates signals above the target frequency, a `high-pass filter <https://en.wikipedia.org/wiki/High-pass_filter>`_  dampens signals below the target, `band pass filters <https://en.wikipedia.org/wiki/Band-pass_filter>`_  dampen all frequencies except those near the target, an `all pass filter <https://en.wikipedia.org/wiki/All-pass_filter>`_  amplifies or dampens all frequencies evenly (though it influences phase), a  peak filter preserves all frequencies but amplifies those near the target frequency, shelf filters  preserve all frequencies, but somewhat increases or decreases frequencies below (low shelf or above (high shelf) the target frequency.
 - Hz: Specify target frequency. Center Frequency or Corner Frequency, or shelf midpoint frequency, depending on filter type.
 - Gain dB: Used only for peaking and shelving filters. These filters pass all frequencies, but will increase or decrease the intensity of the target frequencies by this amount.
 - Q: By default, this value specifies the `Quality factor <https://en.wikipedia.org/wiki/Q_factor>`_ , tuning the selectivity of the filter. However, if “Q is bandwidth” is checked, this value sets the bandwidth in octaves.
 - Q is bandwidth: See above.
 - Filter both forward and reverse: Many filters cause shift signals such that they appear to occur later in time. Running the filters in both directions minimizes this effect.

Clinicians often link their Electromyography (EMG) systems into audio amplifiers. Human auditory perception has great temporal resolution, and clinicians can often hear subtle differences in EMG recordings that are hard to detect by examining a visual plot. To the uninitiated, EMG sounds like rain hitting a metal roof, but these sounds are often important for medical diagnosis. Therefore, the Tools menu for the Windows version of ELEcro includes the ‘Audio’ command, that allows you to listen to a segment of your EMG recording.

Averaging across events
-------------------------------------------

Event files tell the software when different stimuli were presented to the participant. This allows us to generate average waveforms to see what signals are consistent following events. There are actually three steps to averaging the data. First, we need to open or create a new event file that logs the onset and type of each event. Second, we want to visually inspect these events to ensure that each event was a clean recording. Third, we want to create averages for each event type for each channel.

First we need to open or generate an events file. ELEcro can read and write BrainVision VMRK files – these files mark the time and type of events that occur. Choose Events/Open to open an existing file. If you want to generate a new event file, first choose File/Open to open the phsyiological data and then Events/New to specify the settings for detecting events. We typically want to average from multiple conditions, for example looking at hand movements following weak versus strong pulses of brain stimulation. The TMSi Mobi includes a optical trigger for recording this data, but this only generates a binary signal (on or off), which makes it difficult to distinguish between interleaved events of multiple conditions. To deal with this, you can vary the length of your optical triggers during recording, with the duration of the trigger pulse specifying the condition type. After collecting the data, ELEcro can parse the events based on the stimulus duration. This explains why the Events/New settings window is slightly complicated:

 - Trigger channel: which channel is used as the trigger signal. Typically, TMSi computers have a binary channel named ‘digi’, but you could also use one of the analog channels.
 - Threshold: A trigger is counted whenever the input exceeds this integer value. Values larger than zero are easy to understand (e.g. 7 means that any time the signal increases such that it exceeds 7 a trigger event will be generated). The value zero is used for a threshold of 0.5 (useful for binary signals that cycle between zero and one), whereas negative values are for power(10,n), e.g. -2 is 0.01.
 - Pulse width threshold (ms): this is used if different conditions are specified by different trigger durations. For example, if one condition uses a 5ms pulse, and the other uses 15ms, the value 10 will optimally discriminate these values.
 - Ignore start/end (ms). We typically discrad any events that occur near the start or end of the recording. In particular, the first events will be contaminated by our temporal filtering. The final events will also be contaminated if we ran the filter in both forward and reverse directions.

Visually inspecting event files is easy with ELEcro. When you open a VMRK file, a panel appears at the bottom of ELEcro that allows you to navigate through the events. In the figure above, we are seeing the 12th of 203 events, which was of type “Stimulus” and with the description “Cond1” – the onset of this event was the 123427th sample and it lasted 100 samples. A gray box on the graph shows the onset of this event. You can use the &lt; and &gt; buttons to proceed to the previous and next event, and the – button to delete this event (for example if there was an artifact and you do not want to include this event in the analysis).

The standard steps for generating an average are as follows:


 - Use File/Open to open your physiological data.
 - Use Events/Open to open your Events file (this will happen automatically if there is a VMRK file with the same name as your physiological data).
 - Visually inspect the events to exclude unusual trials (you can use Events/Save to save the inspected event file).
 - Choose Events/Average to choose the settings for your average:
 - Start (ms): specify the onset time of the averaging relative to the trigger singal. For example, if you choose -15, then the averaged file will commence 15ms prior to the trigger signal.
 - Duration (ms): specifies the number of time bins averaged. For example, if you chose a start of -15 and a Duration of 100, the average file will include samples from -15 to 85ms relative to the trigger signal.
 - Rectify: The absolute value for each sample will be used. This is only useful for bipolar EMG data.


The figure shows averaging using the defaults settings applied to the simulated data ELEcro creates when it starts (and shown in the other images). Note that channel C4 has two digital triggers, which both occur at 10 Hz (just like the slowest signal), but are out of phase with each other. After averaging, there are 50-51 (‘_51’) trials averaged for each condition, and the fundamental frequencies are clear, with the phase shift clear for our two triggers (though channels C1 and C2 would have looked cleaner if we ran a 25-Hz low pass filter first to remove noise not in phase with our triggers).



Computing statistics
-------------------------------------------


 -  Once you have filtered and averaged your data, you can export the files for analysis with Excel, Open office, or your favorite statistics package. The File/Export command saves the data as tab-delimited text. Note that this software follows electrophsyiological convention of using the dot instead of the comma as a decimal separator (e.g. writing 7.2 instead of 7,2). The software that imports your data should be set up for this format (often you can adjust the Regional settings in your control panel).



Example analysis
-------------------------------------------


 -  Below the steps are described for analyzing the subj001 dataset available from the download section. In this study a TMS pulse was applied to the motor cortex every 5 seconds, creating a motor evoked potential. The participant received concurrent tDCS, and the study was designed to see if the tDCS influenced the size of the TMS-induced MEP. While the file ‘subj001wm.vmrk’ lists the tDCS with respect to the TMS pulses, the timing in this file is not exact. However, an optical trigger signal was sent to the EMG systems concurrent with each pulse. Here is how to analyze this data:


 -  **Creating an event file** 

 - Launch ELEcro and use File/Open to display the file ‘subj001.vhdr’
 - Use Events/Open to display the events from ‘subj001wm.vmrk’
 - A new toolbar appears at the bottom of the display, allowing you to navigate between the 284 events using the ‘&lt;' and '&gt;‘ buttons.
 - Note that the events do not precisely map onto the optical triggers shown in on the channel ‘Ch7’ – the sampling rate of the EEG system was slightly out of sync with the clock. Due to this, we need to create a new event file with correct timings.
 - Choose Events/New. Set the ‘Channel’ to be ‘2’ (you will see [Ch7] displayed). Set the threshold to ‘0’ (The window will say ‘Threshold 0.5’), set pulse width to 10, and ignore and triggers in the first and last ‘500’ ms. This means that the software will identify the timings where a trigger signal was detected on Channel 7. Visual inspection shows that this channel records the timing of the TMS stimulation. Press ‘OK’ – the software will report identifying 284 events, with onset times from 2.7..1423 seconds into the recording.
 - Save this new file, e.g. ‘subj001trig.vmrk’
 - Use Events/Open to view the new trigger file. Note that there are 284 events that are time-locked to the trigger signal seen on Channel 7.
 - Unfortunately, for this example the file ‘subj001wm.vmrk’ has the correct conditions (e.g. tDCS stimulation during TMS pulse) but the wrong timing, whereas the file ‘subj001trig.vmrk’ is time-locked, but does not correctly code the conditions. Because this is the case, we need to merge these two files….
 - Select Events/MergeTwoEventFiles – You will be asked to select the event file with the accurate timing (subj001trig.vmrk) and then asked to select the event file with the accurate condition labels (subj001wm.vmrk). Save the merged file with a sensible name.
 - Use Events/Open to browse your events file. Note that the 284 events now have the accurate condition label and are time-locked to the stimulus onset.
 - As you navigate through the events, you will notice that there are a total of 40 conditions. (Cond001..Cond040). In this example, there are only a few trials of the same condition, and we may want to collapse our data so that similar conditions are averaged together. This will give us a more stable idea of what is going on. In our example, conditions (Cond001..Cond004) are sham, followed by six trials of anodal stimulation (Cond005..Cond010), four sham trials, six anodal trials, four sham trials, six cathodal trials, four sham trials and six cathodal trials. To collapse across these conditions do the following:
 - Choose Events/CollapseConditions. You will be asked to give your desired new labels. For this example enter ‘1S,1S,1S,1S,2A,2A,2A,2A,2A,2A,3S,3S,3S,3S,4A,4A,4A,4A,4A,4A,5S,5S,5S,5S,6C,6C,6C,6C,6C,6C,7S,7S,7S,7S,8C,8C,8C,8C,8C,8C’ Note that our 40 original conditions will be remapped to only 8 conditions. You will be asked to create a new file, give this a sensible name, e.g. ‘subj001collapsed.vmrk’. Note that a text file will also be created (subj001collapsed.txt) it is worth checking this to make sure the collapsing was done accurately (in particular, the conditions are source conditions are sorted alphabetically, so ‘Cond21’ will be sorted before ‘Cond3’, whereas ‘Cond003’ would be sorted before ‘Cond021’). When you view this text file, you will see the mapping used, e.g. ‘Cond006 -&gt; 2A’.

**Analyzing data** 

 - Launch ELEcro and use File/Open to display the file ‘subj001.vhdr’.
 - Select Events/Open to select the event file you want to process (from our previous example this might be ‘subj001.vmrk’ or ‘subj001collapsed.vmrk’).
 - Choose Tools/Filter to apply spatial filters – you can do this multiple times to apply several filters. A standard analysis for EMG might be a 20Hz High Pass Filter. This filter will have the benefit of bringing the signal for each channel to a baseline near 0mv.
 - Use the View/VerticalScale and View/Horizontal scale to show your signal nicely (you can also use the scroll whell on your mouse for this).
 - You may want to use the ‘&gt;’ and ‘&lt;' buttons at the bottom of the image to manually inspect each event. If the data looks bad you can press the '-' button to delete that event. If you do delete any events, you may want to choose Events/Save to save your new file.
 - Choose Events/Average to export your data for analysis. In our example we will want to average data from 15ms after the trigger to 50ms after (typical TMS MEP latency). You will be aksed to name an output tab-delimited text file (e.g. ‘results.tab’).
 - ELEcro will now show you the average wave form for each condition at each channel.
 - You can open the text file (e.g. results.tab) with a spreadsheet like Excel or OpenOffice. At the top you will the events sorted by condition and then trial number, with the minimum, maximum, range (max-min) and onset time for each event. After this you will see the peak-to-peak mean, median, etc for each condition. Finally, you will be shown the mean waveform for each condition at each channel.



Downloads
-------------------------------------------

<TODO> At the bottom of the page you will find attachments for Version 12/2012 and sample datasets:

 - ELEcro for Windows
 - ELEcro for macOS (Intel)
 - ELEcro for Linux (Intel 32-bit, GTK2)
 - ELEcro for Linux (Intel 64-bit, GTK2)
 - ELEcro source code (for either Delphi or Lazarus)
 - Sample data (TMS32 Poly5 format)
 - Sample data (EDF format)
 - Sample data (BrainVision analyzer format)
 - Sample data subj001.eeg for tutorial described above (BrainVision analyzer format)

Links
-------------------------------------------

 - `EDFbrowser <https://www.teuniz.net/edfbrowser/>`_  is an elegant free tool for viewing EDF, EDF+ and BDF format electrophysiological data. It includes many powerful features, and is much more powerful than ELEcro. Further, the current version of ELEcro assumes your EDF data is pretty simple (like generated with TMSi hardware), whereas EDFbrowser can read much more complicated data (for example, with annotation or with channels that have different sampling rates).
 - Some code is based on Michael Vinther’s `EEG Analyzer <https://logicnet.dk/reports/>`_ . His free software has many powerful features.
 - The Butterworth filter was adapted by `Jean-Pierre Moreau <http://jean-pierre.moreau.pagesperso-orange.fr/pascal.html>`_ 
 - :ref:`EMG recorder <my_emg_recorder>` is a simple tool for collecting EMG data that can subsequently by analyzed with ELEcro.
 - My :ref:`Temporal Filters web page <my_temporal>`  is an interactive demonstration of the high pass, low pass and notch filters available in ELEcro.
 - The Twente Medical Systems International `Mobi <https://www.tmsi.com/?id=5>`_ is the EMG system we use. This battery powered unit is able to communicate wirelessly (using bluetooth) or it can simply record data to a standard SD flash memory card.
 - Here are details for the `European Data Format <https://www.edfplus.info/specs/index.html>`_  (EDF and EDF+).
 - The open source `EEGLAB <https://sccn.ucsd.edu/eeglab/index.php>`_  matlab scripts are popular for analyzing electrophysiological data.
