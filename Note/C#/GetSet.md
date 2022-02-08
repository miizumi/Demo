# Get & Set 存取器
林北每次都忘記怎麼用，故作一個筆記
## 目的
限制存取以及寫入的功能，能夠做到唯讀或是唯寫，防止不正常的操作。在遊戲裡可以防止作弊更改某些參數。
## 做法
先設置一個Private變數藏在Class裡面，再設置一個Public的Method作為中介，用Method對變數進行操作。

## 基本語法
```c#
//傳統方式定義屬性必須先定義欄位來封裝
private string name;
public string Name
{
    //存取時執行的程式碼
    get{return name;}//存取時可得到name的值
    //寫入時執行的程式碼
    set{name= value}//寫入時將得到的值寫入name

}
//自動屬性(短寫法)
public string Name { get; set; }
```

## 也可以在Get&Set裡面做判斷
```c#
private int hp;
public int HP
{
    get{return hp}
    set
    {
        if(value<0)
            hp=0;
        else
            hp=value;
    }

}
```