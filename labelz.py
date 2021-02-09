# -*- coding: utf-8 -*-

class Labelz():
    def __init__(self, df):
        print('labelz version 1.0')
        self.across = []
        self.down = []
        self.current_record = 0
        self.fields = []
        self.pscript = ''
        self.df = df
        self.design_mode = False
        
    def set_page_size(self, width, height):
        self.page_width = width
        self.page_height = height
        
    def set_margins(self, left, right, top, bottom):
        self.left_margin = left
        self.right_margin = right
        self.top_margin = top
        self.bottom_margin = bottom
        
    def set_label_size(self, width, height):
        self.label_width = width
        self.label_height = height

    def useable_width(self):
        return(self.page_width - self.left_margin - self.right_margin)

    def useable_height(self):
        return(self.page_height - self.top_margin - self.bottom_margin)
    
    def labelz_across(self):
        return(int(self.useable_width() / self.label_width))

    def labelz_down(self):
        return(int(self.useable_height() / self.label_height))
    
    def labelz_per_page(self):
        return(self.labelz_down() * self.labelz_across())

    def label_horizontal_gap(self):
        return((self.useable_width() - (self.labelz_across() * self.label_width)) / (self.labelz_across() - 1))
    
    def label_vertical_gap(self):
        return((self.useable_height() - (self.labelz_down() * self.label_height)) / (self.labelz_down() - 1))
    
    def page_layout(self):
        self.across = []
        labelz_across = int(self.useable_width() / self.label_width)
        for x in range(labelz_across):
            self.across.append(int(round(self.left_margin + x * (self.label_horizontal_gap() + self.label_width))))
        self.down = []
        labelz_down = int(self.useable_height() / self.label_height)
        for y in range(labelz_down, 0, -1):
            self.down.append(int(round(self.bottom_margin + (y -1) * (self.label_vertical_gap() + self.label_height))))
        self.labelz = []
        for y in self.down:
            for x in self.across:
                self.newlabel = self.Label(x, y)
                self.labelz.append(self.newlabel)
        for x in self.fields:
            pass
            self.field_box(x)
                    
    def print_labelz(self):

        self.number_of_records = len(self.df)
        self.number_of_fields = len(self.fields)

        for self.current_record in range(self.number_of_records):
            self.current_label = self.current_record % self.labelz_per_page()
            if(self.current_label == 0):
                if(self.current_record > 0):
                    self.pscript += 'showpage\n'
# Add new page if needed
            
            self.current_column = self.current_record % self.labelz_across()
            self.current_row = int(self.current_record / self.labelz_across()) % self.labelz_down()
            self.pscript += '/home {\n'
            self.pscript += str(self.across[self.current_column]) + ' '
            self.pscript += str(self.down[self.current_row]) + ' moveto\n'
            self.pscript += 'closepath} def\n'
# Define Home for current label
            
            self.pscript += '/label_box {\n'
            self.pscript += 'newpath\nhome\n'
            self.pscript += '0 ' + str(self.label_height) + ' rlineto\n'
            self.pscript += str(self.label_width) + ' 0' + ' rlineto\n'
            self.pscript += '0 -' + str(self.label_height) + ' rlineto\n'
            self.pscript += 'closepath\n'
            self.pscript += '} def\n'
# Define label_box

            if self.design_mode:
                self.pscript += 'label_box stroke\n'
# Draw Label Box if design_mode = True

            for self.current_field in range(self.number_of_fields):
                self.pscript += 'gsave\n'
                self.pscript += '/field_box {\n'
                self.pscript += 'newpath\nhome\n'
                self.pscript += str(self.fields[self.current_field].across) + ' ' + str(self.fields[self.current_field].up) + ' rmoveto\n'
                self.pscript += '0 ' + str(self.fields[self.current_field].height) + ' rlineto\n'
                self.pscript += str(self.fields[self.current_field].width) + ' 0' + ' rlineto\n'
                self.pscript += '0 -' + str(self.fields[self.current_field].height) + ' rlineto\n'
                self.pscript += 'closepath\n'
                self.pscript += '} def\n'
# Define field_box for selected field

                self.pscript += '/' + self.fields[self.current_field].font + ' findfont\n'
                self.pscript += str(self.fields[self.current_field].font_size) + ' scalefont\n'
                self.pscript += 'setfont\n'
# Get Font info for current Field

                self.pscript += 'home\n'
                self.pscript += str(self.fields[self.current_field].across) + ' ' + str(self.fields[self.current_field].up) + ' rmoveto\n'
                self.pscript += '0 currentfont /FontInfo get\n'
                self.text = self.df.loc[self.current_record][self.fields[self.current_field].name]

                if self.design_mode: self.pscript += 'field_box stroke\n'
                else:
                    self.pscript += 'field_box clip\n'
# Draw Field Box if design_mode = True
# Clip if design_mode = False
                
                self.pscript += 'home\n'
                self.pscript += str(self.fields[self.current_field].across) + ' ' + str(self.fields[self.current_field].up) + ' rmoveto\n'
                self.pscript += '/UnderlinePosition get ' + str(self.fields[self.current_field].font_size * 2) + ' mul neg rmoveto\n'
                self.pscript += '(' + self.text + ') show\n'
                self.pscript += 'grestore\n'
# Print text in current field
        
        self.pscript += 'executive print flush\n'
        return(self.pscript)

    def field_box(self, field):
        self.pscript += '/field_box {\n'
        self.pscript += 'newpath\n'
        self.pscript += 'home\n'
        self.pscript += str(field.across) + ' ' + str(field.up) + ' rmoveto\n'
        self.pscript += '0 ' + str(field.height) + ' rlineto\n'
        self.pscript += str(field.width) + ' 0 rlineto\n'
        self.pscript += '0 -' + str(field.height) + ' rlineto\n'
        self.pscript += 'closepath} def\n'
        
    def add_field(self, name, across, up, width, height, font, font_size):
        self.fields.append(self.Field(name, across, up, width, height, font, font_size))
        
    class Label():
        def __init__(self, horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical
            
    class Field():
        def __init__(self, name, across, up, width, height, font, font_size):
            self.name = name
            self.across = across
            self.up = up
            self.width = width
            self.height = height
            self.font = font
            self.font_size = font_size
