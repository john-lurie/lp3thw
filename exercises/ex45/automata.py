from time import sleep

class Automaton(object):
    """
    A one-dimensional cellular automaton.

    Described in "A New Kind of Science", ch. 2 by S. Wolfram (2002).

    Attributes
    ----------
    rule : int
        An 8-bit number represents the next cell color based on one of 
        eight possible states for a cell and its immediate neighbors.
        If rule < 0 or rule > 255, rule will be set to 0.
    n_cells : int
        Number of cells in the automaton. Forced to be odd so the
        default initial conditions are centered.
    dark_mode : bool
        If True, transpose white and black for dark mode color schemes.
    initial_cond : str
        Initial conditions. Default = "wbw".
        'w' = white cell, 'b' = black cell.
    white_chr : str
        Character used for a white cell in the printout. Default is
        the Unicode "space" character U+0020.
    black_chr : str
        Character used for a black cell. Default is the Unicode 
        "Dark shade" character U+2593.
    photosensitive : bool
        By default, self.run() will warn about possible flashing lights.
    """
    def __init__(self, rule=0, n_cells=79, dark_mode=False):
        # Check if rule in appropriate range.
        if rule < 0 or rule > 255:
            print(f"WARNING: rule '{rule}' outside allowed range: 0 - 255.")
            print(f"Using default value: 0\n")
            self.rule = 0
        else:
            self.rule = rule

        self.n_cells = n_cells
        self.initial_cond = "wbw"
        self.white_chr = "\u0020"
        self.black_chr = "\u2593"
        self.photosensitive = True

        if dark_mode:
            # Transpose white and black.
            self.white_chr, self.black_chr = self.black_chr, self.white_chr

    def _make_table(self):
        """Construct a dict mapping cell states to rule for each state."""
        # Eight possible states for the cell and its immediate neighbors.
        states = ['bbb', 'bbw', 'bwb', 'bww', 'wbb', 'wbw', 'wwb', 'www']
 
        # The rules can be expressed as an 8-bit number.
        binary_rule = "{:0>8b}".format(self.rule)
        # Convert binary number to a str. 0 == 'w', 1 == 'b'.
        for number, color in ('0', 'w'), ('1', 'b'):
            binary_rule = binary_rule.replace(number, color)

        # Make string into a list.
        color_list = [letter for letter in binary_rule]
        # Make a lookup table for the rule.
        self.lookup_table = dict(zip(states, color_list))

    def _initialize_cells(self):
        """Intialize a list of cells based on 'self.initial_cond'."""
        if self.n_cells % 2 != 1:
            print("n_cells should be odd, adding one cell.")
            self.n_cells += 1 

        # Center the initial conditions in white space padding.
        cells_string = self.initial_cond.center(self.n_cells, 'w')
        # Strings do not support item assignment.
        # Thus a list is required that can be altered by 'iterate()'.
        self.cell_colors = [cell for cell in cells_string]

    def _iterate(self):
        """Iterate a single step of the simulation."""
        # This copy gets edited while 'self.cell_colors' is referenced.
        next_colors = self.cell_colors[:]

        for ii in range(0, len(self.cell_colors)):
            # See Wolfram p. 866 on cyclic boundary conditions.
            # Left neighbor of left most cell is rightmost cell.
            # Right neighbor of rightmost cell is leftmost cell.
            state = (self.cell_colors[ii - 1]
                     + self.cell_colors[ii]
                     + self.cell_colors[(ii + 1) % len(self.cell_colors)])
            # Lookup the rule based on three letter str 'state'. 
            next_colors[ii] = self.lookup_table[state]
        
        # Now 'self.cell_colors' can be updated.
        self.cell_colors = next_colors[:]

    def run(self, iterations=20, pause=0.0):
        """Run the simulation.

        Parameters
        ----------
        iterations : int
            Number of iterations to run.
        pause : float
            Duration of pause between iterations, in seconds.
        """
        if self.photosensitive:
            print("WARNING: This simulation can produce flashing lights.")
            print("This may pose a risk for photosensitive users.")
            input("Press ENTER to continue, CTRL-C to exit. ")

        self._make_table()
        self._initialize_cells()
        
        for step in range(iterations):
            # Replace 'w' and 'b' with characters for printing.
            # This keeps 'self.cell_colors' human readable.
            cells_string = ''.join(self.cell_colors)
            cells_string = cells_string.replace('w', self.white_chr)
            cells_string = cells_string.replace('b', self.black_chr)
            print(cells_string)

            # Run the next iteration.
            self._iterate()
            sleep(pause)
