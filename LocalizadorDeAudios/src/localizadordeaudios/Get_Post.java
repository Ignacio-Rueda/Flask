/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package localizadordeaudios;

/**
 *
 * @author rueda
 */
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URL;
import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import org.json.*;


/**
 *
 * @author rueda
 */
public class Get_Post {
    
    public HttpClient cliente = HttpClient.newBuilder().version(HttpClient.Version.HTTP_2).build();
    public String url = "http://localhost:5000";
     public String urlp = "http://localhost:5000/post";
    public HttpRequest peticion = HttpRequest.newBuilder().GET().uri(URI.create(url)).build();
    public String word;
    public String path;
    public String contentJson;
    
    public void show(){
        try{
            HttpResponse response = cliente.send(peticion,HttpResponse.BodyHandlers.ofString());
            String contenido = response.body().toString();
            System.out.println(contenido);
            
        
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
    
   public void send(){
       try{  
           URL url = new URL (urlp);
           HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
           conexion.setRequestMethod("POST");
           conexion.setRequestProperty("Content-Type", "application/json");
           conexion.setDoOutput(true);
           OutputStream output = conexion.getOutputStream();
           output.write(contentJson.getBytes());
           output.flush();
           output.close();
           System.out.println(conexion.getResponseCode());
           System.out.println(conexion.getResponseMessage());
       }catch(MalformedURLException e){
            e.printStackTrace();
       }
       catch(IOException e){
           e.printStackTrace();
       }
  
       }
   public void getJson(String word, String path){
       JSONObject myObject = new JSONObject();
       this.path = path;
       this.word = word;
       myObject.put("path", this.path);
       myObject.put("word", this.word);
       contentJson = myObject.toString();   
   }

           
  
   
   }
    

