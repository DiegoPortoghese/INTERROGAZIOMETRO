<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Password reset </h3>
        <form @submit.prevent="passwordChange" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il reset della password.
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            <i class="fa fa-info-circle"></i>
            Il sistema verificherà la presenza di un account sul portale con la mail indicata
            e se presente, riceverai una email all'indirizzo specificato 
            con il link per effettuare il password reset.
          </b-alert>
          <!-- email -->
          <label for="email" class="mt-2">Email: </label>
          <b-form-input id="email" :state="getFieldState('email')" type="email" autocomplete="email" v-model="formEmail" placeholder="Email" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('email')"> {{ getFieldErrorMessage('email') }}</p>
          <p class="text-monospace text-info small mt-2" v-show="formSuccessMessage">
            Se non ricevi alcuna email o non ricordi l'indirizzo email utilizzato per l'iscrizione, contattaci.
          </p>
          <b-button class="mt-2" variant="primary" type="submit"> 
            <i class="fa fa-send"></i>
            Invia 
          </b-button>
        </form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      formEmail: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false,
      formErrorResponse: false
    }
  },
  layout: 'no-footer',
  methods: {
    async passwordChange() {
      var self = this;
      try {
        await self.$axios.post('/rest-auth/password/reset/', {
          email: self.formEmail,
        }).then( function(data) {
          self.formSuccessMessage = true;
          self.formErrorMessageGeneric = false;
          self.formErrorResponse = false;
        });
      } 
      catch (error) {
        console.log(error.response.data);
        self.formSuccessMessage = false;
        self.formErrorMessageGeneric = true;
        self.formErrorResponse = error.response.data;
      }
    },
    getFieldErrorMessage: function(field_name) {
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return this.formErrorResponse[field_name][0];
      }
    },
    getFieldState: function(field_name) {
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return false;
      }
      return null;
    }
  },
}
</script>