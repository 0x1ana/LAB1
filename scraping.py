import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.washington.edu/datasciencemasters/faculty/'
    html = requests.get(url)


    s = BeautifulSoup(html.content, 'html.parser')
    results = s.find(id = 'main_content')
    professor_name = results.find_all(class_= 'box-outer')
    


#Open/Create a file named friends.txt
    file = open('bio1.txt' , 'w')
    for result in professor_name:
        new_result = result.text
        file.write((str(new_result)) )
    
    print('The names were written to bio.txt')

    #Close file
    file.close()


   


    #Open/Create a file named urls
    file = open('url.txt' , 'w')

    #Write the urls to the file
    for div in results.find_all('div', class_='tile'):
        file.write(str(div.find('h3').text) + '\t')
        file.write(str(div.find('a')['href']) + '\n')
    
    print('The urls were written to url.txt')

   


if __name__ == '__main__':
    main()    