from dataclasses import dataclass, field
import random
import datetime

@dataclass
class Password:
    length: int
    options: str
    
    @property
    def _CHARACTER_DICT(self) -> dict:
        d = \
            {
                'alphabetical_lower': [ chr(char) for char in range(97, 123) ],
                'alphabetical_upper': [ chr(char) for char in range(65, 91) ],
                'numerical': [ chr(char) for char in range(48,58) ],
                'extended': ['!', '@', '#', '$', '%', '^', '^', '&', '*', '?']
            }
        return d
    
    @property
    def character_opts(self) -> list:

        return None

    def generate(self) -> None:
        
        def generate_character(char_list:list) -> str:
            return char_list[random.randint(0,len(char_list) - 1)]
        
        def parse_options(options:str) -> list:
            character_options = []
            opts = options.replace(' ', '')
            opts = opts.replace('-','')
            for op in opts:
                if op == 'A':
                    character_options.append('alphabetical_lower')
                    character_options.append('alphabetical_upper')
                elif op == 'a':
                    character_options.append('alphabetical_lower')
                elif op.lower() == 'n':
                    character_options.append('numerical')
                elif op.lower() == 'e':
                    character_options.append('extended')
                else:
                    raise ValueError(f'''
                                    Bad argument: recived -{op}, expecting:
                                        -A: Upper case alphabetic
                                        -a: Lower case alphabetic
                                        -n: numerical
                                        -e: exteneded
                                    ''')
            character_options = set(character_options)
            return character_options
        
        character_options = parse_options(self.options)
        if self.length < len(character_options):
            raise ValueError(f'''
                             Character options exceed password length.
                                Password length: {self.length}
                                Character options: {len(character_options)}
                             ''')
        else:
            random.seed()
            date = datetime.date.today().strftime("%A %d. %B %Y")
            character_sets = [ self._CHARACTER_DICT[op] for op in character_options if op in self._CHARACTER_DICT ]
            generated_password = []
            for char_set in character_sets:
                generated_password.append(generate_character(char_set))
            
            while len(generated_password) < self.length:
                if len(character_sets) == 1:
                    generated_password.append(generate_character(character_sets[0]))
                else:
                    generated_password.append(generate_character(character_sets[random.randint(0,len(character_sets) - 1)]))
            for i in range(0,random.randint(10,20)):
                random.shuffle(generated_password)
            print(\
f'''
Password:        {''.join(generated_password)}
Generation Date: {date}
'''\
                  )
        return None

def main() ->  None:
    Password(16,'-n -A -e').generate()
    return None

if __name__ == '__main__':
    main()