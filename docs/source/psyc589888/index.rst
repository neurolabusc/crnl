Image to Inference (PSYC589/888)
==========================================

.. _my_psyc589888:

.. image:: teach.jpg
   :width: 25%
   :align: center

Details:
   
 - Course Title: “Neuroimaging: from image to inference”.
 - Instructor: Chris Rorden : Office 227 Discovery I (John Absher will provide clinical lectures)
 - Course Code: (Undergrad) PSYC 589(Grad) PSYC 888,3 credits. In addition, scientists are free to audit this course. Suitable for faculty, post-docs, PhD students and advanced undergraduate students.
 - When: Spring 2021 1:15-2:30 T/Th, Jan 12-Apr 22
 - Where:Hamilton 238 and Virtual Instruction
 - Formal `Syllabus <https://drive.google.com/file/d/1HrzRlMt1iHVNIbzatMs8DpBRKdBItuGQ/view?usp=sharing>`_
 - Course slides: `Google Slides format <https://docs.google.com/presentation/d/1olEutlOWRjtkofv8uiaM0bJ-ImJ104IHvnphcyySVNk/edit>`_
 - License: `the slides and material for this course are distributed under the Creative Commons license <https://creativecommons.org/licenses/by/3.0/>`_ . Further details are in the notes section of the PowerPoint file.
 - Textbook: `Functional Magnetic Resonance Imaging by Huettel, Song, and McCarthy <https://www.amazon.com/Functional-Magnetic-Resonance-Imaging-Second/dp/0878932860/>`_ .
 - Supplemental textbook: `Poldrack et al. <https://www.amazon.com/Handbook-Functional-MRI-Data-Analysis/dp/0521517664/ref=sr_1_1?ie=UTF8&amp;qid=1345812543&amp;sr=8-1&amp;keywords=poldrack"/>`_.
 - Description: Functional magnetic resonance imaging is a recent and powerful tool for inferring brain function. This technique identifies brain regions that are activated by different tasks – for example we can find the brain regions that activate when someone sees a familiar face. This course is designed to give students an understanding of the potential and limitations of this technique, and the ability to critically evaluate the inferences that can be drawn from fMRI. The course describes all stages of an fMRI study – from the design of the behavioral task (e.g. asking the participant to view faces), to the image processing (e.g. correcting images for head movements that occurred during scanning), through to statistical analysis (identifying brain regions that are activated by a task).

Lectures
-------------------------------------------

- Overview.
 
	- The classroom is a computer lab, so all assignments can be completed in the lab. Optionally, FSL and MRIcron on a computer. MRIcron runs on Linux, Windows and macOS. Individuals with macOS and Linux computers can install FSL natively, or students can use the provided DVD to run a NeuroDebian VirtualBox, with `instructions here <https://neuro.debian.net/vm.html>`_ . A final option is to install `FSL on Windows Subsystem For Linux <https://www.nemotos.net/?p=1481">`_.
	- The first homework assignment requires you to mark landmarks on a MRI scan, you can find these landmarks using my `Neuroanatomy Atlas <https://people.cas.sc.edu/rorden/anatomy/home.html>`_ 

- MRI physics: Image Acquisition.

	- `Terrific videos <https://magritek.com/resources/videos/>`_ (from a company that makes a unique instructional MRI system.

- MRI physics: Image Contrast.

	- The `virtual MR <https://sourceforge.net/projects/vmri/files/Virtual%20MR%20scanner/Virtual%20MR%20Scanner%203.2.14/>`_  and `mrilab <https://sourceforge.net/projects/mrilab/>`_ programs allow you to interactively adjust MRI parameters and see the results.
	- `Graphs (and Matlab scripts) <https://github.com/neurolabusc/mri-contrast>`_ for basic MRI contrast effects.

- fMRI Paradigm Design.

	-  My `fMRI simulator <https://github.com/neurolabusc/fMRI-Simulator>`_ allows you to explore the hemodynamic changes induced by different tasks. 

- Statistics and Thresholding.

- Spatial Processing I: Spatial Registration – realignment (motion correction), coregistration, normalization; Spatial interpolation – linear, spline, sinc functions

	- `Spatial Processing Demos <https://github.com/neurolabusc/spatial-processing>`_. 

- Spatial Processing Continued II: Smoothing – filters, edge detection, gaussian blur, homogeneity correction (for EPI and anatomical scans), motion related intensity changes.

	- :ref:`Undistorting fMRI EPI data using the SPM FieldMap toolbox <my_fieldmaps>`. 

- Temporal Processing

	- `Interactive filtering demo <https://github.com/neurolabusc/biquad-filter>`_ shows how low-pass, high-pass and notch filters modulate a signal.
	- `Physiological Artifact Removal Tool <https://github.com/neurolabusc/Part>`_ . 

- FSL and SPM. Hands on demonstrations

	- `fMRI analysis <https://people.cas.sc.edu/rorden/tutorial/index.html>`_.
	- `FSL: block design <https://people.cas.sc.edu/rorden/tutorial/html/block.html>`_. 
	- `FSL: event-related design <https://people.cas.sc.edu/rorden/tutorial/html/event.html>`_. 
	- `SPM: block design <https://people.cas.sc.edu/rorden/tutorial/html/blockspm.html>`_.
	-  :ref:`Automated analysis with SPM (same data as block design tutorial) <my_spm_scripts>`.

- Detecting subtle changes in brain structure: Voxel Based Morphometry and Diffusion Tensor Imaging.

	- `John Ashburner's VBM class (PDF) <https://www.fil.ion.ucl.ac.uk/~john/misc/VBMclass10.pdf>`_.
	- `DTI tutorial <https://people.cas.sc.edu/rorden/tutorial/html/dti.html>`_.
	- :ref:`Advanced DTI tutorial <my_dti>`.

 - Brain injury and neuroimaging. Measuring blood flow and using lesion symptom mapping to understand the consequences of stroke and other neurological disorders.
 - :ref:`Arterial Spin Labeling <my_asl>`.
 - Contrast-enhanced (Gadolinium)  :ref:`Perfusion Weighted Imaging <my_pwi>`.
 - `VLSM using my NPM software <https://people.cas.sc.edu/rorden/mricron/stats.html>`_ 

- Brain stimulation: Transcranial Magnetic Stimulation (TMS), Transcranial Direct Current Stimulation (tDCS). Roger Newman-Norlund and Chris Rorden
 
- Student presentations: Resting state analysis, effective and functional connectivity, independent components analysis, neural current MRI?

Practicals
-------------------------------------------

Practicals will use Amazon Web Services. You will need to install the `Client Application <https://clients.amazonworkspaces.com/>`_. You will receive a user name and password for this system. The material extends the `FSL Training Course <https://fsl.fmrib.ox.ac.uk/fslcourse/>`_ .


- Practical 1 (Thur. Jan. 14, 2021)
	- Download the `Client Application <https://clients.amazonworkspaces.com/>`_
	- Make sure AWS workspace logins work for everyone
	- Getting to know your workspace
	- Terminal (command line) basics
	- Open neuroimaging data with MRIcroGL and FSLeyes
	- Location of images for assignments


- Practical 2 (Thur. Jan. 21, 2021)
  	- slides `here <https://docs.google.com/presentation/d/1y-qssxRlAMeaLBGSSsXG9gzA1_8-M7HUfj-JJ6h69Rc/edit?usp=sharing>`_
  	- Assignment 1 is due soon!
  	- Review drawing and saving images for assignments
  	- Overview of Brain extraction, mathematical operations on brain images, image registration/normalization
  	- Independent student exercises to work through
  	- Assignment 2 is posted


- Practical 3 (Thur. Feb. 4, 2021)
  	- Introduction to the FSL Course material
  	- Work through image registration, unwarping, and transforming image masks
  	- `Lab guide to follow <http://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/registration/index.html>`_
  	- First part of lab is instructor guided
  	- Remaining part of lab is at each student's own pace
  	- These exercises prepare you for the upcoming assignment


- Practical 4 (Thur. Feb. 11, 2021)
  	- Finsih registration, unwarping, and transforming image masks
  	- `Lab guide to follow <http://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/registration/index.html>`_


- Practical 5 (Thur. Feb. 18, 2021)
  	- Start structural analysis (anatomical image segmentation)
  	- `Lab guide to follow <https://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/seg_struc/index.html>`_
	

- Practical 6 (Thur. Mar. 4, 2021)
  	- Start FSL fMRI block design analysis
  	- `Lab guide to follow <https://people.cas.sc.edu/rorden/tutorial/html/block.html>`_
	- `Data to download <https://people.cas.sc.edu/rorden/SW/tutorial/tutorial.zip>`_
	

- Practical 7 (Thur. Mar. 11, 2021)
  	- Finish structural analysis
  	- `Lab guide to follow <https://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/seg_struc/index.html>`_


- Practical 8 (Thur. Mar. 18, 2021)
  	- Single subject fMRI and Featquery
  	- `Lab guide to follow <https://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/feat1/index.html>`_



Assessment and Assignments
-------------------------------------------

The final grade is weighted 30% quizzes, 40% on homework assignments and 30% on the essay. Letter grades assigned as follows A = 90-100%, B = 80-90%, C = 70-80%, D = 60-70%, F = <60%. Graduate students (PSYC888) must also present a research article as a class presentation 45 minute. This presentation is scored as pass or fail that modifies the grade on the essay by x1.0 (pass) or x0.5 (fail), so that a perfect essay (100%) with a failed presentation (x0.5) yields a weighted score of 50%. Material from this article will be included in the quiz, so underdraduates will want to pay careful attention to this presentation. Homework description: Students will submit regular homework assignments, which are due at noon on their due date. Assignments are due in the students' dropbox folder unless otherwise specified. Essay description: Students will write an essay that describes the merits, limitations and potential of a current or potential technique used to infer brain function. Essays should extend beyond the information in the course. Examples include: ERP vs fMRI, MEG, functional connectivity, Independent Component Analysis, Adaptation Designs.

Learning Outcomes
-------------------------------------------

 - Understand the basic elements of neuroimaging.
 - Understand strengths and limitations of complementary tools used in cognitive neuroscience.
 - Ability to evaluate how contemporary methods can be used to understand cognitive functions.
 - Practice software for viewing, preprocessing and statistically analyzing brain imaging data.
 - Practice writing in the form of scientific report that relates behavioral and biomedical constructs.

Attendance
-------------------------------------------

Attendance throughout class is required. By registering for this class you are confirming your availability during class. If you must miss a class, you should talk to the instructor ahead of time. For emergencies (flu, car trouble) it is strongly preferred that you send a text message to the instructor at the time of the class. Failure to meet the 10% rule described in the academic regulations will have homework assignment scores diminished by the proportion of the absences across the term (e.g. missing 15% of classes will mean your final score reflects 85% of your homework score).

Plagiarism
-------------------------------------------

University policy regarding plagiarism, cheating and other forms of academic dishonesty is followed explicitly [See Carolina Community: Student Handbook and Policy Guide, Academic Responsibility]. Any case will be reported to the Dean of the College of Arts and Sciences. A “0” score will be given on a plagiarized assignment, and may result in an “F” for the course in extreme cases.

Disabilities
-------------------------------------------

Students who have disabilities must have certification from the Office of Disability Services and must make clear during the first week of class what accommodations they expect. Students with disabilities must complete the same exams and assignments as other students in order to get course credit.

Links
-------------------------------------------

 - `SPM statistics <https://www.mrc-cbu.cam.ac.uk/Imaging/Common/tutorials.shtml>`_ 
 - `Rik Henson’s fMRI mini-course <https://imaging.mrc-cbu.cam.ac.uk/imaging/SpmMiniCourse>`_ 
 - `Rik Henson’s tips for fMRI design <https://www.mrc-cbu.cam.ac.uk/Imaging/Common/fMRI-efficiency.shtml>`_ 
 - `Duke BIAC Grad Course <https://www.biac.duke.edu/education/courses/fall08/fmri/>`_ 
 - `SPM course <https://www.fil.ion.ucl.ac.uk/spm/course/>`_ , and the `SPM8 manual <https://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf>`_ 
 - `NeuroDebian <https://neuro.debian.net/vm.html>`_ virtual machine is a great way for students to try out neuroimaging tools.
 - `Lin4Neuro <https://www.nemotos.net/lin4neuro/>`_ is an open source Linux distribution that comes with many of the most popular free MRI tools (FSL, MRIcron, etc) already installed.
 
Homework

Assignments added as they are posted:

 - `Assignment 1 <https://drive.google.com/file/d/193ZF0YhVFYCaU2PkRpcQ_613o2cIB6D7/view?usp=sharing>`_
 - `Assignment 2 <https://drive.google.com/file/d/1wIiWZP1vPfVRW1WnHZDCT9hbwM6-HMe_/view?usp=sharing>`_

Calendar
-------------------------------------------

This course follows the `Spring 2021 academic calendar <https://sc.edu/about/offices_and_divisions/registrar/academic_calendars/2020-21_calendar.php>`_ . Classes being

 - Tu 12 Jan
 - Th 14 Jan
 - Tu 19 Jan
 - Th 21 Jan
 - Tu 26 Jan
 - Th 28 Jan
 - Tu 2 Feb
 - Th 4 Feb
 - Tu 9 Feb
 - Th 11 Feb
 - Tu 16 Feb
 - Th 18 Feb
 - Tu 23 Feb
 - Th 25 Feb (Wellness Holiday)
 - Tu 2 Mar
 - Th 4 Mar
 - Tu 16 Mar
 - Th 18 Mar
 - Tu 23 Mar
 - Th 25 Mar
 - Tu 30 Mar (Wellness Holiday)
 - Th 1 Apr
 - Tu 6 Apr
 - Th 8 Apr
 - Tu 13 Apr
 - Th 15 Apr
 - Tu 20 Apr
 - Th 22 Apr
 
