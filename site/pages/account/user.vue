<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Modifica profilo </h3>
        <form @submit.prevent="user" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il salvataggio dati.
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Salvataggio dati effettuato con successo. 
          </b-alert>
          <div class="col-sm-10 mx-auto">
          <img
            v-if="preview"
            class="img-fluid shadow rounded-circle"
            style="width: 400px; height:400px"
            :src="preview"
            alt
          >
          <img
            v-else
            class="img-fluid shadow rounded-circle"
            style="width: 400px; height:400px"
            src="https://via.placeholder.com/400/FFFFFF/808080?text=Foto+Copertina"
            
          >
          </div>
          <br><br>
          <label for>Foto</label>
          <input type="file" name="file" @change="onFileChange">
          <br><br>
          <!-- username -->
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
      formUsername: '',
      formEmail: '',
      formFirstName: '',
      formLastName: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false,
      preview: "",
      
      storeimage:""
    }
  },
  middleware: 'auth',
  layout: 'no-footer',
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    /*
    if(this.loggedInUser.profile[0].complete_progress < 5){
      this.$router.push('/account/userpreference')
    }*/
    var self = this;
    self.formUsername = self.loggedInUser.username || '';
    self.formEmail = self.loggedInUser.email || '';
    self.formFirstName = self.loggedInUser.profile[0].first_name || '';
    self.formLastName = self.loggedInUser.profile[0].last_name || '';
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.storeimage = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async user() {
        var self = this;
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        // for (let data in this.classe) {
        //   formData.append(data, this.classe[data]);
        // }
        formData.append('first_name',this.formFirstName)
        formData.append('last_name',this.formLastName)
        formData.append('avatar_image',this.storeimage)
        try {
          let response = await this.$axios.$put(`api/profile/${self.loggedInUser.profile[0].id}/`, formData, config);
          console.log(response)
          this.$router.push('/account/profile/')
        } catch (e) {
          console.log(e);
        }
    }
  }
}
</script>