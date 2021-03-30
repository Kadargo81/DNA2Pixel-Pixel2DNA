# DNA2pixel and Pixel2DNA
Simple Programs to Make and Decode RNA or DNA Pixel Art 

DNA2Pixel-  
This program takes a txt file of a RNA or DNA sequence
and creates an RGBY pixel map representing the sequence.  
The test sequence was copied from 
https://www.ncbi.nlm.nih.gov/nuccore/MT072688  
The input can handle special characters & numbers also any RNA or DNA sequence could be used.  
The output will be a png in the same directory as the program & it will try to show the image using your OS default image viewer.  
The image will be in a square format and as it would be unlikely to have a base sequence whose sqrt is an exact integer<br>
the final line will be completed with white pixels, this can be changed to your preference.  

Pixel2DNA-  
This program takes a png file reads the pixel data and decodes the RGBY value into an RNA or DNA sequence.  
This is designed to take the output of DNA2Pixel.py as input but any pixelmap will work.  
Input files must have 1 to 1 pixel data, if you use a 3x upscaled image for example it will read 3x as many bases and produce garbage.  
The input files exact RGBY values must be found and changed within the program.
