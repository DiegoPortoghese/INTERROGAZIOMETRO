<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Selezione preferenze</h3>
        <form @submit.prevent="user" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il salvataggio dati.
          </b-alert>
          <b-alert fade dismissible variant="danger" :show="formErrorMessagePoints">
            Attenzione: Si è verificato un errore<br> i punti rimanenti devono essere pari a 0 .
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Salvataggio dati effettuato con successo.
          </b-alert>
          
          <label for="username" class="mt-2">Username:</label>
          <b-form-input id="username" type="text" v-model="formUsername" readonly></b-form-input>
          <!-- email -->
          <label for="email" class="mt-2">Email:</label>
          <b-form-input id="email" type="email" v-model="formEmail" readonly></b-form-input>
          <!-- first_name -->
          <label for="first-name" class="mt-2">Nome:</label>
          <b-form-input id="first-name" type="text" autocomplete="given-name" v-model="formFirstName" ></b-form-input>
          <!-- last_name -->
          <label for="last-name" class="mt-2">Cognome:</label>
          <b-form-input id="last-name" type="text" autocomplete="family-name" v-model="formLastName" ></b-form-input>

          <br>
          <h5 class="col-sm-6" >Punti rimanenti: {{totalPoints}}</h5>
          <br>
          <!-- QUI -->
          <div v-for="materia in listaMaterie" :key="materia.value" >
            <label class="col-sm-5" style="font-size:15px"><b>{{materia.text}}</b></label>
            <b-form-input class="col-sm-6" id="Materia1" v-model="materia.points" type="range" min="0" max="10" @change="funcChangeRange(materia.value,materia.points)"></b-form-input>
          </div>
          

          <button class="btn btn-primary btn-block mt-2" type="submit"> 
            <i class="fa fa-edit"></i>
            Salva e continua
          </button>
        </form> 
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      //totalPoints:0,
      listaMaterie:[
                    { value: 1, text: 'Diritto ed economia', points:5 },
                    { value: 2, text: 'Discipline sportive', points:5 },
                    { value: 3, text: 'Storia dell\'arte', points:5}, 
                    { value: 4, text: 'Filosofia', points:5},
                    { value: 5, text: 'Fisica', points:5},
                    { value: 6, text: 'Informatica', points:5},
                    { value: 7, text: 'Religione', points:5},
                    { value: 8, text: 'Latino', points:5},
                    { value: 9, text: 'Inglese', points:5},
                    { value: 10, text: 'Letteratura', points:5},
                    { value: 11, text: 'Matematica', points:5},
                    { value: 12, text: 'Scienze', points:5},
                    { value: 14, text: 'Storia e Geografia', points:5},
                  ],
      formUsername: '',
      formEmail: '',
      formFirstName: '',
      formLastName: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false,
      formErrorMessagePoints: false
    }
  },
  middleware: 'auth',
  layout: 'no-footer',
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser']),
    totalPoints: function(){
      let sum = 65
      for(let i = 0; i < this.listaMaterie.length; i++){
        sum -= parseFloat(this.listaMaterie[i].points) ;
      }

     return sum;
   }
  },
  mounted() {
    var self = this;
    self.formUsername = self.loggedInUser.username || '';
    self.formEmail = self.loggedInUser.email || '';
    self.formFirstName = self.loggedInUser.profile[0].first_name || '';
    self.formLastName = self.loggedInUser.profile[0].last_name || '';
  },
  methods: {
    async user() {
      var self = this;
      if(self.totalPoints===0){
          try {
            await self.$axios.put(`api/profile/${self.loggedInUser.profile[0].id}/`, {
                //pk: self.loggedInUser.profile.id,
                //email: self.formEmail,
                //username: self.formUsername,
                //password: self.formPassword,
                first_name: self.formFirstName,
                last_name: self.formLastName,
                complete_progress: 5,
                classe: 1
            }).then(function(data){
              self.formSuccessMessage = true;
              self.formErrorMessageGeneric = false;
            });
          } 
          catch (error) {
            // TODO: migliorare la segnalazione errori
            // console.log(response.response.data);
            self.formSuccessMessage = false;
            self.formErrorMessageGeneric = true;
          }
          try{
            for (let key in self.listaMaterie){
                await self.$axios.post(`api/profile/preferenze/`, {
                  profile: self.loggedInUser.profile[0].id,
                  materia: self.listaMaterie[key].value,
                  valore: self.listaMaterie[key].points
                  
              }).then(function(data){
                self.formSuccessMessage = true;
                self.formErrorMessageGeneric = false;
              });
            }
            this.$router.push('/classe/2/') //FINISH
          }catch (error){
            console.log(error)
          }
      }else{
        self.formSuccessMessage = false;
        self.formErrorMessagePoints = true;
      }
    },
    funcChangeRange(value,points){
      console.log(this.listaMaterie.find(x => x.value === value))
      var buff_options = this.listaMaterie.find(x => x.value === value)
      // this.totalPoints = Number(this.totalPoints) + Number(buff_options.points)
    }
  }
}
</script>