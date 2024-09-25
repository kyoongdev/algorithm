
import java.io.*;


public class Baekjoon20546 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer cash = Integer.parseInt(br.readLine());

        
        String[] stocks = br.readLine().split(" ");

        
        Integer jh = cash;
        Integer jhStocks = 0;
        Integer sm = cash;
        Integer smStocks = 0;
        

        for(int i = 0; i < stocks.length ; i++){
            Integer stock = Integer.parseInt(stocks[i]);
            if(jh >= stock){
                jhStocks += jh / stock;
                jh -= (jh / stock) * stock;
             
            }
        }

        for(int i = 3; i  < stocks.length; i++){
            Integer threeBefore = Integer.parseInt(stocks[i - 3]);
            Integer twoBefore = Integer.parseInt(stocks[i - 2]);
            Integer oneBefore = Integer.parseInt(stocks[i - 1]);
            Integer today = Integer.parseInt(stocks[i]);
        
            if(threeBefore < twoBefore && twoBefore < oneBefore && smStocks > 0){
                sm += smStocks * today; // 주식 매도
                smStocks = 0;
            }else if(threeBefore > twoBefore && twoBefore > oneBefore && sm >= today){
                int buyAmount = sm / today; // 구매할 주식 수 계산
                smStocks += buyAmount; // 구매한 주식 수 더하기
                sm -= buyAmount * today; // 현금에서 구매한 주식 가격만큼 차감
            }
        }

        Integer jhResult = jh + jhStocks * Integer.parseInt(stocks[stocks.length - 1]);
        Integer smResult = sm + smStocks * Integer.parseInt(stocks[stocks.length - 1]);
        
        if(jhResult > smResult){
            System.out.println("BNP");
        }else if(jhResult < smResult){
            System.out.println("TIMING");
        }else{
            System.out.println("SAMESAME");
        }
    }
}