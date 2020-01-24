<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Accedi </h3>
        <form @submit.prevent="login" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: si è verificato un errore durante il login.
          </b-alert>
          <!-- email -->
          <label for="email" class="mt-2">Email:</label>
          <b-form-input :state="getFieldState('email')" id="email" type="email" autocomplete="email" v-model="formEmail" placeholder="Email"></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('email')"> {{ getFieldErrorMessage('email') }}</p>
          <!-- password -->
          <label for="password" class="mt-2">Password:</label>{{getFieldErrorMessage('password')}}
          <b-form-input :state="getFieldState('password')" id="password" v-model="formPassword" autocomplete="current-password" type="password" placeholder="Password"></b-form-input>
          <p class="text-monospace text-danger small" v-if="getFieldErrorMessage('password')"> {{ getFieldErrorMessage('password') }}</p>
          <p class="mb-3">
            <b-link to="/account/password-reset/" >Hai dimenticato la password?</b-link>
          </p>
          <button class="btn btn-primary btn-block mt-2" type="submit"> 
            <i class="fas fa-sign-in-alt"></i> 
            Accedi 
          </button>
          <p class="mt-3"> 
            Sei un nuovo utente?
            <b-link to="/account/registration/">Registrati!</b-link>
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
      formEmail: '',
      formPassword: '',
      formErrorResponse: false,
      formErrorMessageGeneric: false
    }
  },
  layout: 'no-footer',
  middleware: 'guest',
  methods: {
    async login() {
      var self = this;
      try {
        await self.$auth.loginWith('local', {
          data: {
            email: self.formEmail,
            password: self.formPassword
          }
        })
      } 
      catch (error) {
        console.log(error.response.data);
        self.formErrorMessageGeneric = true;
        self.formErrorResponse = error.response.data;
      }
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