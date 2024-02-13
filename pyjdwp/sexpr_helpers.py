'''
This class exists because later jdwp.spec files have unclosed quotes on some lines which is problematic for parsing the JDWP spec files.
'''
class QuotesFixer:
    @staticmethod
    def fix_unclosed_quotes_in_line(line):
        """
        Fixes unclosed quotes in a single line, ensuring not to close quotes prematurely
        within valid s-expression syntax.
        """
        new_line = ""
        quote_open = False
        for char in line:
            if char == '"' and not quote_open:
                quote_open = True
            elif char == '"' and quote_open:
                quote_open = False
            new_line += char
        if quote_open:
            new_line += '"'
        return new_line

    def process_text(self, text):
        """
        Processes the input text and returns the cleaned text.
        """
        lines = text.split('\n')
        fixed_lines = [self.fix_unclosed_quotes_in_line(line) for line in lines]
        return '\n'.join(fixed_lines)

