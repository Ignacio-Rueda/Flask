/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package localizadordeaudios;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

public class SearchDirectoryWords{
   public String words(){
    String wordsToFind = JOptionPane.showInputDialog("Introduce las palabras a buscar en el audio");
    return wordsToFind;
   }
    
    public String  path(){     
  
    JFileChooser fileChooser= new JFileChooser();
    fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
    fileChooser.setApproveButtonText("select");
    fileChooser.setDialogTitle("Selecciona la carpeta");
    fileChooser.showOpenDialog(fileChooser);
    //JFileChooser fileChoser = new JFileChooser (ruta); Por defecto la ruta se inicia en documents, desde aquí podemos modificarla
    String path= fileChooser.getSelectedFile().getAbsolutePath();
    return path;
    }




  
        
   
    
    
}
