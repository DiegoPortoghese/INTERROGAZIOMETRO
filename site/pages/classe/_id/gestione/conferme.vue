<template>
<main>
    <div class="nav-scroller bg-white box-shadow">
      <nav class="nav nav-underline">
        <a class="nav-link" href="../gestione/">Principale</a>
        <a class="nav-link" href="#">Note</a>
        <a class="nav-link" href="../gestione/orario">Orario</a>
        <a class="nav-link" href="../gestione/interrogazioni">Interrogazioni</a>
        <a class="nav-link active" href="../gestione/conferme">
          Conferme
          <span class="badge badge-pill bg-light align-text-bottom"></span>
        </a>
      </nav>
    </div>
<div class="container">

<div class="my-3 p-3 bg-white rounded box-shadow">
        <h6 class="border-bottom border-gray pb-2 mb-0">Lista Interrogazioni da confermare</h6>
        <div v-for="item in totalPrevisioni" class="media text-muted pt-3">
          <span class="">&nbsp;</span>
          <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
            <div class="d-flex justify-content-between align-items-center w-100">
              <strong class="text-gray-dark">{{item.last_name}} : {{item.nome_materia_turno}}</strong>
              <div class="col-sm-3 text-right">
              <a href="#" v-on:click="senderConferma(item.id_turno,item.profile)" v-show="checkGiaDichiarata(item.id_turno,item.profile)==1"> Conferma </a>
              <a href="#" style="color:red" v-on:click="senderDeclina(item.id_turno,item.profile)" v-show="checkGiaDichiarata(item.id_turno,item.profile)==1"> Declina </a>
              <a href="#" v-on:click="senderForzaConferma(item.id_turno,item.profile)" v-show="checkGiaDichiarata(item.id_turno,item.profile)==0"> Forza Conferma </a>
              <a href="#" v-on:click="senderForzaDeclina(item.id_turno,item.profile)" v-show="checkGiaDichiarata(item.id_turno,item.profile)==0"> Forza Declina </a>
              </div>
              
            </div>
            <span class="d-block">{{item.data}}</span>
          </div>
        </div>

        <small class="d-block text-right mt-3">
          <a href="#"></a>
        </small>
      </div>

</div>

</main>

</template>



<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      SezioneAnno: '',
      totalPrevisioni : [],
      totalInterrogazioni : []
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
    this.TotalInterrogazioni()
    this.getPrevisioni()
  },
  methods: {

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
        console.log(this.myPrevisioni)
      } catch (e) {
        console.log(e)
      }
    },
    async senderForzaConferma(value,profileId){
      var self = this;
      var avanti = true;
        if(avanti){
            try {
            
              await self.$axios.post(`api/profile/interrogazione/`, {
                        profile: profileId,
                        turnointerrogazione: value,
                        conferma: 1,
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
    async senderForzaDeclina(value,profileId){
      var self = this;
      var avanti = true;
        if(avanti){
            try {
            
              await self.$axios.post(`api/profile/interrogazione/`, {
                        profile: profileId,
                        turnointerrogazione: value,
                        conferma: 2,
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
    
    async senderDeclina(value,profileId){
      var self = this;
      var avanti = true;
      var id_interrogazione = 0;
      var listInterrogazioniTurni = []
      for (var key in self.totalInterrogazioni){
        if(self.totalInterrogazioni[key].profile == profileId){
          listInterrogazioniTurni.push(self.totalInterrogazioni[key])
        }
      }
      for (var key in listInterrogazioniTurni){
        if(listInterrogazioniTurni[key].turnointerrogazione == value && listInterrogazioniTurni[key].conferma == 0){
          id_interrogazione = listInterrogazioniTurni[key].id
        }
      }
        if(id_interrogazione != 0){
            try {
            
              await self.$axios.put(`api/profile/interrogazione/${id_interrogazione}/`, {
                        conferma: 2,
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
    async senderConferma(value,profileId){
      var self = this;
      var avanti = true;
      var id_interrogazione = 0;
      var listInterrogazioniTurni = []
      for (var key in self.totalInterrogazioni){
        if(self.totalInterrogazioni[key].profile == profileId){
          listInterrogazioniTurni.push(self.totalInterrogazioni[key])
        }
      }
      for (var key in listInterrogazioniTurni){
        if(listInterrogazioniTurni[key].turnointerrogazione == value && listInterrogazioniTurni[key].conferma == 0){
          id_interrogazione = listInterrogazioniTurni[key].id
        }
      }
        if(id_interrogazione != 0){
            try {
            
              await self.$axios.put(`api/profile/interrogazione/${id_interrogazione}/`, {
                        conferma: 1
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
    async TotalInterrogazioni(){
      try {
        let data = await this.$axios.$get(`api/profile/interrogazione/`);
        for(var key in data){
            this.totalInterrogazioni.push(data[key])
        }
        console.log()
      } catch (e) {
        console.log(e)
      }
    },
    checkGiaDichiarata(value,userId){
      var self = this;
      var avanti = 0;
      var listInterrogazioniTurni = []
      for (var key in self.totalInterrogazioni){
        if(self.totalInterrogazioni[key].profile == userId){
          listInterrogazioniTurni.push(self.totalInterrogazioni[key])
        }
      }
      for (var key in listInterrogazioniTurni){
        if(listInterrogazioniTurni[key].turnointerrogazione == value && listInterrogazioniTurni[key].conferma == 0){
          return 1
        }
        if(listInterrogazioniTurni[key].turnointerrogazione == value && listInterrogazioniTurni[key].conferma != 0){
          return 2
        }
      }

      return avanti
    }

  }
}
</script>