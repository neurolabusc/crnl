Image to Inference (PSYC589/888)
==========================================

.. image:: teach.jpg
   :width: 25%
   :align: center

Details:
   
 - Course Title: “Neuroimaging: from image to inference”.
 - Instructor: Chris Rorden : Office 227 Discovery I (John Absher will provide clinical lectures)
 - Course Code: (Undergrad) PSYC 589(Grad) PSYC 888,3 credits. In addition, scientists are free to audit this course. Suitable for faculty, post-docs, PhD students and advanced undergraduate students.
 - When: Spring 20211:15-2:30 T/Th, Jan 12-Apr 22
 - Where:Hamilton 238 and Virtual Instruction
 -  `Syllabus <https://www.mccauslandcenter.sc.edu/crnl/sites/sc.edu.crnl/files/attachments/Spring2019_Syl_PSYC%20589_888.pdf>`_ 
 - Course slides: `PPT Powerpoint Format. <http://people.cas.sc.edu/rorden/teaching/589.ppt>`_ also available as `Google Slides <https://docs.google.com/presentation/d/1olEutlOWRjtkofv8uiaM0bJ-ImJ104IHvnphcyySVNk/edit#slide=id.g4bab18663f_2_66>`_
 - License: `the slides and material for this course are distributed under the Creative Commons license <http://creativecommons.org/licenses/by/3.0/>`_ . Further details are in the notes section of the PowerPoint file.
 - Textbook: `Functional Magnetic Resonance Imaging by Huettel, Song, and McCarthy <http://www.amazon.com/Functional-Magnetic-Resonance-Imaging-Second/dp/0878932860/>`_ .
 - Supplemental textbook: `Poldrack et al. <http://www.amazon.com/Handbook-Functional-MRI-Data-Analysis/dp/0521517664/ref=sr_1_1?ie=UTF8&amp;qid=1345812543&amp;sr=8-1&amp;keywords=poldrack"/>`_.
 - Description: Functional magnetic resonance imaging is a recent and powerful tool for inferring brain function. This technique identifies brain regions that are activated by different tasks – for example we can find the brain regions that activate when someone sees a familiar face. This course is designed to give students an understanding of the potential and limitations of this technique, and the ability to critically evaluate the inferences that can be drawn from fMRI. The course describes all stages of an fMRI study – from the design of the behavioral task (e.g. asking the participant to view faces), to the image processing (e.g. correcting images for head movements that occurred during scanning), through to statistical analysis (identifying brain regions that are activated by a task).



Lectures
-------------------------------------------

- Overview.
 
	- The classroom is a computer lab, so all assignments can be completed in the lab. Optionally, FSL and MRIcron on a computer. MRIcron runs on Linux, Windows and OSX. Individuals with OSX and Linux computers can install FSL natively, or students can use the provided DVD to run a NeuroDebian VirtualBox, with `instructions here <http://neuro.debian.net/vm.html>`_ . A final option is to install `FSL on Windows Subsystem For Linux <http://www.nemotos.net/?p=1481">`_.
	- The first homework assignment requires you to mark landmarks on a MRI scan, you can find these landmarks using my `Neuroanatomy Atlas <http://people.cas.sc.edu/rorden/anatomy/home.html>`_ 

- MRI physics: Image Acquisition.

	- `Terrific videos <http://www.magritek.com/support/videos/>`_ (from a company that makes a unique instructional MRI system.

- MRI physics: Image Contrast.

	- The  `virtual MR <https://sourceforge.net/projects/vmri/files/Virtual%20MR%20scanner/Virtual%20MR%20Scanner%203.2.14/>`_  `virtual MRI <http://www.iftm.de/elearning/vmri/idx_download.htm>`_ program allows you to interactively adjust MRI parameters and see the results.
	- `Graphs (and Matlab scripts) <http://www.mccauslandcenter.sc.edu/crnl/teaching/mri>`_ for basic MRI contrast effects.

- fMRI Paradigm Design.

	-  `My fMRI simulator allows you to explore the hemodynamic changes induced by different tasks. <http://www.mccauslandcenter.sc.edu/crnl/tools/fmristim>`_ 

- Statistics and Thresholding.

- Spatial Processing I: Spatial Registration – realignment (motion correction), coregistration, normalization; Spatial interpolation – linear, spline, sinc functions

	-  `Spatial Processing Demos <http://www.mccauslandcenter.sc.edu/crnl/tools/spatial/>`_ 

- Spatial Processing Continued II: Smoothing – filters, edge detection, gaussian blur, homogeneity correction (for EPI and anatomical scans), motion related intensity changes.

	-  `Undistorting fMRI EPI data using the SPM FieldMap toolbox <http://www.mccauslandcenter.sc.edu/crnl/tools/fieldmap/>`_ 

- Temporal Processing

	-  `Interactive filtering demo <http://www.mccauslandcenter.sc.edu/crnl/tools/temporal/>`_ shows how low-pass, high-pass and notch filters modulate a signal.
	-  `Physiological Artifact Removal Tool <http://www.mccauslandcenter.sc.edu/crnl/tools/part/>`_ 

- FSL and SPM. Hands on demonstrations

	-  `fMRI analysis <http://people.cas.sc.edu/rorden/tutorial/index.html>`_ 
	-  `FSL: block design <http://people.cas.sc.edu/rorden/tutorial/html/block.html>`_ 
	-  `FSL: event-related design <http://people.cas.sc.edu/rorden/tutorial/html/event.html>`_ 
	-  `SPM: block design <http://people.cas.sc.edu/rorden/tutorial/html/blockspm.html>`_ 
	-  `Automated analysis with SPM (same data as block design tutorial) <http://www.mccauslandcenter.sc.edu/crnl/tools/spm-script>`_

- Detecting subtle changes in brain structure: Voxel Based Morphometry and Diffusion Tensor Imaging.

	- `John Ashburner's VBM class (PDF) <http://www.fil.ion.ucl.ac.uk/~john/misc/VBMclass10.pdf>`_
	- `DTI tutorial <http://people.cas.sc.edu/rorden/tutorial/html/dti.html>`_ 
	- `Advanced DTI tutorial <http://www.mccauslandcenter.sc.edu/crnl/tools/advanced-dti>`_ 

 - Brain injury and neuroimaging. Measuring blood flow and using lesion symptom mapping to understand the consequences of stroke and other neurological disorders.
 - Arterial Spin Labeling see :ref:`myASL`.
 - Contrast-enhanced (Gadolinium) Perfusion Weighted Imaging  see :ref:`myPWI`.
 - `VLSM using my NPM software <http://people.cas.sc.edu/rorden/mricron/stats.html>`_ 

- Brain stimulation: Transcranial Magnetic Stimulation (TMS), Transcranial Direct Current Stimulation (tDCS). Roger Newman-Norlund and Chris Rorden
 
- Student presentations: Resting state analysis, effective and functional connectivity, independent components analysis, neural current MRI?



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



Relevant Links:
-------------------------------------------

 -  `Online MRI course <http://www.imaios.com/en/e-Courses/e-MRI>`_ 
 -  `SPM statistics <http://www.mrc-cbu.cam.ac.uk/Imaging/Common/tutorials.shtml>`_ 
 -  `Rik Henson’s fMRI mini-course <http://imaging.mrc-cbu.cam.ac.uk/imaging/SpmMiniCourse2008>`_ 
 -  `Rik Henson’s tips for fMRI design <http://www.mrc-cbu.cam.ac.uk/Imaging/Common/fMRI-efficiency.shtml>`_ 
 -  `Duke BIAC Grad Course <http://www.biac.duke.edu/education/courses/fall08/fmri/>`_ 
 -  `SPM course <http://www.fil.ion.ucl.ac.uk/spm/course/>`_ , and the `SPM8 manual <http://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf>`_ 
 -  `NeuroDebian <http://neuro.debian.net/vm.html>`_ virtual machine is a great way for students to try out neuroimaging tools.
 -  `Lin4Neuro <http://sourceforge.net/projects/lin4neuro/>`_ is an open source Linux distribution that comes with many of the most popular free MRI tools (FSL, MRIcron, etc) already installed. Simply burn a CD and reboot your computer. Release notes and other details are `here <http://www.nemotos.net/lin4neuro/>`_ . Kiyotaka Nemoto has graciously included the sample dataset from this course and the tutorial web pages, making it a perfect package for teaching brain imaging (as all the students have the datasets preloaded and in the same folders). For details, read the `Lin4Neuro Article inBMC Medical Imaging <http://www.biomedcentral.com/1471-2342/11/3>`_ article.
