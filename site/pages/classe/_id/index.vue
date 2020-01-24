<template>
<div class="container-fluid">
    <div class="row wrapper_classe">
      <div class="col-sm-6 offset-sm-3" style="">
        <br>
        <div class="rounded-lg box_bax_classe bg-light shadow border">
          <h1 class="text-center shadow-sm "><span class="badge badge-primary w-100 rounded">{{ classe.anno+ " " +classe.sezione}}</span></h1>
          <Calendar :calendarEvents="calendarEvents" :classeId="classe.id" />
        </div>
      </div>
    </div>
    <div class="row mt-2">
      <div class="col-sm-6 offset-sm-3" style="">
      </div>
    </div>
    <div class="row mt-3">
      <br><br>
      <div class="col-sm-6 offset-sm-3" style="">
        <div class="rounded-sm border border-dark p-3">
        <h3>Note della classe</h3>
        <p>{{classe.note}}
        </p><a href="#" class="float-right"></a><br>
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-sm-6 offset-sm-3 text-left">
        <h3>Prossimi interrogati.</h3>
      </div>
    </div>
    <div class="row mt-4 mx-auto" v-bind:class="{'w-50' : isNotMobile }">
      <template v-for="alunno in totalPrevisioni">
      <div :key="alunno.profile" class="col-sm-4 mb-4">
        <Alunno-card-mini :alunno="alunno"></Alunno-card-mini>
      </div>
      </template>
    </div>

  <div class="row mt-4 mx-auto w-50 ">

    <div class="my-3 p-3 bg-white rounded box-shadow border ">
        <h6 class="border-bottom border-gray pb-2 mb-0">Chat della classe</h6>
        <div class="overflow-auto" style="max-height:400px" id="msg_history_scrolling" >
          <div v-for="message in chatgroupmessages" class="media text-muted pt-3">
            <span>&nbsp;</span>
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@{{message.from_user_first_name+" "+message.from_user_last_name}}</strong>
              {{message.message}}
            </p>
          </div>
          
        </div>
        <small class="d-block text-right mt-3">
          <div class="d-flex flex-row bd-highlight mb-3">
            <div class="p-2 bd-highlight" style="width:45vw">
              <b-form-input v-model="TextMessage" placeholder="Scrivi un messagio qui"></b-form-input></div>
              <div class="p-2 bd-highlight"><button class="btn btn-outline-success" v-on:click="sendChatMessage"><i class="fa fa-paper-plane" aria-hidden="true"></i></button></div>

          </div>
          <div class="col-sm-6">
           
          </div>
          <div class="col-sm-2"></div>
        </small>
      </div>
  </div>
  </div>
</template>
<style>
 /* background-image: url('/homepage_cut_new.jpg');*/
.wrapper_classe{
  background-image: linear-gradient(top right, #FFFFFF 0%, #AACFEF 100%);
  /* background-color: #faebd7; */
  background-size: cover;
  background-repeat: no-repeat;
  margin-left: -15px;
  margin-right: -15px;
  /* Full height */
  min-height: 579px;
  /* Center and scale the image nicely */
  background-position: center;
}

.box_bax_classe{
 padding:1vh;
 margin: -1vh;
 padding-top: 2px;
}
/*
.box_bax_mobile_old{
padding:2vh;
margin:-2vh;
border-width:1px;
background-color:rgb(255, 255, 255);
}
.wrapper_2{
  background-image: url('/homepage_cut_new.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  margin-left: -15px;
  margin-right: -15px;
  min-height: 500px;
  background-position: center;
}*/
</style>

<script>
import AlunnoCardMini from "~/components/AlunnoCardMini.vue";

let components = {};
if(process.browser) {
    const Calendar = require('~/components/Calendar').default;
    components = {
        Calendar,
        AlunnoCardMini
    }
}

export default {
    components ,
    mounted() {
      //this.asyncData()
      this.$nextTick(function () {
        this.onResize();
      })
      window.addEventListener('resize', this.onResize)
      this.loadMessage()
      this.setCalendarEvents()
      this.getPrevisioni()
    },
    async asyncData({ $axios, params }) {
      
      try {
        let classe = await $axios.$get(`api/classe/${params.id}/`);
        
        return { classe };
      } catch (e) {
        return { classe: [] };
      }
    },
    data() {
      return {
          classe: {
            sezione: '',
            anno:0,
            nome: "",
            descrizione: "",
          },
          TextMessage:"",
          chatgroupmessages: [],
          calendarEvents: [],
          isNotMobile: false,
          totalPrevisioni : [],
          totalInterrogazioni : [],
          isHidden: false,
          }
      },
      created () {
        this.timer = setInterval(this.loadMessage, 1000)
    },
      updated: function () {
        this.$nextTick(function () {
            var objDiv = document.getElementById("msg_history_scrolling");
            objDiv.scrollTop = objDiv.scrollHeight;
        })
    },
    beforeDestroy () {
      clearInterval(this.timer)
    },
    methods:{
    async loadMessage(){
      try{
        var buf_chatgroupmessages;
        buf_chatgroupmessages = await this.$axios.$get(`api/chatmessages/chatgroup/${this.classe.id}/`);
        if(buf_chatgroupmessages.length > this.chatgroupmessages.length ){
          this.chatgroupmessages =buf_chatgroupmessages
          var objDiv = document.getElementById("msg_history_scrolling");
          objDiv.scrollTop = objDiv.scrollHeight;
        }
      }catch(e){
        console.log(e)
      }
    },
    async sendChatMessage(){
      try {
          const config = {
              headers: { "content-type": "multipart/form-data" }
          };
          console.log(this.sendMessage)
          let formData = new FormData();
          formData.append('group_id',this.classe.id)
          formData.append('message',this.TextMessage)
          let response =  this.$axios.$post(`api/chatmessages/chatgroup/${this.classe.id}/`, formData, config);
          //this.chatgroupmessages.push(response)
          var objDiv = document.getElementById("msg_history_scrolling");
          objDiv.scrollTop = objDiv.scrollHeight;
          this.TextMessage = ''
          this.loadMessage()
      } catch (e) {
          console.log(e);
      }
    },
    dataInItaliano(dataObjectStr){
      var myDate = new Date(dataObjectStr)
      var mesi = new Array();
      mesi[0] = "Gennaio";
      mesi[1] = "Febbraio";
      mesi[2] = "Marzo";
      mesi[3] = "Aprile";
      mesi[4] = "Maggio";
      mesi[5] = "Giugno";
      mesi[6] = "Luglio";
      mesi[7] = "Agosto";
      mesi[8] = "Settembre";
      mesi[9] = "Ottobre";
      mesi[10] = "Novembre";
      mesi[11] = "Dicembre";
    //Crea la tabella dei giorni della settimana
    var giorni = new Array();
      giorni[0] = "Domenica";
      giorni[1] = "Lunedì";
      giorni[2] = "Martedì";
      giorni[3] = "Mercoledì";
      giorni[4] = "Giovedì";
      giorni[5] = "Venerdì";
      giorni[6] = "Sabato";

      return giorni[myDate.getDay()] +" "+myDate.getDate()+" "+ mesi[myDate.getMonth()]

  },
  async getPrevisioni() {
      try {
        let data = await this.$axios.$get(`api/classe/previsione/`);
        for(var key in data.previsioni){
        
            this.totalPrevisioni.push(data.previsioni[key])
        
        }
        for(var key in this.totalPrevisioni){
          this.totalPrevisioni[key].data = this.dataInItaliano(this.totalPrevisioni[key].data)
        }
        console.log(this.totalPrevisioni)
      } catch (e) {
        console.log(e)
      }
    },
      onResize() {
          this.isNotMobile = document.documentElement.clientWidth > 1600;
          console.log(document.documentElement.clientWidth)
        },

      setCalendarEvents(){
        let cls = this.classe
        for (let key in cls.orario){
          var object = cls.orario[key]
          this.calendarEvents.push(
                {
                  groupId: object.id,
                  daysOfWeek: [ (object.giorno_della_settimana).toString() ],
                  startTime: (object.numero_ora).toString()+':00:00',
                  endTime: (object.numero_ora+1).toString()+':00:00',
                  title: object.materia_nome
                }
          )
        }
        console.log(this.calendarEvents)
      }


    }
  }
</script>