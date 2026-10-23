from ccc_levels.abstract_level import AbstractLevel

class Level3(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(3)
        
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

            emitter_id = 1
            emitter_r_d = {}
            emitter_s_d = {}
            emitter_q_d = {}
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
                        case 'M':
                            hex_line.append(Grid(curr_s, curr_r, curr_q, False, False, True))
                            curr_q += 1
                            curr_s -= 1
                        case '-':
                            pass
                        case _:
                            hex_line.append(Grid(curr_s, curr_r, curr_q, int(char), True))
                            emitter_val = int(char)

                            match emitter_val:
                                case 1 | 4:
                                    emitter_r_d[emitter_id] = curr_r
                                case 2 | 5:
                                    emitter_q_d[emitter_id] = curr_q
                                case 3 | 6:
                                    emitter_s_d[emitter_id] = curr_s
                                case _:
                                    raise Exception('Something went horribly wrong-')
                            emitter_id += 1
                            curr_q += 1
                            curr_s -= 1
                hex_list.append(hex_line)
                curr_r += 1
                start_q -= 1

            for hex_line in hex_list:
                for cell in hex_line:
                    e_amount = 0
                    for emitter_r in emitter_r_d:
                        if emitter_r_d[emitter_r] == cell.r:
                            e_amount += 1
                    for emitter_q in emitter_q_d:
                        if emitter_q_d[emitter_q] == cell.q:
                            e_amount += 1
                    for emitter_s in emitter_s_d:
                        if emitter_s_d[emitter_s] == cell.s:
                            e_amount += 1

                    if e_amount == 2:
                        cell.matter = True
                    elif e_amount > 2:
                        cell.matter = False
                    
                    
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
