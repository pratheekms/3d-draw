
package com.thousandthoughts.tutorials;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.Socket;

import android.os.AsyncTask;
import android.util.Log;

public class Send extends AsyncTask<Float, Void, Void> {
	
	public static String serverIp = "192.168.101.153";
	public static int serverPort = 8888;
	Socket s;
	OutputStream ps;
	
	@Override
	protected void onPreExecute() {
				
		
	}
	
	@Override
	protected Void doInBackground(Float... arg0) {
		try {
			
			Log.v("Send", "Test message");
			s = new Socket(serverIp, serverPort);
			PrintStream ps = new PrintStream(s.getOutputStream());
			ps.println(arg0[0].toString()+","+arg0[1].toString()+","+arg0[2].toString()+","+arg0[3].toString()+","+arg0[4].toString()+","+arg0[5].toString()+","+arg0[6].toString());
			Log.v("Send", "Test message");
			s.close();
			ps.flush();
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;		
		
	}

}
