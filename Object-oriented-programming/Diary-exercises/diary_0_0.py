'''Noora Kuorikoski'''

from datetime import datetime

def add(target, day = datetime.today(), *notes ) :
    '''
    parameter 'target' (actual observation e.g.king fisher, blue tit, Perseides) 
    and has a default parameter 'day', that is the current date 
    or a given date, and an optional parameter '*notes'. 
    The function checks that 'target' is not an empty string and, if day is given, 
    the date is not after current date, and then adds
    the observation, date, and possible notes to a list which is returned or 
    if checking of target, date or time fails returns a None value
    '''
    observation = []
    if target == '':
        print('Input needed')
        return None
    if day > datetime.today():
        print('Check the date')
        return None
    else:
        notes_str = ''
        day_str = str(day)
        observation.append(day_str)
        observation.append(target)
        if notes != None:
            for note in notes:
                notes_str += note
            observation.append(notes_str)
    
    return observation

def show(observations) :
    '''
    shows all observations
    '''
    obs_items = observations.items()
    for key, value in obs_items:
        strin = f'{value[0]} | {value[1]} | {value[2]} '
        print(f'#{key} | {strin}')
    

def main() :
    '''
    the function the program is started with. It has a loop that has a loop counter, 
    takes user input, calls function add and if the returned value is not None 
    adds the returned value (list) to 'observations' dictionary 
    (counter as key and returned list as value) and updates the loop counter, 
    calls function show and asks if user wants to add another value or 
    close the program
    '''
    observations = dict()
    counter = 0
    while True:
        ''' User inputs '''
        obs = input('Enter the observation: ')
        date_entry_str = input('Enter a date in YYYY-MM-DD format: ')
        date_obj = None
        if date_entry_str != '':
            date_obj = datetime.strptime(date_entry_str, '%Y-%m-%d')

        if date_obj == None:
            new_observation = add(obs)
        else:
            entry_notes = input('Give notes (additional): ')
            new_observation = add(obs, date_obj, entry_notes)

        if new_observation != None:
            counter += 1
            observations[counter] = new_observation         # Key = counter number. Value = observation, date etc.
        show_all = input('Show all observations? Y/N \n')
        if show_all.upper() == 'Y':
            show(observations)
        else:
            pass
        add_more = input('Add another observation? (Program closes if no) Y/N \n')
        if add_more.upper() == 'N':
            return
        else:
            pass


if __name__ == '__main__' :
    '''
    if the program is started from a script
    '''
    main()