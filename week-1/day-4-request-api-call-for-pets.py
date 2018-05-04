
import requests
from webbrowser import open_new_tab

# Notes: https://programminghistorian.org/lessons/output-data-as-html-file
def _create_html_body(body, breed): 
	file = open('dogs.html', 'w')
	
	wrapper = """
		<html>
			<head>

			</head>
			<body>
				<h1>Dog Breed: {}</h1>
				<hr />
				{}
			</body>
		</html>
	"""
	
	webpage = wrapper.format(breed, body)
	file.write(webpage)
	file.close()

	open_new_tab('./dogs.html')
	

# Test Request
result = requests.get('https://dog.ceo/api/breeds/image/random')

if result.status_code != 200:
	print('Error with request')
	exit(1)

print(result.json())

breed = input("What's your favourite dog breed? ")
api_url = 'https://dog.ceo/api/breed/{}/images'.format(breed)


result = requests.get(api_url)
if result.status_code != 200:
	print('Error with request')
	exit(1)

html_body = ""

for dog in result.json():
	html_body += "<br />"

	img = '<img src={} width="100%" max-width="920px" alt="Breed: {}>"'
	img = img.format(dog, breed)

	html_body += img

_create_html_body(html_body, breed)
print('Thanks for playing!')

