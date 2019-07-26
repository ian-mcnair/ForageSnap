package org.tensorflow.lite.examples.classification;

import android.content.Intent;
//import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.app.Activity;

import androidx.appcompat.app.AppCompatActivity;

public class WarningActivity extends AppCompatActivity {

    //Button button = (Button)findViewById(R.id.warning_button);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_warning);
    }

    public void onButtonClick(View view){
        Intent startCameraActivity = new Intent(WarningActivity.this,
                ClassifierActivity.class );
        Log.d("buttonlog", "before start");
        startActivity(startCameraActivity);
        Log.d("buttonlog", "After start");
    }

}
