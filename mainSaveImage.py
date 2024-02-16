import requests, json

if __name__ == '__main__':
    url = 'https://bestclassicbands.com/wp-content/uploads/2018/11/Heavy-Metal-Covers-Montage-768x510.jpg'
    
    response = requests.get(url, stream=True)
    
    with open('image.jpg','wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()