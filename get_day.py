import os, requests, sys
from settings import session
from datetime import datetime

def get_file_names(day):
    file_location = os.path.dirname(os.path.abspath(__file__))
    directory_name = os.path.join(file_location,f'Day{day:02d}')
    py_name = os.path.join(directory_name,f'day{day:02d}.py')
    data_name = os.path.join(directory_name,f'day{day:02d}.txt')
    day_name = f'Day {day:02d}'
    return {
        'directory': directory_name,
        'py_name': "app.py",       # hardcoding py_name
        'data_name': "input.txt",   # and app
        'day_name': data_name,  # because I didn't like dates
        'day': day              # as file names
    }
def create_directory(file_info):
    print(f'Attempting to create: {file_info["directory"]}')
    if os.path.exists(file_info["directory"]):
        print('Directory already exists.')
    else:
        os.mkdir(file_info["directory"])
def create_py_file(file_name,data_name, day):
    main = f"""
if __name__ == '__main__':
    data = ''
    with open('{data_name}') as f:
        data = f.read().strip()
        data = data.split('\\n')"""
    with open(file_name, 'w') as f:
        f.write(f'# Advent of Code {day}\n')
        f.write(f'#\n# Created: {datetime.now():%m-%d-%Y %H:%M:%S}\n')
        f.write(f'# Creator: Ty Day\n\n\n')
        f.write(main)
def create_data_file(file_name,day):
    cookies = {'session':session }
    page = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies)
    if page.status_code == 200:
        with open(file_name, 'w') as f:
            f.write(page.text)
    else:
        print(f"Could not connect to AoC server: {page.status_code}")

def create_files(file_info):
    # Create python file
    print(f'Attempting to create file: {file_info["py_name"]}')
    if not os.path.exists(file_info['py_name']):
        create_py_file(file_info['py_name'],file_info['data_name'], file_info['day_name'])
        print('File created')
    else:
        print(f'File ({file_info["py_name"]}) already exists.')

    # create input file
    print(f'Attempting to create file: {file_info["data_name"]}')
    if not os.path.exists(file_info['data_name']):
        create_data_file(file_info['data_name'], file_info['day'])
        print('File created')
    else:
        print(f'File ({file_info["data_name"]}) already exists.')
        

def set_up_day(day):
    file_info = get_file_names(day)

    create_directory(file_info)

    create_files(file_info)

    os.chdir(file_info['directory'])
if __name__ == '__main__':
    
    day = ''
    try:
        if len(sys.argv) > 1:
            day = int(sys.argv[1])
    except Exception as e:
        print(e)
    
    if day == '':
        today = datetime.now()
        if today.month == 12:
            day = datetime.now().day
            print(f"Assuming date is today: {today}")
            set_up_day(day)
        else:
            print("must include day")
    # elif os.path.exists(os.join(file_location,)
    elif day != '':
        set_up_day(day)