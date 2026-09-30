package com.polaros;
import com.sun.net.httpserver.*;
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
public final class IngestionServer{
  static void send(HttpExchange e,int code,String body)throws IOException{
    byte[] b=body.getBytes(StandardCharsets.UTF_8);
    e.getResponseHeaders().set("Content-Type","application/json");
    e.getResponseHeaders().set("Access-Control-Allow-Origin","*");
    e.sendResponseHeaders(code,b.length);
    try(OutputStream o=e.getResponseBody()){o.write(b);}
  }
  public static void main(String[] args)throws Exception{
    HttpServer s=HttpServer.create(new InetSocketAddress(9090),0);
    s.createContext("/health",e->{try{send(e,200,"{\"status\":\"online\",\"service\":\"polaros-java-ingestion\"}");}catch(Exception ignored){}});
    s.createContext("/api/catalog",e->{try{send(e,200,"[{\"id\":\"icesat2\",\"type\":\"satellite\"},{\"id\":\"erebus\",\"type\":\"terrain\"}]");}catch(Exception ignored){}});
    s.start();
    System.out.println("PolarOS Java ingestion service listening on :9090");
  }
}