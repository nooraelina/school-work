package fi.jamk.sumcalculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    private var number1: String = ""
    private var number1int: Int = 0
    private var number2: String = ""
    private var number2int: Int = 0
    private var operatorPressed: Boolean = false
    private var operator: String = ""
    private var ans: Int = 0

    fun numberInput(view: View) {
        textView.setText(R.string.empty)
        if (operatorPressed == false) {
            val digit = (view as Button).text.toString().toInt()
            number1 += digit
            // append a new string to textView
            textView.append(number1)
        } else {
            val digit = (view as Button).text.toString().toInt()
            number2 += digit
            // append a new string to textView
            textView.append(number1 + operator + number2)
        }
    }

    fun operatorInput(view: View) {
        operatorPressed = true
        number1int = number1.toInt()
        operator = (view as Button).text.toString()
        textView.append(operator)
    }

    fun calculate(view: View) {
        number2int = number2.toInt()
        when (operator) {
            "+" -> ans = number1int + number2int
            "*" -> ans = number1int * number2int
            "-" -> ans = number1int - number2int
            }
        // setting everything as they were at the start
        textView.setText(R.string.empty)
        number1 = ""
        number1int = 0
        number2 = ""
        number2int = 0
        operatorPressed = false
        operator = ""
        // showing the answer
        textView.append(ans.toString())
    }

    fun clear(view: View) {
        textView.setText(R.string.empty)
        number1 = ""
        number1int = 0
        number2 = ""
        number2int = 0
        operatorPressed = false
        operator = ""
    }
}
