# Image to Inference (PSYC589/88 CRN529948/48893)

![teach](teach.jpg)

### Details:

 - Course Title: “Neuroimaging: from image to inference”.
 - Instructor: [Dr Chris Rorden](https://neurolabusc.github.io/crnl/about/) : Office 138 Discovery I
 - Lab Manager:  [Dr Makayla Gibson](https://neurolabusc.github.io/crnl/about/)
 - Course Code: [PSYC589](https://classes.sc.edu/?details&srcdb=202601&crn=44362) (Undergrad, CRN 44362) [PSYC888](https://classes.sc.edu/?details&srcdb=202601&crn=49444)(Grad, CRN49444) PSYC 888,3 credits. In addition, scientists are free to audit this course. Suitable for faculty, post-docs, PhD students and advanced undergraduate students.
 - When: Spring 2026 T/Th 10:05am-11:20am, 13 Jan - 23 Apr
 - Where: [Discovery I Building](https://sc.edu/visit/map/?id=744#!m/223310?share) Room 259
 - Formal [Syllabus](https://docs.google.com/document/d/1518l1OrFd3vWlJdpydBl-zF1n-uiakhk/edit?usp=sharing&ouid=101539764775409240375&rtpof=true&sd=true)
 - Course slides: [Google Slides](https://docs.google.com/presentation/d/15v3TvxnCAj4wJQm7IWIM6lpEmKUox1Z6DpINysKSmLM/edit?usp=sharing)
 - Supercomputer instances: [neurodeskEDU](https://edu.neurodesk.org)
 - License: [the slides and material for this course are distributed under the Creative Commons license](https://creativecommons.org/licenses/by/3.0/) . Further details are in the notes section of the PowerPoint file.
- Textbook: [Functional Magnetic Resonance Imaging by Huettel, Song, and McCarthy](https://www.amazon.com/Functional-Magnetic-Resonance-Imaging-Second/dp/0878932860/).
- Supplemental textbook: [Poldrack et al.](https://www.amazon.com/Handbook-Functional-MRI-Data-Analysis/dp/0521517664).

### Description:

Functional magnetic resonance imaging is a recent and powerful tool for inferring brain function. This technique identifies brain regions that are activated by different tasks – for example we can find the brain regions that activate when someone sees a familiar face. This course is designed to give students an understanding of the potential and limitations of this technique, and the ability to critically evaluate the inferences that can be drawn from fMRI. The course describes all stages of an fMRI study – from the design of the behavioral task (e.g. asking the participant to view faces), to the image processing (e.g. correcting images for head movements that occurred during scanning), through to statistical analysis (identifying brain regions that are activated by a task).

This laboratory course offers hands-on STEM training with a focus on magnetic resonance imaging (MRI). Students develop a foundational understanding of MRI physics and gain direct experience with image acquisition. They also use [NeurodeskEDU high-performance computing]((https://github.com/neurodesk/neurodeskedu)) tools to preprocess, analyze, and visualize neuroimaging data, applying both classical and artificial intelligence–based methods. Through these activities, students learn how MRI advances our understanding of the human mind and functions as a transformative tool in clinical practice.

### Lectures

  - Overview.
    - The classroom is a computer lab, so all assignments can be completed using your computer. Computation is supported by [Neurodesk play](https://play.neurodesk.org/). Our goal is to leverage and extend [NeurodeskEDU](https://neurodesk.org/edu/intro.html)
  - MRI physics: Image Acquisition.
    - [Terrific videos](https://magritek.com/resources/videos/) (from a company that makes a unique instructional MRI system
  - MRI physics: Image Contrast.
    - Echo time and repetition time influence [T1 (recovery) and T (dephasing)](https://case.edu/med/neurology/NR/MRI%20Basics.htm).
  - fMRI Paradigm Design.
    - My [fMRI simulator](https://github.com/neurolabusc/fMRI-Simulator) allows you to explore the hemodynamic changes induced by different tasks.
  - Statistics and Thresholding.
    - [cluster extent challenges](https://andysbrainblog.blogspot.com/2014/01/how-to-avoid-common-cluster-extent.html)
  - Spatial Processing I: Spatial Registration – realignment (motion correction), coregistration, normalization; Spatial interpolation – linear, spline, sinc functions
    - [Spatial Processing Demos](https://github.com/neurolabusc/spatial-processing).
  - Spatial Processing Continued II: Smoothing – filters, edge detection, gaussian blur, homogeneity correction (for EPI and anatomical scans), motion related intensity changes.
    - [Undistorting fMRI EPI data using the SPM FieldMap toolbox](../fieldmaps/index.md).
  - Temporal Processing
    - [Interactive filtering demo](https://github.com/neurolabusc/biquad-filter) shows how low-pass, high-pass and notch filters modulate a signal.
    - [Physiological Artifact Removal Tool](https://github.com/neurolabusc/Part).
  - FSL and SPM. Hands on demonstrations
    - [fMRI analysis](https://people.cas.sc.edu/rorden/tutorial/index.html).
    - [FSL: block design](https://people.cas.sc.edu/rorden/tutorial/html/block.html).
  - Detecting subtle changes in brain structure: Voxel Based Morphometry and Diffusion Tensor Imaging.
    - [John Ashburner's VBM class (PDF)](https://www.fil.ion.ucl.ac.uk/~john/misc/VBMclass10.pdf).
    - [DTI tutorial](https://people.cas.sc.edu/rorden/tutorial/html/dti.html).
    - [Advanced DTI tutorial](../dti/index.md).
    - Brain injury and neuroimaging. Measuring blood flow and using lesion symptom mapping to understand the consequences of stroke and other neurological disorders.
    - [Arterial Spin Labeling](../asl/index.md).
    - Contrast-enhanced (Gadolinium) [Perfusion Weighted Imaging](../pwi/index.md).
    - [VLSM using my NPM software](https://people.cas.sc.edu/rorden/mricron/stats.html)
  - Brain stimulation: Transcranial Magnetic Stimulation (TMS), Transcranial Direct Current Stimulation (tDCS). Roger Newman-Norlund and Chris Rorden
  - Graduate student presentations: Resting state analysis, effective and functional connectivity, independent components analysis, neural current MRI?

### Calendar [Spring 2026](https://sc.edu/about/offices_and_divisions/registrar/academic_calendars/2025-26_calendar.php)

| Tuesday | Thursday |
|--------|----------|
| Tu 13 Jan Introduction to course | Th 15 Jan Lab: Neurodesk |
| Tu 20 Jan Image Visualization, Safety | Th 22 Jan Lab: Visualization |
| Tu 27 Jan MRI Physics: basics | Th 29 Jan Lab: fslmaths, bet|
| Tu 3 Feb MRI physics: contrast | Th 5 Feb Fieldtrip: [MRI scanner](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/mccausland_center/) |
| Tu 10 Feb fMRI signal and design | Th 12 Feb Lab: fMRI |
| Tu 17 Feb fMRI statistics | Th 19 Feb Lab: fMRI statistics|
| Tu 24 Feb Spatial processing | Th 26 Feb Lab: Spatial processing|
| Tu 3 Mar Temporal processing | Th 5 Mar Lab: Temporal processing|
| Tu 10 Mar Spring Break (no classes) | Th 12 Mar Spring Break (no classes) |
| Tu 17 Mar VBM| Th 19 Mar Lab: VBM|
| Tu 24 Mar Bob Rafal Lesions | Th 26 Mar Lab: VLSM|
| Tu 31 Mar Diffusion | Th 2 Lab: DWI |
| Tu 7 Apr Brain Stimulation | Th 9 Apr Lab: Help with final|
| Tu 14 Apr Machine Learning: AI | Th 16 Apr Lab: Machine learning |
| Tu 21 Apr Presentations | Th 23 Apr Presentations |

[Final Project Deadline](https://sc.edu/about/offices_and_divisions/registrar/final_exams/final-exams-spring-2026.php) Tuesday, May 5 - 9:00 a.m.

### Links

 - [Rik Henson’s fMRI mini-course](https://imaging.mrc-cbu.cam.ac.uk/imaging/SpmMiniCourse)
 - [FSL course](https://open.win.ox.ac.uk/pages/fslcourse/website/index.html)
 - [AFNI course](https://cbmm.mit.edu/afni)