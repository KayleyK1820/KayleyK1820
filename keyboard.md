
```xml
<!-- activity_main.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <!-- 鍵盤布局 -->
    <com.example.LedKeyboard
        android:id="@+id/led_keyboard"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#000000" />

    <!-- 其他布局元素 -->
</LinearLayout>
```

```java
// LedKeyboard.java
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

public class LedKeyboard extends View {

    private Paint mPaint;

    public LedKeyboard(Context context) {
        super(context);
        init();
    }

    public LedKeyboard(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    private void init() {
        mPaint = new Paint();
        mPaint.setColor(Color.BLACK);
        mPaint.setStyle(Paint.Style.FILL);
    }void

    @Override
    protected  onDraw(Canvas canvas) {
        super.onDraw(canvas);

        // 實現彩色背光效果
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                int x = j * 50 + 10;
                int y = i * 50 + 10;

                // 選擇不同顏色來實現彩色背光效果
                if (i % 2 == 0) {
                    mPaint.setColor(Color.RED);
                } else {
                    mPaint.setColor(Color.BLUE);
                }

                canvas.drawRect(x, y, x + 40, y + 40, mPaint);
            }
        }
    }
}
```

```java
// MainActivity.java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private LedKeyboard mLedKeyboard;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mLedKeyboard = findViewById(R.id.led_keyboard);

        // 添加按鈕來切換不同輸入模式
        Button quickInputButton = findViewById(R.id.quick_input_button);
        quickInputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 切換到速成輸入模式
                mLedKeyboard.setInputType(InputType.TYPE_CLASS_TEXT);
            }
        });

        Button strokeInputButton = findViewById(R.id.stroke_input_button);
        strokeInputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 切換到筆劃輸入模式
                mLedKeyboard.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_NO_SUGGESTIONS);
            }
        });

        Button handwritingInputButton = findViewById(R.id.handwriting_input_button);
        handwritingInputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 切換到手寫輸入模式
                InputMethodManager inputMethodManager = (InputMethodManager) getSystemService(INPUT_METHOD_SERVICE);
                inputMethodManager.showSoftInput(mLedKeyboard, InputMethodManager.SHOW_FORCED);
            }
        });

        Button englishInputButton = findViewById(R.id.english_input_button);
        englishInputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 切換到英文輸入模式
                mLedKeyboard.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_NORMAL);
            }
        });

        Button numberInputButton = findViewById(R.id.number_input_button);
        numberInputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 切換到數字輸入模式
                mLedKeyboard.setInputType(InputType.TYPE_CLASS_NUMBER);
            }
        });
    }
}
```


