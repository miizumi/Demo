# JQuery 取Json資料的方法

```javascript
$.ajax({
  url: "URL",   //資料來源網址
  async:fales //同步 True or False
  type: "GET",  //GET or POST
  dataType: "json", //接收的資料格式，可以有data、xml等其他

  //回應成功時的操作
  success: function(Jdata) {
    //若要使用資料 Jdata['key']
    alert("SUCCESS!!!");
  },
  
  error: function() {
    alert("ERROR!!!");
  }
});

```