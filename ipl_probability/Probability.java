package ipl_probability;


import java.sql.SQLException;
//import java.sql.Array;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;


import java.sql.DriverManager;

public class Probability {
	 private static String driverName = "org.apache.hive.jdbc.HiveDriver";
	  
	  public static void main(String[] args) throws SQLException {
	      try {
	      Class.forName(driverName);
	    } catch (ClassNotFoundException e) {
	      // TODO Auto-generated catch block
	      e.printStackTrace();
	      System.exit(1);
	    }
	      //replace "hive" here with the name of the user the queries should run as
	      Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "hadoop", "kavyashree");
	      Statement stmt = con.createStatement();
	     
	      ArrayList<Integer> batcluster=new ArrayList<>();
	      ArrayList<Integer> bowlcluster=new ArrayList<>();
	      ArrayList<Double> dots_prob=new ArrayList<>();
	      ArrayList<Double> ones_prob=new ArrayList<>();
	      ArrayList<Double> twos_prob=new ArrayList<>();
	      ArrayList<Double> threes_prob=new ArrayList<>();
	      ArrayList<Double> fours_prob=new ArrayList<>();
	      ArrayList<Double> fives_prob=new ArrayList<>();
	      ArrayList<Double> sixes_prob=new ArrayList<>();
	      ArrayList<Double> extras_prob=new ArrayList<>();
	      ArrayList<Double> wickets_prob=new ArrayList<>();
	      String database="IPL";
	      //String tableName = "IPL";
	      stmt.execute("use "+database);
	      //stmt.execute("drop table if exists " + tableName);
	      
	      //System.out.println(bowl_clust.keySet());
	      String tableName="players";
	      String sql;
	      for (int i = 1; i <=10; i++) {
			for (int j = 1; j <=10; j++) {
				if(i!=j){
					double dot=0;
					double one=0;
					double two=0;
					double three=0;
					double four=0;
					double five=0;
					double six=0;
					double extra=0;
					double wicket=0;
					double total_ball=1;
					tableName="players";
				      sql = "select * from " + tableName + " where bat_clust = "+i+" and bowl_clust = "+j;
				      System.out.println("Running: " + sql);
				      ResultSet res = stmt.executeQuery(sql);
				      while (res.next()) {
				    	  dot+=res.getInt(3);
				    	  one+=res.getInt(4);
				    	  two+=res.getInt(5);
				    	  three+=res.getInt(6);
				    	  four+=res.getInt(7);
				    	  five+=res.getInt(8);
				    	  six+=res.getInt(9);
				    	  extra+=res.getInt(10);
				    	  wicket+=res.getInt(11);
				    	  total_ball+=res.getInt(12);
				      }
					//System.out.println(total_ball);
					if(total_ball!=0)
					{
					batcluster.add(i);
					bowlcluster.add(j);
					dots_prob.add(dot/total_ball);
					ones_prob.add(one/total_ball);
					twos_prob.add(two/total_ball);
					threes_prob.add(three/total_ball);
					fours_prob.add(four/total_ball);
					fives_prob.add(five/total_ball);
					sixes_prob.add(six/total_ball);
					extras_prob.add(extra/total_ball);
					wickets_prob.add(wicket/total_ball);
					}
					else
					{
						batcluster.add(i);
						bowlcluster.add(j);
						dots_prob.add(0.5);
						ones_prob.add(0.5);
						twos_prob.add(0.5);
						threes_prob.add(0.5);
						fours_prob.add(0.5);
						fives_prob.add(0.5);
						sixes_prob.add(0.5);
						extras_prob.add(0.5);
						wickets_prob.add(0.5);
					}
				}
					
			}
		}
	      
	      //System.out.println(bat_clust.get(1));
	      for (int i = 0; i < batcluster.size(); i++) {
			System.out.println(batcluster.get(i)+"\t"+bowlcluster.get(i)+"\t"+dots_prob.get(i)+"\t"+ones_prob.get(i)+"\t"+twos_prob.get(i)+"\t"+threes_prob.get(i)+"\t"+fours_prob.get(i)+"\t"+fives_prob.get(i)+"\t"+sixes_prob.get(i)+"\t"+extras_prob.get(i)+"\t"+wickets_prob.get(i));
		}
}
}