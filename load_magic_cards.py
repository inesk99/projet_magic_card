# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:32:22 2022

@author: Inès
"""

## Requete API python 

import requests, jsons

####################################
## fonctions

def save_img (url,name,save_path = "C:\\Users\\Inès\\Desktop\\projet Madgic\\projet_madgic\\cartes save") : 
    
    # load image to url extract of json card
    res = requests.get(url)
        
    if res.status_code == 200 :
        # read and write the image to save it in local
        file = open(save_path+"\\"+name+".png","wb")
        file.write(res.content)
        file.close()
        print("Well done ! Image was saved in "+save_path)
    else : 
        print("Error request no found !")
 

def main() : 
    # request to collect some cards 
    res = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=c%3Ared+pow%3D3")
    
    if res.status_code == 200 : 
        
        # transform json data to dict
        datas = jsons.loadb(res.content)
        
        for i in range(len(datas["data"])) : 
            
            # open each card to collected
            data = datas['data'][i]
            
            # keep the name of the card
            name = data["type_line"]
            
            try : 
                # some card haven't url image 
                # keep the url of the card
                url_img = data["image_uris"]["png"]
            
                save_img(url_img, name)
                
            except : 
                print("Image url not found")
                print("Next file")


# execute the main function
main()
