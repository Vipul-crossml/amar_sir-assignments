
import datetime
import os
import getpass
import uuid
import json

# current datetime
now = datetime.datetime.now()
#displaying the output
current_date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date_time)
print(getpass.getuser())

PWD = os.getcwd()
print(PWD)
users_folder = PWD+'/users/'

files_list = os.listdir(users_folder)
person_names_list = []

def display_names(users_folder):
	files_list = os.listdir(users_folder)
	for file_name in files_list:
		# print(file_name)
		# file = open(users_folder+file_name,'r')
		with open(users_folder+file_name,'r') as file:
			person_names_list.extend(file.readlines())
			# for user in user_names_list:
			# 	print(user.strip())
display_names(users_folder)
person_names = [user.strip() for user in person_names_list]


def gen_UUID(user):
	return user[0]+str(uuid.uuid1())

def gen_email(person_name):
	first_name = person_name[0:4]
	last_name = person_name[-1]
	return first_name+last_name+"@try.com"

user_info = []

for person_name in person_names:
	user_info.append({gen_UUID(person_name):{"name":person_name, "email":gen_email(person_name)}})


# print(json.dumps(user_info))


def write_json(data, filename='output.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2)



# with open('output.json') as json_file:
# 	data = json.load(json_file)
#
# 	temp = data['emp_details']

write_json(user_info)

#unit test
json_string = None

with open("output.json") as f:
    json_string = f.read()
try:
    parsed_json = json.loads(json_string)
    formatted_json = json.dumps(parsed_json, indent = 4,sort_keys=True)
    with open("output.json", "w") as f:
        f.write(formatted_json)
except Exception as e:
    print(repr(e))