<template>
<div class="container">
      <nav class="navbar navbar-expand-lg navbar-light bg-warning">
        <a class="navbar-brand" href="#">Menu</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">A Stock <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="#">find other</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Dropdown
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <input v-model="stockcode" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="button" @click="getnewstock()">Search</button>
          </form>
        </div>
      </nav>
  <div class="row">
      <!-- 左右两屏 -->
  <!--  <div class="col-md-4"> -->
      <!-- 左边是编辑部分 -->
   <!--   <div class="form-group"> -->
        <!--  <input type="hidden" v-model="url">
      </div>
      </div> -->
     <!--<div class="form-group">
          <input type="text" v-model="title" class="form-control" placeholder="标题">
      </div>
      <div class="form-group">
          <textarea class="form-control" v-model="content" placeholder="内容"></textarea>
      </div>
      <div class="form-group">
          <button class='btn btn-block btn-success' @click="saveBlog()">保存</button>
      </div>--> 
      
    
    <div class="col-md-12">
      <!-- 右边是博客内容表格部分 -->
      <table class="table table-bordered table-hover">
        <thead>
          <th class="text-center">stockcode</th>
          <th class="text-center">stockname</th>
          <th class="text-center">stocknow</th>
          <th class="text-center">stockhigh</th>
          <th class="text-center">stocklow</th>
          <th class='text-center'>stockopen</th>
          <th class='text-center'>stockchange</th>
          <th class='text-center'>stockyesday</th>
          <th class='text-center'>stockamount</th>
        </thead>
        <tbody>
       <!--    <tr>-->
         <tr v-for='stock in stocks' :key='stock.id' > 
            <td>{{stock.股票代码}}</td>
            <td>{{stock.股票名称}}</td>
            <td>{{stock.最新价}}</td>
            <td>{{stock.最高价}}</td>
            <td>{{stock.最低价}}</td>
            <td>{{stock.开盘价}}</td>
            <td>{{stock.涨跌幅}}</td>
            <td>{{stock.昨收}}</td>
            <td>{{stock.成交额}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import Qs from 'qs';
export default {
  name: 'Container',

  props: {
  },
  data(){
    return{
      //base_url:'http://172.18.204.60:8000/api/stock/',
      stocks:null,
      url:'',
      title:'',
      content:'',
      stockcode:'',
    }
  },
  methods:{

   // getAll(){
   //   axios.get('http://localhost:8000/api/stock/')
     //   .then(res=>{
     //     this.stocks = res.data;
     //     this.url = '';
      //    this.title = ''
      //    this.content = ''
     //   });
    
    getnewstock(){
      if(this.stockcode=='')
      {
        axios({
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          method:'get',
          url :'http://localhost:8000/get_allcode/'

        }).then(res=>{
          this.stocks = res.data
          console.log(res.data)
        })

      }
      else
      {
      let data = {stockcode:this.stockcode}
        axios({
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          method:'post',
          url : 'http://localhost:8000/access_stock_code/',
          data :Qs.stringify(data)
        }).then(res=>{
          this.getnewdata(res.data)
          console.log(res.data)
        })
      }
    },

    getnewdata(stockcode){
      axios({
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        method:'get',
        url :'http://push2.eastmoney.com/api/qt/stock/get?fields=f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f57,f58,f71,f116,f117,f60,f162,f163,f164,f167,f168,f170,f173&secid='+stockcode,

      }).then(res=>{
        this.accessdata(res.data)
        console.log(res.data)
      })

    },

    accessdata(data){
      let data1= {data2 :data}
      axios({
        method:'post',
        url :'http://localhost:8000/accessdata/',
        data :JSON.stringify(data1)
      }).then(res=>{
        console.log(res.data)
        this.stocks = {stock:res.data}
        //   this.stocks={
        //   stock1 : {stockcode : res.data['股票代码'],
        //            stockname : res.data['股票名称'],
        //            stocknow  : res.data['最新价'],
        //            stockhigh : res.data['最高价']},
        //   stock2 : {stockcode : '1231',
        //            stockname : 'dwdwdd',
        //            stocknow  : 12,
        //            stockhigh : 15}
        // }

       // $('#stockcode').text(res.data['股票代码'])
      //  this.stocks.title = res.data['股票名称']
      })
    },


    // saveBlog(){
    //   // 两种情况，一种是新建博客，一种是修改博客,
    //   // 通过 url是否为空来判断 
    //   if(this.url == ''){
    //     // 新增
    //     axios.post(this.base_url,{title:this.title, content:this.content})
    //       .then(()=>{
    //         this.getAll();
    //       })
    //   }else{
    //     //修改 因为要修改的url已经配置好了 
    //     axios.put(this.url, {title:this.title, content:this.content} )
    //       .then(()=>{
    //         this.getAll();
    //       })
    //   }
      
    // },
  //   editBlog(stock){
  //     this.url = stock.url;
  //     this.title = stock.title;
  //     this.content = stock.content;
  //   },
  //   deleteBlog(stock){
  //     axios.delete(stock.url)
  //       .then(()=>{
  //           this.getAll();
  //       });
  //   }
  // },
  created(){
   // this.getAll();
   this.getnewstock();
  }
  }
}
</script>

<style scoped>

</style>