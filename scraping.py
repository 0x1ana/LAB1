import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.washington.edu/datasciencemasters/faculty/'
    html = requests.get(url)


    s = BeautifulSoup(html.content, 'html.parser')
    results = s.find(id = 'main_content')
    professor_name = results.find_all(class_= 'box-outer')
    


    #I was having trouble separating mini bios from course taught. 
    # That's why they're in the same file
    file = open('bios_and_courses_taught.txt' , 'w')
    for result in professor_name:
        new_result = result.text
        file.write((str(new_result)) )
    
    print('The names were written to bios_and_courses_taught.txt')

    #Close file
    file.close()


   


    
    file = open('bios_url.txt' , 'w')

    #Write the urls to the file
    for div in results.find_all('div', class_='tile'):
        file.write(str(div.find('h3').text) + '\t')
        file.write(str(div.find('a')['href']) + '\n')
    
    print('The urls were written to bios_url.txt')

   


if __name__ == '__main__':
    main()    