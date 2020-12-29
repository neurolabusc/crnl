
JPEG Format Variations
=======================================

Most people think that “JPEG” refers to a single format. However, while one format dominates most fields, in medical imaging there are different forms of JPEG images that require different tools to decode them.

The `JPEG (Joint Photographic Experts Group) <http://en.wikipedia.org/wiki/JPEG>`_ defined a number of formats for saving images. In particular, this is a popular format for digital photographs, and is commonly used by digital cameras and web pages. However, some JPEG formats are also used in medical imaging. The expectations for medical imaging is a bit different than other fields, and there is a preference for higher precision data (e.g. saving an image as 65,535 shades of gray instead of just 256) and higher quality (less artifacts).

.. image:: jpeg.jpg
   :width: 70%
   :align: center

This web page describes the different forms of JPEG compression specified for DICOM files, the dominant image format for medical imaging. The DICOM standard currently specifies 35 different ways an image could be embedded into a DICOM file. These formats are referred to as the  `Transfer Syntax <http://www.dicomlibrary.com/dicom/transfer-syntax/>`_. Here I describe the most popular Transfer Syntaxes that use JPEG formats, and demonstrate how my  `dcm2nii <http://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage>`_  software decodes these images.

Baseline JPEG
-------------------------------------------

**Common in DICOM:** Transfer syntax 1.2.840.10008.1.2.4.50 describes the 8-bit standard classic lossy JPEG that is identical to the most common JPEG images created by digital cameras and used on the web page. These are easy to support – you can typically decode these using the API of your operating system, or for universal support use the popular  `IJG library <http://www.ijg.org>`_  or the elegant  `nanoJPEG <http://keyj.emphy.de/nanojpeg/>`_  library. To convert a dicom image to this format you can use  `dcmcjpeg <http://support.dcmtk.org/docs/dcmcjpeg.html>`_  with the command “./dcmcjpeg +eb in.dcm out.dcm”.

**Rare in DICOM** . Transfer syntax 1.2.840.10008.1.2.4.51 describes the standard lossy JPEG format but extended to store higher precision (e.g. 12 rather than 8 bits per pixel, yielding up to 4095 distinct colors). Standard JPEG libraries can not handle these images. The typical solution is for developers to recompile a version of the IJG library to support this pixel format. However, the resulting library is no longer able to cope with the 8-bit images. Fortunately, this format appears to be exceptionally rare: someone who demands high precision data is probably not interested in lossy compression. If you insist on creating one of these images you can use the command “./dcmcjpeg +ee in.dcm out.dcm”.

Compressed lossless JPEG
-------------------------------------------

**Common in DICOM.** Transfer syntaxes 1.2.840.10008.1.2.4.57 and 1.2.840.10008.1.2.4.70 refer to a  `lossless JPEG <http://en.wikipedia.org/wiki/Lossless_JPEG>`_  format that is exceptionally rare **outside**  of the medical domain (and completely different from both the lossless JPEG-LS and lossless JPEG-2000 encoding formats). While this was fully described in the `JPEG ISO/IEC 10918-1:1994 T.81 (09/92) <http://www.w3.org/Graphics/JPEG/itu-t81.pdf>`_, it did not gain traction outside of medical imaging (where GIF and PNG became the most popular lossless formats). This legacy lossless JPEG is a simple format, and only uses the  `Huffman encoding <http://www.compressconsult.com/huffman/>`_  without the typical discrete cosine transforms (DCT). However, the fact that these images are typically saved with 16-bit precision means it is not supported by most libraries, and they generate an error saying they can not decode “SOF type 0xc3”. I have written my own library to support this format, though other tools (e.g. dcmtk) use custom-patched variations of the IJG library. This is not a very efficient compression method, and personally I would strongly recommend users investigate file-based compression (.zip, or disk driver enabled compression) over this arcane format. This is the default output of dcmcjpeg, probably explaining its widespread popularity, for example the command “./dcmcjpeg in.dcm out.dcm” generates a DICOM image with format 1.2.840.10008.1.2.4.70, while the command “./dcmcjpeg +el in.dcm out.dcm” generates an image with syntax 1.2.840.10008.1.2.4.57. You can also create these files withgdcmconv (e.g. 'gdcmconv -J in.dcm out.dcm').

Compress lossless JPEG-LS
-------------------------------------------

**Rare in DICOM**  In theory, the JPEG-LS standard looked promising: better compression than the ancient lossless JPEG, while offering similar compression ratios at far higher speeds to the much more complex JPEG2000 lossless standard. The JPEG-LS (ISO/IEC 14495-1:1999 / ITU-T.87) uses DICOMtransfer syntaxes 1.2.840.10008.1.2.4.80 and 1.2.840.10008.1.2.4.81. These images can be created with `gdcmconv <https://sourceforge.net/projects/gdcm/>`_  (e.g. 'gdcmconv -L in.dcm out.dcm'). Furthermore, you can configure  `Horos <https://horosproject.org/>`_  to save to this format.

Compressed JPEG2000 (lossy and lossless)
-------------------------------------------

**Rare in DICOM:** Transfer syntaxes 1.2.840.10008.1.2.4.90, 1.2.840.10008.1.2.4.91 and 1.2.840.10008.1.2.4.92 refer to JPEG2000 based compression. This is very different from the other JPEG methods, using wavelets rather than DCT. This is a technically impressive format – at extreme compression ratios it does not have the blocky artifacts of conventional JPEG. At typical compression ratios it tends to produce files that are perhaps 15% smaller than conventional JPEG. However, adoption was been very slow, perhaps because conventional JPEG were good enough, JPEG2000 libraries are hard to integrate into software, JPEG2000 is relatively slow to process images, and `JPEG2000 was superceded by newer formats like HEIF  <https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format>`_. In my experience the Jasper library is elegant, but it does have problems with some  `16-bit images <http://en.wikipedia.org/wiki/JPEG_2000>`_ . On the other hand, the  `OpenJPEG <http://www.openjpeg.org>`_  library is cumbersome, the calls have changed a lot between versions, is poorly documented, but is very robust. In my experience, these images remain rare (perhaps since the free dcmcjpeg does not support them, while the professional  `dcmjp2k <http://dicom.offis.de/dcmjp2k.php.en>`_  does).These images can be created with `gdcmconv <https://sourceforge.net/projects/gdcm/>`_  (e.g. 'gdcmconv -K in.dcm out.dcm'). Furthermore, you can configure `Horos <https://horosproject.org/>`_ to save to this format.

Comparing lossless JPEG compression
-------------------------------------------

Since we tend to worry about the consequences of lossless compression, the comparison of the various compression methods is of interest. There are several reasons why you may want to save your raw DICOM data uncompressed: disk space is inexpensive relative to the cost of scanning, decoding compressed images is slow, many tools do not support compressed DICOMs and the fact that while these tools compress the image data, they do not compress the verbose header (so you may be better off simply archiving DICOM data in popular file-level compression formats like .zip).

For those still interested in choosing a lossless compressed DICOM format, here is a quick  `comparison <https://github.com/rordenlab/dcm2niix/blob/master/console/charls/README.md>`_ for MRI data. Note that in this example, JPEG-LS reduces the file size to 60% of the raw image, takes 30% longer to compress than creating JPEG lossless, and is five times slower to decode (open, convert, view) than raw data. This table suggests that the JPEG2000 as implemented in OpenJPEG is exceptionally slow for both compression and decompression. One the other hand, JPEG-LS finds provides good compression with a modest performance penalty.

.. list-table:: JPEG Performance
   :widths: 25 25 25 25
   :header-rows: 1

   * - Method
     - Size
     - Encode
     - Decode
   * - Raw
     - 1.00
     - 
     - 1.0
   * - lossless JPEG
     - 0.65
     - 1.0
     - 5.0
   * - JPEG-LS
     - 0.60
     - 1.3
     - 7.7
   * - JPEG-2000 Lossless
     - 0.61
     - 3.9
     - 71.6

Sample source code
-------------------------------------------

Attached below are three C programs that illustrate converting JPEG compressed DICOM images to uncompressed TIFF images. One example uses NanoJPEG for conventional JPEG images. Another uses my own code for lossless JPEG. The final example uses OpenJPEG for JPEG2000. They all use  `Paul Bourke’s code <http://paulbourke.net/dataformats/tiff/>`_  to generate TIFF images (I chose TIFF since it is a popular format that supports 16-bit images). The sample images come from the  `Lead Tools <http://www.creatis.insa-lyon.fr/%7Ejpr/PUBLIC/gdcm/gdcmSampleData/ColorDataSetLeadTool/>`_  sample images.
