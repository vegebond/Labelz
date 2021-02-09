# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import labelz as lz

data = np.array([['Comment out the line that says, "...design_mode() = True"', '', '', ''],
                 ['', '', '', ''],
                 ['Tod Bloomington', 'CEO', '', ''],
                 ['Sheila Watkins', 'Director', 'Marketing', 'NW'],
                 ['Robert Sheldon', 'Director', 'Supply Chain', 'NW'],
                 ['Brian Jennings', 'Director', 'Human Resources', 'NW'],
                 ['David Edlestein', 'Director', 'Manufacturing', 'NW'],
                 ['Mark Hampton', 'Director', 'Marketing', 'SW'],
                 ['Barbara Elridge', 'Director', 'Supply Chain', 'SW'],
                 ['Jennifer Holder', 'Director', 'Human Resources', 'SW'],
                 ['Stacey Sutton', 'Director', 'Manufacturing', 'SW'],
                 ['Daniel Hollingsworth', 'Director', 'Marketing', 'NE'],
                 ['Holly Bartlette', 'Director', 'Supply Chain', 'NE'],
                 ['David Smart', 'Director', 'Human Resources', 'NE'],
                 ['Valerie Botkins', 'Director', 'Manufacturing', 'NE']])

df = pd.DataFrame(data, columns = ['name', 'title', 'division', 'region'])

# All measurements are in points(1/72")

labelz = lz.Labelz(df)

labelz.set_page_size(612, 792)
# (length, height)

labelz.set_margins(18, 18, 18, 18)
# (left, right, top, bottom)

labelz.set_label_size(288, 126)
# (length, height)

labelz.add_field('region', 211, 24, 72, 42, 'Times-Roman', 42)
labelz.add_field('name', 5, 92, 278, 24, 'Times-Roman', 24)
labelz.add_field('title', 5, 58, 201, 24, 'Times-Roman', 24)
labelz.add_field('division', 5, 24, 201, 24, 'Times-Roman', 24)
# (field name, across, up, length, height)
# positioning is relative to lower left corner of page

labelz.design_mode = True
# If true, this prints border for labels and fields and turns off clipping.

labelz.page_layout()
# The order is important here. This command must come after the preceeding commands.
# The number of labels across, and down, as well as the gaps between them, are calculated.

f = open("labelz.ps", "w")
f.write(labelz.print_labelz())
f.close()
