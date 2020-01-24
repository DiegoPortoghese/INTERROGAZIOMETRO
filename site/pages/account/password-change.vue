<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Cambia password </h3>
        <form @submit.prevent="passwordChange" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il cambio password.
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Cambio password effettuato con successo. 
          </b-alert>
          <label for="old_password" class="mt-2">Password attuale:</label>
          <b-form-input :state="getFieldState('old_password')" id="old_password" v-model="formOldPassword" autocomplete="current-password" type="password" placeholder="Password attuale" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('old_password')"> {{ getFieldErrorMessage('old_password') }}</p>
          <label for="new_password1" class="mt-2">Nuova password:</label>
          <b-form-input id="new_password1" :state="getFieldState('new_password1')" v-model="formNewPassword1" autocomplete="new-password" type="password" placeholder="Nuova password" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('new_password1')"> {{ getFieldErrorMessage('new_password1') }}</p>
          <label for="new_password2" class="mt-2">Conferma la nuova password:</label>
          <b-form-input id="new_password2" :state="getFieldState('new_password2')"  v-model="formNewPassword2" autocomplete="new-password" type="password" placeholder="Nuova password" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('new_password2')"> {{ getFieldErrorMessage('new_password2') }}</p>
          <p class="mt-1">
            <b-link to="/account/password-reset/" >Hai dimenticato la password?</b-link>
          </p>
          <b-button variant="primary" type="submit"> 
            <i class="fa fa-edit"></i>
            Modifica 
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
      formOldPassword: '',
      formNewPassword1: '',
      formNewPassword2: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false,
      formErrorResponse: false
    }
  },
  middleware: 'auth',
  layout: 'no-footer',
  methods: {
    async passwordChange() {
      var self = this;
      try {
        await self.$axios.post('/rest-auth/password/change/', {
          old_password: self.formOldPassword,
          new_password1: self.formNewPassword1,
          new_password2: self.formNewPassword2
        }).then(function(data){
          self.formSuccessMessage = true;
          self.formErrorMessageGeneric = false;
          self.formErrorResponse = false;
        });
      } 
      catch (error) {
        self.formSuccessMessage = false;
        self.formErrorMessageGeneric = true;
        self.formErrorResponse = error.response.data;
        // TODO: migliorare la segnalazione errori
      }
    },
    getFieldErrorMessage: function(field_name){
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return this.formErrorResponse[field_name][0];
      }
    },
    getFieldState: function(field_name){
      console.log(field_name)
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return false;
      }
      return null;
    }
  },
}
</script>