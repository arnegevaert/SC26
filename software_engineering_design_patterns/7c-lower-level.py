# Current offset in resp Buffer
offset: int = 4

# Contains all line-widths inside the document and
# number of appearances.
line_widths: dict[int, int] = {}

# Position in this buffer of the first object that hasn't
# been returned to the client
offset: int = 4

# Holds statistics about line lengths of the form <length, count>
# where length is the number of characters in a line (including
# the newline), and count is the number of lines with
# exactly that many characters. If there are no lines with
# a particular length, then there is no entry for that length.
line_widths: dict[int, int] = {}
