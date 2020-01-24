<template>
<div class="container-fluid">
    <div class="row wrapper_classe">
      <div class="col-sm-6 offset-sm-3" style="">
        <br>
        <div class="rounded-lg box_bax_classe bg-light shadow border">
          <h1 class="text-center shadow-sm "><span class="badge badge-primary w-100 rounded">5 C</span></h1>
          <Calendar />
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
        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it
            to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
            like Aldus PageMaker including versions of Lorem Ipsum. release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
            like Aldus PageMaker including versions of Lorem Ipsum.
        </p><a href="#" class="float-right">Leggi meno recenti</a><br>
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-sm-6 offset-sm-3 text-left">
        <h3>Prossimi interrogati.</h3>
      </div>
    </div>
    <div class="row mt-4 mx-auto" v-bind:class="{'w-50' : isNotMobile }">
      <template v-for="alunno in alunni">
      <div :key="alunno.id" class="col-sm-4 mb-4">
        <Alunno-card-mini :alunno="alunno"></Alunno-card-mini>
      </div>
      </template>
    </div>

  <div class="row mt-4 mx-auto w-50 ">

    <div class="my-3 p-3 bg-white rounded box-shadow border ">
        <h6 class="border-bottom border-gray pb-2 mb-0">Chat della classe</h6>
        <div class="overflow-auto" style="max-height:400px">
          <div class="media text-muted pt-3">
            <img src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@Nome Cognome</strong>
              Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
            </p>
          </div>
          <div class="media text-muted pt-3">
            <img src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@Nome Cognome</strong>
              Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
            </p>
          </div>
          <div class="media text-muted pt-3">
            <img src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded">
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@Nome Cognome</strong>
              Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
            </p>
          </div>
          <div class="media text-muted pt-3">
            <img src="holder.js/32x32?theme=thumb&bg=e83e8c&fg=e83e8c&size=1" alt="" class="mr-2 rounded">
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@Nome Cognome</strong>
              Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
            </p>
          </div>
          <div class="media text-muted pt-3">
            <img src="holder.js/32x32?theme=thumb&bg=6f42c1&fg=6f42c1&size=1" alt="" class="mr-2 rounded">
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@Nome Cognome</strong>
              Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
            </p>
          </div>
        </div>
        <small class="d-block text-right mt-3">
          <div class="d-flex flex-row bd-highlight mb-3">
            <div class="p-2 bd-highlight" style="width:45vw"><b-form-input v-model="text" placeholder="Scrivi un messagio qui"></b-form-input></div>
              <div class="p-2 bd-highlight"><a href="#" class="btn btn-outline-success"><i class="fa fa-paper-plane" aria-hidden="true"></i></a></div>

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
import { mapGetters } from 'vuex'

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
 computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    if(this.isAuthenticated){
      if(this.loggedInUser.profile[0].complete_progress < 5){
        this.$router.push('/account/userpreference')
      }else{
        var composePush = '/classe/'+this.loggedInUser.profile[0].classe+"/"
        this.$router.push(composePush)
      }
    }else{
      this.$router.push('/account/login')
    }
    
    //this.asyncData()
    this.$nextTick(function () {
      this.onResize();
    })
    window.addEventListener('resize', this.onResize)
  },
 data(){
   return{
     alunni:[
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-danger"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-danger"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-warning"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-warning"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-warning"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-warning"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-warning"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-primary"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-primary"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-info"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-info"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Nome Molto Lungo Lungo",
         descrizione:"Matematica",
         info: "Martedi 6 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       {
         id:0,
         nome:"Mario Rossi",
         descrizione:"Storia",
         info: "Mercoledi 7 Gennaio",
         priority_border:"border-0"
       },
       
     ],
     isNotMobile: false
 }}
 ,
 methods:{
   onResize() {
      this.isNotMobile = document.documentElement.clientWidth > 1600;
      console.log(document.documentElement.clientWidth)
    }
 }
}
</script>

