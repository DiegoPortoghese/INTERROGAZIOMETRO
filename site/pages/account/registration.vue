<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Registrati </h3>
        <form @submit.prevent="registration" autocomplete="on">
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Gentile utente, ti abbiamo inviato una email con un link da seguire per completare la registrazione.
          </b-alert>
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante la registrazione.
          </b-alert>
          <!-- username -->
          <label for="username" class="mt-2">Username:</label>
          <b-form-input id="username" :state="getFieldState('username')" type="text" autocomplete="nickname" v-model="formUsername" placeholder="Username" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('username') "> {{ getFieldErrorMessage('username') }}</p>
          <!-- email -->
          <label for="email" class="mt-2">Email: </label>
          <b-form-input id="email" :state="getFieldState('email')" type="email" autocomplete="email" v-model="formEmail" placeholder="Email" required></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('email')"> {{ getFieldErrorMessage('email') }}</p>
          <!-- password -->
          <label for="password1" class="mt-2">Password:</label>
          <b-form-input id="password1" :state="getFieldState('password1')" v-model="formPassword" autocomplete="new-password" type="password" placeholder="Password" required></b-form-input>          
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('password1')"> {{ getFieldErrorMessage('password1') }}</p>
          <!-- privacy -->
          <b-form-checkbox class="mt-2" name="privacy" v-model="formPrivacy" required> 
            <p class="small text-muted">
              Registrandoti accetti le Condizioni d'uso e Regole sulla privacy .
              La nostra Informativa Privacy prevede il tuo consenso per ricevere 
              email promozionali nostre da parte di terzi
            </p>
          </b-form-checkbox>
          <button class="btn btn-primary btn-block mt-2" type="submit"> Registrati! </button>
          <p class="mt-3"> 
            Hai già un account?
            <b-link to="/account/login/">Accedi!</b-link>
          </p>
        </form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>

export default {
  data() {
    return {
      formUsername: '',
      formEmail: '',
      formPassword: '',
      formPasswordConfirm: '',
      formPrivacy: '',
      formErrorResponse: false,
      formErrorMessageGeneric: false,
      formSuccessMessage: false
    }
  },
  middleware: 'guest',
  layout: 'no-footer',
  methods: {
    async registration() {
      var self = this;
        await self.$axios.post('rest-auth/registration/', {
          username: self.formUsername,
          email: self.formEmail,
          password1: self.formPassword,
          password2: self.formPassword
        }).then(function (response) {
          console.log("successo registrazione");
          // salvo un cookie con il token temporaneo per l'autologin
          self.$cookies.set('registration-token', response.data.key, {
            path: '/',
            maxAge: 60 * 60 * 24 * 1
          })
          self.formSuccessMessage = true;
          self.formErrorResponse = false;
          self.formErrorMessageGeneric= false;
        })
        .catch(function (error) {
          console.log("errore registrazione");
          self.formErrorMessageGeneric = true;
          self.formErrorResponse = error.response.data;
        });
    },
    getFieldErrorMessage: function(field_name){
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return this.formErrorResponse[field_name][0];
      }
    },
    getFieldState: function(field_name){
      if(this.formErrorResponse && this.formErrorResponse[field_name]) {
        return false;
      }
      return null;
    }
  }
}
</script>

