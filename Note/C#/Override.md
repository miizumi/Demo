# Override 覆寫

可以重新定義從父類別繼承來的東西。

先將父類別需要被覆寫的Method加上Virtual,再將子類別的Method加上Override。
```Csharp
Class Base
{
    public virtual string Talk()
    {
        #這是父類別
    }

}

Class Derived : Base
{
    public override string Talk()
    {
        #這是子類別
    }

}
```

注意事項：
1. Override可以使用到子類別的方法
2. 覆寫前後的Method名稱與建構子必須相同，否則視為不同Method。