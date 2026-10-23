from ccc_levels.abstract_level import AbstractLevel

class Level2(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(2)
        
    # ----- methods: -----
    
    def solve_singular(self, file: str) -> None:
        input = self.file_access.read_file(file)
        out = []

        line = 0

        cases = int(input[line])

        for i in range(cases):
            line += 1
            
            in_vals = input[line]
            radius = int(in_vals.split(' ')[0])
            rows = int(in_vals.split(' ')[1])
            cols = int(in_vals.split(' ')[2])

            curr_r = radius * -1
            start_q = 0

            emitter_r = 0
            emitter_s = 0
            emitter_q = 0
            emitter_val = 0

            hex_list = []
            
            for j in range(rows):
                line += 1
                this_q = max(radius * -1, start_q)
                this_s = min(radius, radius - curr_r)

                curr_q = this_q
                curr_s = this_s

                hex_in_line = input[line]
                hex_line = []
                for char in hex_in_line:
                    match char:
                        case '*':
                            hex_line.append(Grid(curr_s, curr_r, curr_r, False, True))
                            curr_q += 1
                            curr_s -= 1
                        case 'O':
                            hex_line.append(Grid(curr_s, curr_r, curr_q, False, False))
                            curr_q += 1
                            curr_s -= 1
                        case '-':
                            pass
                        case _:
                            hex_line.append(Grid(curr_s, curr_r, curr_q, int(char), True))
                            emitter_s = curr_s
                            emitter_r = curr_r
                            emitter_q = curr_q
                            emitter_val = int(char)
                            curr_q += 1
                            curr_s -= 1
                hex_list.append(hex_line)
                curr_r += 1
                start_q -= 1

            match emitter_val:
                case 1 | 4:
                    for hex_line in hex_list:
                        for cell in hex_line:
                            if cell.r == emitter_r:
                                cell.set_matter(True)
                case 2 | 5:
                    for hex_line in hex_list:
                        for cell in hex_line:
                            if cell.q == emitter_q:
                                cell.set_matter(True)
                case 3 | 6:
                    for hex_line in hex_list:
                        for cell in hex_line:
                            if cell.s == emitter_s:
                                cell.set_matter(True)
                case _:
                    raise Exception('Something went horribly wrong-')
                    

            hex_out = []
            for j in range(len(hex_list)):
                hex_res = ''
                hex_line = hex_list[j]
                num_dash = abs(j - radius)
                for k in range(num_dash):
                    hex_res += '-'
                for cell in hex_line[:-1]:
                    if cell.emitter:
                        hex_res += str(cell.emitter)
                    elif cell.border:
                        hex_res += '*'
                    elif cell.matter:
                        hex_res += 'M'
                    else:
                        hex_res += 'O'
                    hex_res += '-'
                cell = hex_line[-1]
                if cell.emitter:
                    hex_res += str(cell.emitter)
                elif cell.border:
                    hex_res += '*'
                elif cell.matter:
                    hex_res += 'M'
                else:
                    hex_res += 'O'
                for k in range(num_dash):
                    hex_res += '-'
                hex_out.append(hex_res)

            for hex_line in hex_out:
                out.append(hex_line)
                print(hex_line)

            if i != cases - 1:
                out.append('')
            line += 1
            
        self.file_access.save_file(file, out)
        return None

class Grid:
    def __init__(self, s, r, q, emitter, border, matter=False):
        self.s = s
        self.r = r
        self.q = q
        self.emitter = emitter
        self.border = border
        self.matter = matter

    def set_matter(self, matter):
        self.matter = matter
