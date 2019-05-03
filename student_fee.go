package main
import ("fmt")
func main(){
    var finalFee float64
   
    var course_fee float64
    var marks float64
    var scholar float64
    var extra_fee float64
    course_fee=25000
    marks=70/2
    marks=marks/100
    extra_fee=1500
    scholar=course_fee*marks
    course_fee=course_fee-scholar
    finalFee=course_fee+extra_fee
     
     fmt.Println(finalFee) 
    
}
