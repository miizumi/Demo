# 抽象 Abstract
## 抽象的用途
當父類別有沒辦法確定的方法的時候，可以作成 **「抽象方法」** ，讓子類別在繼承時使其完善。
## 特性
1. 被抽象的類別不能NEW
2. 抽象類別中可以定義抽象方法，但不能實作且必須Public。
3. 抽象類別可以繼承抽象類別
4. 繼承抽象後必須完成
   
## 使用方式
```C#
//以動物來舉例
abstract class Animals
{
    //動物的共同屬性與行為
    public int hand;
    public int leg;
    //每種動物的跑步方法都不一樣，所以沒辦法馬上給予值，故能使用抽象
    abstract string run();
}

//子類別
class Human:Animals //冒號後面是被繼承的物件，也就是父類別
{
    //可以新增其他屬性
    public string skin;
    //要記得寫完父類別留下的東西
    public override string run()
	{
	 return "兩隻腳跑步，有點快";
	}


}