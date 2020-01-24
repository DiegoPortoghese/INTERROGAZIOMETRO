<template>

</template>

<script>

export default {
  data() {
    return {}
  },
  middleware: 'guest',
  layout: 'no-footer',
  mounted() {
    var self = this;
    var key = self.$route.query.key;
    if( !key ){
      self.$router.push("/");
    } else {
      self.confirmRegistration(key);
    }
  },
  methods: {
    async confirmRegistration(key) {
      var self = this;
      await self.$axios.post('rest-auth/registration/confirm-email/', {
        key: key,
      }).then(function (response) {
        console.log("successo conferma registrazione", response);
        // autologgo lo user se è arrivato con il cookie token temporaneo
        // dopo una registrazione e cancello il cookie
        var _token = self.$cookies.get('registration-token');
        if( _token ){
          self.$auth.setUserToken(_token);
          self.$cookies.remove('registration-token', {
            path: '/'
          });
        }
      })
      .catch(function (error) {
        console.log("errore conferma registrazione");
        self.$router.push("/");
      });
    }
  }
}
</script>

