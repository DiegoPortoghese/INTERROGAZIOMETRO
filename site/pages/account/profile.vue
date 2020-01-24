<template>
<main role="main" class="container">
    <br>
<img :src="'http://localhost:8000'+loggedInUser.profile[0].avatar_image" class="rounded mx-auto d-block rounded-circle"  alt="Responsive image" width="300px" height="300px">


      <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
        <a class="btn btn-outline-light mr-3"  style="width:48;height:48;"><h4 class="text-light">{{SezioneAnno}}</h4></a>
        <div class="lh-100">
          <h6 class="mb-0 text-white lh-100">{{first_name+" "+last_name}}</h6>
          <small></small>
        </div>
      </div>

        <div class="my-3 p-3 bg-white rounded box-shadow">
        <h6 class="border-bottom border-gray pb-2 mb-0">Prossime Interrogazioni più recenti</h6>
        <div v-for="item in myPrevisioni" class="media text-muted pt-3">
          <span class="">&nbsp;</span>
          <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
            <div class="d-flex justify-content-between align-items-center w-100">
              <strong class="text-gray-dark">{{item.nome_materia_turno}}</strong>
              <a href="#" v-on:click="senderInterrogazione(item.id_turno)" v-show="checkGiaDichiarata(item.id_turno)">Dichiara</a>
              <span v-show="!checkGiaDichiarata(item.id_turno)">Dichiara</span>
            </div>
            <span class="d-block">{{item.data}}</span>
          </div>
        </div>

        <small class="d-block text-right mt-3">
          <a href="#"></a>
        </small>
      </div>



      <div class="my-3 p-3 bg-white rounded box-shadow">
        <h6 class="border-bottom border-gray pb-2 mb-0">Ultimi messaggi della classe</h6>
          <div v-for="message in chatgroupmessages" class="media text-muted pt-3">
            <span>&nbsp;</span>
            <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
              <strong class="d-block text-gray-dark">@{{message.from_user_first_name+" "+message.from_user_last_name}}</strong>
              {{message.message}}
            </p>
          </div>

        <small class="d-block text-right mt-3">
          <a href="/">Tutti i messaggi</a>
        </small>
      </div>
      
    </main>
</template>

<style>


@media (max-width: 767.98px) {
  .offcanvas-collapse {
    position: fixed;
    top: 56px; /* Height of navbar */
    bottom: 0;
    width: 100%;
    padding-right: 1rem;
    padding-left: 1rem;
    overflow-y: auto;
    background-color: var(--gray-dark);
    transition: -webkit-transform .3s ease-in-out;
    transition: transform .3s ease-in-out;
    transition: transform .3s ease-in-out, -webkit-transform .3s ease-in-out;
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
  .offcanvas-collapse.open {
    -webkit-transform: translateX(-1rem);
    transform: translateX(-1rem); /* Account for horizontal padding on navbar */
  }
}

.nav-scroller {
  position: relative;
  z-index: 2;
  height: 2.75rem;
  overflow-y: hidden;
}

.nav-scroller .nav {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: nowrap;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
  margin-top: -1px;
  overflow-x: auto;
  color: rgba(255, 255, 255, .75);
  text-align: center;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.nav-underline .nav-link {
  padding-top: .75rem;
  padding-bottom: .75rem;
  font-size: .875rem;
  color: var(--secondary);
}

.nav-underline .nav-link:hover {
  color: var(--blue);
}

.nav-underline .active {
  font-weight: 500;
  color: var(--gray-dark);
}

.text-white-50 { color: rgba(255, 255, 255, .5); }

.bg-purple { background-color: var(--purple); }

.border-bottom { border-bottom: 1px solid #e5e5e5; }

.box-shadow { box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05); }

.lh-100 { line-height: 1; }
.lh-125 { line-height: 1.25; }
.lh-150 { line-height: 1.5; }
</style>


<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      chatgroupmessages:[],
      first_name: '',
      last_name: '',
      SezioneAnno: '',
      myPrevisioni : []

    }
  },
  middleware: 'auth',
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    var self = this;
    self.formUsername = self.loggedInUser.username;
    self.formEmail = self.loggedInUser.email;
    self.first_name = self.loggedInUser.profile[0].first_name
    self.last_name = self.loggedInUser.profile[0].last_name
    self.SezioneAnno =  self.loggedInUser.profile[0].classe_info[0].anno+" "+ self.loggedInUser.profile[0].classe_info[0].sezione
    this.getPrevisioni()

    this.loadMessage()
  },
  methods: {
async loadMessage(){
      try{
        this.chatgroupmessages = await this.$axios.$get(`api/chatmessages/chatgroup/limit/${this.loggedInUser.profile[0].classe}/`);
        
      }catch(e){
        console.log(e)
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
          if (data.previsioni[key].profile == this.loggedInUser.profile[0].id){
            this.myPrevisioni.push(data.previsioni[key])
          }
        }
        for(var key in this.myPrevisioni){
          this.myPrevisioni[key].data = this.dataInItaliano(this.myPrevisioni[key].data)
        }
        console.log(this.myPrevisioni)
      } catch (e) {
        console.log(e)
      }
    },
    async senderInterrogazione(value){
      var self = this;
      var avanti = true;
       for (var key in self.loggedInUser.profile[0].interrogazioni){
          if(self.loggedInUser.profile[0].interrogazioni[key].turnointerrogazione == value){
            avanti = false
          }
        }
        if(avanti){
            try {
            
              await self.$axios.post(`api/profile/interrogazione/`, {
                        profile: self.loggedInUser.profile[0].id,
                        turnointerrogazione: value,
                        conferma: 0,
                        voto:0
                    }).then(function(data){
                      
                    });
                    location.reload()
            } 
            catch (error) {
              // TODO: migliorare la segnalazione errori
              // console.log(response.response.data);
              // self.formSuccessMessage = false;
              // self.formErrorMessageGeneric = true;
            }
      }
    },
    checkGiaDichiarata(value){
      var self = this;
      var avanti = true;
       for (var key in self.loggedInUser.profile[0].interrogazioni){
          if(self.loggedInUser.profile[0].interrogazioni[key].turnointerrogazione == value){
            avanti = false
          }
        }
      return avanti
    }

  }
}
</script>