/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package localizadordeaudios;

/**
 *
 * @author rueda
 */
public class LocalizadorDeAudios {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        SearchDirectoryWords search = new SearchDirectoryWords();
        
        //First, we need to know the words to find:
        String wordsToFind=search.words();
        //Second,we need to know the path to search:
        String path = search.path();
        //Third, we need to convert words and path to JSON
        Get_Post ob = new Get_Post();
        
        ob.getJson(wordsToFind,path);
        ob.send();
        ob.show();
       
       
       
 
        
    }
    
}
