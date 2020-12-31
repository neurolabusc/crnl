MRI Contrast
=======================================

.. _my_mri_concepts:

This page describes Matlab scripts which generate some simple graphs to demonstrate basic principles of MRI. T2 and T1 relaxation are two properties we can use to adjust contrast (how bright a tissue will appear). Download the  `Matlab scripts here  <https://github.com/rordenlab/spmScripts>`_ (the relevant scripts have names which start with t2, t1 and tr)

We often want to create an image where the image brightness helps us define the border between tissue types (e.g. defining the edge between gray and white matter). Note that every scan is influenced by both T2 and T1 effects to some extent. However, if we choose a sequence with short echo times (TEs) and repeat times (TRs), T1 effects will predominate the resulting “T1-weighted” image. On the other hand, with long TRs and TEs the T2 effects will dominate (a T2-weighted image). However, many sequences mix these effects, for example a ‘proton density’ scan uses a long TR with a short TE such that the resulting brightness reflects the concentration of hydrogen regardless of tissue type (a balanced scan).


T1 and field strength
-------------------------------------------
T1 refers to the how rapidly nuclei return to alignment with the magnetic field ( longitudinal relaxation). T1 relaxation is directly related to the delay between the radio-pulses which excite the nuclei (the repeat time, TR). While there will be more alignment at higher field strengths, the proportional rate of this change is slower at higher field strengths. This is one reason why TRs are often slower for higher field strengths. This also explains why some motion contrast are disproportionally better at higher field strengths (e.g. better saturation for static tissue for time-of-flight scans).

 -  `Wikipedia entry for T1 relaxation <https://en.wikipedia.org/wiki/Spin-lattice_relaxation_time>`_ 

.. image:: T1.png
   :width: 70%
   :align: center
   
T2 and tissue type
-------------------------------------------

 - T2 refers to the how rapidly nuclei fall out of phase (transverse relaxation). T2 relaxation is directly related to the delay between when we transmit a radio-pulse to the time when we record the radio signal being emitted (the echo time, TE). Since nuclei spin faster at higher field strengths, they tend to fall out of phase more rapidly. This is one reason why TEs are often faster for higher field strengths. Likewise, hydrogen T2 varies with tissue type. This image shows the T2 effects for several different tissue types.

.. image:: T2.png
   :width: 70%
   :align: center

T2 and contrast between tissues
-------------------------------------------

 - T2 refers to the how rapidly nuclei fall out of phase (transverse relaxation). T2 relaxation is directly related to the delay between when we transmit a radio-pulse to the time when we record the radio signal being emitted (the echo time, TE). Likewise, hydrogen T2 varies with tissue type. At very short TEs, all hydrogen will emit a strong signal, regardless of tissue type (all tissue will appear bright). On the other hand, at very long TEs there will be very little signal from any hydrogen, regardless of tissue type (all tissue will appear dark). However, at intermediate TEs, some tissue will emit much more signal than others (and therefore, we can discriminate between these tissues due to their brightness). For example, on a 3 Tesla scanner there will be maximal T2 contrast between gray matter and fat at TEs around 105ms. Note that we often want to maximize contrast between several types of tissue (e.g. for brain scans we want to distinguish white matter, gray matter and cerebral spinal fluid).

TR and flip angle
-------------------------------------------



With short delays between RF pulses (TRs) there will be little longitudinal recovery (T1 relaxation). In this case, sending in a strong RF pulse to induce a 90-degree flip will lead to less signal than a weaker pulse that induces a shallower flip angle. The Ernst angle refers to the optimal flip angle for a given TR. This graph shows the Ernst angle as a function of TR (blue line). The graph also shows the relative signal versus an infinite TR (green). This latter effect shows the diminishing returns seen with shorter TRs: for example a TR of 500ms returns 42% signal (relative to infinite TR), while a 1000m scan returns 59%. Therefore, while scanning twice as fast will provide twice as many samples, each sample will be noisier. Note that as previously described T1 varies with both tissue type and field strength. This graph uses Mark Cohen’s suggestion for an approximate T1 of 1400ms for the brain using a 3T scanner (if your scanner is not 3T, take a look at “T1 and field strength” for approximations).

 - `Wikipedia entry for Ernst Angle <https://en.wikipedia.org/wiki/Ernst_angle>`_ 
 - `Martín-Pastor’s online calculator <https://www.mritoolbox.com/ErnstAngle.html>`_ 
 - `Flip Angle for T2* (fMRI BOLD) contrast <https://pubmed.ncbi.nlm.nih.gov/21073963>`_
