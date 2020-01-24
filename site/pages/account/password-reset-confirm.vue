<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Scegli la tua nuova password </h3>
        <form @submit.prevent="passwordResetConfirm" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il reset della password.
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Reset password effettuato con successo. 
          </b-alert>
          <label for="new_password1" class="mt-2">Nuova password:</label>
          <b-form-input id="new_password1" :state="getFieldState('new_password1')" v-model="formNewPassword1" autocomplete="new-password" type="password" placeholder="Nuova password" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('new_password1')"> {{ getFieldErrorMessage('new_password1') }}</p>
          <label for="new_password2" class="mt-2">Conferma la nuova password:</label>
          <b-form-input id="new_password2" :state="getFieldState('new_password2')"  v-model="formNewPassword2" autocomplete="new-password" type="password" placeholder="Nuova password" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('new_password2')"> {{ getFieldErrorMessage('new_password2') }}</p>
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
      formNewPassword1: '',
      formNewPassword2: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false,
      formErrorResponse: false
    }
  },
  mounted() {
    var self = this;
    var uid = self.$route.query.uid;
    var token = self.$route.query.token;
    if( !uid || !token ){
      self.$router.push("/");
    }
  },
  layout: 'no-footer',
  methods: {
    async passwordResetConfirm() {
      var self = this;
      try {
        await self.$axios.post('/rest-auth/password/reset/confirm/', {
          uid: self.$route.query.uid,
          token: self.$route.query.token,
          new_password1: self.formNewPassword1,
          new_password2: self.formNewPassword2
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