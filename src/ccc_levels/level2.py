from ccc_levels.abstract_level import AbstractLevel

class Level2(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(2)
        
    # ----- methods: -----
    
    def solve_singular(self, file: str) -> None:
        input_list = self.file_access.read_file(file)
        output_list = list()

        cases = int(input_list[0])
        print(cases)
        for i in range(cases):
            molecules = input_list[1 + (3 * i)]
            recipe = input_list[2 + (3 * i)]

            molecule_dict = {}

            for molecule in molecules.split(', '):
                m_amount = int(molecule.split(' ')[0])
                m_name = molecule.split(' ')[1]

                molecule_dict[m_name] = m_amount

            requirement_dict = {}

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
