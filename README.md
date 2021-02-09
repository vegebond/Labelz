Labelz is a python module that creates postscript code for printing labels.<br>
Data is provided via a pandas dataframe.<br>
The user supplies the page dimensions, margins, and label dimensions, all in points(1/72").<br>
The number of labels across and down, as well as the gaps between labels, are calculated from the above information.<br>
User also supplies positioning, relative to lower left corner of label, as well as width, height, font, and font size, for each field.<br>
If design_mode is True, outline of each label and field is printed, and clipping is off. Otherwise, text is clipped, and borders do not print.<br>
In some cases, a label's positioning might display a rounding error of less than 1/2 point(1/144").<br>
I have taken care to ensure that rounding errors do not accumulate, as you move down the page.<br>
You might also note that values entered by the user do not necessarily have to be integers. Decimals are permitted.<br>
If you study the example file I have included, that should tell you everything you need to know.<br>
