from ccc_levels.abstract_level import AbstractLevel

class Level4(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(4)
        
    # ----- methods: -----
    
    def solve_singular(self, file: str) -> None:
        input = self.file_access.read_file(file)
        out = []

        line = 0

        cases = int(input[line])

        for i in range(cases):
            line += 1
            radius = int(input[line])

            line += 1
            func_amount = int(input[line])

            start_q = 0

            em = {}
            em[0] = Grid(radius, 0, -radius, True, True)
            em[1] = Grid(radius, -radius, 0, True, True)
            em[2] = Grid(0, -radius, radius, True, True)
            em[3] = Grid(-radius, 0, radius, True, True)
            em[4] = Grid(-radius, radius, 0, True, True)
            em[5] = Grid(0, radius, -radius, True, True)

            hex_list = []
            for curr_r in range(-radius, radius+1):
                this_q = max(radius * -1, start_q)
                this_s = min(radius, radius - curr_r)
                max_q = min(radius + 1, radius - curr_r + 1)
                curr_q = this_q
                curr_s = this_s

                hex_line = []
                for cell in range(this_q, max_q):
                    if abs(curr_q) == radius or abs(curr_r) == radius or abs(curr_s) == radius:
                        hex_line.append(Grid(curr_s, curr_r, curr_q, False, True))
                    else:
                        hex_line.append(Grid(curr_s, curr_r, curr_q, False, False))
                    curr_q += 1
                    curr_s -= 1
                hex_list.append(hex_line)
                curr_r += 1
                start_q -= 1

                    
            for func in range(func_amount):
                line += 1
                commands = input[line].split(' ')
                for j in range(6):
                    e = em[j]
                    match commands[j]:
                        case 'F':
                            # top
                            if e.r == -radius and e.q < radius:
                                e.q += 1
                                e.s -= 1
                            # top-right
                            elif e.q == radius and e.s > -radius:
                                e.s -= 1
                                e.r += 1
                            # bot-right
                            elif e.s == -radius and e.r < radius:
                                e.r += 1
                                e.q -= 1
                            # bot
                            elif e.r == radius and e.q > -radius:
                                e.q -= 1
                                e.s += 1
                            # bot-left
                            elif e.q == -radius and e.s < radius:
                                e.s += 1
                                e.r -= 1
                            # bot-right
                            elif e.s == radius and e.r > -radius:
                                e.r -= 1
                                e.q += 1
                            # error:
                            else:
                                raise Exception('Moving Forward Error!')
                        case 'B':
                            # top
                            if e.r == -radius and e.s < radius:
                                e.s += 1
                                e.q -= 1
                            # top-right
                            elif e.q == radius and e.r > -radius:
                                e.r -= 1
                                e.s += 1
                            # bot-right
                            elif e.s == -radius and e.q < radius:
                                e.r -= 1
                                e.q += 1
                            # bot
                            elif e.r == radius and e.s > -radius:
                                e.q += 1
                                e.s -= 1
                            # bot-left
                            elif e.q == -radius and e.r < radius:
                                e.s -= 1
                                e.r += 1
                            # bot-right
                            elif e.s == radius and e.q > -radius:
                                e.r += 1
                                e.q -= 1
                            # error:
                            else:
                                raise Exception('Moving Backwards Error!')
                        case 'T':
                            e.active = not e.active
                        case '-':
                            pass
                        case _:
                            raise Exception('SOMETHING IS WRONG')
                        
                for hex_line in hex_list:
                    for cell in hex_line:
                        e_amount = 0
                        for e_key in em.keys():
                            e = em[e_key]
                            match e_key:
                                case 0 | 3:
                                    if e.active and e.r == cell.r:
                                        e_amount += 1
                                case 1 | 4:
                                    if e.active and e.q == cell.q:
                                        e_amount += 1
                                case 2 | 5:
                                    if e.active and e.s == cell.s:
                                        e_amount += 1
                                case _:
                                    raise Exception('Emitter OOB')

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
                    #if cell.emitter:
                    #    hex_res += str(cell.emitter)
                    if cell.border:
                        hex_res += '*'
                    elif cell.matter:
                        hex_res += 'M'
                    else:
                        hex_res += 'O'
                    hex_res += '-'
                cell = hex_line[-1]
                #if cell.emitter:
                #    hex_res += str(cell.emitter)
                if cell.border:
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
    def __init__(self, s, r, q, emitter, border, matter=False, active = False):
        self.s = s
        self.r = r
        self.q = q
        self.emitter = emitter
        self.border = border
        self.matter = matter
        self.active = active

    def set_matter(self, matter):
        self.matter = matter
