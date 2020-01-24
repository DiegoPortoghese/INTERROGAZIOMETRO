import Vue from "vue";
import * as VueGoogleMaps from "vue2-google-maps";

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyCbuNG3KC0wKS4E54ivbJxAHvRdsuzW8SA",
    libraries: "places"
  }
});