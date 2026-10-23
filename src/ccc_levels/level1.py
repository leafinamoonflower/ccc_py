from ccc_levels.abstract_level import AbstractLevel

class Level1(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(1)
        
    # ----- methods: -----
    
    def solve_singular(self, file: str) -> None:
        input_list = self.file_access.read_file(file)
        output_list = list()

        current_line = 0
        buyable_int = int(input_list[0])

        buy_d = {}
        for i in range(buyable_int):
            current_line += 1
            for field in input_list[current_line].split(" -> "):
                b_name = field[0]
                b_cost = field[1]
                buy_d[b_name] = b_cost

        current_line += 2
        cases = int(input_list[current_line])
            
        for i in range(cases):
            current_line += 1
            num_react = int(input_list[current_line])

            for j in num_react:
                current_line += 1
                react_field = input_list[current_line].split(' -> ')
                
            
                input = react_field[0]
                output = react_field[1]

                input_dict = {}
                for mol in input.split(', '):
                    m_amount = int(mol.split(' ')[0])
                    m_name = mol.split(' ')[1]
                    input_dict[m_name] = m_amount

                output_dict = {}

            recipe_requirements = recipe.split(' -> ')[0]
            for recipe_requirement in recipe_requirements.split(', '):
                r_amount = int(recipe_requirement.split(' ')[0])
                r_name = recipe_requirement.split(' ')[1]
                requirement_dict[r_name] = r_amount
                
            results_dict = {}
            
            recipe_results = recipe.split(' -> ')[1]
            print(recipe_results)
            for recipe_result in recipe_results.split(', '):
                res_amount = int(recipe_result.split(' ')[0])
                res_name = recipe_result.split(' ')[1]
                results_dict[res_name] = res_amount
            print(results_dict)

            can_make = True
            #while can_make:
            for r in requirement_dict:
                if molecule_dict[r] < requirement_dict[r]:
                    can_make = False
                    #break

            if can_make:
                for req in requirement_dict:
                    molecule_dict[req] = molecule_dict[req] - requirement_dict[req]
                for res in results_dict:
                    if res in molecule_dict:
                        molecule_dict[res] = molecule_dict[res] + results_dict[res]
                        print('added' + res + str(results_dict[res]))
                    else:
                        molecule_dict[res] = results_dict[res]

            molecule_dict = { k:v for k, v in molecule_dict.items() if v }  

            case_output = ''
            for m in molecule_dict:
                case_output = case_output + str(molecule_dict[m]) + ' ' + m + ', '
            case_output = case_output[:-2]
            output_list.append(case_output)
        
        self.file_access.save_file(file, output_list)
        return None
