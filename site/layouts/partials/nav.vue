<template>
  <header>
    <b-navbar toggleable="lg" type="dark" variant="primary" class="shadow">
      <b-navbar-brand to="/">INTERROGAZIOMETRO</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-left">
          <b-nav-item v-if="!isAuthenticated"></b-nav-item>
          <b-nav-item v-if="isAuthenticated" :to="'/classe/'+loggedInUser.profile[0].classe_info[0].id">{{loggedInUser.profile[0].classe_info[0].anno+" "+  loggedInUser.profile[0].classe_info[0].sezione}}</b-nav-item>
        </b-navbar-nav >
        <b-navbar-nav class="ml-auto">
          
          <b-nav-item-dropdown v-if="isAuthenticated">
            <template v-slot:button-content>
              <i class="fa fa-user"></i> 
              <span class="text-capitalize"> 
                {{ loggedInUser.username }}
              </span>
            </template>
            <b-dropdown-item to="/account/user/">Modifica Profilo</b-dropdown-item>
            <b-dropdown-item to="/account/password-change/">Modifica Password</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item to="/account/profile/">Il tuo profilo</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
          
          <b-nav-item v-show="!isAuthenticated" to="/account/login/">Accedi</b-nav-item>
          <b-nav-item v-show="!isAuthenticated" to="/account/registration/">Registrati</b-nav-item>
          <b-nav-item v-show="isAuthenticated" to="/account/profile">
            <button type="button" class="btn btn-outline-light btn-sm" >Interrogazioni</button>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </header>
</template>
<style>
.bg-purple { background-color: var(--purple); }

</style>
<script>
import { mapGetters } from 'vuex'

export default {
  data(){
    return{
      searchText: '',
      newMessage: false,
      locality:'Località'
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    if (this.isAuthenticated){
        this.CheckNewMessage()
      }
    },
  methods: {
    async logout() {
      await this.$auth.logout();
    },
    
    async Search() {
      if (this.searchText != ''){
        // forse qui sarebbe meglio fare una emit
        let region = ''
        if (this.locality != 'Località'){
          region = this.locality
        }
        this.$router.push({path: '/rooms', query: {search: region+' '+this.searchText }});
      }
    },
    async CheckNewMessage(){
      var self = this;
        try {
          if (this.isAuthenticated){
           let buff_mgs = []
            await self.$axios.$get("api/chatmessages/").then(function(data){
                buff_mgs = data;
            });
            for(let key in buff_mgs){
              if(buff_mgs[key].displayed === false && buff_mgs[key].from_user != this.loggedInUser.profile[0].fields.user){
                this.newMessage = true
                break;
              }
            }
            }
            }catch(error){
              console.log(error)
            }
        },
        async selectLocality(locality){
          this.locality = locality
        }
  },
}
</script>
